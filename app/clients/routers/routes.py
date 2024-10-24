#from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.clients.schemas.schemas_client import ClientCreate, ClientResponse
from app.clients.services.client_services import ClientService
from app.routers import (router)

router = router
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