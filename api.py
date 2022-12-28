# Standard library imports
from http import HTTPStatus
from typing import Dict
import pickle

# Third-party library imports
import pandas as pd
from fastapi import FastAPI

# Local application/library-specific imports
from src.data_handler import Sample


model_pipeline = pickle.load(open('./pkls/best_model_gbt_random_search.pkl', 'rb'))

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
    predection = model_pipeline.predict(sample_dataframe)[0]
    response = {
        'prediction': predection
    }
    return response
