
# Imports
import pandas as pd

# Load data (ensure the path to your CSV is correct)
data = pd.read_csv("../data/cleaned_water_quality_data.csv")
df = pd.DataFrame(data)

# Ensure the collectiondate is in datetime format
df['collectiondate'] = pd.to_datetime(df['collectiondate'], errors='coerce', format='%Y-%m-%d')

# Extract month and year for grouping
df['month'] = df['collectiondate'].dt.month_name()  # Extracts month in 'YYYY-MM' format

# Group by month and calculate required statistics
summary = df.groupby('month').agg(
    number_of_datapoints=('ecoli', 'size'),
    average_ecoli=('ecoli', 'mean'),
    variance=('ecoli', 'var'),
    number_of_points_above_100=('ecoli', lambda x: (x > 100).sum())
).reset_index()

# Display the summary table
summary
