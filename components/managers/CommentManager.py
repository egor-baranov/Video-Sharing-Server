from multipledispatch import dispatch

from components.database.dbworker import DatabaseWorker
from components.managers.UserManager import UserManager
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
            video=video, author=author, replies=[], text=comment_text
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
        comment = CommentManager.get_comment_by_id(comment_id)
        comment.text = "-Комментарий был удален администрацией-"
        CommentManager.update_comment_data(comment)

    @staticmethod
    def update_comment_data(c: Comment):
        comments = DatabaseWorker.read_comments()

        for i in range(len(comments)):
            if comments[i].comment_id == c.comment_id:
                comments[i] = c

        DatabaseWorker.write_comments(comments)

    @staticmethod
    def does_comment_exist(comment_id: int):
        return any([c.comment_id == comment_id for c in DatabaseWorker.read_comments()])

    @staticmethod
    def get_author(c: Comment) -> User:
        phone_user = UserManager.get_user_by_phone(c.author_phone)
        email_user = UserManager.get_user_by_email(c.author_email)

        return email_user if email_user.is_not_fake() else phone_user
