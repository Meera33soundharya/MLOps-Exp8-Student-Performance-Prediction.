import pandas as pd
import joblib
import os
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report
from sklearn.model_selection import train_test_split

def evaluate_model():
    model_path = 'model/student_model.pkl'
    data_path = 'data/student_data.csv'

    if not os.path.exists(model_path):
        print(f"Model not found at {model_path}. Run train.py first.")
        return

    if not os.path.exists(data_path):
        print(f"Data not found at {data_path}. Run generate_data.py first.")
        return

    # Load model and data
    model = joblib.load(model_path)
    df = pd.read_csv(data_path)

    X = df.drop('result', axis=1)
    y = df['result'].map({'Pass': 1, 'Fail': 0})

    # Get the test set
    _, X_test, _, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Predict
    y_pred = model.predict(X_test)

    # Calculate metrics
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    print("Student Performance Model Evaluation\n")
    print(f"Accuracy  : {acc:.2f}")
    print(f"Precision : {prec:.2f}")
    print(f"Recall    : {rec:.2f}")
    print(f"F1 Score  : {f1:.2f}\n")

    print("Classification Report:")
    # Map back to Pass/Fail for the report
    target_names = ['Fail', 'Pass']
    print(classification_report(y_test, y_pred, target_names=target_names))

if __name__ == '__main__':
    evaluate_model()
