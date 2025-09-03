import json
from asyncio import new_event_loop
from http.client import responses
from typing import List
from fastapi import FastAPI, Request
from pydantic import BaseModel
from pyexpat.errors import messages
from starlette.responses import Response, JSONResponse

app = FastAPI()

@app.get("/ping")
def ping():
    return {"ping": "pong"}

class cars(BaseModel):
    id: str
    brand: str
    model : str
    characteristics : object

cars : List[cars]

@app.post("/cars")
def create_car():
    cars.extend(cars)
    return JSONResponse({messages: "Created"}, status_code=201)

@app.get("/cars")
def read_cars(cars : cars):
    return JSONResponse(content="This is the list of cars"+cars, status_code=200)

@app.get("/cars/{id}")
def find_cars(id : str):
    if cars.id == id :
        return JSONResponse({messages: "Ok"}, status_code=200)
    else :
        return JSONResponse({messages: "Not found"}, status_code=404)
