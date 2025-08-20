# main.py
from modules.scheduler import Scheduler
from modules.telemetry import TelemetryLogger
import modules.sensors as sensors

def read_and_log():
    temp = sensors.read_temperature()
    light = sensors.read_light()
    telemetry.log(temp=temp, light=light)
    print(f"Logged: Temp={temp}C, Light={light}lux")

if __name__ == "__main__":
    telemetry = TelemetryLogger()
    scheduler = Scheduler()
    scheduler.add_task(5, read_and_log) # Every 5 seconds
    scheduler.run()
