import pandas as pd
# Read the two CSV files into separate dataframes
df1 = pd.read_csv('csvs/transports.csv')
df2 = pd.read_csv('Og_dataset/transports.csv')
# Use the compare() method of the dataframes to compare them
df_diff = df1.compare(df2)
print(df_diff)

datasets1 = ["csvs/accidents_2017.csv", "csvs/air_quality_Nov2017.csv", "csvs/air_stations_Nov2017.csv", "csvs/bus_stops.csv", "csvs/deaths.csv","csvs/immigrants_by_nationality.csv","csvs/immigrants_emigrants_by_age.csv","csvs/immigrants_emigrants_by_destination.csv","csvs/immigrants_emigrants_by_destination2.csv","csvs/immigrants_emigrants_by_sex.csv","csvs/life_expectancy.csv", "csvs/most_frequent_baby_names.csv","csvs/most_frequent_names.csv","csvs/population.csv","csvs/transports.csv","csvs/unemployment.csv"]
datasets2 = ["Og_dataset/accidents_2017.csv", "Og_dataset/air_quality_Nov2017.csv", "Og_dataset/air_stations_Nov2017.csv", "Og_dataset/bus_stops.csv", "Og_dataset/deaths.csv","Og_dataset/immigrants_by_nationality.csv","Og_dataset/immigrants_emigrants_by_age.csv","Og_dataset/immigrants_emigrants_by_destination.csv","Og_dataset/immigrants_emigrants_by_destination2.csv","Og_dataset/immigrants_emigrants_by_sex.csv","Og_dataset/life_expectancy.csv", "Og_dataset/most_frequent_baby_names.csv","Og_dataset/most_frequent_names.csv","Og_dataset/population.csv","Og_dataset/transports.csv","Og_dataset/unemployment.csv"]

for i in  range(len(datasets1)):
    df1 = pd.read_csv(datasets1[i])
    df2 = pd.read_csv(datasets2[i])
    df_diff = df1.compare(df2)
    print(df_diff)
