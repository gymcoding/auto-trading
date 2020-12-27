from pymongo import MongoClient
from pymongo.cursor import CursorType
import configparser
from autotrading.db.base_handler import DBHandler

class MongoDBHandler(DBHandler):
    def __init__(self, db_name=None, collection_name=None):
        config = configparser.ConfigParser()
        config.read('conf/config.ini')
        self.USERNAME = config['MONGODB']['username']
        self.PASWORD = config['MONGODB']['password']
        self._client = MongoClient(f'mongodb+srv://{self.USERNAME}:{self.PASWORD}@cluster0.hokoq.mongodb.net')
        self._db = self._client[db_name]
        self._collection = self._db[collection_name]

    def set_db_collection(self, db_name=None, collection_name=None):
        if db_name is None:
            raise Exception('Need to dbname name')
        
        self._db = self._client[db_name]
        if collection_name is not None:
            self._collection = self._db[collection_name]

        self._db = self._client[db_name]
        if collection_name is not None:
            self._collection = self._db[collection_name]

    def get_current_db_name(self):
        return self._db.name
    
    def get_current_collection_name(self):
        return self._collection.name

    def insert_item(self, data, db_name=None, collection_name=None):
        if db_name is not None:
            self._db = self._client[db_name]
        if collection_name is not None:
            self._collection = self._db[collection_name]
        return self._collection.insert_one(data).inserted_id

    def insert_items(self, datas, db_name=None, collection_name=None):
        if db_name is not None:
            self._db = self._client[db_name]
        if collection_name is not None:
            self._collection_name = self._db[collection_name]
        return self._collection.insert_many(datas).inserted_ids

    def find_items(self, condition=None, db_name=None, collection_name=None):
        if condition is None:
            condition = {}
        if db_name is not None:
            self._db = self._client[db_name]
        if collection_name is not None:
            self._collection = self._db[collection_name]
        return self._collection.find(condition, no_cursor_timeout=True, cursor_type=CursorType.EXHAUST)
    
    def find_item(self, condition=None, db_name=None, collection_name=None):
        if condition is None:
            condition = {}
        if db_name is not None:
            self._db = self._client[db_name]
        if collection_name is not None:
            self._collection = self._db[collection_name]
        return self._collection.find_one(condition)

    def delete_items(self, condition=None, db_name=None, collection_name=None):
        if condition is None:
            raise Exception('Need to condition')
        if db_name is not None:
            self._db = self._client[db_name]
        if collection_name is not None:
            self._collection = self._db[collection_name]
        return self._collection.delete_many(condition)

    def update_items(self, condition=None, update_value=None, db_name=None, collection_name=None):
        if condition is None:
            raise Exception('Need to condition')
        if update_value is None:
            raise Exception('Need to update value')
        if db_name is not None:
            self._db = self._client[db_name]
        if collection_name is not None:
            self._collection = self._db[collection_name]
        return self._collection.update_many(filter=condition, update=update_value)

    def aggregate(self, pipeline=None, db_name=None, collection_name=None):
        if pipeline is None:
            raise Exception('Need to pipeline') 
        if db_name is not None:
            self._db = self._client[db_name]
        if collection_name is not None:
            self._collection = self._db[collection_name]
        return self._collection.aggregate(pipeline)

