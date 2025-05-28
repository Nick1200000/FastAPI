from fastapi import FastAPI # pyright: ignore[reportMissingImports]
import json
import os

app = FastAPI()

def load_data():
    base_path = os.path.dirname(__file__)
    file_path = os.path.join(base_path, "patients.json")
    with open(file_path, "r") as f:
        data = json.load(f)
    
    return data

@app.get("/")
def hello():
    return {"message": "Patient Management System API"}

@app.get("/about")
def about():
    return {"message": "This is a Patient Management System API built with FastAPI."}

@app.get("/view")
def view():
    data = load_data()
    return data

