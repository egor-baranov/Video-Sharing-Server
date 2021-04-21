import time
import typing


class Video:
    title: str

    author_username: str
    author_email: str
    author_phone: str

    description: str
    tags: str
    size: int
    length: int
    views: int
    likes: int
    video_id: int
    upload_time: float

    comments: typing.List[int] = []

    is_promotional: bool
    max_show_count: int

    def __init__(
            self,
            title: str = "",
            author_username: str = "",
            author_email: str = "",
            author_phone: str = "",
            description: str = "",
            tags: str = "",
            size: int = 0,
            length: int = 0,
            views: int = 0,
            like_count: int = 0,
            video_id: int = 0,
            comments: typing.List[int] = None,
            upload_time: float = 0,
            is_promotional: bool = False,
            max_show_count: int = -1
    ):
        self.title = title
        self.author_username: str = author_username
        self.author_email: str = author_email
        self.author_phone: str = author_phone
        self.description = description
        self.tags = tags
        self.size = size
        self.length = length
        self.views = views
        self.likes = like_count
        self.video_id = video_id
        self.comments = comments if comments else []
        self.upload_time = time.time() if upload_time == 0 else upload_time
        self.is_promotional = is_promotional
        self.max_show_count = max_show_count

    def to_dict(self):
        return {
            "title": self.title,
            "authorUsername": self.author_username,
            "authorEmail": self.author_email,
            "authorPhone": self.author_phone,
            "description": self.description,
            "tags": self.tags,
            "size": self.size,
            "length": self.length,
            "views": self.views,
            "likeCount": self.likes,
            "videoId": self.video_id,
            "comments": self.comments,
            "uploadTime": self.upload_time,
            "url": "https://res.cloudinary.com/kepler88d/video/upload/fl_attachment/" + str(self.video_id) + ".mp4",
            "isPromotional": self.is_promotional,
            "maxShowCount": self.max_show_count
        }


class VideoFactory:
    @staticmethod
    def new_fake_video() -> Video:
        return Video()

    @staticmethod
    def new_video(
            title: str,
            author_username: str,
            author_email: str,
            author_phone: str,
            description: str,
            tags: str,
            size: int,
            length: int,
            views: int,
            like_count: int,
            video_id: int,
            comments=None,
            upload_time: float = 0,
            is_promotional: bool = False,
            max_show_count: int = -1
    ):
        return Video(
            title,
            author_username,
            author_email,
            author_phone,
            description,
            tags,
            size,
            length,
            views,
            like_count,
            video_id,
            comments=comments if comments is not None else [],
            upload_time=upload_time,
            is_promotional=is_promotional,
            max_show_count=max_show_count
        )

    @staticmethod
    def from_dict(data: dict):
        return VideoFactory.new_video(
            title=data["title"],
            author_username="" if "authorUsername" not in data.keys() else data["authorUsername"],
            author_email="" if "authorEmail" not in data.keys() else data["authorEmail"],
            author_phone="" if "authorPhone" not in data.keys() else data["authorPhone"],
            description=data["description"],
            tags=data["tags"],
            size=data["size"],
            length=data["length"],
            views=data["views"],
            like_count=data["likeCount"],
            video_id=data["videoId"],
            comments=[] if "comments" not in data.keys() else data["comments"],
            upload_time=0 if "uploadTime" not in data.keys() else data["uploadTime"],
            is_promotional=False if "isPromotional" not in data.keys() else data["isPromotional"],
            max_show_count=-1 if "maxShowCount" not in data.keys() else data["maxShowCount"]
        )
