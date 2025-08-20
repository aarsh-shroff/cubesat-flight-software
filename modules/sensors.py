# modules/sensors.py
import random

def read_temperature():
    return round(20 + random.random() * 5, 2)

def read_light():
    return round(1000 + random.random() * 200, 2)
