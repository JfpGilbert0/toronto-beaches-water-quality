import pandas as pd

# Load data (ensure the path to your CSV is correct)
data = pd.read_csv("../data/cleaned_water_quality_data.csv")
df = pd.DataFrame(data)

# Ensure the collectiondate is in datetime format
df['collectiondate'] = pd.to_datetime(df['collectiondate'], errors='coerce', format='%Y-%m-%d')

# Extract month and year for grouping
df['day'] = df['collectiondate'].dt.day_name()  # Extracts month in 'YYYY-MM' format

# Group by month and calculate required statistics
summary = df.groupby('day').agg(
    n=('ecoli', 'size'),
    average_ecoli=('ecoli', 'mean'),
    variance=('ecoli', 'var'),
    unsafe_levels=('ecoli', lambda x: (x > 100).sum())
).reset_index()
summary.index = range(1,8)
summary['percentage_unsafe'] = round((summary['unsafe_levels']/summary['n'])*100, 2)
# order by dow
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
summary['day'] = pd.Categorical(summary['day'], categories=days, ordered=True)
summary = summary.sort_values(by='day').reset_index(drop=True)
print(summary)