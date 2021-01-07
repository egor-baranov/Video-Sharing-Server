import random
import typing

from dto.Comment import Comment


class Video:
    title: str
    description: str
    tags: str
    size: int
    length: int
    views: int
    likes: int
    video_id: int

    # todo: should be refactored to List[Comment]
    comments: typing.List[str] = []

    def __init__(self,
                 title: str = "",
                 description: str = "",
                 tags: str = "",
                 size: int = 0,
                 length: int = 0,
                 views: int = 0,
                 like_count: int = 0,
                 video_id: int = 0,
                 comments: typing.List[str] = None):
        self.title = title
        self.description = description
        self.tags = tags
        self.size = size
        self.length = length
        self.views = views
        self.likes = like_count
        self.video_id = video_id
        self.comments = comments if comments else []

    def to_dict(self):
        return {"title": self.title,
                "description": self.description,
                "tags": self.tags,
                "size": self.size,
                "length": self.length,
                "views": self.views,
                "likeCount": self.likes,
                "videoId": self.video_id,
                "comments": self.comments}


class VideoFactory:
    @staticmethod
    def new_fake_video() -> Video:
        return Video()

    @staticmethod
    def new_video(title: str, description: str, tags: str, size: int, length: int, views: int, like_count: int,
                  video_id: int, comments: typing.List[str]):
        return Video(title, description, tags, size, length, views, like_count, video_id, comments)

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
            comments=data["comments"]
        )
