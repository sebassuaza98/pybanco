from fastapi import FastAPI
from app.clients.routers.routes import router as fund_router_client  # Importa el router
from app.founds.routers.routes import router as fund_router_found
from app.transactions.routers.routers import router as fund_router_transaction

app = FastAPI()
#fund_router = fund_router_c + fund_router_f
app.include_router(fund_router_client)  # Asegúrate de que este es el nombre correcto
app.include_router(fund_router_found)  # Asegúrate de que este es el nombre correcto
app.include_router(fund_router_transaction)
@app.get("/")
async def read_root():
    return {"message": "Bienvenido a la API de Fondos"}
