import pandas as pd

df = pd.read_csv('../data/pokemon_data.csv')


# add new data as dict format
new_row = {'#': 222, 'Name': "New Pokemon", 'Type 1': "New Type 1", "Type 2": "New Type 1"}
df = df.append(new_row, ignore_index=True)

print(df.tail())

# add new data as dict format
new_row = [
            {'#': 333, 'Name': "New Pokemon 2", 'Type 1': "New Type 3", "Type 2": "New Type 3"},
            {'#': 444, 'Name': "New Pokemon 4", 'Type 1': "New Type 4", "Type 2": "New Type 4"}
            ]
df = df.append(new_row, ignore_index=True)

print(df.tail())
