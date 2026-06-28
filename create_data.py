import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

products = ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard', 'Mouse', 'Headphones', 'Printer']
categories = {'Laptop': 'Electronics', 'Phone': 'Electronics', 'Tablet': 'Electronics',
              'Monitor': 'Electronics', 'Keyboard': 'Accessories', 'Mouse': 'Accessories',
              'Headphones': 'Accessories', 'Printer': 'Office'}
regions = ['North', 'South', 'East', 'West']

rows = []
start_date = datetime(2023, 1, 1)

for i in range(1, 501):
    product = random.choice(products)
    sale = round(random.uniform(100, 2000), 2)
    profit = round(sale * random.uniform(0.1, 0.4), 2)
    date = start_date + timedelta(days=random.randint(0, 364))
    rows.append({
        'Order_ID': f'ORD{i:04d}',
        'Product': product,
        'Category': categories[product],
        'Region': random.choice(regions),
        'Sales': sale,
        'Profit': profit,
        'Date': date.strftime('%Y-%m-%d')
    })

df = pd.DataFrame(rows)
df.to_csv('sales_data.csv', index=False)
print("✅ Dataset created! File: sales_data.csv")
print(f"Total rows: {len(df)}")
print(df.head())