# Sort

import pandas as pd

df = pd.read_csv('../data/pokemon_data.csv')

# # sort data by row index
print(df.sort_index(axis=0, ascending=False))

# # sort data by columns
print(df.sort_index(axis=1, ascending=True))
print(list(df.index))

# sort data by multiple columns
df.sort_values(by=['Type 1', 'Attack'], ascending=[False, True], inplace=True)
print(df[ ['Type 1', 'Attack'] ])
