from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI",
        "author": "Learn With Motaleb",
        "version": "1.0.0"
    }


@app.get("/about")
def about():
    return {
        "message": "This is a FastAPI application",
        "author": "Learn With Motaleb",
        "version": "1.0.0"
    }

@app.get("/contact")
def contact():
    return {
        "message": "Contact us at info@learnwithmotaleb.com",
        "author": "Learn With Motaleb",
        "version": "1.0.0"
    }

@app.post("/submit")
def submit(data: dict):
    return {
        "message": "Data submitted successfully",
        "data": data,
        "author": "Learn With Motaleb",
        "version": "1.0.0"
    }

@app.get("/status")
def status():
    return{
        "message": "API is running",
        "status": "OK",
        "author": "Learn With Motaleb",
        "version": "1.0.0"
    }
@app.post("/status")
def status(data: dict):
    return{
        "message": "API is running",
        "status": "OK",
        "author": "Learn With Motaleb",
        "version": "1.0.0"
    }

@app.post("/login")
def login(data: dict):
    username = data.get("username")
    password = data.get("password")
    if username == "admin" and password == "password":
        return {
            "message": "Login successful",
            "author": "Learn With Motaleb",
            "version": "1.0.0"
        }
    else:
        return {
            "message": "Invalid credentials",
            "author": "Learn With Motaleb",
            "version": "1.0.0"
        }