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
    if len(averages) < 2:  # Need at least 2 points to calculate stability
        return

    ax.clear()

    # --- TODO: STABILITY MONITORING LOGIC ---

    # 1. TODO: Calculate the Standard Deviation of the last 10 scans.
    # This tells us how 'jittery' the robot has been recently.
    # Hint: recent_stability = np.std(averages[-10:])
    recent_jitter = np.std(averages[-10:])

    # 2. TODO: Plot the primary data line (use your Day 18 logic).
    # ax.plot(averages, ...)
    ax.plot(averages, marker='o', color='blue', label='Distance')

    # 3. TODO: Create a Dynamic Label for the Title.
    # If jitter > 15, Status = "UNSTABLE". If < 15, Status = "STABLE".
    status_text = "Checking..."
    if recent_jitter > 15:
        status_text = "UNSTABLE"
    else:
        status_text = "STABLE"

    # 4. TODO: Add a colored 'Stability Bar' or 'Text Box' in the corner.
    # Hint: ax.text(0.02, 0.95, f"Jitter: {recent_jitter:.2f}", transform=ax.transAxes,
    #         bbox=dict(facecolor='orange' if recent_jitter > 15 else 'green', alpha=0.5))

    ax.text(0.02, 0.95, f"Jitter: {recent_jitter:.2f}", transform=ax.transAxes, bbox=dict(
        facecolor='orange' if recent_jitter > 15 else 'green', alpha=0.5))

    # Professional Styling
    ax.set_title(f"Robot Telemetry - System Status: {status_text}")
    ax.set_xlabel("Scan Count")
    ax.set_ylabel("Distance (cm)")
    ax.grid(True, alpha=0.3)


ani = FuncAnimation(fig, animate, interval=1000, cache_frame_data=False)
plt.show()
