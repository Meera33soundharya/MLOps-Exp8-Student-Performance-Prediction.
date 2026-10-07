import pandas as pd
import numpy as np
import os

def generate_data():
    os.makedirs('data', exist_ok=True)
    np.random.seed(42)
    n_samples = 500

    study_hours = np.random.uniform(1.0, 10.0, n_samples)
    attendance = np.random.uniform(50, 100, n_samples)
    previous_marks = np.random.uniform(40, 100, n_samples)
    assignment_score = np.random.uniform(40, 100, n_samples)
    internal_score = np.random.uniform(40, 100, n_samples)

    # Simple logic to determine Pass/Fail
    # Weighted average score
    score = (0.2 * study_hours * 10) + (0.2 * attendance) + (0.2 * previous_marks) + (0.2 * assignment_score) + (0.2 * internal_score)
    
    # Threshold for passing (adjust for balance)
    threshold = np.median(score)
    result = ['Pass' if s >= threshold else 'Fail' for s in score]

    df = pd.DataFrame({
        'study_hours': np.round(study_hours, 1),
        'attendance': np.round(attendance, 1),
        'previous_marks': np.round(previous_marks, 1),
        'assignment_score': np.round(assignment_score, 1),
        'internal_score': np.round(internal_score, 1),
        'result': result
    })

    df.to_csv('data/student_data.csv', index=False)
    print(f"Generated {n_samples} records in data/student_data.csv")
    print(df['result'].value_counts())

if __name__ == '__main__':
    generate_data()
