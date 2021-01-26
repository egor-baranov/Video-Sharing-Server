import typing
import random
from dto.User import User


class Comment:
    video_id: int
    author_email: str
    author_phone: str
    replies: typing.List = []
    likes: int
    text: str
    comment_id: int

    def __init__(self, video_id: int, author: User, replies: typing.List, text: str):
        self.video_id = video_id
        self.author = author
        self.replies = replies
        self.text = text
        self.likes = 0
        self.comment_id = random.randint(100000, 999999)

    def to_dict(self):
        return {
            "video_id": self.video_id,
            "authorEmail": self.author.to_dict()["email"],
            "authorPhone": self.author.to_dict()["phone"],
            "replies": [r.to_dict() for r in self.replies],
            "text": self.text,
            "likes": self.likes,
            "commentId": self.comment_id
        }


class CommentFactory:
    @staticmethod
    def new_comment(video_id: int, author: User, replies, text: str):
        return Comment()

    @staticmethod
    def from_dict(data: dict):
        return CommentFactory.new_comment(data)
