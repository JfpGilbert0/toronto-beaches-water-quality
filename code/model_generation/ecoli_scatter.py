# Import packages
import pandas as pd
import tabulate as tab
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import MaxNLocator

# Import data
data = pd.read_csv("../data/cleaned_water_quality_data.csv")
df = pd.DataFrame(data)

# generate graph
df['collectiondate'] = pd.to_datetime(df['collectiondate'])
df['log_ecoli'] = np.log(df['ecoli'])

sns.set(style="whitegrid", context="talk")

# Create a scater plot
sns.scatterplot(data=df, x='collectiondate', y='log_ecoli', hue='beachname', palette='Set1', s=20, alpha=0.7)

# Set title and labels
plt.title('E. coli Levels Over Time by Site and Beach', fontsize=16)
plt.xlabel('Collection Date', fontsize=14)
plt.ylabel('E. coli Level (Log(MPN/100mL))', fontsize=14)
plt.grid(True, axis='x')
# modify x axis labels
plt.xticks(df['collectiondate'], fontsize=10, rotation=75 )  
plt.yticks(df['log_ecoli'], fontsize=10)
plt.tight_layout()

plt.gca().xaxis.set_major_locator(MaxNLocator(nbins=17))
plt.gca().yaxis.set_major_locator(MaxNLocator(nbins=10))

plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %Y'))
plt.legend(title='Beach Name', loc='upper left', bbox_to_anchor=(1.05, 1))
 

plt.show