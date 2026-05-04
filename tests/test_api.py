from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.api import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict():
    payload = {
        "MedInc": 3.5, "HouseAge": 30, "AveRooms": 5.0, "AveBedrms": 1.0,
        "Population": 1000, "AveOccup": 2.5, "Latitude": 37.8, "Longitude": -122.4
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "predicted_price" in response.json()
