from pydantic import BaseModel

class ClientCreate(BaseModel):
    identification: str
    first_name: str
    last_name: str
    phone: str
    email: str
    balance: float

class ClientResponse(BaseModel):
    identification: str
    first_name: str
    last_name: str
    phone: str
    email: str
    balance: float
