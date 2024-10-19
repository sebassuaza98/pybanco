from fastapi import FastAPI
from app.routers.routes import router as fund_router  # Importa el router

app = FastAPI()

app.include_router(fund_router)  # Asegúrate de que este es el nombre correcto

@app.get("/")
async def read_root():
    return {"message": "Bienvenido a la API de Fondos"}
