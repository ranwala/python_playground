def print_notification(notifications):
    for notification in notifications:
        notif = f"""
        \t--{notification.n_id.upper()}--
        \tTitle: {notification.title}
        \tMessage: {notification.msg}
        \tType: {notification.notification_type}
        \tTime: {notification.time}
        \tInterval: {notification.interval_minutes} minutes
        \tStatus: {notification.status}
        \tCreated At: {notification.created_at}
        \tTemplate Name: {notification.template_name}
        """

        print(notif)