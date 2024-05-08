from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/add")
def add_numbers(x: int, y: int):
    return {"result": x + y}

@app.get("/subtract")
def subtract_numbers(x: int, y: int):
    return {"result": x - y}

@app.get("/multiply")
def multiply_numbers(x: int, y: int):
    return {"result": x * y}

@app.get("/divide")
def divide_numbers(x: int, y: int):
    if y == 0:
        return {"error": "Division by zero"}
    return {"result": x / y}
