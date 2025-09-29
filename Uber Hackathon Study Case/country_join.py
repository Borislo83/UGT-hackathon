import pandas as pd

power_file_path = "/Users/borislo830/Desktop/Uber Hackathon Study Case/global_power_plant_database.csv"
country_file_path = "/Users/borislo830/Desktop/Uber Hackathon Study Case/country_code_data.csv"

country = pd.read_csv(country_file_path)
power = pd.read_csv(power_file_path)


# Perform the left join on the multiple join conditions
cleaned_df = pd.merge(power, country, left_on='country',
                      right_on='alpha-3', how='left')

# cleans for row without any null values
# cleaned_df = merged_df.dropna(how='any')

print(cleaned_df.shape[0])

# saving to a .csv
cleaned_df.to_csv(
    '/Users/borislo830/Desktop/Uber Hackathon Study Case/output.csv', index=False)
