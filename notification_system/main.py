from notifier import notify
from scheduler import schedule_at, countdown_timer, recurring_reminder
from notification_model import NotificationModel
from datetime import datetime
from utils import generate_notification_id
from notification_enum import NotificationTypes
from notification_service import NotificationService
from notification_printer import print_notification
from notification_enum import JsonModel

notification_service = NotificationService()

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

def load_notifications():
    notifications = notification_service.load_notifications(JsonModel.NotificationModel.name)
    return notifications

def main():
    # Load notifications
    notifications = load_notifications()

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
                "Active",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                template_name,
                time_str,
                None,
                )

            if is_save.lower() == "y":
                notifications.append(notification_model)
                notification_service.save_notifications(notifications)

            schedule_at(time_str, title, message)

        elif notification_option == 3:
            minutes = int(input("Enter time (in minutes): "))
            title = input("Enter title: ")
            message = input("Enter message: ")
            is_save = input("Save this notification? (y/n): ")

            notification_model = NotificationModel(
                generate_notification_id(len(notifications)),
                title,
                message,
                NotificationTypes(notification_option).label,
                "Active",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                None,
                minutes,
                None
            )

            if is_save.lower() == 'y':
                notifications.append(notification_model)
                notification_service.save_notifications(notifications)

            countdown_timer(minutes, title, message)

        elif notification_option == 4:
            minutes = int(input("Enter minutes: "))
            sessions = int(input("Enter sessions: "))
            title = input("Enter title: ")
            message = input("Enter message: ")
            is_save = input("Save this notification? (y/n): ")

            notifications.append(NotificationModel(
                generate_notification_id(len(notifications)),
                "Recurring Notification",
                f"This is a recurring notification for {sessions} sessions",
                NotificationTypes(notification_option).label,
                "Active",
                datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                None,
                minutes,
                None
            ))

            if is_save.lower() == 'y':
                notification_service.save_notifications(notifications)

            recurring_reminder(minutes, sessions, title, message)

    elif option == 2:
        templates = notification_service.load_notifications(JsonModel.TemplateModel.name)
        print("--- Templates ---")

        for template in templates:
            notification_service.send_notification(template)

    elif option == 3:
        if len(notifications) > 0:
            print("--- All Notifications ---")
            print_notification(notifications)
        else:
            print("--- No Notifications ---")

    elif option == 4:
        notifications = [notification for notification in notifications if notification.status == "Active"]
        if len(notifications) > 0:
            print("--- Active Notifications ---")
            print_notification(notifications)
        else:
            print("--- No Notifications ---")

    elif option == 5:
        if len(notifications) > 0:
            notification_service.cancel_notifications(notifications)
        else:
            print("--- No Notifications ---")

    else:
        exit()

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")