# MLOps-Exp8-Student-Performance-Prediction

[![Python Version](https://img.shields.io/badge/python-3.11-blue.svg)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.103.1-009688.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com)
[![Docker](https://img.shields.io/badge/Docker-Enabled-2496ED.svg?style=flat&logo=Docker&logoColor=white)](https://www.docker.com/)
[![Apache Airflow](https://img.shields.io/badge/Airflow-Pipeline-017CEE.svg?style=flat&logo=Apache-Airflow&logoColor=white)](https://airflow.apache.org/)

## 📖 Overview

The **Student Performance Prediction** project is a comprehensive end-to-end Machine Learning Operations (MLOps) demonstration. This system predicts whether a student will pass or fail based on core academic metrics. It showcases the lifecycle of an ML project, bridging the gap between model development and production deployment.

This repository implements synthetic data generation, model training and selection (Logistic Regression vs. Random Forest), model serving via a REST API, containerization for reproducibility, and pipeline orchestration.

---

## ✨ Features

- **Synthetic Data Generation**: Reproducibly generates balanced, realistic datasets without requiring external dependencies.
- **Automated Model Training & Evaluation**: Trains multiple classification algorithms, automatically evaluates them using Accuracy, Precision, Recall, and F1-Score, and persists the optimal model.
- **RESTful API Serving**: Leverages FastAPI to serve predictions rapidly with built-in Pydantic data validation.
- **Containerization**: Includes a lightweight, production-ready `Dockerfile` ensuring parity across environments.
- **Pipeline Orchestration**: Integrates with Apache Airflow to automate the data-to-deployment workflow.

---

## 🏗️ Architecture Architecture & Workflow

1. **Data Generation** (`src/generate_data.py`) ➔ Creates synthetic student records.
2. **Model Training** (`src/train.py`) ➔ Trains LogReg & RF, selects the best model based on F1-Score, and exports `student_model.pkl`.
3. **Model Evaluation** (`src/evaluate.py`) ➔ Validates the serialized model against the holdout test set.
4. **API Serving** (`api/app.py`) ➔ Loads the model into a FastAPI instance and exposes a `/predict` endpoint.
5. **Containerization** (`Dockerfile`) ➔ Packages the application into a standalone Docker image.
6. **Orchestration** (`airflow/student_pipeline.py`) ➔ Automates the sequential execution of the data pipeline.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.9+
- Docker (optional, for containerization)
- Git

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Meera33soundharya/MLOps-Exp8-Student-Performance-Prediction..git
   cd MLOps-Exp8-Student-Performance-Prediction
   ```

2. **Create and activate a virtual environment:**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🧠 Model Training Lifecycle

To execute the core machine learning pipeline locally, run the following scripts sequentially:

```bash
# 1. Generate the dataset
python src/generate_data.py

# 2. Train the models and save the best pipeline
python src/train.py

# 3. Evaluate model performance metrics
python src/evaluate.py
```

---

## 🌐 API Deployment

### Running Locally (Uvicorn)

Start the FastAPI server:
```bash
uvicorn api.app:app --host 0.0.0.0 --port 8000 --reload
```
- **Health Check**: `http://localhost:8000/health`
- **Interactive API Docs (Swagger UI)**: `http://localhost:8000/docs`

### Sample Prediction Request (cURL)

```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "study_hours": 6.5,
  "attendance": 88.0,
  "previous_marks": 75.0,
  "assignment_score": 82.5,
  "internal_score": 80.0
}'
```

---

## 🐳 Docker Containerization

Deploy the API seamlessly using Docker.

1. **Build the image:**
   ```bash
   docker build -t student-performance-api:v1 .
   ```

2. **Run the container:**
   ```bash
   docker run -d -p 8000:8000 --name student_api student-performance-api:v1
   ```
The API will be accessible at `http://localhost:8000`.

---

## 🔄 Airflow Orchestration

An Apache Airflow DAG is provided in `airflow/student_pipeline.py`. To utilize it:
1. Copy the DAG file to your Airflow `dags/` directory.
2. The DAG `student_performance_pipeline` will orchestrate the data generation, training, and evaluation steps automatically.

---

## 📄 License

This project is licensed under the MIT License.
