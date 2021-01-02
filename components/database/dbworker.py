from data.User import UserFactory
from data.Video import Video


class DatabaseWorker:

    Users = [UserFactory.new_user(
        username="admin",
        password="password",
        email="admin@admin.com",
        birth_date="31.12.2000",
        city="city",
        phone="89004445533"
    )]

    BlockedUsers = []

    Videos = [
        Video(title="Видео для отладки 1", length=2374),
        Video(title="Видео для отладки 2", length=24),
        Video(title="Видео для отладки 3", length=123)
    ]

    Comments = []
