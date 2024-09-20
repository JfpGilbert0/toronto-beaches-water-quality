# Import packages
import pandas as pd
import tabulate as tab
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Import data
data = pd.read_csv("data/cleaned_water_quality_data.csv")
df = pd.DataFrame(data)


# Summary stats tables
def create_counts(data):
    df = data
    summary_stats = pd.DataFrame({
        'Metric': [
            'Data points',
            'Date Range',
            'Unique Beach Names',
            'N0 of Unique Site Names',
            'No of Unique Locations',
        ],
        'Value': [
            len(df),
            f"{df['collectiondate'].min()} to {df['collectiondate'].max()}",
            df['beachname'].nunique(),
            df['sitename'].nunique(),
            df.groupby(['longitude', 'latitude']).ngroups
        ]
    })
    sum_stats = tab.tabulate(summary_stats, headers='keys', tablefmt='github')
    return sum_stats


def create_ecoli_stats(df):
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
    ecoli_stats = tab.tabulate(ecoli_stats, headers='keys', tablefmt='github')
    return ecoli_stats



def main():
    #Import Data
    data = pd.read_csv("data/cleaned_water_quality_data.csv")
    df = pd.DataFrame(data)

    with open("results/summary_table.md", "w") as file:
        file.write(create_counts(df))
    
    with open("results/ecoli_stats.md", "w") as file:
        file.write(create_ecoli_stats(df))


# Run the script
if __name__ == "__main__":
    main()
