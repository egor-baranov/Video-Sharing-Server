import typing
import random
from data.User import User


class Comment:
    video_id: int
    author: User
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
            "author": self.author.to_dict(),
            "replies": [r.to_dict() for r in self.replies],
            "likes": self.likes,
            "text": self.text
        }
