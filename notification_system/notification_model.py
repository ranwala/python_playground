class NotificationModel:
    def __init__(self, n_id, title, msg, notification_type, status, created_at, template_name, time, interval_minutes,):
        self.n_id = n_id
        self.title = title
        self.msg = msg
        self.notification_type = notification_type
        self.time = time
        self.interval_minutes = interval_minutes
        self.status = status
        self.created_at = created_at
        self.template_name = template_name