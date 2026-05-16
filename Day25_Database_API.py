import json
import numpy as np
from fastapi import FastAPI, BackgroundTasks, HTTPException, Depends
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session

# Import our database infrastructure from previous days
from Day22_Database_Setup import SensorLogTable, SessionLocal, init_db
from Day24_Database_Query import get_recent_logs, get_incidents_only

app = FastAPI()

# Initialize tables on startup if they don't exist


@app.on_event("startup")
def startup_event():
    init_db()

# --- DAY 25 TODO: DATABASE DEPENDENCY INJECTION ---


def get_db():
    """
    Yields a database session per web request and guarantees closure after completion.
    This is a critical senior-level pattern to prevent database connection leaks.
    """
    db = SessionLocal()
    try:
        # TODO 1: Yield the database session to the FastAPI endpoint injection handler
        yield db
    finally:
        # TODO 2: Ensure the session is securely closed after the request lifecycle terminates
        db.close()


class SensorData(BaseModel):
    readings: List[float]

# --- DAY 25 TODO: PROTECTED DB WRITE ENDPOINT ---


@app.post("/process-sensors")
def process_external_data(
    data: SensorData,
    db: Session = Depends(get_db)  # Injecting our managed DB session here
):
    # Week 1 Core Signal Processing Pipeline
    raw_list = np.array(data.readings)
    invalid_mask = (raw_list <= 0) | (raw_list > 500)
    raw_list[invalid_mask] = 50.0
    mean_val = float(np.mean(raw_list))

    # Serialization format for Relational Columns
    raw_str = json.dumps(data.readings)
    cleaned_str = json.dumps(raw_list.tolist())

    # TODO 3: Create a database row instance using the SensorLogTable model mapped above
    new_log = SensorLogTable(
        # Pass parameters matching your Day 22 table
        raw_readings=raw_str,
        cleaned_readings=cleaned_str,
        average_clearance=mean_val
    )

    try:
        # TODO 4: Add and Commit the record into the active database session block safely
        db.add(new_log)
        db.commit()
        return {"message": "Success", "database_id": new_log.id, "average": mean_val}
    except Exception as e:
        # TODO 5: Perform transactional rollback on database operations exception state
        db.rollback()
        raise HTTPException(
            status_code=500, detail=f"Database transaction failure: {str(e)}")

# --- DAY 25 TODO: DB READ ENDPOINT ---


@app.get("/history")
def get_history(limit: int = 5, db: Session = Depends(get_db)):
    # TODO 6: Query the database to retrieve logs sorted descending by key id matching input limit
    # Hint: You can use your query engine pattern from Day 24 or query directly here using the 'db' variable.
    logs = db.query(SensorLogTable).order_by(
        SensorLogTable.id.desc()).limit(limit).all()

    # Serialize database objects cleanly out to JSON response structures
    output = []
    for log in logs:
        output.append({
            "id": log.id,
            "timestamp": log.timestamp,
            "raw": json.loads(log.raw_readings),
            "cleaned": json.loads(log.cleaned_readings),
            "average": log.average_clearance
        })
    return {"history": output}
