# Austin Sound Ordinance Permits Analysis

A comprehensive data analysis and machine learning project examining sound ordinance permits in Austin, Texas to understand permit processing patterns, approval times, and factors influencing the city's noise management policies.

## 📋 Project Overview

Austin, Texas is home to nearly 1 million people, and with increasing population density, effective noise management is crucial for public health and quality of life. This project analyzes sound ordinance permit data to understand how the city handles noise management and what factors influence permit processing times.

### 🎯 Research Questions

1. **How do the organization applying and the event subtype influence how quickly a permit is issued?**
2. **What features influence issuance time?**
3. **Are there shared factors between subtypes that could help predict the likely subtype of an event?**

## 📊 Dataset

- **Source**: City of Austin Open Data Portal
- **Original Size**: 67 columns, 6,730 rows
- **Cleaned Dataset**: 48 columns, 6,023 rows  
- **Time Period**: 2009-2025
- **Update Frequency**: Daily

### Key Features
- Application and issuance dates
- Event start times and duration
- Permit subtypes (Concrete Pouring, Outdoor Music Venue, Advertising Sound Amplification, etc.)
- Geographic data (latitude, longitude, zip code, council district)
- Decibel levels and venue capacity
- Applicant organization information

## 🔍 Key Findings

### 🏗️ Construction Bias
- **Construction permits are prioritized**: Concrete pouring permits have the shortest approval times (often same-day approval)
- **Music venues face delays**: Outdoor music venue permits take an average of ~70 days to process
- **Policy implication**: Despite Austin's identity as a live music hub, construction activities are prioritized over cultural events

### 🌍 Geographic Patterns
- **Location has minimal impact**: Geographic location alone is not a strong predictor of approval times
- **No population density correlation**: No meaningful correlation between population density and decibel levels across the city

### 🗓️ Seasonal Trends
- **Concrete pouring peaks**: Spring and summer months see the highest volume of construction permits
- **Timing optimization**: Construction permits typically occur at night (12 AM - 6 AM) for optimal weather conditions
- **Event-specific patterns**: Advertising permits spike in March (Q1 deadlines), government permits increase during election seasons

### 🏢 Company Type Impact
- **Food service experiences longest delays**: Average wait time of ~45 days
- **Construction companies get fastest processing**: Average processing time of <1 day

## 🛠️ Methods & Models

### Data Preprocessing
- Removed 24 irrelevant/redundant columns
- Converted time data to numerical format (0-23 hours)
- Created `time_diff` variable (target variable for prediction models)
- Used LLM (Gemini 2.5) to categorize companies into generic types
- Handled missing values strategically to preserve data integrity

### Machine Learning Models

**1. Linear & Polynomial Regression**
- Predicted permit processing times
- Polynomial regression achieved R² = 0.49, RMSE = 20.6 days
- Identified outdoor music venues and zip codes as key predictors

**2. Random Forest**
- Feature importance analysis
- Subtype prediction with 88.4% accuracy
- Geographic analysis with 26% variance explained

**3. K-Means Clustering**
- Geographic clustering analysis
- Identified 3 main clusters (limited by data composition)

## 📁 Project Structure

```
austin-sound-permits/
├── README.md
├── CompanyTypeCode/                           # Company type prediction model code
│   ├── AddCompanyTypeToCSV.py                 # Add company type classifications to the permit data code
│   ├── CleanedSoundOrdinancePermits.csv       # Cleaned dataset for script using
│   ├── company_names.txt                      # Companies to be labeled text file
│   ├── CompanyNameToText.py                   # Companies to text script
│   ├── CompanyTypePrediction.ipynb            # Graph modeling of relationships notebook
│   ├── companyTypes.txt                       # Gemini 2.5 Pro labeling text file
│   ├── DataClean.py                           # CSV cleaning script
│   ├── StepsTaken.txt                         # Short documentation of steps taken by Daniel Lam
│   ├── TimesCleanedCompanyType.csv            # Cleaned times dataset for modeling
│   └── Updated_SoundOrdinancePermits.csv      # Final dataset with labeling for modeling
├── Reports/                                   # Project documentation and analysis reports
│   ├── Final-Report.pdf                       # Comprehensive project report
│   ├── Sound-Ordinance-Data-Exploration.pdf   # Initial data exploration findings
│   └── Sound-Ordinance-Modelling.pdf          # Machine learning analysis
├── df_times_cleaned.csv                       # Cleaned dataset with processed time data
├── soundOrdinance.md                          # Additional project documentation
├── soundOrdinanceModel.ipynb                  # Machine learning model development
├── sound_ordinance_data.csv                   # Original dataset
├── time_formatted_sound_ordinance_data.csv    # Time-formatted dataset
└── zipcode.ipynb                              # Geographic analysis and zipcode modeling

```

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/[username]/austin-sound-permits
   cd SOUNDORDINANCEPROJECT
   ```

2. **Install dependencies**
   ```bash
   pip install pandas scikit-learn matplotlib seaborn jupyter
   ```

3. **Run the data processing pipeline**
   ```bash
   # Clean and process the data
   python CompanyTypeCode/DataClean.py
   python CompanyTypeCode/AddCompanyTypetoCSV.py
   ```

4. **Run the analysis**
   ```bash
   # Main analysis notebooks
   jupyter notebook Reports/soundOrdinanceModel.ipynb
   jupyter notebook Reports/zipcode.ipynb
   jupyter notebook CompanyTypeCode/CompanyTypePrediction.ipynb
   ```

5. **Access the data**
   - Download the dataset from [City of Austin Open Data Portal](https://data.austintexas.gov/Recreation-and-Culture/Sound-Ordinance-Permits/ryu3-tuin/about_data)
   - Place the raw data in the `Reports/` directory as `sound_ordinance_data.csv`

## 🎯 Policy Implications

### Recommendations
1. **Dynamic Prioritization**: Implement seasonal permit prioritization strategies
   - Favor construction permits during spring peak season
   - Support outdoor music venue permits during summer/fall event seasons

2. **Resource Allocation**: Balance development goals with cultural preservation
   - Allocate additional resources for processing music venue permits
   - Streamline approval processes for cultural events

3. **Data Quality Improvement**: Enhance record-keeping practices
   - Standardize missing value handling for decibel levels and capacity
   - Implement consistent permit status tracking

## 👥 Contributors

- **Eshi Kohli** - Data cleaning, decibel vs location analysis, linear regression modeling
- **Maadhav Kothuri** - Data preprocessing, determined prediction factors, random forest modeling
- **Daniel Lam** - Cleaned OMV times, outdoor music venue analysis, permit processing research, application time factors, linear regression modeling
- **Nneoma Onochie** - Time conversion functions, application time analysis, application time factors, linear and polynomial regression modeling
- **Greg Zachariah** - Data cleaning, permit type seasonal analysis, application time factors, k-mean and random forest modeling

## 🤖 Technology Used

- **Programming**: Python (pandas, scikit-learn, matplotlib, seaborn)
- **Machine Learning**: Linear/Polynomial Regression, Random Forest, K-Means
- **Data Processing**: LLM integration (Gemini 2.5) for company categorization
- **Analysis**: Jupyter Notebooks, R Markdown


## 🏛️ Responsible Research & Innovation

This project considers the impact on multiple stakeholders, including city officials, venue owners, musicians, and Austin residents. Our findings aim to support data-driven policy decisions that balance urban development with Austin's cultural identity as the "Live Music Capital of the World."

***

**Course**: SDS 322E  
**Institution**: The University of Texas at Austin  
**Date**: April 20, 2025
