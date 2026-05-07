import pandas as pd
import numpy as np
import json
from datetime import datetime
import os

class DriftMonitor:
    def __init__(self, reference_data_path='data/raw/california_housing.csv'):
        # Try to load real reference data; if not found, generate synthetic reference
        if os.path.exists(reference_data_path):
            df = pd.read_csv(reference_data_path)
            self.reference_df = df.drop('target', axis=1)
        else:
            print("Reference CSV not found. Generating synthetic reference data for CI.")
            # Generate synthetic reference based on typical California housing stats
            np.random.seed(42)
            n_samples = 1000
            self.reference_df = pd.DataFrame({
                'MedInc': np.random.normal(3.87, 1.9, n_samples),
                'HouseAge': np.random.normal(28.6, 12.6, n_samples),
                'AveRooms': np.random.normal(5.43, 2.5, n_samples),
                'AveBedrms': np.random.normal(1.08, 0.5, n_samples),
                'Population': np.random.normal(1425, 1132, n_samples),
                'AveOccup': np.random.normal(3.07, 10.4, n_samples),
                'Latitude': np.random.normal(35.6, 2.0, n_samples),
                'Longitude': np.random.normal(-119.6, 2.0, n_samples)
            })
        self.num_features = self.reference_df.columns.tolist()
    
    def _calculate_psi(self, expected, actual, bins=10):
        expected = np.array(expected)
        actual = np.array(actual)
        combined = np.concatenate([expected, actual])
        percentiles = np.linspace(0, 100, bins+1)
        bin_edges = np.percentile(combined, percentiles)
        bin_edges[0] = -np.inf
        bin_edges[-1] = np.inf
        
        expected_bins = np.histogram(expected, bins=bin_edges)[0]
        expected_pct = expected_bins / len(expected)
        actual_bins = np.histogram(actual, bins=bin_edges)[0]
        actual_pct = actual_bins / len(actual)
        
        psi = 0.0
        for e_pct, a_pct in zip(expected_pct, actual_pct):
            if a_pct > 0 and e_pct > 0:
                psi += (a_pct - e_pct) * np.log(a_pct / e_pct)
        return min(psi, 2.0)
    
    def check_drift(self, current_df: pd.DataFrame) -> dict:
        drift_by_feature = {}
        for feature in self.num_features:
            if feature in current_df.columns:
                psi = self._calculate_psi(
                    self.reference_df[feature].dropna(),
                    current_df[feature].dropna()
                )
                drift_by_feature[feature] = {
                    "psi": float(round(psi, 4)),
                    "drift_detected": bool(psi > 0.25)
                }
        drift_detected = any(v["drift_detected"] for v in drift_by_feature.values())
        return {
            "timestamp": datetime.now().isoformat(),
            "drift_detected": bool(drift_detected),
            "drift_by_feature": drift_by_feature,
            "num_features_drifted": int(sum(1 for v in drift_by_feature.values() if v["drift_detected"]))
        }

def simulate_current_data(n_samples=100):
    np.random.seed(42)
    return pd.DataFrame({
        'MedInc': np.random.normal(3.5, 1.2, n_samples),
        'HouseAge': np.random.normal(32, 12, n_samples),
        'AveRooms': np.random.normal(5.5, 1.8, n_samples),
        'AveBedrms': np.random.normal(1.1, 0.4, n_samples),
        'Population': np.random.normal(1100, 700, n_samples),
        'AveOccup': np.random.normal(2.9, 1.2, n_samples),
        'Latitude': np.random.normal(37.6, 0.4, n_samples),
        'Longitude': np.random.normal(-122.0, 0.9, n_samples)
    })

if __name__ == "__main__":
    monitor = DriftMonitor()
    current = simulate_current_data()
    result = monitor.check_drift(current)
    print(json.dumps(result, indent=2))
    with open('drift_report.json', 'w') as f:
        json.dump(result, f, indent=2)
