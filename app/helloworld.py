from fastapi import APIRouter, Depends
from app.models.user import User
from app.resources.messages import get_welcome_message
from app.source.utils import read_config
import os
from dotenv import load_dotenv

load_dotenv()

router = APIRouter()

@router.get("/")
async def root():
    return {"message": get_welcome_message()}

@router.post("/user/")
async def create_user(user: User):
    return {"username": user.username, "email": user.email}

@router.get("/config/")
async def get_config():
    config = read_config()
    return {"config": config}
