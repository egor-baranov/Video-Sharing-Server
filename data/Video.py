import random
import typing

from data.Comment import Comment


class Video:
    title: str
    description: str
    tags: str
    size: int
    length: int
    views: int
    likes: int
    video_id: int

    comments: typing.List[Comment] = []

    def __init__(self,
                 title: str = "",
                 description: str = "",
                 tags: str = "",
                 size: int = 0,
                 length: int = 0,
                 views: int = 0,
                 cloudinary_id: int = 0):
        self.title = title
        self.description = description
        self.tags = tags
        self.size = size
        self.length = length
        self.views = views
        self.cloudinary_id = cloudinary_id
        self.likes = 0

    def to_dict(self):
        return {"title": self.title,
                "description": self.description,
                "tags": self.tags,
                "size": self.size,
                "length": self.length,
                "views": self.views,
                "likeCount": self.likes,
                "videoId": self.cloudinary_id}


class VideoFactory:
    @staticmethod
    def new_fake_video() -> Video:
        return Video()

    @staticmethod
    def new_video(title: str, description: str, tags: str, size: int, length: int, views: int, cloudinary_id: int):
        return Video(title, description, tags, size, length, views, cloudinary_id)
