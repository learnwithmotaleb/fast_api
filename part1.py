from fastapi import FastAPI

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