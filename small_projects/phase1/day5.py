 # load the orders, customers, and products tables
# merge all three into a single master dataframe
# find total revenue per customer
# identify customers who never placed a second order
# use melt to reshape wide monthly sales columns into long format
# extract the year and month from order dates
# find the average delivery time in days and identify cities with the slowest deliveries

import pandas as pd

orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")
products = pd.read_csv("products.csv")

master_df = pd.merge(orders, customers, on="customer_id", how="inner")

master_df = pd.merge(master_df, products, on="product_id", how="inner")

print(master_df.head())

revenue = master_df.groupby("customer_id")["price"].sum()

print(revenue)

order_counts = master_df.groupby("customer_id")["order_id"].nunique()

single_order_customers = order_counts[order_counts == 1]

print(single_order_customers)

sales_data = pd.DataFrame({
    "product": ["A", "B"],
    "jan": [100, 200],
    "feb": [150, 250],
    "mar": [120, 300]
})

melted = sales_data.melt(
    id_vars="product",
    var_name="month",
    value_name="sales"
)

print(melted)

master_df["order_purchase_timestamp"] = pd.to_datetime(
    master_df["order_purchase_timestamp"]
)

master_df["year"] = master_df["order_purchase_timestamp"].dt.year

master_df["month"] = master_df["order_purchase_timestamp"].dt.month

print(master_df[["year", "month"]].head())

master_df["order_delivered_customer_date"] = pd.to_datetime(
    master_df["order_delivered_customer_date"]
)

delivery_days = (
    master_df["order_delivered_customer_date"] -
    master_df["order_purchase_timestamp"]
).dt.days

master_df["delivery_days"] = delivery_days

avg_delivery = master_df["delivery_days"].mean()

print("average delivery days:", avg_delivery)

slowest_cities = (
    master_df.groupby("customer_city")["delivery_days"]
    .mean()
    .sort_values(ascending=False)
    .head(5)
)

print(slowest_cities)