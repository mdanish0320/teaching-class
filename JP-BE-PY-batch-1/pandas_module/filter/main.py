import re
import pandas as pd

df = pd.read_csv('../data/pokemon_data.csv')

# select all rows that contains the value "Grass" in Column "Type 1"
new_df = df.loc[df['Type 1'] == 'Grass']
print(new_df)

# select all rows that contains the value "Grass" in Column "Type 1" and value "Poison" in Column "Type 2"
new_df = df.loc[(df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')]
print(new_df)

# select all rows that contains the value "Grass" in Column "Type 1" and value "Poison" in Column "Type 2" and whose HP is greater than 70
new_df = df.loc[(df['Type 1'] == 'Grass') & (
    df['Type 2'] == 'Poison') & (df['HP'] > 70)]
print(new_df)

# select all rows that contains the value "Grass" in Column "Type 1" and value "Poison" in Column "Type 2"
# OR
# select all rows that contains the value "Fire" in Column "Type 1" and value "Flying" in Column "Type 2"
new_df = df.loc[((df['Type 1'] == 'Grass') & (df['Type 2'] == 'Poison')) |
                ((df['Type 1'] == 'Fire') & (df['Type 2'] == 'Flying'))]
print(new_df)

# select all rows that contains the value "Poison" OR "Water" in column "Type 2"
new_df = df[df['Type 2'].isin(['Poison', 'Water'])]
print(new_df)

# select all rows that DOES NOT contain the value "Poison" OR "Water" in column "Type 2"
# in other words
# select all rows but remove the rows that contains the value "Poison" OR "Water" in column "Type 2"
new_df = df[~df['Type 2'].isin(['Poison', 'Water'])]
print(len(new_df))

# # find sub string using str method contains
# find the data that contains the value Mega in column Name
df.loc[df['Name'].str.contains("Mega")]

# find the data that contains the value Fire OR Grass in column Name
df.loc[df['Name'].str.contains("Fire | Grass", flags=re.I, regex=True)]  # case insensitive

# find the data that whose value starts with pi in the column Name
df.loc[df['Name'].str.contains("^pi[A-Z]*", flags=re.I, regex=True)]  # case insensitive

