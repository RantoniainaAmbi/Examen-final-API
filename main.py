import json
from http.client import responses
from typing import List
from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.responses import Response, JSONResponse

app = FastAPI()

@app.get("/ping")
def ping():
    return {"ping": "pong"}


@app.post("/cars")
def create_car():
    return

@app.get("/cars")
def read_cars(cars= cars):
    return JSONResponse(content="This is the list of cars"+cars, status_code=200)

@app.get("/cars/{id}")
def find_cars(id : str):
    if cars.id == id :
        return JSONResponse(content=find_car, status_code=200)
    else
        return JSONResponse(content= "Not found", status_code=404)
