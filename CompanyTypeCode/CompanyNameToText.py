import pandas as pd
import os

def extract_company_names(csv_filename, output_filename):
    """
    Extract company names from the APPLICANT_ORGANIZATION column of a CSV file
    and write them to a text file.
    """
    try:
        # Check if the CSV file exists
        if not os.path.exists(csv_filename):
            print(f"Error: The file '{csv_filename}' does not exist.")
            return False
        
        # Load the CSV file
        print(f"Reading data from '{csv_filename}'...")
        data = pd.read_csv(csv_filename)
        
        # Check if the required column exists
        if "APPLICANT_ORGANIZATION" not in data.columns:
            print("Error: The 'APPLICANT_ORGANIZATION' column does not exist in the CSV file.")
            return False
        
        # Extract unique company names and filter out non-string values
        company_names = data["APPLICANT_ORGANIZATION"].dropna().unique()
        company_names = [name for name in company_names if isinstance(name, str)]
        
        # Sort alphabetically
        company_names.sort()
        
        # Write to text file
        with open(output_filename, 'w') as f:
            for company in company_names:
                f.write(f"{company}\n")
        
        print(f"Successfully extracted {len(company_names)} unique company names to '{output_filename}'.")
        return True
    
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

# File paths
csv_file = "Cleaned_SoundOrdinancePermits.csv"
output_file = "company_names.txt"

# Execute the function
extract_company_names(csv_file, output_file)
