from pymongo import MongoClient
from app.clients.models.client import Client
from app.clients.schemas.schemas_client import ClientCreate
from app.clients.exceptions.exceptions import ClientAlreadyExistsException, ClientNotFoundException

class Database:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

db = Database("mongodb://localhost:27017", "btg_fondos")

class ClientService:
    def list_clients(self):
        return list(db.db.clients.find())

    def create_client(self, client_data: ClientCreate):
        if db.db.clients.find_one({"identification": client_data.identification}):
            raise ClientAlreadyExistsException(client_data.identification)
        client = Client(**client_data.dict())
        db.db.clients.insert_one(client.dict())
        return client

    def filter_by_identification(self, identification: str):
        client = db.db.clients.find_one({"identification": identification})
        if not client:
            raise ClientNotFoundException(identification)
        return Client(**client)
