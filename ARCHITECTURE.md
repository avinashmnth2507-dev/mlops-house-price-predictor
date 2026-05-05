# 🏗️ System Architecture (Core Completed)

The following diagram shows the components already implemented and integrated.

```mermaid
graph TB
    subgraph "Data and Training"
        A[California Housing Dataset] -->|DVC| B[Versioned Data]
        B -->|Optuna| C[Hyperparameter Tuning]
        C -->|MLflow| D[Model Training]
        D --> E[model.joblib]
    end

    subgraph "Serving"
        E --> F[FastAPI app]
        F -->|/predict| G[Prediction]
        F -->|/health| H[Health Check]
    end

    subgraph "Container and Orchestration"
        F -->|Dockerfile| I[Docker Image]
        I -->|k8s deployment| J[Kubernetes Pods 2 replicas]
        J -->|Service| K[LoadBalancer or Port-forward]
    end

    subgraph "CI/CD"
        L[Git push] -->|GitHub Actions| M[Run tests]
        M --> N[Build Docker image]
        N --> O[Push to ghcr.io]
        O -->|Trigger| J
    end

    K -->|curl| G
