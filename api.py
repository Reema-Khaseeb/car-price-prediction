# Standard library imports
from http import HTTPStatus
from typing import Dict
import pickle

# Third-party library imports
import numpy as np
import pandas as pd
import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Local application/library-specific imports
from src.data_handler import Sample, rename_columns_dict



gbr_model_hp_pipeline = pickle.load(open('./pkls/best_model_gbr_random_search.pkl', 'rb'))



# Define application
app = FastAPI()

# templates = Jinja2Templates(directory="templates")

# app.mount("./Front-End/static", StaticFiles(directory="/Front-End/static"), name="static")

# Check the connection is OK by initial path
@app.get("/")
def _health_check() -> Dict:
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {},
    }
    return response

# @app.get('/render_template')
# def render_template(request: Request):
#     return templates.TemplateResponse("predict-car-price.html", {
#     "request": request,
#     })


@app.post("/predict/")
def _predicted_price(sample: Sample) -> Dict:
    sample = [vars(sample)]
    sample_dataframe = pd.DataFrame(sample) 
    # sample_dataframe.rename(columns = rename_columns_dict, inplace=True)
    predection = gbr_model_hp_pipeline.predict(sample_dataframe)[0]
    response = {
        'prediction': predection
    }
    return response
