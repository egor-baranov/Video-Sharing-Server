from data.User import UserFactory
from data.Video import Video

import components.config as config
import json
import typing
import data


class DatabaseWorker:
    # Users = [UserFactory.new_user(
    #     username="admin",
    #     password="password",
    #     email="admin@admin.com",
    #     birth_date="31.12.2000",
    #     city="city",
    #     phone="89004445533"
    # )]

    @staticmethod
    def read_users():
        with open(config.users_path, "rt") as f:
            return [UserFactory.from_dict(d) for d in json.loads(f.read())]

    @staticmethod
    def write_users(d: typing.List[data.User]):
        with open(config.users_path, "wt") as f:
            f.write(json.dumps([u.to_dict() for u in d]))

    @staticmethod
    def add_user(u: data.User):
        users = DatabaseWorker.read_users()
        users.append(u)
        DatabaseWorker.write_users(users)

    @staticmethod
    def remove_user(u: data.User):
        users = DatabaseWorker.read_users()
        users.remove(u)
        DatabaseWorker.write_users(u)

    BlockedUsers = []

    Videos = [
        Video(title="Видео для отладки 1", length=2374),
        Video(title="Видео для отладки 2", length=24),
        Video(title="Видео для отладки 3", length=123)
    ]

    Comments = []
