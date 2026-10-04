from notifier import notify
from scheduler import schedule_at, countdown_timer, recurring_reminder
from notification_model import NotificationModel
from datetime import datetime
from utils import generate_notification_id
from notification_enum import NotificationTypes, NotificationStatus
from notification_service import NotificationService
from notification_printer import print_notification
from notification_enum import JsonModel

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

def main():
    # Load notifications
    notification_service = NotificationService()
    notifications = notification_service.load_notifications(JsonModel.NotificationModel.name)

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
                notification_service.save_notifications(notifications)

            schedule_at(time_str, title, message)

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
            notification_service.save_notifications(notifications)

            countdown_timer(minutes, title, message)

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

            notification_service.save_notifications(notifications)

            recurring_reminder(minutes, sessions)

    elif option == 2:
        templates = notification_service.load_notifications(JsonModel.TemplateModel.name)
        print("--- Templates ---")

        for template in templates:
            match template.type:
                case NotificationTypes.Schedule.label:
                    schedule_at(template.time, template.title, template.message)
                case NotificationTypes.Recurring.label:
                    recurring_reminder(template.interval_minutes, template.use_count, template.title, template.message)
                case NotificationTypes.CountdownTimer.label:
                    countdown_timer(template.interval_minutes, template.title, template.message)

    elif option == 3:
        print("--- All Notifications ---")
        print_notification(notifications)

    elif option == 4:
        print("--- Active Notifications ---")
        print_notification(notifications)

    else:
        exit()

if __name__ == "__main__":
    main()