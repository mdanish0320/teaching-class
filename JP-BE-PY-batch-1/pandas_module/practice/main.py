import pandas as pd
import numpy as np


df = pd.read_csv('pokemon_data.csv')


# # count num of columns and rows
# print(df.shape)

# # view the columns in file
# print(df.columns)

# # see data of first few rows
# print(df.head())

# # see data of last few rows
# print(df.tail())

# # see data of first 10 rows
# print(df.head(10))




# # single value 
# print(df.loc[0, 'Name'])

# # single but specific whole row
# print(df.loc[0]) # Label of Column



# # single but specific whole column
# print(df.loc[: , ['Name']])

# shorthand
# # display whole data of 2 columns
# print(df[ ['Name', 'Type 1'] ])


# # display not whole data but 2 rows and 2 columns
# print(df.loc[[0, 1] , ['Name', "Type 1"]])


# # filter
# new_df = df.loc[ df['Type 1'] == 'Grass']
# print(new_df)

# new_df = df.loc[ (df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') ]
# print(new_df)

# new_df = df.loc[ (df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
# print(new_df)

# new_df = df.loc[ (df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70)]
# print(new_df)

# new_df = df.loc[ ((df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison') & (df['HP'] > 70))  |  
#                 ((df['Type 1'] == 'Fire') & (df['Type 2'] == 'Flying') & (df['HP'] > 70))]
# print(new_df)

# new_df = df[ df['Type 2'].isin(['Poison', 'Water']) ]
# print(new_df)

# new_df = df[ ~df['Type 2'].isin(['Poison', 'Water', 'Flying', 'Dark', 'Fairy', 'Dragon', 'Ground', np.nan, 'Grass', 'Fighting', 'Normal']) ]
# print(len(new_df))



# Sort

# # sort data by rows
# print(df.sort_index(axis=0, ascending=False))

# # sort data by columns
# print(df.sort_index(axis=1, ascending=True))

# print(list(df.index))

# # sort by multiple columns
# df.sort_values(by=['Type 1', 'Attack'], ascending=[False, True], inplace=True)
# print(df[ ['Type 1', 'Attack'] ])


# Aggregation
# Group by

# find unique values in Type 1
# print(df['Type 1'].nunique())

# for x in df['Type 1'].unique():
#     print(x)


# count
# sum
# mean -> average
# min
# max
# median

# print(df.groupby('Type 1').nunique()['Name'])

# new_df = df.groupby("Type 1").count()['Type 2']
# print(new_df)

# # count valid types 2 in group BUg
# proof on bug type
# new_df = df.loc[ (df['Type 1'] == 'Bug')]
# print(len(new_df))
# # print(new_df)
# x = 0
# for index, row in new_df.iterrows():
#     if pd.isna(row['Type 2']):
#         x += 1
# print(x)


# # find unique values of type 2 in group Type 1
# new_df = df.groupby("Type 1").nunique()['Type 2']
# print(new_df)

# # proof on bug type
# new_df = df.loc[ (df['Type 1'] == 'Bug')]
# print(len(new_df))
# ss = set()
# for index, row in new_df.iterrows():
#     ss.add(row['Type 2'])
# print(len(ss))
# print(ss)

# # find out the highest attack of type 1 and type 2
# new_df = df.groupby(["Type 1", "Type 2"]).max().sort_values(by=['Type 1', 'Attack', 'Type 2', ], ascending=[True, False, True])['Attack']
# print(new_df.head(20))


# Modify
# join,  Merge, Join
# str contains
# deleting duplicates

# example data
# https://github.com/KeithGalli/Pandas-Data-Science-Tasks/tree/master/SalesAnalysis/Sales_Data







