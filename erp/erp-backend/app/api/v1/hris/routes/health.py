from fastapi import APIRouter
from sqlalchemy import text
from app.db.session import engine

router = APIRouter()

@router.get("/ping")
async def ping():
    return {
        "message": "yapping"
    }

@router.get("/test-db")
def test_db():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT version();"))
            version = result.scalar()

        return {
            "status": "success",
            "postgres_version": version
        }

    except Exception as e:
        return {
            "status": "error",
            "detail": str(e)
        }