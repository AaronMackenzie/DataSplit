import pandas as pd

# Load the dataset
dataset = pd.read_csv('dataset.csv')

# Define age ranges
age_ranges = [(0, 11), (12, 27), (28, 43), (44, 59), (60, 78), (79, 96)]

# Iterate over age ranges and split the dataset
for age_range in age_ranges:
    start_age, end_age = age_range
    filtered_data = dataset[(dataset['age'] >= start_age) & (dataset['age'] <= end_age)]
    filename = f'DatasetOf{start_age}-{end_age}.csv'
    filtered_data.to_csv(filename, index=False)

