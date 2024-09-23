import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data (ensure the path to your CSV is correct)
data = pd.read_csv("../data/cleaned_water_quality_data.csv")
df = pd.DataFrame(data)

# Ensure the collectiondate is in datetime format
df['collectiondate'] = pd.to_datetime(df['collectiondate'], errors='coerce', format='%Y-%m-%d')

# Add a column for the day of the week
df['day_of_week'] = df['collectiondate'].dt.day_name()

df['above_88'] = df['ecoli'].apply(lambda x: 1 if x > 88 else 0)

#summary table for dow.
day_counts = df['day_of_week'].value_counts().reindex([
    'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'
]).reset_index()

# Rename the columns for clarity
day_counts.columns = ['day_of_week', 'count']

# Display the summary table
print(day_counts)
# Group by day of the week and beachname, then calculate average E. coli levels
average_dangerous = df.groupby(['day_of_week', 'beachname'])['above_88'].mean().reset_index()

# Sort days of the week in the typical order
average_dangerous['day_of_week'] = pd.Categorical(
    average_dangerous['day_of_week'],
    categories=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    ordered=True
)

# Create binary value for dangeroud e-coli levels


# Create the bar chart
plt.figure(figsize=(14, 8))
sns.barplot(data=average_dangerous, x='day_of_week', y='above_88', hue='beachname', palette='viridis')
plt.title('Average times Ecoli levels above 88MLN/100ml', fontsize=15)
plt.xlabel('Day of the Week', fontsize=14)
plt.ylabel('Average days, E. coli Level above 88 (MPN/100mL)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(title='Beach Name', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()