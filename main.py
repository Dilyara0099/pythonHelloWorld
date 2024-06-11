from fastapi import FastAPI
from app.helloworld import router as helloworld_router

app = FastAPI()

app.include_router(helloworld_router)
