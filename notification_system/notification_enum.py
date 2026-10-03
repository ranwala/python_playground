from enum import Enum

class NotificationTypes(Enum):
    Instant = 1
    Schedule = 2
    CountdownTimer = 3
    Recurring = 4

    @property
    def label(self):
        return self.name.title()


class NotificationStatus(Enum):
    Active = "Active"
    Completed = "Completed"
    Cancelled = "Cancelled"