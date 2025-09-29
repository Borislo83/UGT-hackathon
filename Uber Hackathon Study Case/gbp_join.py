import pandas as pd

power_file_path = "/Users/borislo830/Desktop/Uber Hackathon Study Case/clean.csv"
gbp_file_path = "/Users/borislo830/Desktop/Uber Hackathon Study Case/gbp_data.csv"

gbp = pd.read_csv(gbp_file_path)
power = pd.read_csv(power_file_path)


# Perform the right join on the multiple join conditions
merged_df = pd.merge(power, gbp, left_on='country',
                     right_on='Country Code', how='left')

# Turning data from float to integer
merged_df['commissioning_year'] = merged_df['commissioning_year'].astype(int)

# Making sure data is within bounds of GBP data
filtered_df = merged_df[(merged_df['commissioning_year'] > 1960) & (
    merged_df['commissioning_year'] < 2022)]

filtered_df['extracted_gdp'] = None

#
for index, row in filtered_df.iterrows():
    commissioning_year = row['commissioning_year']
    gdp_value = row[str(commissioning_year)]

    # Set the extracted GDP value for the row
    filtered_df.loc[index, 'extracted_gdp'] = gdp_value

# defining what columns want for the output data
selected_columns = ['name', 'country', 'primary_fuel',
                    'commissioning_year', 'extracted_gdp']

# selecting desired columns
filtered_df = filtered_df[selected_columns]

# removing rows where there are NaN values as that will impact analysis
cleaned_df = filtered_df.dropna(how='any')

print(cleaned_df.shape[0])

# saving to a .csv
cleaned_df.to_csv(
    '/Users/borislo830/Desktop/Uber Hackathon Study Case/output.csv', index=False)
