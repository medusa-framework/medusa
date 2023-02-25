from datetime import datetime
import json


def validate_int(id):
    if isinstance(id, str) and id.isdigit():
        return int(id)
    elif isinstance(id, int):
        return id
    else:
        return None


def serialize(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    return {k: v for k, v in obj.__dict__.items() if not k.startswith('_')}


def to_json(obj):
    json_str = json.dumps(obj, default=serialize)
    return json_str
