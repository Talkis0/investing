import requests
# alpha vantage api key: BIDSOENB1ORVQ4BI

import pandas as pd

# Load the CSV file
df = pd.read_csv('SMA_10.csv')

# Reverse the DataFrame
df = df.iloc[::-1].reset_index(drop=True)

# Save it back to the same file
df.to_csv('SMA_10.csv', index=False)
