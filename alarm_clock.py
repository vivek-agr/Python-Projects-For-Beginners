from playsound import playsound
import datetime
import time

def set_alarm(alarm_time):
    print(f"Alarm set for {alarm_time}")
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)

        if current_time == alarm_time:
            print("Wake Up!")
            playsound("alarm.mp3")

            is_running = False

        time.sleep(1)

if __name__ == "__main__":
    alarm_time = input("Enter the alarm time: ")
    set_alarm(alarm_time)
