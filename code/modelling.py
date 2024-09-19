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

def e_levels_by_site(df):

    df['log_ecoli'] = np.log(df['ecoli'])
    # Resample by week and calculate the mean ecoli level, grouping by beachname and sitename
    
    sns.set(style="whitegrid", context="talk")

    # Create the line plot
    plt.figure(figsize=(12, 6))
    sns.lineplot(
        df,
        x='collectiondate',
        y='log_ecoli',
        hue='beachname',  # Color by beachname
        style='beachname',  # Style lines by sitename
        dashes=False,  # Solid lines
        palette='tab10'  # Optional: Choose a color palette
    )

    plt.title('E. coli Levels Over Time by Site and Beach')
    plt.xlabel('Collection Date')
    plt.ylabel('E. coli Level')
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.legend(title='Beach Name', bbox_to_anchor=(1.05, 1), loc='upper left')  # Place legend outside the plot
    plt.tight_layout() 

    plt.savefig("results/ecoli_levels_plot.png", dpi=300, bbox_inches='tight') 
    return "graph_1 made"

def main():
    #Import Data
    data = pd.read_csv("data/cleaned_water_quality_data.csv")
    df = pd.DataFrame(data)

    #with open("results/summary_table.md", "w") as file:
    #    file.write(create_counts(df))
    
    #with open("results/ecoli_stats.md", "w") as file:
    #    file.write(create_ecoli_stats(df))

    e_levels_by_site(df)

# Run the script
if __name__ == "__main__":
    main()
