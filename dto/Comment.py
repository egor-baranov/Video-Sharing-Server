import time
from typing import List
import random

from dto.User import User
from dto.Video import Video


class Comment:
    video_id: int
    author_email: str
    author_phone: str
    replies: List[int] = []
    text: str
    likes: int
    comment_id: int

    creation_time: float

    def __init__(
        self,
        video_id: int,
        author_email: str,
        author_phone: str,
        text: str,
        replies: List[int] = None,
        likes: int = 0,
        comment_id: int = 0,
        creation_time: float = 0,
    ):
        self.video_id = video_id
        self.author_email = author_email
        self.author_phone = author_phone
        self.text = text
        self.likes = likes

        self.replies = replies if replies is not None else []
        self.comment_id = (
            random.randint(100000, 999999) if comment_id == 0 else comment_id
        )
        self.creation_time = time.time() if creation_time == 0 else creation_time

    def to_dict(self):
        return {
            "video_id": self.video_id,
            "authorEmail": self.author_email,
            "authorPhone": self.author_phone,
            "replies": self.replies,
            "text": self.text,
            "likes": self.likes,
            "commentId": self.comment_id,
            "creationTime": self.creation_time,
        }


class CommentFactory:
    @staticmethod
    def new_comment(
        video_id: int,
        author_email: str,
        author_phone: str,
        text: str,
        replies: List[int] = None,
        likes: int = 0,
        creation_time: float = 0,
        comment_id: int = 0,
    ):
        return Comment(
            video_id,
            author_email,
            author_phone,
            text=text,
            replies=replies,
            likes=likes,
            creation_time=creation_time,
            comment_id=comment_id,
        )

    @staticmethod
    def from_dict(data: dict):
        return CommentFactory.new_comment(
            video_id=data["videoId"],
            author_email=data["authorEmail"],
            author_phone=data["authorPhone"],
            text=data["text"],
            replies=data["replies"],
            likes=data["likes"],
            creation_time=data["creationTime"],
            comment_id=data["commentId"],
        )
