import time
from typing import List
import random

from dto.User import User
from dto.Video import Video


class Comment:
    video_id: int
    author_email: str
    author_phone: str
    replies: List = []
    likes: int
    text: str
    comment_id: int

    creation_time: float

    def __init__(
        self,
        video_id: int,
        author: User,
        replies: List,
        text: str,
        creation_time: float = 0,
    ):
        self.video_id = video_id
        self.author = author
        self.replies = replies
        self.text = text
        self.likes = 0

        self.comment_id = random.randint(100000, 999999)
        self.creation_time = time.time() if creation_time == 0 else creation_time

    def to_dict(self):
        return {
            "video_id": self.video_id,
            "authorEmail": self.author.to_dict()["email"],
            "authorPhone": self.author.to_dict()["phone"],
            "replies": [r.to_dict() for r in self.replies],
            "text": self.text,
            "likes": self.likes,
            "commentId": self.comment_id,
            "creationTime": self.creation_time,
        }


class CommentFactory:
    @staticmethod
    def new_comment(video: Video, author: User, replies: List[int], text: str):
        return Comment()

    @staticmethod
    def from_dict(data: dict):
        return CommentFactory.new_comment(data)
