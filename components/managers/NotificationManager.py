import typing

from components.database.DatabaseWorker import DatabaseWorker
from components.managers.UserManager import UserManager

from dto.Notification import Notification, NotificationFactory


class NotificationManager:
    @staticmethod
    def add_rate_video_notification(
            user_id: int, other_user_id: int, video_title: str, creation_time: float
    ):
        NotificationManager._add_notification(
            user_id=user_id,
            notification_type=Notification.TYPE_RATE_VIDEO,
            text=f"Пользователь {UserManager.get_user_by_id(other_user_id)} "
                 f"оценил ваше видео {video_title[:20]}.",
            creation_time=creation_time
        )

    @staticmethod
    def add_subscribe_notification(user_id: int, other_user_id: int, creation_time: float):
        NotificationManager._add_notification(
            user_id=user_id,
            notification_type=Notification.TYPE_SUBSCRIBE,
            text=f"Пользователь {UserManager.get_user_by_id(other_user_id)} "
                 f"подписался на вас.",
            creation_time=creation_time
        )

    @staticmethod
    def add_broadcast_notification(
            user_id: int, other_user_id: int, broadcast_title: str, creation_time: float
    ):
        NotificationManager._add_notification(
            user_id=user_id,
            notification_type=Notification.TYPE_BROADCAST,
            text=f"Пользователь {UserManager.get_user_by_id(other_user_id)} "
                 f"начал трансляцию {broadcast_title[:20]}.",
            creation_time=creation_time
        )

    @staticmethod
    def add_rate_comment_notification(
            user_id: int, other_user_id: int, comment_text: str, creation_time: float
    ):
        NotificationManager._add_notification(
            user_id=user_id,
            notification_type=Notification.TYPE_RATE_COMMENT,
            text=f"Пользователь {UserManager.get_user_by_id(other_user_id)} "
                 f"оценил ваш комментарий {comment_text[:20]}.",
            creation_time=creation_time
        )

    @staticmethod
    def _add_notification(user_id: int, notification_type: int, text: str, creation_time: float):
        notifications = DatabaseWorker.read_notifications()
        notifications.append(
            NotificationFactory.new_notification(
                text=text,
                user_id=user_id,
                notification_type=notification_type,
                creation_time=creation_time,
            )
        )

    @staticmethod
    def get_notifications_of_user(user_id: int) -> typing.List[Notification]:
        return list(filter(lambda n: n.user_id == user_id, DatabaseWorker.read_notifications()))
