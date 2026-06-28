import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('sales_data.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month_name()
month_order = ['January','February','March','April','May','June','July','August','September','October','November','December']

fig, axes = plt.subplots(2, 2, figsize=(16, 10))
fig.suptitle('Sales Analysis Dashboard', fontsize=20, fontweight='bold')

top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False)
axes[0,0].bar(top_products.index, top_products.values, color='steelblue')
axes[0,0].set_title('Top Products by Sales')
axes[0,0].set_xlabel('Product')
axes[0,0].set_ylabel('Total Sales')
axes[0,0].tick_params(axis='x', rotation=45)

region_sales = df.groupby('Region')['Sales'].sum()
axes[0,1].pie(region_sales.values, labels=region_sales.index, autopct='%1.1f%%')
axes[0,1].set_title('Sales by Region')

monthly = df.groupby('Month')['Sales'].sum().reindex(month_order).dropna()
axes[1,0].plot(monthly.index, monthly.values, marker='o', color='green', linewidth=2)
axes[1,0].set_title('Monthly Sales Trend')
axes[1,0].set_xlabel('Month')
axes[1,0].set_ylabel('Total Sales')
axes[1,0].tick_params(axis='x', rotation=45)

category = df.groupby('Category')[['Sales','Profit']].sum()
x = range(len(category))
axes[1,1].bar([i-0.2 for i in x], category['Sales'], width=0.4, label='Sales', color='steelblue')
axes[1,1].bar([i+0.2 for i in x], category['Profit'], width=0.4, label='Profit', color='orange')
axes[1,1].set_xticks(x)
axes[1,1].set_xticklabels(category.index)
axes[1,1].set_title('Sales vs Profit by Category')
axes[1,1].legend()

plt.tight_layout()
plt.savefig('dashboard.png', dpi=150, bbox_inches='tight')
plt.show()
print('Dashboard created!')