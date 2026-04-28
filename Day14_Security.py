import json
import os
import numpy as np
import requests
from fastapi import FastAPI, BackgroundTasks, HTTPException, Security, Depends
from fastapi.security.api_key import APIKeyHeader
from pydantic import BaseModel
from typing import List
from starlette import status

app = FastAPI()
LOG_FILE = "sensor_history.json"
CLOUD_URL = "https://httpbin.org"

# --- SECURITY CONFIG ---
API_KEY = "SUPER_SECRET_ROBOT_KEY_123"
API_KEY_NAME = "access_token"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

def get_api_key(header_value: str = Depends(api_key_header)):
    # TODO: Check if header_value == API_KEY
    # If no match, raise HTTPException(status_code=403, detail="Invalid Key")
    if header_value == API_KEY:
        return header_value
    raise HTTPException(status_code=403, detail="Invalid API Key")

class SensorData(BaseModel):
    readings: List[float]

# --- DAY 13 LOGIC: CLOUD UPLINK ---
def send_to_cloud(data_to_send: dict):
    try:
        response = requests.post(CLOUD_URL, json=data_to_send)
        if response.status_code in [200, 201]:
            print("✅ Cloud Sync Success")
    except Exception as e:
        print(f"❌ Cloud Sync Failed: {e}")

# --- PROTECTED ENDPOINTS ---

@app.post("/process-sensors")
def process_external_data(
    data: SensorData, 
    background_tasks: BackgroundTasks,
    auth: str = Depends(get_api_key) # TODO: Complete the dependency
):
    # 1. NumPy Pipeline (Week 1)
    raw_list = np.array(data.readings)
    invalid_mask = (raw_list <= 0) | (raw_list > 500)
    raw_list[invalid_mask] = 50.0
    mean_val = float(np.mean(raw_list))
    
    new_entry = {
        "raw": data.readings,
        "cleaned": raw_list.tolist(),
        "avg": mean_val
    }

    # 2. Persistence (Day 11)
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, "w") as f: json.dump([], f)
    with open(LOG_FILE, "r") as f: logs = json.load(f)
    logs.append(new_entry)
    with open(LOG_FILE, "w") as f: json.dump(logs, f, indent=4)

    # 3. Background Cloud Sync (Day 13)
    background_tasks.add_task(send_to_cloud, new_entry)
    
    return {"message": "Authenticated, Processed & Syncing", "result": new_entry}

@app.get("/history")
def get_history(limit: int = 5, auth: str = Depends(get_api_key)):
    # TODO: Complete this dependency to protect history
    if not os.path.exists(LOG_FILE):
        return {"history": []}
    with open(LOG_FILE, "r") as f:
        all_logs = json.load(f)
    return {"history": all_logs[-limit:]}
