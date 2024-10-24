from pymongo import MongoClient
from pymongo.database import Database
from typing import List
from app.founds.schemas.schemas_found import FundResponse
from app.conts import (URL)

class Database:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
        
db = Database(URL, "btg_fondos")

class FundService:
    def list_funds(self):
        return list(db.db.funds.find())