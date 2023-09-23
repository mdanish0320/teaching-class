# # Modify
# update column names
# all
# df.columns = ['col1', 'col2', 'col3']
## selected
# df.rename(columns={'col1': 'col_1', 'col2': 'col_2'})

# # # update selected 1 complete row
# df.loc[0] = ['val_1', 'val_2', 'val_3']
# # update few column in selected row
# df.loc[0, ['col_1', 'col_2']] = ['val_1', 'val_2']

# # # update whole column
# df['email'] = df['email'].str.lower()

# # # conditional update
# filt = (df['email' == 'danish@abc.com'])
# df.loc[filt, 'email'] = 'new_email@gmail.co'

# df.drop('col_name', axis=1) # delete column
# df.drop(index_name, axis=0) # delete row named “0”
