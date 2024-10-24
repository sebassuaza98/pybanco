from fastapi import HTTPException

class ClientAlreadyExistsException(HTTPException):
    def __init__(self, identification: str):
        super().__init__(status_code=400, detail=f"Client with identification {identification} already exists.")

class ClientNotFoundException(HTTPException):
    def __init__(self, identification: str):
        super().__init__(status_code=404, detail=f"Client with identification {identification} not found.")
