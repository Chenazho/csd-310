import pymongo
from pymongo import MongoClient
client = MongoClient("mongodb+srv://admin:admin@cluster0.tchuumd.mongodb.net/?retryWrites=true&w=majority")
db = client ["pytech"]
collection = db ["students"]


post = {"_id": 1012, "First Name": "Luka" , "Last Name": "Lazalde"}

post = {"_id": 1013, "First Name": "Matias" , "Last Name": "Lazalde"}

post = {"_id": 1014, "First Name": "Julieta" , "Last Name": "Lazalde"}

post = {"_id": 1015, "First Name": "Luna" , "Last Name": "Lazalde"}


collection.insert_one(post)

