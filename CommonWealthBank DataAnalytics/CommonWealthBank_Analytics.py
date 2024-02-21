import pandas as pd

df = pd.read_excel(r"C:\Users\kritr\.vscode\Python Projects\CommonWealthBank DataAnalytics\supermarket_transactions.xlsx")
df.index = df["Unnamed: 0"]
df.drop(columns=["Unnamed: 0"],inplace=True)
# Across locations, how many apples were purchased in cash?
mask1 = df["product_name"]=="apple"
# How much total cash was spent on these apples?
mask2 = df["payment_method"] == "cash"
apple = (df[mask1 & mask2])
# print(f"Across locations, {apple["quantity"].sum()} apples were purchased in cashed.")
# print(f"{apple["total_amount"].sum().round(2)} cash was spend on these apples.")
# Across all payment methods, how much money was spent at the Bakershire store location by non-member customers?
mask3 = df["store"] == "Bakershire"
mask4 = df["customer_type"] == "non-member"
# print(df[mask3&mask4]["total_amount"].sum().round(2))

df2 = pd.read_excel(r"C:\Users\kritr\.vscode\Python Projects\CommonWealthBank DataAnalytics\mobile_customers.xlsx")
df2.drop(columns=["Unnamed: 0", 'current_location', 'employer'], inplace=True)
print(df2.columns)
