import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data (ensure the path to your CSV is correct)
data = pd.read_csv("../data/cleaned_water_quality_data.csv")
df = pd.DataFrame(data)

# Ensure the collectiondate is in datetime format
df['collectiondate'] = pd.to_datetime(df['collectiondate'], errors='coerce', format='%Y-%m-%d')

# Add a column for the day of the week
df['month'] = df['collectiondate'].dt.month_name()

# Group by day of the week and beachname, then calculate average E. coli levels
average_ecoli = df.groupby(['month', 'beachname'])['ecoli'].mean().reset_index()

# Sort days of the week in the typical order


# Create the bar chart
plt.figure(figsize=(14, 8))
sns.barplot(data=average_ecoli, x='month', y='ecoli', hue='beachname', palette='viridis')
plt.title('Average E. coli Rates by Day of the Week and Beach', fontsize=16)
plt.xlabel('Day of the Week', fontsize=14)
plt.ylabel('Average E. coli Level (MPN/100mL)', fontsize=14)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(title='Beach Name', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
