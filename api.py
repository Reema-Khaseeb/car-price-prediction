from http import HTTPStatus
from typing import Dict
import pickle
from fastapi import FastAPI, Request
from sklearn.preprocessing import PolynomialFeatures
import numpy as np
import uvicorn
import requests

# from src.data_handler import Sample


models = pickle.load(open('./pkls/models1.pkl', 'rb'))
best_model = models['ols']['model']


# Define application
app = FastAPI()


# Check the connection is OK by initial path
@app.get("/")
def _health_check() -> Dict:
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {},
    }
    return response


@app.post("/predict/")
async def _predicted_price(reqest: Sample) -> Dict:
    data = await reqest.json()
    values = np.array(list(data.values()))
    predict = best_model.predict(values.reshape(1, len(values)))[0]
    # print('\n\n',predict, '\n\n')
    print('\n\n', values.reshape(1, len(values)), '\n\n')
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "values": f"{values}",
        'pred': f"{predict}"
    }
    return response
