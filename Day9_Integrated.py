from fastapi import FastAPI
import numpy as np

app = FastAPI()

class NavigationSystem:
    def __init__(self):
        self.raw_history = np.array([50, 52, -1, 48, 999, 51, 49, 50])

    def get_processed_data(self):
        # 1. CLEANING (Day 4)
        invalid_mask = (self.raw_history <= 0) | (self.raw_history > 500)
        self.raw_history[invalid_mask] = 50
        
        # 2. SMOOTHING (Day 6)
        smoothed = []
        window_size = 3
        for i in range(len(self.raw_history) - window_size + 1):
            window = self.raw_history[i : i + window_size]
            smoothed.append(np.mean(window))
            
        return np.array(smoothed)

# --- DAY 9 API INTEGRATION ---

@app.get("/robot/nav-scan")
def get_nav_scan():
    nav = NavigationSystem()
    # TODO: Call the 'get_processed_data' method
    processed_data = nav.get_processed_data()
    
    # TODO: Return a JSON response containing:
    # 1. The original "raw_history" (converted to list)
    # 2. The new "processed_data" (converted to list)
    # 3. The current "average_clearance" (using np.mean)
    return {
        "raw_data": nav.raw_history.tolist(),
        "processed_data":processed_data.tolist(),
        "average_clearance": float(np.mean(processed_data))
    }
