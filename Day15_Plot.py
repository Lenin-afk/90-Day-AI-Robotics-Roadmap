import json
import matplotlib.pyplot as plt
import os

# --- DAY 15 TODO: THE VISUALIZER ---

def generate_dashboard():
    LOG_FILE = "sensor_history.json"
    
    # 1. TODO: Defensive Check - If file doesn't exist, print "No data" and return
    if not os.path.exists(LOG_FILE):
        print("No history found to visualize.")
        return

    # 2. TODO: Read the JSON file
    with open(LOG_FILE, "r") as f:
        logs = json.load(f)

    # 3. TODO: High-Pay Skill - Data Extraction
    # Extract all 'avg' values into a list called 'averages'
    # Hint: [entry['avg'] for entry in logs]
    averages = [entry['avg'] for entry in logs]

    # 4. TODO: Plotting Logic
    plt.figure(figsize=(10, 5))
    plt.plot(averages, marker='o', linestyle='-', color='b', label='Avg Clearance')
    
    # TODO: Add a Title "Robot Navigation History" and Labels for X (Scan #) and Y (CM)
    plt.title("Robot Navigation History")
    plt.xlabel("Scan Number")
    plt.ylabel("Distance (cm)")
    plt.grid(True)
    plt.legend()

    # 5. Save the plot as an image
    plt.savefig("robot_dashboard.png")
    print("✅ Dashboard updated: robot_dashboard.png created.")
    plt.show()

if __name__ == "__main__":
    generate_dashboard()
