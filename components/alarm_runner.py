from datetime import datetime
from plyer import notification
import time
import os
import simpleaudio as sa

ALARM_FILE = "alarms.txt"
last_triggered = None


def load_alarms():
    if not os.path.exists(ALARM_FILE):
        return []
    with open(ALARM_FILE, "r") as f:
        return [line.strip() for line in f]


def play_alarm_sound():
    try:
        wave_obj = sa.WaveObject.from_wave_file("components/alarm.wav")
        wave_obj.play()
    except Exception as e:
        print(f"Error playing alarm sound: {e}")


def run_alarm_check():
    global last_triggered
    now_str = datetime.now().strftime("%H:%M")
    alarms = load_alarms()

    if now_str in alarms and now_str != last_triggered:
        last_triggered = now_str
        play_alarm_sound()

        try:
            notification.notify(
                title="⏰ Alarm!",
                message=f"It's {now_str}",
                timeout=5  # seconds
            )
        except Exception as e:
            print(f"Error showing notification: {e}")

        print(f"[{now_str}] Alarm triggered.")
    else:
        print(f"[{now_str}] No alarm.")


def main():
    print("🚀 Alarm runner started...")
    while True:
        run_alarm_check()
        now = datetime.now()
        seconds_to_next_minute = 60 - now.second
        time.sleep(seconds_to_next_minute)


if __name__ == "__main__":
    main()
