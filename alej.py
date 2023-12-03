#%%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Display Inital Stats

#%%
# Read the CSV file into a Pandas DataFrame
data = pd.read_csv('/Users/alejc/OneDrive/Desktop/CS158/LA-Crime/data/crime_in_la.csv')

# Display the first few rows to understand the data
print(data.head())

# Check basic information about the dataset
print(data.info())

# Check for missing values
print(data.isnull().sum())

# Clean Data 
#%% 
data = pd.read_csv('/Users/alejc/OneDrive/Desktop/CS158/LA-Crime/data/crime_in_la.csv')

# Display the columns in the DataFrame
print("Columns before removing:")
print(data.columns.tolist())

# Remove a columns
columns_to_remove = ['DATE OCC','DR_NO', 'AREA NAME', 'Rpt Dist No', 'Crm Cd Desc', 'Mocodes', 'Premis Desc', 'Weapon Desc', 'Status', 'Status Desc', 'LOCATION', 'LAT', 'LON']
for c in columns_to_remove:
    if c in data.columns:
        data.drop(columns=c, inplace=True)
    else:
        print(f"Column '{c}' not found.")

# Display the columns in the modified DataFrame
print("\nColumns after removing:")
print(data.columns.tolist())

# Bin Ages 
# ages = data['Vict Age']

#if the age is 0 (unknown) drop
ages = data[data['Vict Age'] != 0]


# Helper to categorize age into decades
def categorize_decade(age):
    return (age // 10) * 10
data['Vict Age'] = ages.apply(categorize_decade)

# Bin Times into hour blocks
data['TIME OCC'] = pd.to_datetime(data['TIME OCC']).dt.hour
# helper to categorize hour into hour blocks
def categorize_hour(hour):
    return hour
data['TIME OCC'] = data['TIME OCC'].apply(categorize_hour)

# output new CSV file 
data.to_csv('Simple_LA_Crime.csv', index=False)  # Set index=False to avoid writing row indices    

#%%
