FROM python:3.12-slim

WORKDIR /app

# Install only the packages needed for API serving
RUN pip install --no-cache-dir \
    fastapi==0.136.1 \
    joblib==1.5.3 \
    numpy==2.4.4 \
    pydantic==2.13.3 \
    scikit-learn==1.8.0 \
    uvicorn[standard]==0.46.0

COPY src/ ./src/
COPY models/model.joblib ./models/

EXPOSE 8000

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]
