import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#opening dataset
dataset_path = "fixed_datasets/fixed-NaNs-life_expectancy.csv"
df = pd.read_csv(dataset_path)

#getting average life expectancy for each neighborhood
df['avgle'] = df[['2006-2010','2007-2011','2008-2012','2009-2013','2010-2014']].sum(axis=1)
df['avgle'] = df['avgle']/5

#removing unnecessary columns
df = df.drop(['2006-2010','2007-2011','2008-2012','2009-2013','2010-2014'], axis=1)

#prepare male column for merge
male_df = df[df['Gender'] == 'Male']
male_df.rename(columns={'avgle': 'avgle_male'}, inplace=True)
male_df.drop(columns=['Gender'])
male_df = male_df.drop("Gender", axis=1)
male_df.reset_index(drop=True, inplace=True)

#prepare female column for merge
female_df = df[df['Gender'] == 'Female']
female_df.rename(columns={'avgle': 'avgle_female'}, inplace=True)
female_df = female_df.drop("Gender", axis=1)
female_df.reset_index(drop=True, inplace=True)

#full inner join dataa(no new rows)
merged_df = pd.merge(male_df, female_df, on='Neighborhood', how='inner')

#drop unnecessary columns from joining
merged_df.drop("Unnamed: 0_y", axis=1, inplace=True)
merged_df.drop("Unnamed: 0_x", axis=1, inplace=True)

#round data to int
merged_df['avgle_male'] = merged_df['avgle_male'].round(0).astype(int)
merged_df['avgle_female'] = merged_df['avgle_female'].round(0).astype(int)

#leave data in a output.csv to chec,
merged_df.to_csv('fixed_datasetdupes/output.csv', index=False)

# merged_df = merged_df.sample(20)
#swarmplot
sns.swarmplot(x='avgle_male', y='Neighborhood', data=merged_df, color='blue')
sns.swarmplot(x='avgle_female', y='Neighborhood', data=merged_df, color='red')

# Set plot labels and title
plt.xlabel('Average Life Expectancy')
plt.ylabel('Neighborhood')
plt.title('Average Life Expectancy by Neighborhood and Gender')

plt.show()

#jointplot
sns.jointplot(x='avgle_male', y='avgle_female', data=merged_df, kind='scatter')

# Set plot labels and title
plt.xlabel('Average Life Expectancy (Male)')
plt.ylabel('Average Life Expectancy (Female)')
plt.title('Average Life Expectancy Comparison between Male and Female')

# Display the plot
plt.show()

#histogram male
sns.histplot(data=merged_df, x='avgle_male', kde=True)

# Set plot labels and title
plt.xlabel('Average Life Expectancy (Male)')
plt.ylabel('Frequency Density}')
plt.title('Distribution of Average Life Expectancy for Males')


# Display the plot
plt.show()

#female histogram
sns.histplot(data=merged_df, x='avgle_female', kde=True, color='red')

# Set plot labels and title
plt.xlabel('Average Life Expectancy (Male)')
plt.ylabel('Frequency Density}')
plt.title('Distribution of Average Life Expectancy for Female')


# Display the plot
plt.show()