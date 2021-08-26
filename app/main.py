from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

from app.net import predict


class Image(BaseModel):
    base64_str: bytes


app = FastAPI(title="ArtWayNN")


@app.post('/predict/', response_model=List[float], tags=["Predict"])
async def make_prediction(image: Image):
    preds = predict(image.base64_str)
    return preds
