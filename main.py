import json
from typing import List
from fastapi import FastAPI, Request
from pydantic import BaseModel
from starlette.responses import Response

app = FastAPI()

@app.get("/ping")
def ping():
    return {"ping": "pong"}