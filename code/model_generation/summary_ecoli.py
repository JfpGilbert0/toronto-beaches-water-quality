# Import packages
import pandas as pd
import tabulate as tab
from IPython.display import display

# Import data
data = pd.read_csv("../data/cleaned_water_quality_data.csv")
df = pd.DataFrame(data)

df['collectiondate'] = pd.to_datetime(df['collectiondate'])


ecoli_summary = df['ecoli'].describe()

# Additional statistics
ecoli_variance = df['ecoli'].var()

# Create a summary table
ecoli_stats = pd.DataFrame({
    'Statistic': [
        'Count',
        'Mean',
        'Standard Deviation',
        'Min',
        '25th Percentile (Q1)',
        'Median (Q2)',
        '75th Percentile (Q3)',
        'Max',
        'Variance'
    ],
    'Value': [
        ecoli_summary['count'],
        ecoli_summary['mean'],
        ecoli_summary['std'],
        ecoli_summary['min'],
        ecoli_summary['25%'],
        ecoli_summary['50%'],
        ecoli_summary['75%'],
        ecoli_summary['max'],
        ecoli_variance
    ]})

with open("../results/tables/ecoli_summary.md", "w") as file:
        file.write(ecoli_stats.to_csv())
