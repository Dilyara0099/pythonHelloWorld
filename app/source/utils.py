import os

def read_config():
    return {
        "app_name": os.getenv("APP_NAME", "FastAPI App"),
        "environment": os.getenv("ENVIRONMENT", "development")
    }
