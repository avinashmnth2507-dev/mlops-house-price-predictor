import pandas as pd
from sklearn.datasets import fetch_california_housing
import os

def load_and_save_data(raw_path='data/raw/california_housing.csv'):
    data = fetch_california_housing(as_frame=True)
    df = data.frame
    df['target'] = data.target
    os.makedirs(os.path.dirname(raw_path), exist_ok=True)
    df.to_csv(raw_path, index=False)
    print(f"Data saved to {raw_path}")
    print(f"Shape: {df.shape}")
    return df

if __name__ == "__main__":
    load_and_save_data()
