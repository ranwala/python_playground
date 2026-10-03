from notifier import notify
from scheduler import schedule_at, countdown_timer, recurring_reminder
from notification_model import NotificationModel
from datetime import datetime
from json_loder import save_json, load_json
from utils import generate_notification_id
from notification_enum import NotificationTypes

icons = {
    1: "️ℹ️",
    2: "✅",
    3: "⚠️",
    4: "❌",
}

print("##################################################################")
print("Smart Notification Manager")
print("##################################################################")

main_menu = """Main Notification Menu:
\t 1. Create new notification
\t 2. Create from template
\t 3. List all notifications
\t 4. View active notifications
\t 5. Cancel all notifications
\t 6. Manage templates
\t 7. Exit
"""

notification_type = """---Create New Notifications---
\t Notification Types:
\t 1. Instant
\t 2. Schedule (Specific Time)
\t 3. Countdown Timer
\t 4. Recurring
"""

notifications = []
notifications = load_json(NotificationModel, 'notifications.json')

print(main_menu)

option = int(input("Choose and option (1-7): "))

if option == 1:
    print(notification_type)
    notification_option = int(input("Choose type (1-4): "))

    if notification_option == 1:
        title = input("Enter title: ")
        message = input("Enter message: ")

        notify(title, message)

    elif notification_option == 2:
        title = input("Enter title: ")
        message = input("Enter message: ")
        time_str = input("Enter time (HH:MM): ")
        is_save = input("Save this notification? (y/n): ")
        template_name = input("Enter template name (Weekly Meeting): ")

        notification_model = NotificationModel(
            generate_notification_id(len(notifications)),
            title,
            message,
            NotificationTypes(notification_option).label,
            time_str,
            None,
            "Active",
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            template_name)

        if is_save.lower() == "y":
            notifications.append(notification_model)
            save_json(notifications, 'notifications.json')

        #schedule_at(time_str, title, message)

    elif notification_option == 3:
        minutes = int(input("Enter time (in minutes): "))
        title = input("Enter title: ")
        message = input("Enter message: ")

        notification_model = NotificationModel(
            generate_notification_id(len(notifications)),
            title,
            message,
            NotificationTypes(notification_option).label,
            None,
            minutes,
            "Active",
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            None
        )

        notifications.append(notification_model)
        save_json(notifications, 'notifications.json')

        #countdown_timer(minutes, title, message)

    elif notification_option == 4:
        minutes = int(input("Enter minutes: "))
        sessions = int(input("Enter sessions: "))

        notifications.append(NotificationModel(
            generate_notification_id(len(notifications)),
            "Recurring Notification",
            f"This is a recurring notification for {sessions} sessions",
            NotificationTypes(notification_option).label,
            None,
            minutes,
            "Active",
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            None
        ))

        save_json(notifications, 'notifications.json')

        #recurring_reminder(minutes, sessions)

else:
    exit()