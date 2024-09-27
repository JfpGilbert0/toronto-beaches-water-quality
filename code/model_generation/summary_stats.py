# Import packages
import pandas as pd
import tabulate as tab
from IPython.display import display

# Import data
data = pd.read_csv("../data/cleaned_water_quality_data.csv")
df = pd.DataFrame(data)

df['collectiondate'] = pd.to_datetime(df['collectiondate'])
# Summary stats tables
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

with open("../results/tables/data_summary.md", "w") as file:
        file.write(summary_stats.to_csv())
