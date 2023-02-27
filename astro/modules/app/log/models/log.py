from astro import db
from astro.modules.app.base.models.crud import CRUD


class Log(CRUD, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String())
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
    ip_address = db.Column(db.String)
    action = db.Column(db.String)
    status = db.Column(db.String)
    user = db.Column(db.String)
    level = db.Column(db.String)
    message = db.Column(db.String)
    record_id = db.Column(db.Integer)
