# 🏠 MLOps House Price Predictor

[![CI/CD](https://github.com/avinashmnth2507-dev/mlops-house-price-predictor/actions/workflows/ci-cd.yml/badge.svg?branch=master)](https://github.com/avinashmnth2507-dev/mlops-house-price-predictor/actions/workflows/ci-cd.yml)
[![Docker](https://img.shields.io/badge/docker-ghcr.io-blue?logo=docker)](https://github.com/avinashmnth2507-dev/mlops-house-price-predictor/pkgs/container/house-price-api)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

Production-ready MLOps pipeline that trains a house price prediction model, serves predictions through 
FastAPI,
containerizes with Docker, orchestrates with Kubernetes, and automates CI/CD using GitHub Actions.

Includes advanced production-grade features:

- Model Drift Detection
- Prometheus & Grafana Monitoring
- FinOps Cost Tracking
- MLflow Experiment Tracking
- Kubernetes Deployment

---

# 🚀 Features

- ✅ Data Versioning using DVC
- ✅ MLflow Experiment Tracking
- ✅ Optuna Hyperparameter Tuning
- ✅ FastAPI REST API
- ✅ Dockerized Application
- ✅ GitHub Actions CI/CD
- ✅ Kubernetes Deployment
- ✅ PSI-based Drift Monitoring
- ✅ Prometheus Metrics
- ✅ Grafana Dashboards
- ✅ FinOps Cost Tracking
- ✅ GitHub Container Registry (GHCR)

---

# 📦 Quick Start

## 1️⃣ Clone Repository

```bash
git clone https://github.com/avinashmnth2507-dev/mlops-house-price-predictor.git
cd mlops-house-price-predictor
```

---

## 2️⃣ Create Virtual Environment

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run FastAPI Application

```bash
uvicorn app.main:app --reload
```

API will run at:

```bash
http://127.0.0.1:8000
```

---

# 🖼️ Demo

## 🚀 API Prediction

FastAPI endpoint serving real-time house price predictions.

![API Prediction](images/prediction.png)

---

## 📊 MLflow Experiment Tracking

Track model experiments, metrics, parameters, and artifacts.

![MLflow Tracking](images/mlflow-ui.png)

---

## 📈 Drift Monitoring

PSI-based model drift monitoring and production validation.

![Drift Monitoring](images/drift_check_output.png)

### Drift Detection Endpoint

![Drift Endpoint](images/drift_endpoint.png)

---

## ⚙️ GitHub Actions CI/CD

Automated testing, Docker build, and deployment pipeline.

![GitHub Actions](images/github-actions.png)

---

## 📡 Prometheus + Grafana Monitoring

### Grafana Datasource

![Grafana Datasource](images/grafana_datasource.png)

### Grafana Dashboard

![Grafana Dashboard](images/grafana_dashboard.png)

### Prometheus Service Discovery

![Prometheus Discovery](images/prometheus_service_discovery.png)

---

## 💰 FinOps Cost Tracking

Infrastructure cost monitoring and optimization recommendations.

![FinOps Cost](images/finops_cost.png)

---

## ☸️ Kubernetes Deployment

### Kubernetes Pods

![Kubernetes Pods](images/k8s-pods.png)

### Kubernetes Prediction Service

![Kubernetes Prediction](images/k8s-prediction.png)

---

## 📦 Published Container Image

Docker image published to GitHub Container Registry.

![GHCR Package](images/ghcr-package.png)

---

## 🐳 Docker

### Build the image
```bash
docker build -t house-price-api:latest .
```

## Run Docker Container

```bash
docker run -p 8000:8000 mlops-house-price-predictor
```

---

## ☸️ Kubernetes Deployment

> Requires a running Kubernetes cluster (e.g., Minikube).

Apply the manifests:
```bash
kubectl apply -f k8s/
Check pods:

kubectl get pods
```

---

# 📊 MLflow

Start MLflow UI:

```bash
mlflow ui
```

Open:

```bash
http://127.0.0.1:5000
```

---

## 📡 Monitoring

> Prometheus and Grafana are deployed via Helm in the `monitoring` namespace. See 
[ARCHITECTURE.md](ARCHITECTURE.md) for details.

- **Prometheus metrics**: `/metrics`
- **Drift monitoring**: `/drift/status`
- **FinOps cost**: `/cost`
```

---

# 🛠️ Tech Stack

- Python 3.12
- FastAPI
- Scikit-learn
- MLflow
- Optuna
- Evidently AI
- Docker
- Kubernetes
- Prometheus
- Grafana
- GitHub Actions
- DVC

---

# 📜 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

Avinash Mani Tripathi

GitHub:
https://github.com/avinashmnth2507-dev
