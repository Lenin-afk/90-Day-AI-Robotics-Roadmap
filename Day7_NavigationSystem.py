import numpy as np


class NavigationSystem:
    def __init__(self, name):
        self.name = name
        # TODO: Define a raw history with some glitches (e.g., -1 or 999)
        self.raw_history = np.array([50, 52, -1, 48, 999, 51, 49, 50])

    def pipeline(self):
        print(f"--- Starting {self.name} Pipeline ---")

        # 1. CLEANING (Day 4)
        # TODO: Create a mask for values <= 0 or > 500 and replace them with 50
        invalid_mask = (self.raw_history <= 0) | (self.raw_history > 500)
        self.raw_history[invalid_mask] = 50
        print(f"Step 1 (Cleaned): {self.raw_history}")

        # 2. SMOOTHING (Day 6)
        # TODO: Apply a moving average (window=3) to the cleaned data
        smoothed = []
        window_size = 3
        for i in range(len(self.raw_history)-window_size+1):
            window = self.raw_history[i:i+window_size]
            smoothed.append(np.mean(window))
        self.smoothed_data = np.array(smoothed)
        print(f"Step 2 (Smoothed): {self.smoothed_data}")

        # 3. SAFETY CHECK (Day 2 & 5)
        # TODO: Calculate the final average and standard deviation
        # TODO: If Std Dev > 5, print "CAUTION: Unstable Environment"
        final_average = np.mean(self.smoothed_data)
        final_std_deviation = np.std(self.smoothed_data)
        print(f"Final Avg: {final_average:.2f} cm")
        print(f"Final Noise (Std Dev): {final_std_deviation:.2f}")

        if final_std_deviation > 5:
            print("CAUTION: Unstable Environment")
        else:
            print("Environment Stable")

        print("Pipeline Complete.")


# --- TEST YOUR WEEK 1 MILESTONE ---
nav = NavigationSystem("Nav-Arch-01")
nav.pipeline()
