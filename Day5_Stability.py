import numpy as np


class SmartRobot:
    def __init__(self, name):
        self.name = name
        # 4 scans of 3 sensors (Front, Left, Right)
        self.history = np.array([
            [50, 20, 10],
            [51, 80, 11],
            [49, 15, 10],
            [50, 90, 12]
        ])

    def calculate_confidence(self):
        print(f"Analyzing Sensor Stability for {self.name}...")

        # TODO: Calculate the Standard Deviation for each sensor (column)
        # Hint: Use np.std() with axis=0
        sensor_noise = np.std(self.history, axis=0)

        # TODO: High-Pay Logic - Find the index of the MOST unstable sensor
        # Hint: Use np.argmax() on your sensor_noise array
        unstable_idx = np.argmax(sensor_noise)

        sensor_names = ["Front", "Left", "Right"]

        print(f"Noise Level per Sensor (Std Dev): {sensor_noise}")
        print(f"The most UNRELIABLE sensor is: {sensor_names[unstable_idx]}")

        # TODO: Threshold Logic - If any sensor noise is > 10.0,
        # print "WARNING: High noise detected. Switching to backup sensors."
        if any(sensor_noise > 10):
            print("WARNING: High noise detected. Switching to backup sensors.")


# --- TEST YOUR ARCHITECTURE ---
bot = SmartRobot("Titan-05")
bot.calculate_confidence()
