import data
import json
import components.config as config
from data.User import UserFactory
from components.database.dbworker import DatabaseWorker


class UserManager:
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

    @staticmethod
    def block_user(u: data.User):
        users = DatabaseWorker.read_users()
        users.remove(u)

        with open(config.blocked_users_path, "rt") as f:
            blocked_users = [UserFactory.from_dict(d) for d in json.loads(f.read())]

        blocked_users.append(u)

        with open(config.users_path, "wt") as f:
            f.write(json.dumps([u.to_dict() for u in blocked_users]))


