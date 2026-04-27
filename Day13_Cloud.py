import json
import os
import numpy as np
import requests
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
from typing import List

app = FastAPI()
LOG_FILE = "sensor_history.json"
# This URL simulates a real cloud receiver
CLOUD_URL = "https://httpbin.org/post"


class SensorData(BaseModel):
    readings: List[float]

# --- DAY 13: THE UPLINK FUNCTION ---


def send_to_cloud(data_to_send: dict):
    """
    Simulates sending data to a remote cloud server.
    """
    print(f"☁️ Cloud Sync: Attempting to upload to {CLOUD_URL}...")

    # 1. TODO: Use requests.post() to send the 'data_to_send' to 'CLOUD_URL'
    # 2. TODO: Check if response.status_code is 200 or 201.
    # 3. TODO: Print "Sync Success" or "Sync Failed" based on the result.
    response = requests.post(CLOUD_URL, data_to_send)
    if response.status_code in [200, 201]:
        print("Sync Success")
    else:
        print("Sync Failed")


@app.post("/process-sensors")
def process_external_data(data: SensorData, background_tasks: BackgroundTasks):
    # --- PREVIOUS LOGIC ---
    raw_list = np.array(data.readings)
    invalid_mask = (raw_list <= 0) | (raw_list > 500)
    raw_list[invalid_mask] = 50.0
    mean_val = float(np.mean(raw_list))

    new_entry = {
        "raw": data.readings,
        "cleaned": raw_list.tolist(),
        "avg": mean_val
    }

    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f:
            json.dump([], f)
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)
    logs.append(new_entry)
    with open(LOG_FILE, "w") as f:
        json.dump(logs, f, indent=4)

    # --- DAY 13 TODO: BACKGROUND TASK ---
    # 4. TODO: Add 'send_to_cloud' to the background_tasks queue
    # Hint: background_tasks.add_task(function_name, argument)
    background_tasks.add_task(send_to_cloud, new_entry)

    return {"message": "Processing complete. Cloud sync started.", "result": new_entry}


@app.get("/history")
def get_history(limit: int = 5):
    if not os.path.exists(LOG_FILE):
        return {"history": []}
    with open(LOG_FILE, "r") as f:
        all_logs = json.load(f)
    return {"history": all_logs[-limit:]}
