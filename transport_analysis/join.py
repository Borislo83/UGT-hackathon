import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data_frame_bustops = pd.read_csv("fixed_datasets/fixed-NaNs-bus_stops.csv")
data_frame_transports= pd.read_csv("fixed_datasets/fixed-NaNs-transports.csv")

#Condense the data into district and number of stops per district and also renaming it for merging
data_frame_bustops = data_frame_bustops.groupby('District.Name').size().reset_index(name='count')
data_frame_bustops = data_frame_bustops.rename(columns={'count': 'busstops'})

#Doing the same for transport
data_frame_transports = data_frame_transports.groupby('District.Name').size().reset_index(name='count')
data_frame_transports = data_frame_transports.rename(columns={'count': 'trainstops'})


#merging the datasets
merged_df = pd.merge(data_frame_bustops, data_frame_transports, on='District.Name')
merged_df.to_csv('transport_analysis/all_stops.csv', index=False)

#sorting
merged_df['total_count'] = merged_df['busstops'] + merged_df['trainstops']

# Sort the DataFrame by the 'total_count' column in descending order
merged_df = merged_df.sort_values('total_count', ascending=True)

#drop temp table
merged_df.drop('total_count', axis=1, inplace=True)



#Setting index to district name

merged_df.set_index('District.Name', inplace=True)

#adjusting plot


# Create the stacked bar chart
merged_df.plot(kind='barh', stacked=True,figsize=(12, 8))

# Set labels and title
plt.ylabel('District Name')
plt.xlabel('Number of Bus/Train Stops ')
plt.title('Number of Bus Stops and Train Stops by District')

# Display the chart
plt.show()

print(merged_df)


