from fastapi import HTTPException

class FondoNotFoundException(HTTPException):
    def __init__(self, fondo_id: str):
        detail = f"Fondo with ID {fondo_id} not found."
        super().__init__(status_code=404, detail=detail)

class ClientNotFoundException(HTTPException):
    def __init__(self, cliente_id: str):
        detail = f"Client with ID {cliente_id} not found."
        super().__init__(status_code=404, detail=detail)

class InsufficientFundsException(HTTPException):
    def __init__(self):
        super().__init__(status_code=400, detail="Insufficient funds to complete the transaction.")

class TransactionAlreadyCancelledException(HTTPException):
    def __init__(self, transaccion_id: str):
        detail = f"Transaction {transaccion_id} is already cancelled."
        super().__init__(status_code=400, detail=detail)

class UnauthorizedClientException(HTTPException):
    def __init__(self):
        super().__init__(status_code=403, detail="Client is not authorized for this transaction.")
