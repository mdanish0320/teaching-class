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
