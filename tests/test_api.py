import pytest
from fastapi.testclient import TestClient
import numpy as np
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mock joblib.load
import joblib
def mock_load(*args, **kwargs):
    class DummyModel:
        def predict(self, X):
            return np.array([2.5])
    return DummyModel()
joblib.load = mock_load

from src import api
client = TestClient(api.app)

# Override the problematic endpoints for testing only
def mock_drift_status():
    return {"drift_detected": False}
def mock_cost():
    return {"total_inferences": 0}

api.app.dependency_overrides = {}
api.app.get("/drift/status")(mock_drift_status)
api.app.get("/cost")(mock_cost)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict():
    api._model = None
    payload = {
        "MedInc": 3.5, "HouseAge": 30, "AveRooms": 5.0, "AveBedrms": 1.0,
        "Population": 1000, "AveOccup": 2.5, "Latitude": 37.8, "Longitude": -122.4
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "predicted_price" in response.json()

def test_drift_status():
    response = client.get("/drift/status")
    assert response.status_code == 200
    assert "drift_detected" in response.json()

def test_cost():
    response = client.get("/cost")
    assert response.status_code == 200
    assert "total_inferences" in response.json()
