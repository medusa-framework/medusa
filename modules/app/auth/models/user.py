from config.packages import db, bcrypt, login_manager
from modules.app.base.models.base import BaseModel
from modules.app.auth.controllers.user import UserController
from modules.app.auth.routes.user import UserRoute
from flask_login import login_user, current_user, logout_user, UserMixin, login_required

user_access_group = db.Table(
    "user_access_group",
    db.Column("access_group_id", db.Integer, db.ForeignKey(
        "access_group.id"), primary_key=True),
    db.Column("user_id", db.Integer, db.ForeignKey(
        "user.id"), primary_key=True)
)


class User(BaseModel, UserRoute, UserController, UserMixin, db.Model):
    username = db.Column(db.String(255))
    email = db.Column(db.String(255))
    password = db.Column(db.String(255))
    display_name = db.Column(db.String(255))
    user_access_group = db.relationship(
        "AccessGroup",
        secondary=user_access_group,
        lazy="subquery",
        backref=db.backref("user", lazy=True)
    )

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    def model_create(self, **kwargs):
        kwargs["password"] = self.hashed_password(kwargs.get("password"))
        return super().model_create(**kwargs)

    def hashed_password(self, password=None):
        hashed_password = bcrypt.generate_password_hash(
            password).decode("utf-8")
        return hashed_password

    def model_login(self, **kwargs):
        if kwargs.get("email") and kwargs.get("password"):
            record = self.query.filter_by(email=kwargs.get("email")).first()
            if record and bcrypt.check_password_hash(record.password, kwargs.get("password")):
                login_user(record, remember=kwargs.get("remember"))
                return current_user

    def model_logout(self):
        if current_user.is_authenticated:
            user = self.query.filter_by(id=current_user.id).first()
            logout_user()
            return user
