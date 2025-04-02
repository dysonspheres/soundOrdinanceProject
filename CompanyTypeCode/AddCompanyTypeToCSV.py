import csv
import os

# --- Configuration ---
input_csv_filename = 'CleanedSoundOrdinancePermits.csv'
lookup_txt_filename = 'companyTypes.txt' # File containing "Company Name: Type"
output_csv_filename = 'Updated_SoundOrdinancePermits.csv'
applicant_org_column_name = 'APPLICANT_ORGANIZATION'
new_column_name = 'COMPANY_TYPES'
lookup_delimiter = ': ' # Delimiter between name and type in the text file

# --- Function to load company types from the text file ---
def load_company_types(filename):
    """Reads the lookup file and returns a dictionary mapping company names to types."""
    company_type_map = {}
    print(f"Loading company types from '{filename}'...")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                line = line.strip()
                if not line:
                    continue
                try:
                    # Split only once based on the defined delimiter
                    parts = line.split(lookup_delimiter, 1)
                    if len(parts) == 2:
                        company_name = parts[0].strip()
                        company_type = parts[1].strip()
                        if company_name: # Ensure company name is not empty
                             company_type_map[company_name] = company_type
                        else:
                             print(f"Warning: Empty company name found on line {i+1} in {filename}")
                    else:
                        print(f"Warning: Could not parse line {i+1} in {filename}: '{line}' - Expected delimiter '{lookup_delimiter}' not found or format incorrect.")

                except Exception as e:
                    print(f"Error processing line {i+1} in {filename}: '{line}'. Error: {e}")
    except FileNotFoundError:
        print(f"Error: Lookup file '{filename}' not found.")
        return None
    except Exception as e:
        print(f"Error reading lookup file '{filename}': {e}")
        return None

    print(f"Loaded {len(company_type_map)} company type mappings.")
    return company_type_map

# --- Main Processing ---
if __name__ == "__main__":
    # Load the lookup data
    company_types = load_company_types(lookup_txt_filename)

    if company_types is None:
        print("Exiting due to error loading lookup file.")
    elif not os.path.exists(input_csv_filename):
         print(f"Error: Input CSV file '{input_csv_filename}' not found.")
    else:
        print(f"\nProcessing '{input_csv_filename}'...")
        rows_processed = 0
        rows_written = 0
        try:
            with open(input_csv_filename, 'r', encoding='utf-8', newline='') as infile, \
                 open(output_csv_filename, 'w', encoding='utf-8', newline='') as outfile:

                reader = csv.reader(infile)
                writer = csv.writer(outfile)

                # Read header
                header = next(reader)
                rows_processed += 1

                # Find the index of the applicant organization column
                try:
                    applicant_org_index = header.index(applicant_org_column_name)
                except ValueError:
                    print(f"Error: Column '{applicant_org_column_name}' not found in '{input_csv_filename}'.")
                    print(f"Available columns are: {header}")
                    exit() # Stop processing if the crucial column is missing

                # Write new header to output file
                new_header = header + [new_column_name]
                writer.writerow(new_header)
                rows_written += 1

                # Process data rows
                for row in reader:
                    rows_processed += 1
                    if len(row) > applicant_org_index:
                        applicant_name = row[applicant_org_index].strip()

                        # Look up the company type, default to 'Unknown' if not found
                        company_type = company_types.get(applicant_name, 'Unknown')

                        # Append the company type to the row
                        row.append(company_type)
                        writer.writerow(row)
                        rows_written += 1
                    else:
                        # Handle potentially short rows if necessary, e.g., write as is or skip
                        print(f"Warning: Row {rows_processed} is shorter than expected. Skipping or handling as needed.")
                        # Example: Write row as is, padding with empty string for the new column
                        # row.append('')
                        # writer.writerow(row)
                        # rows_written += 1


            print("\nProcessing complete.")
            print(f"Total rows read from input: {rows_processed}")
            print(f"Total rows written to output: {rows_written}")
            print(f"Output saved to '{output_csv_filename}'")

        except FileNotFoundError:
             print(f"Error: Input CSV file '{input_csv_filename}' not found during processing.")
        except Exception as e:
            print(f"An error occurred during CSV processing: {e}")