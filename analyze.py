import pandas as pd

# ── 1. LOAD DATA ──────────────────────────────────────────
df = pd.read_csv('sales_data.csv')
print("✅ Data Loaded!")
print(f"Rows: {len(df)}, Columns: {len(df.columns)}")

# ── 2. CLEAN DATA ─────────────────────────────────────────
df['Date'] = pd.to_datetime(df['Date'])
df.drop_duplicates(inplace=True)
df.dropna(inplace=True)
df['Month'] = df['Date'].dt.month_name()
df['Year'] = df['Date'].dt.year
print("\n✅ Data Cleaned!")

# ── 3. KEY METRICS ────────────────────────────────────────
total_sales  = df['Sales'].sum()
total_profit = df['Profit'].sum()
total_orders = len(df)
avg_sale     = df['Sales'].mean()

print("\n📊 KEY METRICS")
print(f"   Total Sales  : ₹{total_sales:,.2f}")
print(f"   Total Profit : ₹{total_profit:,.2f}")
print(f"   Total Orders : {total_orders}")
print(f"   Avg Sale     : ₹{avg_sale:,.2f}")

# ── 4. TOP PRODUCTS ───────────────────────────────────────
print("\n🏆 TOP 5 PRODUCTS BY SALES")
top_products = df.groupby('Product')['Sales'].sum().sort_values(ascending=False).head(5)
print(top_products)

# ── 5. BEST REGIONS ───────────────────────────────────────
print("\n🌍 SALES BY REGION")
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print(region_sales)

# ── 6. MONTHLY TREND ──────────────────────────────────────
print("\n📅 MONTHLY SALES TREND")
month_order = ['January','February','March','April','May','June',
               'July','August','September','October','November','December']
monthly = df.groupby('Month')['Sales'].sum().reindex(month_order).dropna()
print(monthly)

print("\n✅ Analysis Complete!")