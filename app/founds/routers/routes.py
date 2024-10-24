#from fastapi import APIRouter
from fastapi.responses import JSONResponse
from app.founds.schemas.schemas_found import FundResponse
from app.founds.services.fund_service import FundService
from app.routers import (router)

router = router
fund_service = FundService()
@router.get("/funds", response_model=list[FundResponse]) 
async def list_funds():
    return fund_service.list_funds()
