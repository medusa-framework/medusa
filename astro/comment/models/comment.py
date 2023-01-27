from astro import db
from flask import request
from datetime import datetime


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String())
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer)

    def __init__(self, message=None, user_id=None):
        self.message = message
        self.user_id = user_id

    def __repr__(self):
        return f"{self.__class__.__name__}{self.__dict__}"

    def create(self, message=None, user_id=None):
        self.message = message
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        self.user_id = user_id
        db.session.add(self)
        db.session.commit()
        return self.query.order_by(Comment.id.desc()).first()

    def get_all(self):
        return self.query.order_by("id").all()

    def get(self):
        id = request.args.get("id")
        return self.query.filter_by(id=id).first()

    def update(self, message=None, user_id=None):
        comment = self.get()
        comment.message = message
        comment.updated_at = datetime.now()
        comment.user_id = user_id
        db.session.commit()
        return self.query.filter_by(id=comment.id).first()

    def update_all(self, message=None, user_id=None):
        comments = self.query.all()
        for comment in comments:
            comment.message = message
            comment.updated_at = datetime.now()
            comment.user_id = user_id
            db.session.commit()
        return self.query.order_by("id").all()

    def delete(self):
        comment = self.get()
        temp_comment = self.get()
        db.session.delete(comment)
        db.session.commit()
        return temp_comment

    def delete_all(self):
        # get all comments
        comments = self.query.all()
        temp_comments = self.query.all()
        # loop through comments
        for comment in comments:
            # delete records
            db.session.delete(comment)
            db.session.commit()
        return temp_comments
