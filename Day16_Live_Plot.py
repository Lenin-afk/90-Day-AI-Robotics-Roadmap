import json
import os
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Initialize the figure and axis
fig, ax = plt.subplots(figsize=(10, 5))
LOG_FILE = "sensor_history.json"

def animate(i):
    """
    This function is called repeatedly by FuncAnimation.
    """
    # 1. TODO: Check if LOG_FILE exists. If not, return.
    if not os.path.exists(LOG_FILE):
        return
    
    
    # 2. TODO: Open and read the JSON file. 
    # Use a try/except block to handle cases where the file is busy.
    try:
        with open(LOG_FILE, 'r') as f:
            data = json.load(f)   
    except:
        return

    # 3. TODO: Extract the 'avg' values from the logs into a list.
    averages = [entry['avg'] for entry in data]

    # 4. TODO: Clear the previous plot using ax.clear()
    ax.clear()

    # 5. TODO: Re-plot the updated data. 
    # Add a title "Live Robot Feed" and labels.
    ax.plot(averages, marker='o', color='r', label='Live Clearance (cm)')
    ax.set_title("Live Robot Feed")
    ax.set_xlabel("Scan Count")
    ax.set_ylabel("Distance")
    ax.legend(loc='upper right')
    ax.grid(True)

# --- THE ANIMATION ENGINE ---
# TODO: Call FuncAnimation. 
# Arguments needed: the 'fig', the 'animate' function, and an 'interval' of 1000ms.
ani = FuncAnimation(fig, animate, interval=1000)

plt.show()
