import dto
import json
import typing
import components.config as config
from components.managers.VideoManager import VideoManager
from dto.User import UserFactory, User
from components.database.DatabaseWorker import DatabaseWorker


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
    def get_user_by_id(user_id: int):
        for user in DatabaseWorker.read_users():
            if user.user_id == user_id:
                return user
        return User()

    @staticmethod
    def add_user(u: User):
        users = DatabaseWorker.read_users()
        users.append(u)
        DatabaseWorker.write_users(users)

    @staticmethod
    def remove_user(u: User):
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
    def restore_user(u: User):
        pass

    @staticmethod
    def update_user_data(u: User):
        users = DatabaseWorker.read_users()

        for i in range(len(users)):
            if users[i].user_id == u.user_id:
                users[i] = u
                break

        DatabaseWorker.write_users(users)

    @staticmethod
    def get_video_owner(video_id: int) -> User:
        for u in DatabaseWorker.read_users():
            if video_id in u.uploaded_videos:
                return u
        return UserFactory.new_fake_user()

    @staticmethod
    def get_favourite_tags(user_id: int) -> typing.Dict:
        result_dict = {}
        user = UserManager.get_user_by_id(user_id)
        for video_id in user.liked_videos:
            video = VideoManager.get_video_by_id(video_id)
            for tag in video.tags.split(", "):
                result_dict[tag] += 1
        return result_dict
