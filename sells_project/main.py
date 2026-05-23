import pandas as pd

df = pd.read_csv("module_1_repo/sells_project/data/sales_data.csv")

print("SALES DATASET")
print(df)

print("\nTotal Sales:")
print(df["Total_Sales"].sum())

top_product = df.loc[df["Total_Sales"].idxmax()]
print("\nTop Selling Product:")
print(top_product["Product"], "-", top_product["Total_Sales"])

print("\nRegion Wise Sales:")
print(df.groupby("Region")["Total_Sales"].sum())

print("\nCategory Wise Sales:")
print(df.groupby("Category")["Total_Sales"].sum())