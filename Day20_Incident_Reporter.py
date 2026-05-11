import json
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime

fig, ax = plt.subplots(figsize=(10, 5))
LOG_FILE = "sensor_history.json"
INCIDENT_DIR = "incidents"

# Create a directory for logs if it doesn't exist
if not os.path.exists(INCIDENT_DIR):
    os.makedirs(INCIDENT_DIR)


def animate(i):
    if not os.path.exists(LOG_FILE):
        return

    with open(LOG_FILE, "r") as f:
        try:
            logs = json.load(f)
        except:
            return

    averages = [entry['avg'] for entry in logs]
    if len(averages) < 2:
        return

    ax.clear()
    latest_avg = averages[-1]
    recent_jitter = np.std(averages[-10:])

    # --- TODO: INCIDENT REPORTING LOGIC ---

    # 1. TODO: Define a 'Critical Condition'.
    # Example: If latest_avg < 15 OR recent_jitter > 25
    is_critical = latest_avg < 15 or recent_jitter > 25

    # 3. TODO: Plot your lines and baselines (use your logic from Day 18 & 19).
    # ax.plot(averages, ...)
    ax.plot(averages, marker='o', color='blue')

    # 4. TODO: Add a Visual Indicator on the screen if an incident is being recorded.
    # Hint: ax.text(...) or change ax.set_facecolor(...)

    # 2. TODO: If 'is_critical' is True, save the current plot.
    # Hint: Generate a unique filename using datetime.now().strftime("%H%M%S")
    # Hint: plt.savefig(f"{INCIDENT_DIR}/incident_{timestamp}.png")

    if is_critical:
        # Save logic here

        ax.set_facecolor('#ffe6e6')
        ax.text(0.3, 0.9, "Incident Recording",
                transform=ax.transAxes, color='red', fontsize=14)
        timestamp = datetime.now().strftime("%H%M%S")
        plt.savefig(f"{INCIDENT_DIR}/incident_{timestamp}.png")
        print("🚨 CRITICAL EVENT: Incident report saved to disk.")

        # Professional Styling
    ax.set_title(
        f"Mission Control - {'[RECORDING INCIDENT]' if is_critical else 'System Nominal'}")
    ax.grid(True, alpha=0.3)


ani = FuncAnimation(fig, animate, interval=1000, cache_frame_data=False)
plt.show()
