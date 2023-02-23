from datetime import datetime
import json


class Utils():

    def validate_int(self, id):
        if isinstance(id, str) and id.isdigit():
            return int(id)
        elif isinstance(id, int):
            return id
        else:
            return None

    def serialize(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return {k: v for k, v in obj.__dict__.items() if not k.startswith('_')}

    def to_json(self, obj):
        json_str = json.dumps(obj, default=self.serialize)
        return json_str
