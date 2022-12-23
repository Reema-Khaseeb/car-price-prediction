# Standard library imports
from http import HTTPStatus
from typing import Dict
import pickle

# Third-party library imports
import numpy as np
import pandas as pd
import requests
import uvicorn
from fastapi import FastAPI, Request

# Local application/library-specific imports
from src.data_handler import Sample, rename_columns_dict


model_pipeline = pickle.load(open('./pkls/gbr_model_pipeline.pkl', 'rb'))

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
def _predicted_price(sample: Sample) -> Dict:
    sample = [vars(sample)]
    sample_dataframe = pd.DataFrame(sample) 
    # sample_dataframe.rename(columns = rename_columns_dict, inplace=True)
    predection = model_pipeline.predict(sample_dataframe)[0]
    response = {
        'Car Price prediction': predection
    }
    return response
