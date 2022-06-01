import pymongo
import json
import requests
from pymongo import MongoClient, InsertOne

client = pymongo.MongoClient("mongodb://localhost:27017")

db = client.pymongo
collection = db.pymongo
requesting = []
response = requests.get("https://restcountries.com/v3.1/all")
val = json.loads(response.text)
for i in val:
    # print(type(myDict))
    # print(type(myDict))
    requesting.append(InsertOne(i))

result = collection.bulk_write(requesting)
client.close()
