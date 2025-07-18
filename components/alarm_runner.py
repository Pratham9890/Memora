from datetime import datetime
from win11toast import toast
import time
import os
import simpleaudio as sa

ALARM_FILE = "alarms.txt"

def load_alarms():
    if not os.path.exists(ALARM_FILE):
        return []
    with open(ALARM_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]

def play_alarm_sound():
    wave_obj = sa.WaveObject.from_wave_file("components/alarm.wav")
    wave_obj.play()

def run_alarm_check():
    now_str = datetime.now().strftime("%H:%M")
    alarms = load_alarms()
    
    if now_str in alarms:
        play_alarm_sound()
        toast("⏰ Alarm!", f"It's {now_str}")
        print(f"[{now_str}] Alarm triggered.")
        
    else:
        print(f"[{now_str}] No alarm.")

def main():
    print("🚀 Alarm runner started...")

    while True:
        run_alarm_check()

        # Sleep until the start of the next minute
        now = datetime.now()
        seconds_to_next_minute = 60 - now.second
        time.sleep(seconds_to_next_minute)

if __name__ == "__main__":
    main()
