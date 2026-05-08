import json
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots(figsize=(10, 5))
LOG_FILE = "sensor_history.json"


def animate(i):
    if not os.path.exists(LOG_FILE):
        return

    with open(LOG_FILE, "r") as f:
        try:
            logs = json.load(f)
        except:
            return

    averages = [entry['avg'] for entry in logs]
    if not averages:
        return

    # TODO: Get the most recent average from the list
    latest_avg = averages[-1]

    ax.clear()

    # --- TODO: INTELLIGENT UI LOGIC ---

    # 1. TODO: Create a conditional 'line_color' variable.
    # If latest_avg < 20, set to 'red'. Otherwise, set to 'green'.
    line_color = 'blue'
    if latest_avg < 20:
        line_color = 'red'
    else:
        line_color = 'green'

    # 2. TODO: Plot the data using your dynamic color
    # ax.plot(averages, marker='o', color=line_color)
    ax.plot(averages, marker='o', color=line_color)

    # 3. TODO: If latest_avg < 20, add a warning text to the graph.
    # Hint: ax.text(x_pos, y_pos, "WARNING", fontsize=15, color='red')
    # Use len(averages)-1 for x_pos and latest_avg for y_pos.
    if latest_avg < 20:
        ax.text(len(averages)-1, latest_avg,
                "WARNING", fontsize=15, color='red')

    # 4. TODO: Set background color to light red if in danger.
    # Hint: ax.set_facecolor('#ffe6e6')
        ax.set_facecolor('#ffe6e6')

    # Standard Styling
    ax.set_title(
        f"Live Robot Feed - Status: {'DANGER' if latest_avg < 20 else 'SAFE'}")
    ax.set_ylabel("Distance (cm)")
    ax.grid(True, linestyle='--')


ani = FuncAnimation(fig, animate, interval=1000, cache_frame_data=False)
plt.show()
