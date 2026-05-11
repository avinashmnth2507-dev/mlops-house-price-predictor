# 🏠 MLOps House Price Predictor

[![CI/CD](https://github.com/avinashmnth2507-dev/mlops-house-price-predictor/actions/workflows/ci-cd.yml/badge.svg?branch=master)](https://github.com/avinashmnth2507-dev/mlops-house-price-predictor/actions/workflows/ci-cd.yml)
[![Docker](https://img.shields.io/badge/docker-ghcr.io-blue?logo=docker)](https://github.com/avinashmnth2507-dev/mlops-house-price-predictor/pkgs/container/house-price-api)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Production‑ready MLOps pipeline** – trains a house price model, serves predictions via a REST API, containerises with 
Docker, orchestrates with Kubernetes, and automates everything with GitHub Actions CI/CD. Includes advanced features: 
**model drift detection**, **Prometheus/Grafana monitoring**, and **FinOps cost tracking**.

---

## 🚀 Features (all completed)

- ✅ Data versioning with **DVC** (California Housing dataset)
- ✅ Model training with **MLflow** experiment tracking + **Optuna** hyperparameter tuning
- ✅ **FastAPI** prediction endpoint (`/predict`, `/health`)
- ✅ Dockerised service (Python 3.12)
- ✅ **GitHub Actions** CI/CD: test → build → push to GHCR
- ✅ **Kubernetes** deployment (Minikube) with 2 replicas, health probes
- ✅ **PSI‑based model drift monitoring** (`/drift/status`)
- ✅ **Prometheus metrics** endpoint (`/metrics`) + Grafana dashboard
- ✅ **FinOps cost tracking** (`/cost`) with recommendations
- ✅ Public container image on GitHub Container Registry

---

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/avinashmnth2507-dev/mlops-house-price-predictor.git
cd mlops-house-price-predictor
