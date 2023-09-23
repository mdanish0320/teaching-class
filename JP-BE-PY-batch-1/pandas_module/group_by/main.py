# Aggregation
# Group by
import pandas as pd
df = pd.read_csv('../data/employee_data.csv')

# Common Aggregattion Methods
# count
# sum
# mean -> average
# min
# max
# median

# count how many employees are in each department
new_df = df.groupby(["Department"]).count()['Name']
print(new_df)

# count how many employees are in each department also tell how many are male and female in each groupe
new_df = df.groupby(["Department",'Gender']).count()
print(new_df)

# tell which department has most salary spent on
new_df = df.groupby(["Department"]).sum()['Salary']
print(new_df)

# tell which department has most salary spent on and also tell the how much salary spent on male and female in each department
new_df = df.groupby(["Department"]).sum()['Salary']
print(new_df)

# tell the average age of employees in each department
new_df = df.groupby(["Department"]).mean()['Age']
print(new_df)

# tell the max, min and mean age of employees in each department
new_df = df.groupby(['Department']).agg({"Age": ['min', 'max', 'mean']})
print(new_df)

 

