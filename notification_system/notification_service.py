import os
from json_loder import load_json, save_json
from notification_model import NotificationModel
from template_model import TemplateModel
from notification_enum import JsonModel

class NotificationService:
    def load_notifications(self, json_model):
        model_cls = NotificationModel if json_model == JsonModel.NotificationModel else TemplateModel
        if os.path.exists('notifications.json'):
            notifications = load_json(model_cls, 'notifications.json')
            return notifications
        return []

    def save_notifications(self, notifications):
        save_json(notifications, 'notifications.json')
        print("Notifications saved successfully.")

