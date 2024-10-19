from pydantic import BaseModel

# Modelo para crear un fondo
class FundCreate(BaseModel):
    name: str  # Nombre del fondo
    minimum_investment: int  # Inversión mínima
    category: str  # Categoría del fondo

class FundResponse(BaseModel):
    id: str
    name: str
    minimum_investment: float
    category: str
