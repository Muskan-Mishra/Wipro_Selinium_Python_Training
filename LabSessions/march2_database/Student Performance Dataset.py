from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt

client = MongoClient("mongodb://localhost:27017/")
db = client["school_db"]
collection = db["students"]

df = pd.read_csv("student_performance.csv")

collection.delete_many({})
collection.insert_many(df.to_dict("records"))

print("Initial Data Inserted into MongoDB")
print(pd.DataFrame(list(collection.find())).drop(columns=["_id"]))

for student in collection.find():
    avg = (student["Math"] + student["Science"] + student["English"]) / 3
    result = "Pass" if avg >= 40 else "Fail"
    collection.update_one(
        {"_id": student["_id"]},
        {"$set": {"Average_Marks": avg, "Result": result}}
    )

print("\nData After Adding Average_Marks and Result")
df_updated = pd.DataFrame(list(collection.find()))
print(df_updated.drop(columns=["_id"]))

avg_math = df_updated["Math"].mean()
avg_science = df_updated["Science"].mean()
avg_english = df_updated["English"].mean()

print("\nAverage Score Per Subject")
print("Math:", avg_math)
print("Science:", avg_science)
print("English:", avg_english)

gender_avg = df_updated.groupby("Gender")["Average_Marks"].mean()
print("\nPerformance by Gender")
print(gender_avg)

result_count = df_updated["Result"].value_counts()
print("\nPass vs Fail Count")
print(result_count)

correlation = df_updated["Attendance"].corr(df_updated["Average_Marks"])
print("\nAttendance Correlation with Performance:", correlation)

plt.figure()
plt.bar(["Math","Science","English"], [avg_math, avg_science, avg_english])
plt.title("Average Subject Scores")
plt.show()

plt.figure()
plt.scatter(df_updated["Attendance"], df_updated["Average_Marks"])
plt.title("Attendance vs Average Marks")
plt.xlabel("Attendance")
plt.ylabel("Average Marks")
plt.show()

plt.figure()
df_updated.boxplot(column="Average_Marks", by="Gender")
plt.title("Marks Distribution by Gender")
plt.suptitle("")
plt.show()

plt.figure()
plt.pie(result_count.values, labels=result_count.index, autopct="%1.1f%%")
plt.title("Pass vs Fail")
plt.show()