import requests
# alpha vantage api key: BIDSOENB1ORVQ4BI

import pandas as pd

# Load the CSV file

file_name = "SMA_195.csv"
df = pd.read_csv(file_name)

# Reverse the DataFrame
df = df.iloc[::-1].reset_index(drop=True)

# Save it back to the same file
df.to_csv(file_name, index=False)
