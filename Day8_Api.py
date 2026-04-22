from fastapi import FastAPI

# Create the 'App' - this is your web server
app = FastAPI()

@app.get("/")
def home():
    # TODO: Return a JSON message: {"status": "Robot Online", "message": "Welcome to the Navigation API"}
    return {"Status": "Robot Online", "Message": "Welcome to the Navigation API"}

@app.get("/robot/status")
def get_status():
    # TODO: Return a JSON with the robot's name and its current battery (simulated)
    # Example: {"name": "Titan-01", "battery": 95}
    return {"Name": "Titan-01", "Battery": 95}

# --- HOW TO RUN ---
# In terminal: uvicorn main:app --reload
# Then open your browser to http://127.0.0.1:8000
