import typing


class Comment:
    pass


class Video:
    title: str
    description: str
    tags: str
    size: int
    length: int
    views: int
    likes: int

    comments: typing.List[Comment] = []

    def __init__(self, title: str = "", description: str = "", tags: str = "", size: int = 0, length: int = 0,
                views: int = 0, likes: int = 0):
        self.title = title
        self.description = description
        self.tags = tags
        self.size = size
        self.length = length
        self.views = views
        self.likes = likes

    def to_dict(self):
        return {"title": self.title,
                "description": self.description,
                "tags": self.tags,
                "size": self.size,
                "length": self.length}


class VideoFactory:
    @staticmethod
    def new_fake_video() -> Video:
        return Video()

    @staticmethod
    def new_video(title: str, description: str, tags: str, size: int, length: int, views: int, likes: int):
        return Video(title, description, tags, size, length, views, likes)

