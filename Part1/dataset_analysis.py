import pandas as pd

# Load the data into a dataframe
df = pd.read_csv('epss_scores.csv')

# Create a dictionary to store the counts for each interval
interval_counts = {}

# Iterate over the intervals
for i in range(11):
    low = i * 0.1
    high = (i + 1) * 0.1
    interval_counts[f'{low}-{high}'] = len(df[(df['epss'] >= low) & (df['epss'] < high)])

# Print the counts
print(interval_counts)
