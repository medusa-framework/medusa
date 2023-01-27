from astro.comment.models.comment import Comment
from astro import to_json


class CommentController:

    def create(self):
        message = "this is a comment"
        return to_json(Comment().create(
            message=message,
            user_id=12  # TODO: Change to current logged in user
        ))

    def get_all(self):
        return to_json(Comment().get_all())

    def get(self):
        return to_json(Comment().get())

    def delete_all(self):
        return to_json(Comment().delete_all())

    def delete(self):
        return to_json(Comment().delete())

    def update_all(self):
        message = "this is a comment that was updated by update all"
        return to_json(Comment().update_all(
            message=message,
            user_id=12,  # TODO: Change to current logged in user
        ))

    def update(self):
        message = "this is a comment that was updated"
        return to_json(Comment().update(
            message=message,
            user_id=12,  # TODO: Change to current logged in user
        ))
