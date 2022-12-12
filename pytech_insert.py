import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.tchuumd.mongodb.net/?retryWrites=true&w=majority")
db = client ["pytech"]
collection = db ["students"]


post = {"_id": 1007, "First Name": "Luka" , "Last Name": "Lazalde"}

post = {"_id": 1008, "First Name": "Matias" , "Last Name": "Lazalde"}

post = {"_id": 1009, "First Name": "Julieta" , "Last Name": "Lazalde"}
post = {"_id": 1010, "First Name": "Luna" , "Last Name": "Lazalde"}


collection.insert_one(post)

