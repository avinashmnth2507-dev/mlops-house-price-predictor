from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from drift_monitor import DriftMonitor, simulate_current_data
from prometheus_fastapi_instrumentator import Instrumentator
from finops import FinOps

app = FastAPI(title="House Price Predictor", version="1.0")

instrumentator = Instrumentator().instrument(app)

@app.on_event("startup")
async def _startup():
    instrumentator.expose(app)

_finops = FinOps()

class HouseFeatures(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

class PredictionResponse(BaseModel):
    predicted_price: float

_model = None

def get_model():
    global _model
    if _model is None:
        model_path = os.environ.get("MODEL_PATH", "models/model.joblib")
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Model not found at {model_path}")
        _model = joblib.load(model_path)
    return _model

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predict", response_model=PredictionResponse)
def predict(features: HouseFeatures):
    try:
        model = get_model()
        input_array = np.array([[
            features.MedInc, features.HouseAge, features.AveRooms,
            features.AveBedrms, features.Population, features.AveOccup,
            features.Latitude, features.Longitude
        ]])
        prediction = model.predict(input_array)[0]
        _finops.record_inference()
        return {"predicted_price": float(prediction)}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/drift/status")
def drift_status():
    monitor = DriftMonitor()
    current = simulate_current_data()
    return monitor.check_drift(current)

@app.get("/cost")
def get_cost():
    return _finops.get_summary()
