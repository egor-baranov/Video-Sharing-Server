from data.Video import *
from components.database.dbworker import DatabaseWorker


class VideoManager:
    @staticmethod
    def add_video(v: Video):
        videos = DatabaseWorker.read_videos()
        videos.append(v)
        DatabaseWorker.write_videos(videos)

    @staticmethod
    def get_video_by_id(video_id: int):
        for video in DatabaseWorker.read_videos():
            if video.video_id == video_id:
                return video
