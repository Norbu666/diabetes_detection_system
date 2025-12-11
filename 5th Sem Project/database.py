from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["diabetes_db"]

general_collection = db["predictions"]
male_collection = db["male_predictions"]

def save_prediction(data):
    general_collection.insert_one(data)

def get_all_predictions():
    return list(general_collection.find())

def save_male_prediction(data):
    male_collection.insert_one(data)

def get_male_predictions():
    return list(male_collection.find())
