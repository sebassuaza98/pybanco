from pydantic import BaseModel
from datetime import datetime

# Schema for creating a Transaction
class TransactionCreate(BaseModel):
    fund_id: str
    mount: float
    client_id: str

# Schema for Transaction response
class TransactionResponse(BaseModel):
    fund_id: str
    mount: float
    client_id: str

# Schema for creating a HistoryTransaction
class HistoryTransactionCreate(BaseModel):
    fund_id: str
    mount: float
    client_id: str

# Schema for HistoryTransaction response
class HistoryTransactionResponse(BaseModel):
    id: str
    fund_id: str
    type: str
    mount: float
    date: datetime
    client_id: str
