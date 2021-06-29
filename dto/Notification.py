import typing


class Notification:
    TYPE_RATE_VIDEO = 0
    TYPE_SUBSCRIBE = 1
    TYPE_BROADCAST = 2
    TYPE_RATE_COMMENT = 3

    text: str
    user_id: int
    notification_type: int
    creation_time: float

    def __init__(self, text: str, user_id: int, notification_type: int, creation_time: float):
        self.text = text
        self.user_id = user_id
        self.notification_type = notification_type
        self.creation_time = creation_time

    def to_dict(self):
        return {
            "text": self.text,
            "userId": self.user_id,
            "notificationType": self.notification_type,
            "creationTime": self.creation_time,
        }


class NotificationFactory:
    @staticmethod
    def new_notification(
            text: str, user_id: int, notification_type: int, creation_time: float
    ) -> Notification:
        return Notification(text, user_id, notification_type, creation_time)

    @staticmethod
    def from_dict(data: dict) -> Notification:
        return NotificationFactory.new_notification(
            text=data["text"],
            user_id=data["userId"],
            notification_type=data["notificationType"],
            creation_time=data["creationTime"],
        )
