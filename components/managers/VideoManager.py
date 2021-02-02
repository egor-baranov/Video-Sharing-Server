from dto.Comment import CommentFactory
from dto.User import User
from dto.Video import *
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

    @staticmethod
    def update_video_data(v: Video):
        videos = DatabaseWorker.read_videos()

        for i in range(len(videos)):
            if videos[i].video_id == v.video_id:
                videos[i] = v
                break

        DatabaseWorker.write_videos(videos)

    @staticmethod
    def add_comment_to_video(video_id: int, author: User, comment_text: str):
        video = VideoManager.get_video_by_id(video_id)

        comment = CommentFactory.new_comment(video_id=video_id, text=comment_text, author_phone=author.phone,
                                             author_email=author.email)

        video.comments.append(comment.comment_id)
        VideoManager.update_video_data(video)
