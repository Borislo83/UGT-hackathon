import pandas as pd
dataset_path = "fixed_datasets/fixed-NaNs-bus_stops.csv"

output_file_path = "fixed_datasetdupes/fixed-dupes-busstops.csv"

data_frame = pd.read_csv(dataset_path)
data_frame = data_frame.drop_duplicates(subset=["Bus.Stop","District.Name","Neighborhood.Name"])

data_frame.to_csv(output_file_path, index=False)
print(data_frame)


    

    
