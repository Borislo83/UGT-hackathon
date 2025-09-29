import pandas as pd

dataset_paths = ["csvs/accidents_2017.csv", "csvs/air_quality_Nov2017.csv", "csvs/air_stations_Nov2017.csv", "csvs/bus_stops.csv", "csvs/deaths.csv","csvs/immigrants_by_nationality.csv","csvs/immigrants_emigrants_by_age.csv","csvs/immigrants_emigrants_by_destination.csv","csvs/immigrants_emigrants_by_destination2.csv","csvs/immigrants_emigrants_by_sex.csv","csvs/life_expectancy.csv", "csvs/most_frequent_baby_names.csv","csvs/most_frequent_names.csv","csvs/population.csv","csvs/transports.csv","csvs/unemployment.csv"]
output_file_path = "output.txt"

for dataset in dataset_paths:
    
    #Do the operations to find percentage null values for each column
    data_frame = pd.read_csv(dataset)
    rows_with_null = data_frame.isnull().sum()
    total_rows = len(data_frame)
    rows_with_null_percentage = rows_with_null / total_rows * 100
    
    #Display in terminal
    print(f"\nDataset:{dataset} \n")
    print(rows_with_null_percentage)
    
    
    with open(output_file_path, "a") as file:  
        file.write("\n\n")
        file.write(f"\nDataset: {dataset}\n")
        file.write(rows_with_null_percentage.to_string())

    

    
