import subprocess


def notify(title, message):
    print("Start Notification")
    subprocess.run([
        "osascript",
        "-e",
        f'display notification "{message}" with title "{title}"'
    ])
    print("End Notification")

def send_info(title, message):
    notify(title, message)

def send_success(title, message):
    notify(title, message)

def send_urgent(title, message):
    notify(title, message)

def send_error(title, message):
    notify(title, message)
