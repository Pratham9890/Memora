from datetime import datetime
from win11toast import toast


class Alarm:
    def __init__(self, time_str):
        self.time_str = time_str.strip()
        self.triggered = False

    def should_trigger(self, current_time_str):
        return current_time_str == self.time_str and not self.triggered

    def trigger(self):
        toast("⏰ Alarm!", f"It's {self.time_str}")
        print(f"Alarm triggered at {self.time_str}")
        self.triggered = True

    def reset(self):
        self.triggered = False

    def __repr__(self):
        return f"Alarm({self.time_str}, triggered={self.triggered})"
