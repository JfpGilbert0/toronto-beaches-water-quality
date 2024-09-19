import pandas as pd 

data = pd.read_csv("data/cleaned_water_quality_data.csv")
df = pd.DataFrame(data)
print(df['loc_type'].unique())