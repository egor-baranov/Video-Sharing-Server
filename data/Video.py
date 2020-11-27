class Video:
    title = ""
    description = ""
    tags = ""
    size = 0
    length = 0
    views = 0
    likes = 0

    comments = []

    def to_dict(self):
        return {"title": self.title,
                "description": self.description,
                "tags": self.tags,
                "size": self.size,
                "length": self.length}


class Comment:
    pass
