import pandas as pd

df = pd.read_csv('../data/pokemon_data.csv')

# select all rows that contains the value "Grass" in Column "Type 1"
new_df = df.loc[df['Type 1'] == 'Grass']

new_df_2 = df.loc[df['Type 1'] == 'Fire']


new_df.to_csv("../output/type_1_grass.csv")
new_df_2.to_csv("../output/type_1_fire.csv")


