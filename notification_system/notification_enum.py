from enum import Enum

class NotificationTypes(Enum):
    Instant = 1
    Schedule = 2
    CountdownTimer = 3
    Recurring = 4

    @property
    def label(self):
        return self.name


class NotificationStatus(Enum):
    Active = "Active"
    Completed = "Completed"
    Cancelled = "Cancelled"


    @property
    def label(self):
        return self.name


class JsonModel(Enum):
    NotificationModel = 1
    TemplateModel = 2

    @property
    def label(self):
        return self.name