from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime
from fastapi import HTTPException
from app.conts import (URL)
from app.transactions.exceptions.exceptions import (
    FondoNotFoundException, 
    ClientNotFoundException, 
    InsufficientFundsException,
    TransactionAlreadyCancelledException,
    UnauthorizedClientException
)

class Database:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

db = Database(URL, "btg_fondos")

class TransactionService:
    def __init__(self, db: Database):
        self.db = db.db 

    def subscribe_fund(self, fund_id: str, client_id: str, mount: float):
        # Buscar fondo
        fund = self.db.funds.find_one({"id": fund_id})
        if not fund:
            raise FondoNotFoundException(fund_id)

        # Buscar cliente
        client = self.db.clients.find_one({"identification": client_id})
        if not client:
            raise ClientNotFoundException(client_id)

        # Verificar monto mínimo
        if mount < fund["minimum_investment"]:
            raise HTTPException(status_code=400, detail="Amount below minimum")

        # Verificar saldo del cliente
        new_balance = client["balance"] - mount
        if new_balance < 0:
            raise InsufficientFundsException()

        # Crear transacción de suscripción
        transaction = {
            "fund_id": fund_id,
            "client_id": client_id,
            "mount": mount,
            "type": "Subscription",  # Tipo de transacción
        }
        
        # Insertar la transacción en la base de datos
        result = self.db.transactions.insert_one(transaction)

        # Registrar en el historial
        history_transaction = transaction.copy()
        history_transaction["_id"] = ObjectId()  # Nuevo ID para el historial
        self.db.historytransactions.insert_one(history_transaction)

        # Actualizar saldo del cliente
        self.db.clients.update_one(
            {"identification": client_id},
            {"$set": {"balance": new_balance}}
        )

        return {**transaction, "id": str(result.inserted_id)}
