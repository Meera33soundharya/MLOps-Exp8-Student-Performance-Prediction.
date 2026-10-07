# Student Performance MLOps

## Overview
This project predicts whether a student will Pass or Fail using machine learning based on basic student-related features. It demonstrates a simple and beginner-friendly MLOps workflow, including data generation, model training, evaluation, a prediction API, containerization, and workflow orchestration.

## Features
* Synthetic dataset generation
* Machine learning training
* Logistic Regression
* Random Forest
* Model evaluation
* Best model selection
* Model persistence
* FastAPI prediction API
* Docker deployment
* Airflow pipeline

## Architecture
```text
Student Data
     ↓
Data Generation
     ↓
Model Training
     ↓
Model Evaluation
     ↓
Best Model
     ↓
student_model.pkl
     ↓
FastAPI
     ↓
Docker
```

## Installation
1. Clone or download this repository.
2. Navigate into the project folder: `cd Student-Performance-MLOps`
3. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   # On Windows: venv\Scripts\activate
   # On Mac/Linux: source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Run Training
To generate data and train the model, run:
```bash
python src/generate_data.py
python src/train.py
```

## Run Evaluation
To evaluate the trained model, run:
```bash
python src/evaluate.py
```

## Run FastAPI
To start the prediction API, run:
```bash
uvicorn api.app:app --reload --port 8000
```
* **API URL**: `http://127.0.0.1:8000`
* **Swagger Docs**: `http://127.0.0.1:8000/docs`

### Example API Request
Using `curl` or Postman:
```json
{
  "study_hours": 6,
  "attendance": 85,
  "previous_marks": 75,
  "assignment_score": 80,
  "internal_score": 78
}
```

## Docker
To build and run the API using Docker:
```bash
docker build -t student-performance-api:v1 .
docker run -p 8000:8000 student-performance-api:v1
```

## Airflow
The project includes a basic Apache Airflow DAG in `airflow/student_pipeline.py`.
The pipeline executes tasks in the following sequence:
```text
generate_data → train_model → evaluate_model
```
To run it, copy `airflow/student_pipeline.py` to your Airflow `dags` folder and enable the `student_performance_pipeline` DAG in the Airflow UI.

## MLOps Workflow
This project covers an end-to-end MLOps workflow:
1. **Data Generation**: Creates synthetic student records.
2. **Training & Selection**: Trains Logistic Regression and Random Forest models, picking the one with the best F1 Score.
3. **Persistence**: Saves the best model pipeline (`student_model.pkl`).
4. **Evaluation**: Evaluates the saved model against the test set.
5. **Deployment**: Serves the model via a FastAPI endpoint.
6. **Containerization**: Packages the API into a Docker image.
7. **Orchestration**: Automates the training workflow using Apache Airflow.
