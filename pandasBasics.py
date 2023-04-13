# It's build on the Numpy package and it's key data structure
# is called DataFrame. DataFrames allow you to store and manipulate
# tabular data in rows of observations and columns of variables.

#! There are several way to create DataFrames

countries = {
  "countries": ["Brazil", "Russia", "India", "China", "South Africa"],
  "capital": ["Brasilia", "Moscow", "New Dehli", "Beijing", "Pretoria"],
  "area (Km)": [8.516, 17.10, 3.286, 9.597, 1.221],
  "population (M)": [200.4, 143.5, 1252, 1357, 52.98]
}

import pandas as pd

brics = pd.DataFrame(countries)
print(brics)

# If you want to change the index values to show somethings else 
# besides number you can do it as follows

brics.index = ["BR", "RU", "IN", "CH", "SA"]
print(f"\n Changed index \n {brics}")

# ! DataFrames also can be created from csv files
# they can be imported using pd,read_csv

# Import the cars.csv data: cars
# cars = pd.read_csv('cars.csv')


# ! Indexing DataFrames
#  You can either use a single bracket or a double bracket.
# The single bracket will output a Pandas Series (give info of 
# name and datatype), while a double bracket will output a 
# Pandas DataFrame.
print("\n Indexing DataFrames \n")
print(brics[["countries"]])

#! Rows are known as observations
print("\n Ranges of Rows \n")
print(brics[0:2])


# You can also use loc and iloc to perform just about any data
# selection operation. loc is label-based, which means that you
# have to specify rows and columns based on their row and column 
# labels. iloc is integer index based, so you have to specify rows
# and columns #! by their integer index

print("\n Using loc and iloc \n")
print(brics.iloc[2])
print(brics.loc[["RU", "CH"]])