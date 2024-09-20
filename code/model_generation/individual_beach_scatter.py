
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator

data = pd.read_csv("../data/cleaned_water_quality_data.csv")
df = pd.DataFrame(data)

# Separate data by beach
beach1_df = df[df['beachname'] == 'Sunnyside Beach']
beach2_df = df[df['beachname'] == 'Marie Curtis Park East Beach']

# Create the plot for Sunnyside Beach
plt.figure(figsize=(14, 7))
sns.scatterplot(data=beach1_df, x='collectiondate', y='ecoli', hue='sitename', palette='Set1', s=75, alpha=0.6)
plt.title('E. coli Levels Over Time - Sunnyside Beach', fontsize=16)
plt.xlabel('Collection Date', fontsize=14)
plt.ylabel('E. coli Level', fontsize=14)
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=8))
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %Y'))
plt.xticks(rotation=45, ha='right')
  # Log scale for better representation
plt.grid(visible=True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(title='Site Name', loc='upper left', bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()

# Create the plot for Marie Curtis Park East Beach
plt.figure(figsize=(14, 7))
sns.scatterplot(data=beach2_df, x='collectiondate', y='ecoli', hue='sitename', palette='Set2', s=75, alpha=0.6)
plt.title('E. coli Levels Over Time - Marie Curtis Park East Beach', fontsize=16)
plt.xlabel('Collection Date', fontsize=14)
plt.ylabel('E. coli Level', fontsize=14)
plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=8))
plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %Y'))
plt.xticks(rotation=45, ha='right')
  # Log scale for better representation
plt.grid(visible=True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend(title='Site Name', loc='upper left', bbox_to_anchor=(1.05, 1))
plt.tight_layout()
plt.show()
