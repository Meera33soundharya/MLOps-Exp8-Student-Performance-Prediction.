from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import joblib
import os
import pandas as pd

app = FastAPI(title="Student Performance Prediction API")

MODEL_PATH = "model/student_model.pkl"
model = None

# Load model at startup
@app.on_event("startup")
def load_model():
    global model
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)

class StudentData(BaseModel):
    study_hours: float = Field(..., ge=0, le=24, description="Hours studied per week")
    attendance: float = Field(..., ge=0, le=100, description="Attendance percentage")
    previous_marks: float = Field(..., ge=0, le=100, description="Previous marks percentage")
    assignment_score: float = Field(..., ge=0, le=100, description="Assignment score percentage")
    internal_score: float = Field(..., ge=0, le=100, description="Internal exam score percentage")

@app.get("/")
def read_root():
    return {"message": "Student Performance Prediction API"}

@app.get("/health")
def health_check():
    if model is None:
        return {"status": "unhealthy", "reason": "Model not loaded"}
    return {"status": "healthy"}

@app.post("/predict")
def predict_performance(data: StudentData):
    if model is None:
        raise HTTPException(status_code=503, detail="Model not loaded. Please train the model first.")
    
    # Prepare data for prediction
    input_df = pd.DataFrame([data.dict()])
    
    try:
        prediction = model.predict(input_df)
        result = "Pass" if prediction[0] == 1 else "Fail"
        return {"prediction": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
