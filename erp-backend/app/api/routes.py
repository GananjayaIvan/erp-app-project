from fastapi import APIRouter

router = APIRouter(prefix="/api", tags=["API"])

# In-memory "database" for testing
fake_users = []


@router.get("/")
def api_root():
    return {"message": "API is working"}


@router.get("/users")
def get_users():
    return {
        "status": "success",
        "data": fake_users
    }


@router.post("/users")
def create_user(user: dict):
    fake_users.append(user)
    return {
        "status": "created",
        "data": user
    }


@router.get("/users/{user_id}")
def get_user(user_id: int):
    if 0 <= user_id < len(fake_users):
        return fake_users[user_id]
    return {"error": "User not found"}