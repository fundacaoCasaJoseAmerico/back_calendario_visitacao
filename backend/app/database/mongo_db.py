from pymongo import MongoClient

from .DAO import DAO

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "calendario_fcja"

class MongoDAO(DAO):
    def __init__(self, client: MongoClient):
        self.__db = client[DB_NAME]

    @property
    def db(self):
        return self.__db
