import pandas as pd

df_1 = pd.read_csv('../output/type_1_fire.csv')

df_2 = pd.read_csv('../output/type_1_grass.csv')


df_3 = pd.concat([df_1, df_2])

df_3.to_csv("../output/type_1_fire_and_grass_merged.csv")
