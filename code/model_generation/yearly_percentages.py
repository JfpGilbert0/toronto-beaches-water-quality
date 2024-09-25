# Imports
from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# Load data (ensure the path to your CSV is correct)
data = pd.read_csv("../data/cleaned_water_quality_data.csv")
df = pd.DataFrame(data)

# Ensure the collectiondate is in datetime format
df['collectiondate'] = pd.to_datetime(df['collectiondate'], errors='coerce', format='%Y-%m-%d')

# Extract year for grouping
df['year'] = df['collectiondate'].dt.year  # Extracts month in 'YYYY-MM' format

# Group by year and calculate required statistics
yearly_avg = df.groupby('year').agg(
    n=('ecoli', 'size'),
    average_ecoli=('ecoli', 'mean'),
    variance=('ecoli', 'var'),
    unsafe_levels=('ecoli', lambda x: (x > 100).sum())
).reset_index()
yearly_avg['percentage_unsafe'] = round((yearly_avg['unsafe_levels']/yearly_avg['n'])*100, 2)
yearly_avg = yearly_avg.sort_values(by='year').reset_index(drop=True)
# Create Graph
# Create the scatter plot
plt.figure(figsize=(14, 7))
sns.barplot(data=yearly_avg, x='year', y='percentage_unsafe', alpha=0.6)
plt.title(f'Percentage of tests above 100MPN/100ml By Year', fontsize=16)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Percentage of unsafe ecoli levels', fontsize=10)
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.show()

