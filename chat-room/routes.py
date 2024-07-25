from fastapi import APIRouter, HTTPException
from models import User
from utils import create_jwt_token
from database import db

router = APIRouter()

@router.post("/register")
async def register(user: User):
    existing_user = await db.users.find_one({"email": user.email})
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    await db.users.insert_one(user.dict())
    token = create_jwt_token(user.email)
    return {"token": token}

@router.post("/login")
async def login(email: str):
    user = await db.users.find_one({"email": email})
    if not user:
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = create_jwt_token(email)
    return {"token": token}

@router.get("/some-endpoint")
async def some_endpoint():
    return {"message": "This is a response from some endpoint!"}
