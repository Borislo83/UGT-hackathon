import pandas as pd
output_file_path = "transports_cleaning/duplicate_removed.csv"

dataset_path = "csvs/transports.csv"

data_frame = pd.read_csv(dataset_path)
data_frame = data_frame.drop_duplicates(subset="Station")

data_frame.to_csv(output_file_path, index=False)
print(data_frame)


    

    
