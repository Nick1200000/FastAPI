from fastapi import FastAPI # pyright: ignore[reportMissingImports]
import os
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI from Codespaces!"}

@app.get("/about")
def about():
    return {"message":"This is Github Codespace"}
