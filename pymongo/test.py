from pymongo import MongoClient

client = MongoClient()

db = client.test

coll = db.dataset
