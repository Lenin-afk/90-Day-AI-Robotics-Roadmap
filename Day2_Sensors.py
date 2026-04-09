import numpy as np

class SmartRobot:
    def __init__(self, name):
        self.name = name
        # TODO: Initialize an empty variable self.sensors to hold your data later
        self.sensors = None

    def scan_environment(self):
        # Scenario: Sensors report these distances in cm: 5, 20, 8, 50, 3
        # TODO: Create a NumPy array with those 5 values and assign it to self.sensors
        self.sensors = np.array([5,20,8,50,3])

    def process_sensors(self):
        print(f"Scanning with {self.name}...")
        
        # TODO: Create a boolean array 'danger' where distance is less than 10cm
        # Hint: Use a single comparison operator on the whole array
        if self.sensors is None:
            print("No sensor values")
            return
        
        danger = self.sensors <10
        
        # TODO: Calculate the average (mean) distance of all sensors using a NumPy function
        avg_dist = np.mean(self.sensors)
        closest = np.min(self.sensors)
        if closest < 10:
            print("STOP")
        elif closest < 30:
            print("SLOW")
        else:
            print("MOVE")
        
        print(f"Sensor Readings: {self.sensors}")
        print(f"Danger Zones (True/False): {danger}")
        print(f"Average Clearance: {avg_dist} cm")

        # TODO: Use np.any() to check if at least one sensor is in danger
        # If true, print "EMERGENCY STOP"
        if np.any(danger):
            print('EMERGENCY STOP')

# --- TEST YOUR ARCHITECTURE ---
bot = SmartRobot("Titan-02")
bot.scan_environment()
bot.process_sensors()

