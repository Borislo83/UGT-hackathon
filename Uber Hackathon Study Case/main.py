import pandas as pd


file_path = "/Users/borislo830/Desktop/Uber Hackathon Study Case/global_power_plant_database.csv"

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Defining Country, primary fuel, name, year
selected_columns = ['name', 'country', 'primary_fuel', 'commissioning_year']

# Selecting the rows
selected_df = df[selected_columns]
# Dropping rows where a single column or more have a NaN/Null value
cleaned_df = df[selected_columns].dropna(how='any')


# Saving the data to an output file
cleaned_df.to_csv(
    '/Users/borislo830/Desktop/Uber Hackathon Study Case/output.csv', index=False)
print(df)
