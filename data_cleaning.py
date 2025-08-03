import pandas as pd

sales = pd.read_csv("data/sales.csv")
products = pd.read_csv("data/products.csv")
customers = pd.read_csv("data/customers.csv")

df = sales.merge(products, on="product_id").merge(customers, on="customer_id")

df['order_date'] = pd.to_datetime(df['order_date'])

monthly_sales = df.groupby(df['order_date'].dt.to_period("M"))['sales'].sum().reset_index()
monthly_sales['order_date'] = monthly_sales['order_date'].astype(str)

df.to_csv("data/cleaned_sales.csv", index=False)
monthly_sales.to_csv("data/monthly_sales.csv", index=False)

print("Data processing complete.")
