import pandas as pd

def null_finder(output_file_path, dataset_path):
    output_file_path = str(output_file_path)

    dataset_path = str(dataset_path)

    data_frame = pd.read_csv(dataset_path)
    null_rows = data_frame[data_frame.isnull().any(axis=1)]

    null_rows.to_csv(output_file_path, index=False)

null_finder("transports_cleaning/nulls.csv","transports_cleaning/duplicate_removed.csv")

    

    
