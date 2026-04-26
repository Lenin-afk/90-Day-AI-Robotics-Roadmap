import json
import os
import numpy as np
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()
LOG_FILE = "sensor_history.json"

class SensorData(BaseModel):
    readings: List[float]

@app.post("/process-sensors")
def process_external_data(data: SensorData):
    # --- PREVIOUS LOGIC (Cleaning & Persistence) ---
    raw_list = np.array(data.readings)
    invalid_mask = (raw_list <= 0) | (raw_list > 500)
    raw_list[invalid_mask] = 50.0
    mean_val = float(np.mean(raw_list))
    cleaned_list = raw_list.tolist()
    
    new_entry = {
        "raw": data.readings,
        "cleaned": cleaned_list,
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

    return {"message": "Data processed and logged", "result": new_entry}

# --- DAY 12 TODO: HISTORY RETRIEVAL ENDPOINT ---

@app.get("/history")
def get_history(limit: int = 5):
    """
    Retrieves the last 'N' entries from the sensor history file.
    Example Usage: http://127.0.0
    """
    # 1. TODO: Defensive Check: Check if LOG_FILE exists. 
    # If not, return {"message": "No history found", "history": []}
    if not os.path.exists(LOG_FILE):
        return {"message": "No history found", "history": []}
    # 2. TODO: Read the file and load the JSON data into a variable 'all_logs'
    # Hint: with open(LOG_FILE, "r") as f: ...
    with open(LOG_FILE,"r") as f:
        all_logs=json.load(f)
    
    # 3. TODO: High-Pay Skill: Slicing the list.
    # Grab the most recent 'limit' number of entries from 'all_logs'
    # Hint: Use negative slicing: all_logs[-limit:]
    recent_logs = all_logs[-limit:] 

    # 4. TODO: Return a JSON response with status, total count, and the history list
    return {
        "status": "success",
        "total_in_storage": len(all_logs), # Update this with len(all_logs)
        "history": recent_logs
    }
