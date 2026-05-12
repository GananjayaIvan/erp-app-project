from fastapi import APIRouter

router = APIRouter()

@router.get("/ping")
async def ping():
    return {
        "message": "pong"
    }

@router.get("/health")
async def health():
    return {
        "status": "ok"
    }