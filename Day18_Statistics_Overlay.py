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

    ax.clear()

    # --- TODO: STATISTICAL OVERLAY LOGIC ---

    # 1. TODO: Calculate the overall mean of the 'averages' list using NumPy.
    # Hint: overall_mean = np.mean(averages)
    overall_mean = np.mean(averages)

    # 2. TODO: Plot the primary live data line (use your logic from Day 17).
    # ax.plot(averages, ...)
    ax.plot(averages, marker='o', color='blue', label='Live Distance')

    # 3. TODO: Draw a horizontal dashed line representing the overall mean.
    # Hint: ax.axhline(y=overall_mean, color='gray', linestyle='--', label='Historical Mean')
    ax.axhline(y=overall_mean, color='grey',
               linestyle='--', label='Historical Mean')

    # 4. TODO: Add a "Fill" between the live line and the mean line.
    # This visually highlights the 'deviation'.
    # Hint: ax.fill_between(range(len(averages)), averages, overall_mean, alpha=0.2, color='blue')
    ax.fill_between(range(len(averages)), averages,
                    overall_mean, alpha=0.2, color='blue')

    # Professional Styling
    ax.set_title("Robot Performance vs. Historical Baseline")
    ax.set_xlabel("Scan Count")
    ax.set_ylabel("Distance (cm)")
    ax.legend(loc='upper right')
    ax.grid(True, alpha=0.3)


ani = FuncAnimation(fig, animate, interval=1000, cache_frame_data=False)
plt.show()
