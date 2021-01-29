from multipledispatch import dispatch

from components.database.dbworker import DatabaseWorker
from dto.Comment import Comment, CommentFactory
from dto.User import User
from dto.Video import Video


class CommentManager:
    @staticmethod
    def get_comment_by_id(comment_id: int) -> Comment:
        for comment in DatabaseWorker.read_comments():
            if comment.comment_id == comment_id:
                return comment

    @staticmethod
    @dispatch(User, Video, str)
    def add_comment(author: User, video: Video, comment_text: str):
        new_comment = CommentFactory.new_comment(
            video=video,
            author=author,
            replies=[],
            text=comment_text
        )

        comments = DatabaseWorker.read_comments()
        comments.append(new_comment)
        DatabaseWorker.write_comments(comments)

    @staticmethod
    @dispatch(Comment)
    def add_comment(c: Comment):
        comments = DatabaseWorker.read_comments()
        comments.append(c)
        DatabaseWorker.write_comments(comments)

    @staticmethod
    def delete_comment(comment_id: int):
        pass

    @staticmethod
    def update_comment_data(c: Comment):
        comments = DatabaseWorker.read_comments()

        for i in range(len(comments)):
            if comments[i].comment_id == c.comment_id:
                comments[i] = c

        DatabaseWorker.write_comments(comments)
