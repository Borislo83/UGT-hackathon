import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#opening dataset
dataset_path = "cluster_analysis/clustered_neighborhoods.csv"
df = pd.read_csv(dataset_path)

population_df = df[['Neighborhood.Name', '2013_population', '2014_population', '2015_population', '2016_population', '2017_population', 'Clusters', 'Clusters Category']]

population_df['avg_population'] = population_df[['2013_population', '2014_population', '2015_population', '2016_population', '2017_population']].mean(axis=1)

# Remove the columns '2013_population', '2014_population', '2015_population', '2016_population', '2017_population'
population_df.drop(columns=['2013_population', '2014_population', '2015_population', '2016_population', '2017_population'], inplace=True)
population_df['avgle_male'] = population_df['avg_population'].round(0).astype(int)
print(population_df)

population_df = population_df.groupby('Clusters').sum("avg_population").reset_index()
print(population_df)
avg_population = population_df['avg_population'].tolist()
clusters = population_df['Clusters'].tolist()

def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct,v=val)
    return my_autopct

print(avg_population, clusters)

plt.pie(population_df['avg_population'], labels=population_df['Clusters'], autopct=make_autopct(avg_population))
plt.title("Percentage population distribution across each cluster")
plt.axis('equal')
plt.legend(title="Cluster", loc="center left", bbox_to_anchor=(1, 0.5))
# plt.title('Distribution of Bus stops by District')

# Display the chart
plt.show()