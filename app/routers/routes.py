from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.schemas.schemas_client import ClientCreate, ClientResponse
from app.schemas.schemas_found import FundResponse
from app.services.client_services import ClientService
from app.services.fund_service import FundService

router = APIRouter()
client_service = ClientService()

@router.get("/clients", response_model=list[ClientResponse])
async def list_clients():
    return client_service.list_clients()

@router.post("/clients", response_model=ClientResponse)
async def create_client(client: ClientCreate):
    created_client = client_service.create_client(client)
    return created_client

@router.get("/clients/filter/{identification}", response_model=ClientResponse)
async def filter_by_identification(identification: str):
    client = client_service.filter_by_identification(identification)
    return client

fund_service = FundService()
@router.get("/funds", response_model=list[FundResponse]) 
async def list_funds():
    return fund_service.list_funds()
