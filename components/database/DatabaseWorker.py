import json
import typing
import os

import components.config as config
from dto.Notification import Notification, NotificationFactory

from dto.User import UserFactory, User
from dto.Video import Video, VideoFactory
from dto.Comment import CommentFactory, Comment


class DatabaseWorker:
    @staticmethod
    def read_users() -> typing.List[User]:
        with open(config.users_path, "rt", encoding="utf-8") as f:
            return [UserFactory.from_dict(d) for d in json.loads(f.read())]

    @staticmethod
    def write_users(d: typing.List[User]):
        with open(config.users_path, "wt", encoding="utf-8") as f:
            f.write(json.dumps([u.to_dict() for u in d], ensure_ascii=False))

    @staticmethod
    def read_blocked_users() -> typing.List[User]:
        with open(config.blocked_users_path, "rt", encoding="utf-8") as f:
            return [UserFactory.from_dict(d) for d in json.loads(f.read())]

    @staticmethod
    def read_videos() -> typing.List[Video]:
        with open(config.videos_path, "rt", encoding="utf-8") as f:
            return [VideoFactory.from_dict(d) for d in json.loads(f.read())]

    @staticmethod
    def write_videos(d: typing.List[Video]):
        with open(config.videos_path, "wt", encoding="utf-8") as f:
            f.write(json.dumps([v.to_dict() for v in d], ensure_ascii=False))

    @staticmethod
    def read_comments() -> typing.List[Comment]:
        with open(config.comments_path, "rt", encoding="utf-8") as f:
            return [CommentFactory.from_dict(d) for d in json.loads(f.read())]

    @staticmethod
    def write_comments(d: typing.List[Comment]):
        with open(config.comments_path, "wt", encoding="utf-8") as f:
            f.write(json.dumps([c.to_dict() for c in d], ensure_ascii=False))

    @staticmethod
    def read_notifications() -> typing.List[Notification]:
        with open(config.notifications_path, "rt", encoding="utf-8") as f:
            return [NotificationFactory.from_dict(d) for d in json.loads(f.read())]

    @staticmethod
    def write_notifications(d: typing.List[Notification]):
        with open(config.notifications_path, "wt", encoding="utf-8") as f:
            f.write(json.dumps([n.to_dict() for n in d], ensure_ascii=False))

    @staticmethod
    def get_used_disc_space() -> int:
        return sum(
            os.stat(i).st_size
            for i in [
                config.users_path,
                config.blocked_users_path,
                config.comments_path,
                config.videos_path,
            ]
        )
