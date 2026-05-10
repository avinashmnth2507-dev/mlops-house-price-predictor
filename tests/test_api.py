import pytest
from fastapi.testclient import TestClient
import numpy as np
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Mock joblib.load to avoid real model file
import joblib
def mock_load(*args, **kwargs):
    class DummyModel:
        def predict(self, X):
            return np.array([2.5])
    return DummyModel()
joblib.load = mock_load

# Mock drift_monitor
import drift_monitor
drift_monitor.DriftMonitor = lambda *args, **kwargs: type('Mock', (), {
    'check_drift': lambda self, df: {"drift_detected": False}
})
drift_monitor.simulate_current_data = lambda *args, **kwargs: None

# Mock finops
import finops
finops.FinOps = lambda: type('Mock', (), {
    'record_inference': lambda self: None,
    'get_summary': lambda self: {"total_inferences": 0, "cost_per_inference_usd": 1e-6, "total_cost_usd": 0.0, "recommendations": []}
})

# Mock prometheus instrumentation
import prometheus_fastapi_instrumentator
prometheus_fastapi_instrumentator.Instrumentator = lambda: type('Mock', (), {
    'instrument': lambda self, app: self,
    'expose': lambda self, app: None
})

# Now import the app
from src import api
client = TestClient(api.app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_predict():
    # Ensure the internal _model is None so get_model() uses our mock
    api._model = None
    payload = {
        "MedInc": 3.5, "HouseAge": 30, "AveRooms": 5.0, "AveBedrms": 1.0,
        "Population": 1000, "AveOccup": 2.5, "Latitude": 37.8, "Longitude": -122.4
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "predicted_price" in response.json()
    assert response.json()["predicted_price"] == 2.5

def test_drift_status():
    response = client.get("/drift/status")
    assert response.status_code == 200
    assert "drift_detected" in response.json()

def test_cost():
    response = client.get("/cost")
    assert response.status_code == 200
    assert "total_inferences" in response.json()
