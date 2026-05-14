import json
from sqlalchemy.orm import sessionmaker
from Day22_Database_Setup import engine, SensorLogTable, SessionLocal

# --- DAY 23 TODO: DATA INGESTION ENGINE ---


def insert_sensor_log(raw_list: list, cleaned_list: list, avg_val: float):
    """
    Inserts a processed sensor log entry securely into the SQLite database.
    Handles data serialization and transaction management.
    """
    # Initialize your local database session
    db_session = SessionLocal()

    try:
        # 1. TODO: Convert raw_list and cleaned_list to strings.
        # Hint: Relational databases cannot store pure Python lists.
        # Convert them using json.dumps(list) so they save as clean strings.
        raw_str = json.dumps(raw_list)
        cleaned_str = json.dumps(cleaned_list)

        # 2. TODO: Create an instance of your SensorLogTable class.
        # Map the function inputs to the columns you defined on Day 22.
        new_record = SensorLogTable(
            raw_readings=raw_str,
            cleaned_readings=cleaned_str,
            average_clearance=avg_val

        )

        # 3. TODO: Add the new record instance to your database session.
        # Hint: db_session.add(record)
        db_session.add(new_record)

        # 4. TODO: Commit the transaction permanently to the database file.
        # Hint: db_session.commit()
        db_session.commit()

        print("✅ Success: Telemetry successfully committed to the database.")

    except Exception as error:
        # 5. TODO: Crucial Production Skill - Rollback on Error
        # If the database fails to write, you must undo the session changes.
        # Hint: db_session.rollback()
        db_session.rollback()
        print(f"❌ Error encountered: {error}. Rolling back transaction.")

    finally:
        # 6. TODO: Close the session to free up system memory and file locks.
        # Hint: db_session.close()
        db_session.close()


if __name__ == "__main__":
    # Test Data Simulation
    sample_raw = [50, 52, -1, 48, 999, 51, 49, 50]
    sample_cleaned = [50, 52, 50, 48, 50, 51, 49, 50]
    sample_avg = 50.12

    insert_sensor_log(sample_raw, sample_cleaned, sample_avg)
