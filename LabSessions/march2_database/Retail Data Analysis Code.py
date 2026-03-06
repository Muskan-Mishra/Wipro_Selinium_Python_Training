import pandas as pd
import matplotlib.pyplot as plt

data = {
    "OrderID": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    "Date": [
        "2024-01-05","2024-01-10","2024-02-15","2024-02-20","2024-03-05",
        "2024-03-18","2024-04-02","2024-04-15","2024-05-01","2024-05-12",
        "2024-05-25","2024-06-05","2024-06-18","2024-06-30","2024-07-10"
    ],
    "Region": [
        "North","South","North","West","East",
        "South","North","West","East","South",
        "North","West","East","South","North"
    ],
    "Product": [
        "Laptop","Phone","Shoes","TV","Watch",
        "Laptop","Phone","Shoes","TV","Watch",
        "Tablet","Jacket","Phone","Shoes","TV"
    ],
    "Category": [
        "Electronics","Electronics","Fashion","Electronics","Fashion",
        "Electronics","Electronics","Fashion","Electronics","Fashion",
        "Electronics","Fashion","Electronics","Fashion","Electronics"
    ],
    "Quantity": [2,3,5,1,4,1,2,3,2,6,3,2,4,7,1],
    "Price": [50000,20000,2000,40000,3000,50000,20000,2000,40000,3000,25000,5000,20000,2000,40000]
}

df = pd.DataFrame(data)
df.to_csv("sales_data.csv", index=False)

df = pd.read_csv("sales_data.csv")

df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

df["Revenue"] = df["Quantity"] * df["Price"]

print(df.isnull().sum())

df["Quantity"] = df["Quantity"].fillna(0)
df["Price"] = df["Price"].fillna(0)

df = df.dropna(subset=["OrderID", "Date", "Region", "Product", "Category"])

region_revenue = df.groupby("Region")["Revenue"].sum().sort_values(ascending=False)
print(region_revenue)
print("Highest Revenue Region:", region_revenue.idxmax())

df["Month"] = df["Date"].dt.to_period("M")
monthly_revenue = df.groupby("Month")["Revenue"].sum()
monthly_revenue.index = monthly_revenue.index.astype(str)
print(monthly_revenue)

category_revenue = df.groupby("Category")["Revenue"].sum().sort_values(ascending=False)
print(category_revenue)
print("Best Performing Category:", category_revenue.idxmax())

top_products = df.groupby("Product")["Revenue"].sum().sort_values(ascending=False).head(5)
print(top_products)

plt.figure()
plt.bar(region_revenue.index, region_revenue.values)
plt.title("Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.show()

plt.figure()
plt.plot(monthly_revenue.index, monthly_revenue.values)
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Total Revenue")
plt.xticks(rotation=45)
plt.show()

plt.figure()
plt.pie(category_revenue.values, labels=category_revenue.index, autopct="%1.1f%%")
plt.title("Category Contribution")
plt.show()

plt.figure()
plt.barh(top_products.index, top_products.values)
plt.title("Top 5 Products by Revenue")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.show()