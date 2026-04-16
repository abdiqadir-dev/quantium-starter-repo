import pandas as pd
import os

# 1.  the paths to the data files
data_files = [
    "./data/daily_sales_data_0.csv",
    "./data/daily_sales_data_1.csv",
    "./data/daily_sales_data_2.csv"
]

processed_dataframes = []

for file in data_files:
    df = pd.read_csv(file)

    df = df[df['product'].str.lower() == 'pink morsel']

    df['price'] = df['price'].replace('[\$,]', '', regex=True).astype(float)
    df['quantity'] = df['quantity'].astype(int)
    
    df['sales'] = df['price'] * df['quantity']

    df = df[['sales', 'date', 'region']]

    processed_dataframes.append(df)

final_df = pd.concat(processed_dataframes)

final_df.to_csv("formatted_data.csv", index=False)

print("Data processing complete! Go look for 'formatted_data.csv' in your folder.")