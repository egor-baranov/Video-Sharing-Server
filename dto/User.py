import json
import typing


class User:
    username: str
    phone: str
    password: str
    city: str
    birth_date: str
    email: str

    uploaded_videos: typing.List[int] = []
    liked_videos: typing.List[int] = []
    liked_comments: typing.List[int] = []

    def __init__(self,
                 username: str = "",
                 phone: str = "",
                 password: str = "",
                 city: str = "",
                 birth_date: str = "",
                 email: str = "",
                 uploaded_videos: typing.List[int] = None,
                 liked_videos: typing.List[int] = None,
                 liked_comments: typing.List[int] = None):
        self.username = username
        self.phone = phone
        self.password = password
        self.city = city
        self.birth_date = birth_date
        self.email = email
        self.uploaded_videos = uploaded_videos if uploaded_videos is not None else []
        self.liked_videos = liked_videos if liked_videos is not None else []
        self.liked_comments = liked_comments if liked_comments is not None else []

    def is_fake(self) -> bool:
        return not self.is_not_fake()

    def is_not_fake(self) -> bool:
        return len(self.username) > 0

    def to_dict(self) -> dict:
        return {
            "username": self.username,
            "phone": self.phone,
            "password": self.password,
            "city": self.city,
            "birthDate": self.birth_date,
            "email": self.email,
            "uploadedVideos": self.uploaded_videos,
            "likedVideos": self.liked_videos,
            "likedComments": self.liked_comments
        }

    def upload_video(self, video_id: int):
        self.uploaded_videos.append(video_id)

    def like_video(self, video_id: int):
        self.liked_videos.append(video_id)

    def like_comment(self, comment_id: int):
        self.liked_comments.append(comment_id)


class UserFactory:
    @staticmethod
    def new_fake_user() -> User:
        return User()

    @staticmethod
    def new_user(username: str, phone: str, password: str, city: str, birth_date: str, email: str,
                 uploaded_videos: typing.List[int], liked_videos: typing.List[int],
                 liked_comments: typing.List[int]) -> User:
        return User(username, phone, password, city, birth_date, email, uploaded_videos, liked_videos, liked_comments)

    @staticmethod
    def from_dict(data: dict):
        return UserFactory.new_user(
            username=data["username"],
            phone=data["phone"],
            password=data["password"],
            city=data["city"],
            birth_date=data["birthDate"],
            email=data["email"],
            uploaded_videos=data["uploadedVideos"],
            liked_videos=data["likedVideos"],
            liked_comments=data["likedComments"]
        )

    @staticmethod
    def user_to_json(user: User) -> str:
        return json.dumps(user.to_dict())

    @staticmethod
    def json_to_user(json_string: str):
        return UserFactory.from_dict(json.loads(json_string))
