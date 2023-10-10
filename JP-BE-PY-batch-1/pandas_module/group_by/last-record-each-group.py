import pandas as pd

# Sample DataFrame
data = {
    'patient_id': [1, 1, 2, 2, 3],
    'record_date': ['2023-01-01', '2023-02-01', '2023-01-15', '2023-02-15', '2023-01-10']
}

df = pd.DataFrame(data)

# Convert 'record_date' column to datetime
df['record_date'] = pd.to_datetime(df['record_date'])


## first solution
# Sort the DataFrame by 'record_date' in descending order within each group
df_sorted = df.sort_values(by='record_date', ascending=False)
# Get the index of the first occurrence of each 'patient_id' group after sorting
latest_record_indices = df_sorted.groupby('patient_id').head(1).index

## second solution
# Find the index of the maximum 'record_date' within each 'patient_id' group
latest_record_indices = df.groupby('patient_id')['record_date'].idxmax()



# Get the latest records using the obtained indices
latest_records = df.loc[latest_record_indices]

print(latest_records)