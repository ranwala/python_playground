import threading
import time
from datetime import datetime, timedelta
from notifier import notify


def _run_countdown(scheduled_time, title, message):
    remaining_time = (scheduled_time - datetime.now()).total_seconds()

    if remaining_time > 0:
        timer = threading.Timer(remaining_time, notify, args=(title, message))
        timer.start()


def _parse_time(time_str):
    # Split the time in to hours and minutes
    hours, minutes = map(int, time_str.split(":"))

    now = datetime.now()

    # Combine with specified time
    scheduled_time = now.replace(hour=hours, minute=minutes, second=0)

    if scheduled_time < now:
        scheduled_time += timedelta(days=1)

    return scheduled_time


def schedule_at(time_str: str, title: str, message: str):
    scheduled_time = _parse_time(time_str)
    _run_countdown(scheduled_time, title, message)
    print("The notification will be sent at: ", scheduled_time.strftime("%Y-%m-%d %H:%M:%S"))


def countdown_timer(count_down_time_in_minutes: int, title: str, message: str):
    timer = threading.Timer(count_down_time_in_minutes * 60, notify, args=(title, message))
    timer.start()
    print("The notification will be sent in: ", count_down_time_in_minutes, "minutes")


def recurring_reminder(minutes: int, sessions: int):
    while sessions > 0:
        print("Timer starts now, will notify you in ", minutes, "minutes")
        time.sleep(minutes * 60)
        notify("Drink a water", "Time to take a break!")
        sessions -= 1


def start_pomodoro(sessions: int):
    for i in range(sessions):
        print("Work Time starts now, will notify you in 1 minutes for a break")
        time.sleep(1 * 60)
        notify("Break Time", "Drink Some water")

        if i < sessions - 1:
            time.sleep(1 * 60)
            notify("Resume Work", "Back to work!")


if __name__ == "__main__":
    start_pomodoro(3)