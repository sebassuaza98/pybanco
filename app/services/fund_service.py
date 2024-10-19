from pymongo import MongoClient
from pymongo.database import Database
from typing import List
from app.schemas.schemas_found import FundResponse

class Database:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        
db = Database("mongodb://localhost:27017", "btg_fondos")

class FundService:
    def list_funds(self):
        return list(db.db.funds.find())