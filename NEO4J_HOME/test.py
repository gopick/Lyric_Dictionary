import pymongo
from pymongo import MongoClient

conn = MongoClient('localhost',27017)

db = conn.test

names = db.names
names.insert({'name':"Hari"})
items = names.find()
for i in items:
    print i['name']