# -- coding: utf-8 --
"""
Created on Mon Nov 11 18:56:24 2024

@author: Owner
"""
"1"
import pandas as pd
import os
path = "C:/Users/Owner/Downloads"
filename = 'Bicycle_Thefts_Open_Data_-6397344066137313418.csv'
fullpath = os.path.join(path,filename)
data_group8 = pd.read_csv(fullpath)

"Display the column names"
data_group8.columns.values

"Display the shape of the data frame i.e number of rows and number of columns"
data_group8.shape

"Display the main statistics of the data"
data_group8.describe()

"Display the types of columns"
data_group8.dtypes

"Display the first five records"
data_group8.head(5)

"2"
#Means of Columns"
means = data_group8.mean()
print(means)
#Median of Columns
medians = data_group8.median()
print(medians)
#Standard Deviation of Columns
std_devs = data_group8.std()
print(std_devs)
#Correlation between Numerical Columns
correlations = data_group8.corr()
print(correlations)

"3"
# Check for missing values 
missing_data = data_group8.isnull().sum()
"Missing Data Counts"
print(missing_data)


"4"
import pandas as pd
import matplotlib.pyplot as plt
"Trend of bike thefts over the years"
# Group data by year and count occurrences
thefts_by_year = data_group8['OCC_YEAR'].value_counts().sort_index()
# Plot the time series
plt.figure(figsize=(10, 6))
thefts_by_year.plot(kind='line', marker='o', linestyle='-', color='b')
plt.title('Number of Bike Thefts by Year')
plt.xlabel('Year')
plt.ylabel('Number of Thefts')
plt.grid(True)
plt.show()

"5"
"Histogram of bike thefts by occurrence year"
plt.figure(figsize=(10, 6))
data_group8['OCC_YEAR'].plot(kind='hist', bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram of Bike Thefts by Year')
plt.xlabel('Occurrence Year')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

"6"
"Box plot of bike theft occurrences over the years"
plt.figure(figsize=(10, 6))
data_group8.boxplot(column='OCC_YEAR', grid=True)
plt.title('Box Plot of Bike Thefts by Year')
plt.ylabel('Occurrence Year')
plt.grid(True)
plt.show()
