import pandas as pd
import matplotlib.pyplot as plt

dataset_path = "fixed_datasetdupes/fixed-dupes-busstops.csv"
df = pd.read_csv(dataset_path)
print(df)

df = df.groupby('District.Name').size().reset_index(name="count")
print(df)

plt.pie(df['count'], labels=df['District.Name'], autopct='%1.1f%%')
plt.axis('equal')
# plt.title('Distribution of Bus stops by District')

# Display the chart
plt.show()

