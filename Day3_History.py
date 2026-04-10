import numpy as np

class SmartRobot:
    def __init__(self, name):
        self.name = name
        self.history = None

    def record_history(self):
        # Scenario: 3 scans taken 1 second apart. Each scan has 5 sensors.
        # This is a 3x5 Matrix (3 rows, 5 columns)
        data = [
            [50, 45, 60, 55, 70], # Scan at 0s
            [40, 42, 58, 52, 68], # Scan at 1s
            [30, 40, 55, 50, 65]  # Scan at 2s
        ]
        # TODO: Convert the 'data' list into a NumPy array called self.history
        self.history=np.array(data)

    def analyze_trends(self):
        print(f"Analyzing {self.name} history...")
        
        # TODO: Calculate the MINIMUM distance recorded in the ENTIRE matrix
        # Hint: np.min()
        absolute_min = np.min(self.history)

        # TODO: Calculate the AVERAGE distance for each sensor OVER TIME
        # Hint: Use np.mean() with axis=0 (this averages down the columns)
        sensor_averages = np.mean(self.history,axis=0)

        # TODO: High-Pay Logic: Calculate the 'Delta' (Difference) between 
        # the last scan (row 2) and the first scan (row 0).
        # Hint: last_row - first_row
        movement_delta = self.history[2]-self.history[0]

        print(f"History Matrix:\n{self.history}")
        print(f"Closest any obstacle ever got: {absolute_min} cm")
        print(f"Average sensor readings over 3 seconds: {sensor_averages}")
        print(f"Movement Delta (Negative means getting closer): {movement_delta}")

        # TODO: Logic check - If ANY value in 'movement_delta' is negative, 
        # print "Warning: Obstacles are approaching!"
        if np.any(movement_delta < 0):
            print("Warning: Obstacles are approaching!")

# --- TEST YOUR ARCHITECTURE ---
bot = SmartRobot("Titan-03")
bot.record_history()
bot.analyze_trends()
