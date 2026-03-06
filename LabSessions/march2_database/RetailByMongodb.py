from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt

client = MongoClient("mongodb://localhost:27017/")
db = client["retail_db"]
collection = db["orders"]

df = pd.read_csv("retail_data.csv")

df["Date"] = pd.to_datetime(df["Date"])
df["Revenue"] = df["Quantity"] * df["Price"]
df = df.dropna()

collection.delete_many({})
collection.insert_many(df.to_dict("records"))

region_pipeline = [
    {"$group": {"_id": "$Region", "TotalRevenue": {"$sum": "$Revenue"}}},
    {"$sort": {"TotalRevenue": -1}}
]
region_df = pd.DataFrame(list(collection.aggregate(region_pipeline)))

monthly_pipeline = [
    {"$group": {
        "_id": {"year": {"$year": "$Date"}, "month": {"$month": "$Date"}},
        "TotalRevenue": {"$sum": "$Revenue"}
    }},
    {"$sort": {"_id.year": 1, "_id.month": 1}}
]
monthly_data = list(collection.aggregate(monthly_pipeline))
monthly_df = pd.DataFrame(monthly_data)
monthly_df["Month"] = monthly_df["_id"].apply(lambda x: f"{x['year']}-{x['month']:02d}")

category_pipeline = [
    {"$group": {"_id": "$Category", "TotalRevenue": {"$sum": "$Revenue"}}},
    {"$sort": {"TotalRevenue": -1}}
]
category_df = pd.DataFrame(list(collection.aggregate(category_pipeline)))

product_pipeline = [
    {"$group": {"_id": "$Product", "TotalRevenue": {"$sum": "$Revenue"}}},
    {"$sort": {"TotalRevenue": -1}},
    {"$limit": 5}
]
product_df = pd.DataFrame(list(collection.aggregate(product_pipeline)))

plt.figure()
plt.bar(region_df["_id"], region_df["TotalRevenue"])
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.title("Revenue by Region")
plt.show()

plt.figure()
plt.plot(monthly_df["Month"], monthly_df["TotalRevenue"])
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.title("Monthly Revenue Trend")
plt.xticks(rotation=45)
plt.show()

plt.figure()
plt.pie(category_df["TotalRevenue"], labels=category_df["_id"], autopct="%1.1f%%")
plt.title("Category Contribution")
plt.show()

plt.figure()
plt.barh(product_df["_id"], product_df["TotalRevenue"])
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.title("Top 5 Products")
plt.show()