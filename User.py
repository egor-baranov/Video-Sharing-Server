import json
import typing


class User:
    username: str
    phone: str
    password: str
    city: str
    birth_date: str
    email: str

    def __init__(self, name: str = "", phone: str = "", password: str = "", city: str = "", birth_date: str = "",
                 email: str = ""):
        self.username = name
        self.phone = phone
        self.password = password
        self.city = city
        self.birth_date = birth_date
        self.email = email

    def is_not_fake(self) -> int:
        return len(self.username) > 0

    def to_dict(self) -> typing.Dict[str: str]:
        return {
            "username": self.username,
            "phone": self.phone,
            "password": self.password,
            "city": self.city,
            "birthDate": self.birth_date,
            "email": self.email
        }


class UserFactory:
    @staticmethod
    def new_fake_user() -> User:
        return User()

    @staticmethod
    def new_user(name: str, phone: str, password: str, city: str, birth_date: str, email: str) -> User:
        return User(name, phone, password, city, birth_date, email)

    @staticmethod
    def from_dict(data: typing.Dict[str: str]):
        return UserFactory.new_user(
            name=data["username"],
            phone=data["phone"],
            password=data["password"],
            city=data["city"],
            birth_date=data["birth_date"],
            email=data["email"]
        )

    @staticmethod
    def user_to_json(user: User) -> str:
        return json.dumps(user.to_dict())

    @staticmethod
    def json_to_user(json_string: str):
        return UserFactory.from_dict(json.loads(json_string))
