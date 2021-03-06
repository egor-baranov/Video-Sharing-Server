import random
import typing
import time


class Video:
    title: str
    description: str
    tags: str
    size: int
    length: int
    views: int
    likes: int
    video_id: int
    upload_time: float

    comments: typing.List[int] = []

    def __init__(
        self,
        title: str = "",
        description: str = "",
        tags: str = "",
        size: int = 0,
        length: int = 0,
        views: int = 0,
        like_count: int = 0,
        video_id: int = 0,
        comments: typing.List[int] = None,
        upload_time: float = 0,
    ):
        self.title = title
        self.description = description
        self.tags = tags
        self.size = size
        self.length = length
        self.views = views
        self.likes = like_count
        self.video_id = video_id
        self.comments = comments if comments else []
        self.upload_time = time.time() if upload_time == 0 else upload_time

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "tags": self.tags,
            "size": self.size,
            "length": self.length,
            "views": self.views,
            "likeCount": self.likes,
            "videoId": self.video_id,
            "comments": self.comments,
            "uploadTime": self.upload_time,
        }


class VideoFactory:
    @staticmethod
    def new_fake_video() -> Video:
        return Video()

    @staticmethod
    def new_video(
        title: str,
        description: str,
        tags: str,
        size: int,
        length: int,
        views: int,
        like_count: int,
        video_id: int,
        comments=None,
        upload_time: float = 0,
    ):
        return Video(
            title,
            description,
            tags,
            size,
            length,
            views,
            like_count,
            video_id,
            comments=comments if comments is not None else [],
            upload_time=upload_time,
        )

    @staticmethod
    def from_dict(data: dict):
        return VideoFactory.new_video(
            title=data["title"],
            description=data["description"],
            tags=data["tags"],
            size=data["size"],
            length=data["length"],
            views=data["views"],
            like_count=data["likeCount"],
            video_id=data["videoId"],
            comments=[] if "comments" not in data.keys() else data["comments"],
            upload_time=0 if "uploadTime" not in data.keys() else data["uploadTime"],
        )
