from fastapi import APIRouter, Depends, HTTPException
from app.transactions.services.transaction_services import TransactionService, db
from app.transactions.schemas.schemas_transaction import TransactionCreate, TransactionResponse
from fastapi.responses import JSONResponse
from typing import Optional
from app.transactions.exceptions.exceptions import (
    FondoNotFoundException, 
    ClientNotFoundException, 
    InsufficientFundsException,
    TransactionAlreadyCancelledException,
    UnauthorizedClientException
)

router = APIRouter()

transaction_service = TransactionService(db)

@router.post("/transactions/subscribe", response_model=TransactionResponse)
async def subscribe_fund(data: TransactionCreate):
    try:
        transaction_data = transaction_service.subscribe_fund(data.fund_id, data.client_id, data.mount)
        
        transaction_response = TransactionResponse(
            fund_id=transaction_data["fund_id"],
            type=transaction_data["type"],
            mount=transaction_data["mount"],
            client_id=transaction_data["client_id"]
        )
        
        return JSONResponse(status_code=201, content=transaction_response.dict())
    
    except InsufficientFundsException as e:
        raise HTTPException(status_code=e.status_code, detail=str(e.detail))
    except Exception as e:
        # Manejar otras excepciones generales
        raise HTTPException(status_code=500, detail="Internal server error")
