import dto
import json
import components.config as config
from dto.User import UserFactory, User
from components.database.dbworker import DatabaseWorker


class UserManager:
    @staticmethod
    def get_user_by_email(email: str):
        for user in DatabaseWorker.read_users():
            if user.email == email:
                return user
        return User()

    @staticmethod
    def get_user_by_phone(phone: str):
        for user in DatabaseWorker.read_users():
            if user.phone == phone:
                return user
        return User()

    @staticmethod
    def add_user(u: dto.User):
        users = DatabaseWorker.read_users()
        users.append(u)
        DatabaseWorker.write_users(users)

    @staticmethod
    def remove_user(u: dto.User):
        users = DatabaseWorker.read_users()

        new_users = []

        for i in users:
            if i.phone != u.phone and i.email != u.email:
                new_users.append(i)

        print([i.to_dict() for i in new_users])

        DatabaseWorker.write_users(new_users)

    @staticmethod
    def block_user(u: dto.User):
        with open(config.blocked_users_path, "rt") as f:
            blocked_users = [UserFactory.from_dict(d) for d in json.loads(f.read())]

        blocked_users.append(u)
        UserManager.remove_user(u)

        with open(config.blocked_users_path, "wt") as f:
            f.write(json.dumps([u.to_dict() for u in blocked_users]))

    @staticmethod
    def restore_user(u: dto.User):
        pass

    @staticmethod
    def update_user_data(u: dto.User):
        users = DatabaseWorker.read_users()

        for i in range(len(users)):
            if users[i].phone == u.phone or users[i].email == u.email:
                users[i] = u
                break

        DatabaseWorker.write_users(users)
