class SmartRobot:
    def __init__(self, name, battery_level):
        self.name = name
        self.battery = battery_level
        self.position = 0  # Starts at position 0
        print(f"Robot {self.name} is online with {self.battery}% battery.")

    def move(self, distance):
        # TODO: Logic - If battery is > 5, move the robot and decrease battery by 5.
        # Otherwise, print "Low battery! Charge required."
        if self.battery > 5:
            self.position += distance
            self.battery-=5
        else:
            print("Low battery! Charge required")

    def report_status(self):
        # TODO: Print the current position and battery level.
        print(f"Current position {self.position} and Battery level {self.battery} ")

# --- TEST YOUR CODE ---
my_bot = SmartRobot("Titan-01", 100)
my_bot.move(10)
my_bot.report_status()
