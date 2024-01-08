from pymongo import MongoClient
from config.config import Config


class MongoDB:
    def __init__(self):
        self.client = MongoClient(Config.MONGODB_URI)
        self.db = self.client[Config.MONGODB_DATABASE]
        self.collection = self.db[Config.MONGODB_COLLECTION]

    def get_all_data(self):
        return list(self.collection.find())

    def find(self, query):
        return self.collection.find(query)

    def write_to_mongodb(self, message):
        self.collection.insert_one(message)
