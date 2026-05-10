import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Create fake modules before importing src.api
import types
from unittest.mock import MagicMock

# Fake drift_monitor
fake_drift_monitor = types.ModuleType('drift_monitor')
fake_drift_monitor.DriftMonitor = MagicMock()
fake_drift_monitor.simulate_current_data = MagicMock(return_value=None)
sys.modules['drift_monitor'] = fake_drift_monitor

# Fake finops
fake_finops = types.ModuleType('finops')
fake_finops.FinOps = MagicMock()
sys.modules['finops'] = fake_finops

# Fake prometheus_fastapi_instrumentator
fake_prometheus = types.ModuleType('prometheus_fastapi_instrumentator')
fake_prometheus.Instrumentator = MagicMock()
sys.modules['prometheus_fastapi_instrumentator'] = fake_prometheus

# Mock joblib
import joblib
import numpy as np
joblib.load = MagicMock(return_value=MagicMock(predict=MagicMock(return_value=np.array([2.5]))))

# Now import the app
from src import api
from fastapi.testclient import TestClient
client = TestClient(api.app)

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
