## installation

# pip3 install pandas
# OR
# pip install pandas

import pandas as pd

df = pd.read_csv('../data/pokemon_data.csv')

# display count of num of columns and rows in file
print(df.shape) # (801, 12) # (rows, columns)


# display column names
print(df.columns)
print(
  list(df.columns)
)


# display first 5 rows of the file
print(df.head())
print(df.head(20)) # display first 20 rows


# display last 5 rows of the file
print(df.tail())
print(df.tail(20))  # display last 20 rows


# display all rows and all columns
print(df)


# display specified row data 
print(df.loc[5]) # 5th row data

# display whole data of 2 rows
print(df.loc[[5, 10], : ])  # 5th row and 10th row


# display 1 column data
print(df['Name'])
# another way
print(
  df.loc[: , ['Name']]
) 

# display whole data of 2 columns
print(df[ ['Name', 'Type 1'] ])


# display single value
print(
  df.loc[0, ['Name']]
) # name in first row


# display multiple values of in rows and columns
print(
  df.loc[[0, 5], ['Name', 'Type 1']]
)  # name and type 1 value from row 0 and row 5


# save file to CSV format
df.to_csv("../output/basic_example.csv")
