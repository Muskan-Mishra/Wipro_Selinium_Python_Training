#mongo db connection

from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017/")
print("Connected successfully")



db = client["school"]
collection = db["students"]
#insert the data to the collection
students =[
    {"name":"Ravi","Subject":"Science","marks":90},
    {"name":"Sneha","Subject":"Math","marks":78},
    {"name":"Kiran","Subject":"Science","marks":88},
]
collection.insert_many(students)


for doc in collection.find():
    print(doc)

#update the data

collection.update_one(
    {"name": "Ravi"},
    {"$set": {"marks": 95}}
)
#deletion
collection.delete_many({"name": "Sneha"})



