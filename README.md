# 🏠 MLOps House Price Predictor

[![CI/CD](https://github.com/avinashmnth2507-dev/mlops-house-price-predictor/actions/workflows/ci-cd.yml/badge.svg?branch=master)](https://github.com/avinashmnth2507-dev/mlops-house-price-predictor/actions/workflows/ci-cd.yml)
[![Docker](https://img.shields.io/badge/docker-ghcr.io-blue?logo=docker)](https://github.com/avinashmnth2507-dev/mlops-house-price-predictor/pkgs/container/house-price-api)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Production‑ready MLOps pipeline** – trains a house price model, serves predictions via REST API, containerises with Docker, orchestrates with Kubernetes, and automates everything with GitHub Actions CI/CD.

---

## 🚀 Features (completed)

- ✅ Data versioning with **DVC** (California Housing dataset)
- ✅ Model training with **MLflow** + **Optuna** hyperparameter tuning
- ✅ **FastAPI** prediction endpoint (`/predict`, `/health`)
- ✅ Dockerised service (Python 3.12)
- ✅ **GitHub Actions** CI/CD: test → build → push to GHCR
- ✅ **Kubernetes** deployment (Minikube) with 2 replicas, health probes, port‑forward
- ✅ Public container image on GitHub Container Registry

---
## 🖼️ Demo

### API Prediction
![Prediction output](images/prediction.png)

### MLflow Experiment Tracking
![MLflow UI](images/mlflow-ui.png)

### GitHub Actions CI/CD
![GitHub Actions](images/github-actions.png)

### Docker Container
![Docker run](images/docker-demo.png)

### Kubernetes Deployment
![K8s pods](images/k8s-pods.png)
![K8s prediction](images/k8s-prediction.png)

### Published Container Image
![GHCR package](images/ghcr-package.png)
## 📦 Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/avinashmnth2507-dev/mlops-house-price-predictor.git
cd mlops-house-price-predictor
