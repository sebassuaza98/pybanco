from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional

class MongoBaseModel(BaseModel):
    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {
            ObjectId: str
        }

class Client(MongoBaseModel):
    identification: str
    first_name: str
    last_name: str
    phone: str
    email: str
    balance: float
