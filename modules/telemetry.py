# modules/telemetry.py
import csv
import os
from datetime import datetime

class TelemetryLogger:
    def __init__(self, log_dir="logs", log_file="sensor_log.csv"):
        os.makedirs(log_dir, exist_ok=True)
        self.path = os.path.join(log_dir, log_file)
        if not os.path.exists(self.path):
            with open(self.path, "w", newline='') as f:
                writer = csv.writer(f)
                writer.writerow(["timestamp", "temp", "light"])
    
    def log(self, temp=None, light=None):
        now = datetime.now().isoformat()
        with open(self.path, "a", newline='') as f:
            writer = csv.writer(f)
            writer.writerow([now, temp, light])
