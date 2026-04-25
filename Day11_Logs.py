import json
import os
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import numpy as np

app = FastAPI()
LOG_FILE = "sensor_history.json"


class SensorData(BaseModel):
    readings: List[float]


@app.post("/process-sensors")
def process_external_data(data: SensorData):
    # --- YOUR EXISTING LOGIC ---
    raw_list = np.array(data.readings)
    invalid_mask = (raw_list <= 0) | (raw_list > 500)
    raw_list[invalid_mask] = 50.0
    mean_val = float(np.mean(raw_list))
    cleaned_list = raw_list.tolist()

    # This is the "Record" we want to save
    new_entry = {
        "raw": data.readings,
        "cleaned": cleaned_list,
        "avg": mean_val
    }

    # --- DAY 11 TODO: THE MEMORY LOGIC ---

    # 1. TODO: Check if LOG_FILE exists. If not, create it with an empty list [].
    # Hint: if not os.path.exists(LOG_FILE): ...
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE,"w") as f:
            json.dump([],f)
    # 2. TODO: Open the file in 'read' mode, load the current list of logs.
    # Hint: with open(LOG_FILE, "r") as f: logs = json.load(f)
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)

    # 3. TODO: Append 'new_entry' to your list of logs.
    logs.append(new_entry)

    # 4. TODO: Open the file in 'write' mode and save the updated list.
    # Hint: json.dump(logs, f, indent=4)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

    return {"message": "Data processed and logged", "result": new_entry}
