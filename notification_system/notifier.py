import subprocess

def notify(title, message):
    subprocess.run([
        "osascript",
        "-e",
        f'display notification "{message}" with title "{title}"'
    ])

def send_info(title, message):
    notify(title, message)