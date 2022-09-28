import pymongo
from pymongo import MongoClient

CONNECTION_STRING = "mongodb+srv://jialii:Xujiali1@cluster0.wnpabny.mongodb.net/Ingredients"
client = MongoClient(CONNECTION_STRING)
docs = [
    {"name": "Rice", "price": 7.0}, #set bread to $7 since the burger costs $7
	{"name": "Zucchini", "price": 0.5},
	{"name": "Avocado", "price": 1.0},
    {"name": "Shrimp", "price": 1.0},
	{"name": "Broccoli", "price": 0.5},
	{"name": "Chicken", "price": 1.0},
    {"name": "Salmon", "price": 1.0},
    {"name": "Tuna", "price": 1.0},
    ]

client.Ingredients.Sushi.insert_many(docs)

# display the results of your operation
#print(result.inserted_ids)