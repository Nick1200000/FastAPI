from fastapi import FastAPI, Path, HTTPException
import os
import json

app = FastAPI()

def load_data():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "patients.json")
    with open(file_path, "r") as f:
        data = json.load(f)

    return data 

@app.get("/")
def root():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message": "This is a Patient Management System API built with FastAPI."}

@app.get("/view")
def view():
    data = load_data()
    return data

@app.get("/patient/{patient_id}")
def patient_view(patient_id: str = Path(..., description="The ID of the patient to view", example="P001")):
    data = load_data()
    if patient_id in data:
        return data[patient_id]
    # return {"error": "patient not found"}
    raise HTTPException(status_code=404, detail="Patient not found")    