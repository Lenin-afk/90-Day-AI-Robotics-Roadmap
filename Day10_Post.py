from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import numpy as np

app = FastAPI()

# This 'Schema' tells the API exactly what kind of data to expect


class SensorData(BaseModel):
    readings: List[float]  # A list of decimal numbers


@app.post("/process-sensors")
def process_external_data(data: SensorData):
    # The user sends data like: {"readings": [10, -5, 999, 50]}
    raw_list = data.readings
    raw_list = np.array(raw_list)
    invalid_mask = (raw_list <= 0) | (raw_list > 500)
    raw_list[invalid_mask] = 50.0
    mean = np.mean(raw_list)
    # TODO: Convert the raw_list into a NumPy array
    # TODO: Apply your "Day 4" Cleaning Logic:
    #       Replace values <= 0 or > 500 with 50.0

    # TODO: Calculate the mean of the cleaned data

    # TODO: Return a JSON response with:
    # 1. "cleaned_readings" (as a list)
    # 2. "safe_to_proceed" (True if mean > 20, else False)
    return {
        "cleaned_readings": raw_list.tolist(),
        "safe_to_proceed": True if mean > 20 else False
    }
