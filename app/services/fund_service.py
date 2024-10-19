from fastapi import HTTPException
from app.database import funds_collection, transactions_collection
from app.models.fund import Fund
from bson import ObjectId

class FundService:
    def get_all_funds(self):
        """Devuelve la lista de fondos disponibles."""
        funds = list(funds_collection.find())
        return funds

    def subscribe_to_fund(self, transaction: dict):
        """Suscribe al cliente a un fondo si tiene suficiente saldo."""
        fund_id = transaction.get("fund_id")
        fund = funds_collection.find_one({"id": fund_id})

        if not fund:
            raise FundNotFoundException(f"Fondo con ID {fund_id} no encontrado")

        # Lógica de saldo (deberías manejarlo con base de datos real)
        available_balance = 500000  # Saldo inicial, reemplaza con tu lógica de saldo
        if transaction["amount"] < fund["minimum_investment"]:
            raise InsufficientBalanceException(f"No tiene saldo disponible para vincularse al fondo {fund['name']}")

        # Generar ID único para la transacción
        transaction_data = {
            "id": str(ObjectId()),
            "fund_id": fund["id"],
            "action": "subscribe",
            "amount": transaction["amount"]
        }

        # Guardar la transacción en la base de datos
        transactions_collection.insert_one(transaction_data)
        return transaction_data

    def unsubscribe_from_fund(self, transaction: dict):
        """Cancela la suscripción del cliente a un fondo."""
        fund_id = transaction.get("fund_id")
        fund = funds_collection.find_one({"id": fund_id})

        if not fund:
            raise FundNotFoundException(f"Fondo con ID {fund_id} no encontrado")

        transaction_data = {
            "id": str(ObjectId()),
            "fund_id": fund["id"],
            "action": "unsubscribe",
            "amount": transaction["amount"]
        }

        # Guardar la transacción en la base de datos
        transactions_collection.insert_one(transaction_data)
        return transaction_data

    def get_all_transactions(self):
        """Devuelve el historial de transacciones."""
        transactions = list(transactions_collection.find())
        return transactions