import os
import threading
from json_loder import load_json, save_json
from notification_model import NotificationModel
from template_model import TemplateModel
from notification_enum import JsonModel
from notification_enum import NotificationTypes
from scheduler import schedule_at, countdown_timer, recurring_reminder

class NotificationService:
    def load_notifications(self, json_model):
        model_cls = NotificationModel if json_model == JsonModel.NotificationModel.name else TemplateModel
        file_path = 'notifications.json' if json_model == JsonModel.NotificationModel.name else 'template.json'
        if os.path.exists(file_path):
            notifications = load_json(model_cls, file_path)
            return notifications
        return []

    def save_notifications(self, notifications):
        save_json(notifications, 'notifications.json')
        print("Notifications saved successfully.")


    def cancel_notifications(self, notifications):
        for notification in notifications:
            notification.status = 'Cancelled'

        print("Notifications canceled successfully.")
        self.save_notifications(notifications)


    def send_notification(self, notification_type, template):

        handlers = {
            NotificationTypes.Schedule.label: (schedule_at, lambda n: (n.time, n.title, n.message)),
            NotificationTypes.Recurring.label: (recurring_reminder, lambda n:
            (n.interval_minutes, n.use_count, n.title, n.message)),
            NotificationTypes.CountdownTimer.label: (countdown_timer, lambda n:
            (n.interval_minutes, n.title, n.message))
        }

        func, get_args = handlers[notification_type]

        thread = threading.Thread(target=func, args=get_args(template))
        thread.start()