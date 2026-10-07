from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
import os

# Adjust default args
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Define DAG
with DAG(
    'student_performance_pipeline',
    default_args=default_args,
    description='A simple MLOps pipeline for Student Performance Prediction',
    schedule_interval='@daily',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['mlops'],
) as dag:

    # Define tasks using BashOperator to run the python scripts
    # We assume Airflow runs in the project root or the script paths are absolute.
    # For a simple local setup, assuming execution from the project root:

    generate_data_task = BashOperator(
        task_id='generate_data',
        bash_command='python src/generate_data.py ',
    )

    train_model_task = BashOperator(
        task_id='train_model',
        bash_command='python src/train.py ',
    )

    evaluate_model_task = BashOperator(
        task_id='evaluate_model',
        bash_command='python src/evaluate.py ',
    )

    # Set task dependencies
    generate_data_task >> train_model_task >> evaluate_model_task
