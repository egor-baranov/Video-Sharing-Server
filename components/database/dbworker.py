import json
import typing

import components.config as config

from dto.User import UserFactory
from dto.Video import Video, VideoFactory
from dto.Comment import CommentFactory, Comment


class DatabaseWorker:
    # user dto methods
    @staticmethod
    def read_users():
        with open(config.users_path, "rt") as f:
            return [UserFactory.from_dict(d) for d in json.loads(f.read())]

    @staticmethod
    def write_users(d):
        with open(config.users_path, "wt") as f:
            f.write(json.dumps([u.to_dict() for u in d]))

    @staticmethod
    def read_blocked_users():
        with open(config.blocked_users_path, "rt") as f:
            return [UserFactory.from_dict(d) for d in json.loads(f.read())]

    # videos dto methods
    @staticmethod
    def read_videos():
        with open(config.videos_path, "rt") as f:
            return [VideoFactory.from_dict(d) for d in json.loads(f.read())]

    @staticmethod
    def write_videos(d: typing.List[Video]):
        with open(config.videos_path, "wt") as f:
            f.write(json.dumps([v.to_dict() for v in d]))

    # comments dto methods
    @staticmethod
    def read_comments():
        with open(config.comments_path, "rt") as f:
            return [CommentFactory.from_dict(d) for d in json.loads(f.read())]

    @staticmethod
    def write_comments(d: typing.List[Comment]):
        with open(config.comments_path, "wt") as f:
            f.write(json.dumps([c.to_dict() for c in d]))
