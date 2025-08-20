# modules/scheduler.py
import schedule
import time

class Scheduler:
    def __init__(self):
        self.jobs = []
    
    def add_task(self, interval_seconds, function):
        job = schedule.every(interval_seconds).seconds.do(function)
        self.jobs.append(job)
    
    def run(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
