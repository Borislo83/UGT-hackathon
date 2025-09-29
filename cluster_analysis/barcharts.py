import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#opening dataset
dataset_path = "cluster_analysis/clustered_neighborhoods.csv"
df = pd.read_csv(dataset_path)

df['<18'] = df['10-14_population'] + df['15-19_population']
df['adults'] = df[['20-24_population', '25-29_population', '30-34_population', '35-39_population',
                   '40-44_population', '45-49_population', '50-54_population', '55-59_population',
                   '60-64_population', '65-69_population']].sum(axis=1)
df['seniors'] = df[['70-74_population', '75-79_population', '80-84_population', '85-89_population',
                    '90-94_population', '>=95_population']].sum(axis=1)

df['<18'] = df['<18'].round(0).astype(int)
df['adults'] = df['adults'].round(0).astype(int)
df['seniors'] = df['seniors'].round(0).astype(int)



# Display the updated DataFrame

selected_columns = ['<18', 'adults', 'seniors', 'Clusters Category']
df = df[selected_columns]
print(df)

df = df.groupby('Clusters Category')[['<18', 'adults','seniors']].sum().reset_index()
print(df)

df.set_index('Clusters Category', inplace=True)

#adjusting plot


# Create the stacked bar chart
df.plot(kind='barh', stacked=True,figsize=(12, 8))

# Set labels and title
plt.ylabel('Age groups')
plt.xlabel('Clusters')
plt.title('Age distribution by clusters')

# Display the chart
plt.show()

print(df)