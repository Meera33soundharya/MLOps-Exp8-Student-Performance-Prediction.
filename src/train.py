import pandas as pd
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import warnings
warnings.filterwarnings('ignore')

def train_models():
    print("Training Student Performance Model...\n")

    # 1. Load data
    data_path = 'data/student_data.csv'
    if not os.path.exists(data_path):
        print(f"Data not found at {data_path}. Please run generate_data.py first.")
        return

    df = pd.read_csv(data_path)

    # 2. Separate features and target
    X = df.drop('result', axis=1)
    y = df['result']

    # 3. Convert Pass/Fail to 1/0
    y = y.map({'Pass': 1, 'Fail': 0})

    # 4. Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # 5. Preprocessing & Models (Pipeline)
    log_reg_pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', LogisticRegression(random_state=42))
    ])

    rf_pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('classifier', RandomForestClassifier(random_state=42))
    ])

    # 6. Train Models
    log_reg_pipeline.fit(X_train, y_train)
    rf_pipeline.fit(X_train, y_train)

    # 7. Evaluate Models for Selection
    log_reg_preds = log_reg_pipeline.predict(X_test)
    rf_preds = rf_pipeline.predict(X_test)

    log_reg_f1 = f1_score(y_test, log_reg_preds)
    rf_f1 = f1_score(y_test, rf_preds)

    print(f"Logistic Regression F1 Score: {log_reg_f1:.4f}")
    print(f"Random Forest F1 Score: {rf_f1:.4f}")

    # 8. Select best model
    if rf_f1 >= log_reg_f1:
        best_model = rf_pipeline
        best_name = "Random Forest"
    else:
        best_model = log_reg_pipeline
        best_name = "Logistic Regression"

    print(f"\nBest Model: {best_name}\n")

    # 9. Save the selected model
    os.makedirs('model', exist_ok=True)
    model_path = 'model/student_model.pkl'
    joblib.dump(best_model, model_path)
    
    print(f"Model saved successfully:\n{model_path}")

if __name__ == '__main__':
    train_models()
