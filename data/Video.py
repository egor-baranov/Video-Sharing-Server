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
                 like_count: int = 0,
                 cloudinary_id: int = 0,
                 comments: typing.List[Comment] = None):
        self.title = title
        self.description = description
        self.tags = tags
        self.size = size
        self.length = length
        self.views = views
        self.likes = like_count
        self.cloudinary_id = cloudinary_id
        self.comments = comments

    def to_dict(self):
        return {"title": self.title,
                "description": self.description,
                "tags": self.tags,
                "size": self.size,
                "length": self.length,
                "views": self.views,
                "likeCount": self.likes,
                "videoId": self.cloudinary_id,
                "comments": self.comments}


class VideoFactory:
    @staticmethod
    def new_fake_video() -> Video:
        return Video()

    @staticmethod
    def new_video(title: str, description: str, tags: str, size: int, length: int, views: int, like_count: int,
                  cloudinary_id: int, comments: typing.List[Comment]):
        return Video(title, description, tags, size, length, views, like_count, cloudinary_id, comments)

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
            cloudinary_id=data["videoId"],
            comments=data["comments"]
        )
