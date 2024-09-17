# Import necessary packages
import pandas as pd
import janitor
import json

# Function to load and clean the CSV data
def load_and_clean_data(csv_file):
    # 1) Load the CSV file
    df = pd.read_csv(csv_file)
    
    
    # 1.5) Geometry column seperation
    df[['loc_type', 'longitude', 'latitude']] = df['geometry'].apply(extract_location_info)   
    
    # 2) Clean the data
    # Clean column names: Make them lowercase, remove special characters, and replace spaces with underscores
    df = janitor.clean_names(df)
    
    # Step 3: Handle missing data (e.g., drop rows with missing values)
    df = df.dropna()  
    
    # Step 4: Remove duplicates
    df = df.drop_duplicates()
    
    # 4) Remove any irrelevant columns 
    columns_to_keep = ['_id', 'beachid', 'beachname', 'sitename', 'collectiondate', 'ecoli', 'comments', 'loc_type', 'longitude', 'latitude']  # Specify which columns to keep
    df = df[columns_to_keep]
    
    # Step 6: Convert data types (if needed)
    # Example: Convert a column to datetime
    df['collectiondate'] = pd.to_datetime(df['collectiondate'])
    
    return df

# Funcion to seperate geometry column into many
def extract_location_info(location_str):
    # Parse the string as a JSON object
    location_data = json.loads(location_str)
    
    # Extract values from the dictionary
    loc_type = location_data.get('type')
    longitude = location_data.get('coordinates')[0]
    latitude = location_data.get('coordinates')[1]
    
    return pd.Series([loc_type, longitude, latitude])

# Main function to call the data cleaning process
def main():
    csv_file = 'data/raw_water_quality_data.csv'  # Replace with your actual CSV file path
    
    # Load and clean the data
    cleaned_data = load_and_clean_data(csv_file)

    print(cleaned_data.dtypes)
    # Save the cleaned data to a new CSV file
    cleaned_data.to_csv('data/cleaned_water_quality_data.csv', index=False)
    print("Data cleaned and saved to 'cleaned_water_quality_data.csv'")

# Run the script
if __name__ == "__main__":
    main()
