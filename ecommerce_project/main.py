import pandas as pd

df = pd.read_csv("module_1_repo/ecommerce_project/data/ecommerce_data.csv")

print("ECOMMERCE DATASET")
print(df)

print("\nTotal Revenue:")
print(df["Total_Amount"].sum())

top_product = df.loc[df["Total_Amount"].idxmax()]
print("\nHighest Revenue Product:")
print(top_product["Product"], "-", top_product["Total_Amount"])

print("\nCategory Wise Revenue:")
print(df.groupby("Category")["Total_Amount"].sum())

print("\nPayment Method Usage:")
print(df["Payment_Method"].value_counts())