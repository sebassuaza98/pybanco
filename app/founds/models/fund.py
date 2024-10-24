from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional

# Modelo base para MongoDB
class MongoBaseModel(BaseModel):
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str  # Convierte ObjectId a str para la serialización
        }

# Modelo de Fondos
class Fund(MongoBaseModel):
    id: str
    name: str
    minimum_investment: int
    category: str
