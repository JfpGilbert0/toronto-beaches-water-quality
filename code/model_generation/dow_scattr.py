import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator

# Sample data creation (replace this with your actual data)
data = pd.read_csv("data/cleaned_water_quality_data.csv")

# Create a DataFrame
df = pd.DataFrame(data)

# Add a column for the day of the week
df['collectiondate'] = pd.to_datetime(df['collectiondate'])
df['day_of_week'] = df['collectiondate'].dt.day_name()

# Days of the week order for plotting
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Create scatter plots for each day of the week
for day in days_of_week:
    # Filter data for the specific day of the week
    day_df = df[df['day_of_week'] == day]
    
    # Create the scatter plot
    plt.figure(figsize=(14, 7))
    sns.scatterplot(data=day_df, x='collectiondate', y='ecoli', hue='beachname', palette='Set1', s=75, alpha=0.6)
    plt.title(f'E. coli Levels Over Time - {day}', fontsize=16)
    plt.xlabel('Collection Date', fontsize=14)
    plt.ylabel('E. coli Level', fontsize=14)
    plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=8))
    plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %Y'))
    plt.xticks(rotation=45, ha='right')
      # Log scale for better representation
    plt.grid(visible=True, linestyle='--', linewidth=0.5, alpha=0.7)
    plt.legend(title='Beach Name', loc='upper left', bbox_to_anchor=(1.05, 1))
    plt.tight_layout()
    plt.show()