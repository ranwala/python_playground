class TemplateModel:

    def __init__(self, name, type, title, message, time = None, interval_minutes = None, use_count = None):
        self.name = name
        self.type = type
        self.time = time
        self.interval_minutes = interval_minutes
        self.title = title
        self.message = message
        self.use_count = use_count