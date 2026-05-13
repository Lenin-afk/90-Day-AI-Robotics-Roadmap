import os
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

# Define the database location (creates a file named robot_telemetry.db)
DATABASE_URL = "sqlite:///robot_telemetry.db"

# The Engine manages the raw connections to the database file
# echo=True prints raw SQL queries to your terminal
engine = create_engine(DATABASE_URL, echo=True)

# SessionLocal is what we use to actually read/write data in our code
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# This Base class maps our Python classes directly to SQL tables
Base = declarative_base()

# --- DAY 22 TODO: DEFINE THE LOG TABLE SCHEMA ---


class SensorLogTable(Base):
    # TODO 1: Set the SQL table name to 'sensor_logs'
    __tablename__ = "sensor_logs"

    # TODO 2: Define an auto-incrementing Primary Key column named 'id' (Integer)
    id = Column(Integer, primary_key=True, index=True)

    # TODO 3: Define a column for the timestamp (DateTime, defaults to datetime.utcnow)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # TODO 4: Define a column to store the raw array as a string (String)
    # Hint: Since SQL tables can't store Python lists easily, we save them as strings like "50,52,-1"
    raw_readings = Column(String)

    # TODO 5: Define a column to store the cleaned array as a string (String)
    cleaned_readings = Column(String)

    # TODO 6: Define a column to store the final calculated average (Float)
    average_clearance = Column(Float)


def init_db():
    print("Initializing Database...")
    # TODO 7: Use the Base class metadata to create all tables in the engine
    # Hint: Base.metadata.create_all(bind=engine)
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    init_db()
