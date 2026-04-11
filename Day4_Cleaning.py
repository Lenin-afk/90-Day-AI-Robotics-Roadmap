import numpy as np


class SmartRobot:
    def __init__(self, name):
        self.name = name
        self.history = np.array([
            [50, 45, 999, 55, 70],  # 999 is a glitch (Too far)
            [40, -1, 58, 52, 68],   # -1 is a glitch (Impossible)
            [30, 40, 55, 50, 65]
        ])

    def clean_data(self):
        print(f"Cleaning data for {self.name}...")

        # TODO: Create a "Mask" for invalid data.
        # Invalid data is anything <= 0 OR anything > 500.
        # Hint: Use (self.history <= 0) | (self.history > 500)
        invalid_mask = (self.history <= 0) | (self.history > 500)

        # TODO: High-Pay Skill - Boolean Indexing
        # Replace all invalid values in self.history with the number 50 (a safe default)
        # Hint: self.history[invalid_mask] = 50
        self.history[invalid_mask] = 50

        # TODO: Advanced Task - Find the "Last Row" dynamically.
        # Use the index [-1] to grab the most recent scan regardless of matrix size.
        last_scan = self.history[-1]

        print(f"Cleaned History Matrix:\n{self.history}")
        print(f"Most recent safe scan: {last_scan}")


# --- TEST YOUR ARCHITECTURE ---
bot = SmartRobot("Titan-04")
bot.clean_data()
