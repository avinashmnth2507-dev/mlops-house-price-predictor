import pytest
from fastapi.testclient import TestClient
import numpy as np

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def mock_joblib_load(*args, **kwargs):
    class DummyModel:
        def predict(self, X):
            return np.array([2.5])
    return DummyModel()

import joblib
joblib.load = mock_joblib_load

from src import api
client = TestClient(api.app)

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
    assert response.json()["predicted_price"] == 2.5
