from faker import Faker
from medusa.modules.app.base.controllers.base import BaseController
from medusa.modules.app.base.models.base import Base
from medusa import db
from medusa.modules.app.user.models.access_right import AccessRight
from medusa.modules.app.user.seeders.access_group import access_groups as seeds


access_group_rights = db.Table(
    "access_group_rights",
    db.Column("access_right_id", db.Integer, db.ForeignKey(
        "access_right.id"), primary_key=True),
    db.Column("access_group_id", db.Integer, db.ForeignKey(
        "access_group.id"), primary_key=True)
)


class AccessGroup(Base, db.Model):
    name = db.Column(db.String())
    access_group_rights = db.relationship(
        "AccessRight",
        secondary=access_group_rights,
        lazy="subquery",
        backref=db.backref("accessgroup", lazy=True)
    )

    def __init__(self) -> None:
        self._controller = BaseController(self)
        self._seeds = seeds
        super().__init__()

    def create(self, **kwargs):
        return self.post(**kwargs)

    def update(self, **kwargs):
        return self.post(**kwargs)

    def post(self, **kwargs):
        print(kwargs)
        access_rights = kwargs.get("access_group_rights")
        if access_rights:
            access_right_records = []
            for access_right in access_rights:
                access_right_record = AccessRight().query.filter_by(
                    id=access_right).first()
                if access_right_record:
                    access_right_records.append(access_right_record)
            kwargs["access_group_rights"] = access_right_records
        if kwargs.get("request_type") == "PATCH":
            return super().update(**kwargs)
        elif kwargs.get("request_type") == "POST":
            return super().create(**kwargs)

    def factory(self):
        faker = Faker()
        name = faker.word()
        json = {"name": name}
        return json


AccessGroup()
