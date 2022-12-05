import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.tchuumd.mongodb.net/?retryWrites=true&w=majority")
db = client ["pytech"]
collection = db ["students"]

results = collection.find_one({"_id":1012})
print (results)