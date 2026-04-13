import numpy as np

class SmartRobot:
    def __init__(self, name):
        self.name = name
        # Jittery sensor data for 10 seconds (1 sensor)
        self.raw_data = np.array([50, 52, 48, 90, 51, 49, 10, 50, 52, 48])

    def smooth_signals(self, window_size=3):
        print(f"Smoothing signals for {self.name}...")
        
        # High-Pay Skill: Moving Average
        # TODO: Create a loop that calculates the average of every 'window_size' chunk
        # Example: Average of [50, 52, 48], then [52, 48, 90], etc.
        smoothed = []
        
        for i in range(len(self.raw_data) - window_size + 1):
            # TODO: Slice the array from index 'i' to 'i + window_size'
            window =self.raw_data[i:i+window_size]
            
            # TODO: Calculate the mean of that window and append to 'smoothed'
            # Hint: np.mean(window)
            smoothed.append(np.mean(window))
        
        self.smoothed_data = np.array(smoothed)
        
        print(f"Raw Data: {self.raw_data}")
        print(f"Smoothed Data (Window={window_size}): {self.smoothed_data}")

# --- TEST YOUR ARCHITECTURE ---
bot = SmartRobot("Titan-06")
bot.smooth_signals()
