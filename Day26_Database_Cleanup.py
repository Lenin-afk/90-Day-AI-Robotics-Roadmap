from datetime import datetime, timedelta, timezone
from sqlalchemy import delete
from Day22_Database_Setup import SensorLogTable, SessionLocal

# --- DAY 26 TODO: RETENTION ENGINE ---


def purge_old_records(days_retention: int = 7):
    """
    Permanently deletes all database logs older than the specified number of days.
    This runs efficiently directly inside the database engine.
    """
    db_session = SessionLocal()

    # 1. TODO: Calculate the cutoff timestamp (Current time minus retention days)
    # Hint: cutoff_time = datetime.utcnow() - timedelta(days=days_retention)
    cutoff_time = datetime.now(timezone.utc) - timedelta(days=days_retention)

    try:
        print(f"🧹 Maintenance: Purging records older than {cutoff_time}...")

        # 2. TODO: Construct a bulk deletion query using filter conditions
        # Target rows where the 'timestamp' column is LESS THAN your cutoff_time
        # Hint: query = db_session.query(SensorLogTable).filter(SensorLogTable.timestamp < cutoff_time)
        # To execute the delete operation cleanly, chain the .delete() method onto your query.
        deleted_count = db_session.query(SensorLogTable).filter(
            SensorLogTable.timestamp < cutoff_time).delete()

        # 3. TODO: Commit the transaction permanently to apply the purge to disk
        # Hint: db_session.commit()
        db_session.commit()

        print(
            f"✅ Maintenance Complete: Successfully purged {deleted_count} stale entries.")
        return deleted_count

    except Exception as error:
        # 4. TODO: Roll back the transaction if the bulk delete execution fails
        # Hint: db_session.rollback()
        db_session.rollback()
        print(f"❌ Maintenance Failed: {error}. Rollback executed.")
        return 0

    finally:
        # 5. TODO: Securely close the database connection to release system locks
        # Hint: db_session.close()
        db_session.close()


if __name__ == "__main__":
    print("--- Simulating Database Maintenance Cycle ---")
    # For testing, we can simulate purging records older than 0 days to clean the environment
    purge_old_records(days_retention=0)
