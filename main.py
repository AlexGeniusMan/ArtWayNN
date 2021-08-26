from fastapi import FastAPI
from net import predict
from pydantic import BaseModel
from typing import List


class Image(BaseModel):
    base64_str: bytes


app = FastAPI(title="ArtWayNN")


@app.post('/predict/', response_model=List[float], tags=["Predict"])
async def make_prediction(image: Image):
    preds = predict(image.base64_str)
    return preds
