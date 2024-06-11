import sys
import os
from fastapi.testclient import TestClient
from dotenv import load_dotenv

# Add the app directory to the system path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app.helloworld import router as helloworld_router  # Adjusted import for router
from main import app  # Assuming you have main app definition in app/main.py

# Load environment variables from the .env file
load_dotenv()

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, welcome to the FastAPI project!"}

def test_create_user():
    response = client.post("/user/", json={"username": "testuser", "email": "testuser@example.com"})
    assert response.status_code == 200
    assert response.json() == {"username": "testuser", "email": "testuser@example.com"}

def test_get_config():
    response = client.get("/config/")
    assert response.status_code == 200
    assert "config" in response.json()
