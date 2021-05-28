from components.managers.CommentManager import CommentManager
from dto.Comment import CommentFactory
from dto.User import User
from dto.Video import *
from components.database.DatabaseWorker import DatabaseWorker


class VideoManager:
    @staticmethod
    def add_video(v: Video):
        videos = DatabaseWorker.read_videos()
        videos.append(v)
        DatabaseWorker.write_videos(videos)

    @staticmethod
    def promotional_video_list():
        promotional_videos = []

        for v in DatabaseWorker.read_videos():
            if v.is_promotional and (
                    v.max_show_count == -1 or v.max_show_count > v.views) and v.display_option != "none":
                promotional_videos.append(v)

        return promotional_videos

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
                                             author_email=author.email, author_username=author.username)

        CommentManager.add_comment(comment)

        video.comments.append(comment.comment_id)
        VideoManager.update_video_data(video)

    @staticmethod
    def delete_video(video_id: int):
        videos = DatabaseWorker.read_videos()
        videos.remove(list(filter(lambda it: it.video_id == video_id, videos))[0])
        DatabaseWorker.write_videos(videos)
