# load the superstore sales dataset
# find total sales and profit by region and category
# identify the top 3 performing sub-categories in each region
# calculate profit margin percentage as a new column
# create a pivot table of average sales by region and segment
# find months with negative total profit
# find quarterly sales trends after converting the order date column to datetime

import pandas as pd

df = pd.read_csv("superstore.csv")

grouped = df.groupby(["Region", "Category"])[["Sales", "Profit"]].sum()

print(grouped)

top_sub = (
    df.groupby(["Region", "Sub-Category"])["Sales"]
    .sum()
    .reset_index()
    .sort_values(["Region", "Sales"], ascending=[True, False])
)

print(top_sub.groupby("Region").head(3))

df["Profit Margin %"] = (df["Profit"] / df["Sales"]) * 100

print(df[["Profit Margin %"]].head())

pivot = pd.pivot_table(
    df,
    values="Sales",
    index="Region",
    columns="Segment",
    aggfunc="mean"
)

print(pivot)

df["Order Date"] = pd.to_datetime(df["Order Date"])

df["Month"] = df["Order Date"].dt.month

negative_profit = df.groupby("Month")["Profit"].sum()

print(negative_profit[negative_profit < 0])

quarterly_sales = (
    df.set_index("Order Date")
    .resample("Q")["Sales"]
    .sum()
)

print(quarterly_sales)