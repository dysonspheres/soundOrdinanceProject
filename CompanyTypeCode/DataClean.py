import pandas as pd

# Load the CSV file
data = pd.read_csv("SoundOrdinancePermits.csv")

# Drop rows where 'APPLICANT_ORGANIZATION' is empty
data = data.dropna(subset=['APPLICANT_ORGANIZATION'])

# Remove duplicate rows based on 'APPLICANT_ORGANIZATION'
data = data.drop_duplicates(subset=['APPLICANT_ORGANIZATION'])

# Save the cleaned data to a new CSV file
data.to_csv("Cleaned_SoundOrdinancePermits.csv", index=False)

# Display the first few rows of the cleaned data
print(data.head())