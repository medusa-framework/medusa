from faker import Faker
from astro.modules.app.base.controllers.base import BaseController
from astro.modules.app.base.models.base import Base
from astro import db
from astro.modules.app.user.models.access_right import AccessRight
from astro.modules.app.user.seeders.access_group import access_groups as seeds


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
        kwargs["json"]["request_type"] = "create"
        return self.post(**kwargs)

    def update(self, **kwargs):
        kwargs["json"]["request_type"] = "update"
        return self.post(**kwargs)

    def post(self, **kwargs):
        access_group_rights = kwargs.get("json").get("access_group_rights")
        if access_group_rights:
            access_right_records = []
            for access_right in access_group_rights:
                access_right_record = AccessRight().query.filter_by(
                    id=access_right).first()
                if access_right_record:
                    access_right_records.append(access_right_record)
            kwargs["json"]["access_group_rights"] = access_right_records
        if kwargs.get("json").get("request_type") == "update":
            return super().update(**kwargs)
        elif kwargs.get("json").get("request_type") == "create":
            return super().create(**kwargs)

    def factory(self):
        faker = Faker()
        name = faker.word()
        json = {"name": name}
        return json


AccessGroup()
