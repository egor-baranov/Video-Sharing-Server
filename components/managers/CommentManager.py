from dto.Comment import *
from components.database.dbworker import DatabaseWorker


class CommentManager:
    @staticmethod
    def get_comment_by_id(comment_id: int) -> Comment:
        for comment in DatabaseWorker.read_comments():
            if comment.comment_id == comment_id:
                return comment
