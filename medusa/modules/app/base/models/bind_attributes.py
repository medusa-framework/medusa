from datetime import datetime
from medusa.modules.app.base.controllers.base import BaseController
from medusa.modules.app.base.models.base import Base
from medusa import db


class BindClass(Base, db.Model):

    def bind_attributes(self, **kwargs):
        object.updated_at = datetime.now()
        for arg in kwargs:
            setattr(self, arg, kwargs.get(arg))
