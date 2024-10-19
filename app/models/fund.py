from pydantic import BaseModel
from typing import Optional

class Fund(BaseModel):
    id: str
    name: str
    minimum_investment: int
    category: str

class Transaction(BaseModel):
    id: str
    fund_id: str
    amount: int
    type: str  # "subscription" o "cancellation"
    date: Optional[str] = None
