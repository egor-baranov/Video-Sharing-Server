from data.Video import *
from components.database.dbworker import DatabaseWorker


class VideoManager:
    @staticmethod
    def add_video(v: Video):
        videos = DatabaseWorker.read_videos()
        videos.append(v)
        DatabaseWorker.write_videos(videos)
