import json
from Day22_Database_Setup import SensorLogTable, SessionLocal

# --- DAY 24 TODO: DATABASE RETRIEVAL ENGINE ---

def get_recent_logs(limit: int = 5):
    """
    Queries the database and returns the most recent 'limit' entries.
    Orders them by ID descending (newest first).
    """
    db_session = SessionLocal()
    try:
        # 1. TODO: Query the SensorLogTable. Order it by id descending, and apply the limit.
        # Hint: db_session.query(SensorLogTable).order_by(SensorLogTable.id.desc()).limit(limit).all()
        records = db_session.query(SensorLogTable).order_by(SensorLogTable.id.desc()).limit(limit).all()
        return records
    finally:
        db_session.close()

def get_incidents_only(threshold: float = 20.0):
    """
    Queries the database for historical entries where the average clearance 
    dropped below the critical safety threshold.
    """
    db_session = SessionLocal()
    try:
        # 2. TODO: Use filter() to fetch entries where average_clearance is LESS THAN the threshold.
        # Hint: db_session.query(SensorLogTable).filter(SensorLogTable.average_clearance < threshold).all()
        incidents = db_session.query(SensorLogTable).filter(SensorLogTable.average_clearance < threshold).all()
        return incidents
    finally:
        db_session.close()

if __name__ == "__main__":
    print("--- Testing Database Queries ---")
    
    # Test 1: Fetch recent records
    recent = get_recent_logs(limit=2)
    print(f"\nFetched {len(recent)} recent records:")
    for record in recent:
        # Hint: Use json.loads(record.cleaned_readings) to convert the string back to a Python list
        print(f"ID: {record.id} | Timestamp: {record.timestamp} | Avg: {record.average_clearance} cm")
        
    # Test 2: Fetch critical incidents
    critical_threshold = 25.0
    incidents = get_incidents_only(threshold=critical_threshold)
    print(f"\nFound {len(incidents)} critical incidents below {critical_threshold} cm:")
    for incident in incidents:
        print(f"🚨 Incident ID: {incident.id} | Reported Avg: {incident.average_clearance} cm")
