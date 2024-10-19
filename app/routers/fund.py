from fastapi import APIRouter, HTTPException
from app.models.fund import Fund
from app.services.fund_service import FundService

router = APIRouter()
fund_service = FundService()

@router.get("/funds/", response_model=list[Fund])
async def get_funds():
    """Obtiene la lista de fondos disponibles."""
    funds = fund_service.get_all_funds()
    return [Fund(**fund) for fund in funds]  # Convertir a instancias de Fund

@router.post("/subscribe/", response_model=dict)
async def subscribe_to_fund(transaction: dict):
    """Suscribe al cliente a un fondo si tiene suficiente saldo."""
    if "amount" not in transaction:
        raise HTTPException(status_code=400, detail="Falta el campo 'amount' en la transacción.")
    return fund_service.subscribe_to_fund(transaction)

@router.post("/unsubscribe/", response_model=dict)
async def unsubscribe_from_fund(transaction: dict):
    """Cancela la suscripción del cliente a un fondo."""
    return fund_service.unsubscribe_from_fund(transaction)

@router.get("/transactions/", response_model=list)
async def get_transactions():
    """Obtiene el historial de transacciones."""
    return fund_service.get_all_transactions()
