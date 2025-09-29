import pandas as pd

data_frame = pd.read_csv("transports_cleaning/duplicate_removed.csv")


rows_with_null = data_frame.isnull().sum()
total_rows = len(data_frame)
rows_with_null_percentage = rows_with_null / total_rows * 100
    
#Display in terminal
print(f"\nDataset:{data_frame} \n")
print(rows_with_null_percentage)