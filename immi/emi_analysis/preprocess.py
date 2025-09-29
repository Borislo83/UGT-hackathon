import pandas as pd
import matplotlib.pyplot as plt

#selecting relevant rows for analysis
data_frame = pd.read_csv("csvs/immigrants_emigrants_by_sex.csv")


different_data_frame = data_frame[['Year','Immigrants','Emigrants']]
different_data_frame = different_data_frame.groupby('Year')[['Emigrants','Immigrants']].sum().reset_index()
different_data_frame['Difference'] = different_data_frame['Immigrants'] - different_data_frame['Emigrants']
different_data_num = different_data_frame["Difference"].tolist()
different_data_year = different_data_frame['Year'].tolist()
print(different_data_frame)



immigrant_data = data_frame.groupby('Year')['Immigrants'].sum().reset_index()
immigrant_num = immigrant_data["Immigrants"].tolist()
immigrant_year = immigrant_data['Year'].tolist()

emigrant_data = data_frame.groupby('Year')['Emigrants'].sum().reset_index()
emigrant_num = emigrant_data["Emigrants"].tolist()
emigrant_year = emigrant_data['Year'].tolist()




plt.scatter(emigrant_year, emigrant_num)


plt.title('Emigrant Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()

plt.scatter(immigrant_year, immigrant_num)


plt.title('Immigrant Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()

plt.scatter(different_data_year, different_data_num)


plt.title('Net Immigration Graph')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

plt.show()
# print(emigrant_data)
# print(immigrant_data)




