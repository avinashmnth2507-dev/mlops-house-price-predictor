import pandas as pd
import numpy as np
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
import optuna
import joblib
import os

mlflow.set_tracking_uri("file:./mlruns")

def load_data():
    df = pd.read_csv('data/raw/california_housing.csv')
    X = df.drop('target', axis=1)
    y = df['target']
    return train_test_split(X, y, test_size=0.2, random_state=42)

def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))

def objective(trial, X_train, y_train, X_val, y_val):
    params = {
        'n_estimators': trial.suggest_int('n_estimators', 50, 300),
        'max_depth': trial.suggest_int('max_depth', 3, 20),
        'min_samples_split': trial.suggest_int('min_samples_split', 2, 10),
        'min_samples_leaf': trial.suggest_int('min_samples_leaf', 1, 5)
    }
    model = RandomForestRegressor(**params, random_state=42, n_jobs=-1)
    model.fit(X_train, y_train)
    preds = model.predict(X_val)
    return rmse(y_val, preds)

def main():
    X_train, X_test, y_train, y_test = load_data()
    
    study = optuna.create_study(direction='minimize')
    study.optimize(lambda trial: objective(trial, X_train, y_train, X_test, y_test), n_trials=10)
    best_params = study.best_params
    
    with mlflow.start_run(run_name="random_forest_tuned"):
        mlflow.log_params(best_params)
        
        model = RandomForestRegressor(**best_params, random_state=42, n_jobs=-1)
        model.fit(X_train, y_train)
        
        predictions = model.predict(X_test)
        rmse_val = rmse(y_test, predictions)
        r2 = r2_score(y_test, predictions)
        
        mlflow.log_metric("rmse", rmse_val)
        mlflow.log_metric("r2", r2)
        
        os.makedirs('models', exist_ok=True)
        joblib.dump(model, 'models/model.joblib')
        mlflow.sklearn.log_model(model, "model")
        
        print(f"Best RMSE: {rmse_val:.3f}, R2: {r2:.3f}")
        print(f"Best parameters: {best_params}")
        print("Model saved to models/model.joblib")

if __name__ == "__main__":
    main()
