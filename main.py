from fastapi import FastAPI
from net import predict
from pydantic import BaseModel


class Image(BaseModel):
    base64_str: bytes


class Prediction(BaseModel):
    label_id: int


app = FastAPI(title="ArtWayNN")


@app.post('/predict', response_model=Prediction)
def make_prediction(image: Image):
    '''
    Predict the image's label.
    '''

    label_id = predict(image.base64_str)
    return Prediction(label_id=label_id+1)
