from datetime import datetime
import json


def serialize(obj):
    """
    Serializes an object to JSON format.
    Args:
        obj (object): The object to serialize.
    Returns:
        str or dict: The serialized object.
    """
    if isinstance(obj, datetime):
        return obj.isoformat()
    return {k: v for k, v in obj.__dict__.items() if not k.startswith('_')}


def to_json(obj):
    """
    Converts an object to a JSON string.
    Args:
        obj (object): The object to convert.
    Returns:
        str: The JSON string representation of the object.
    """
    json_str = json.dumps(obj, default=serialize)
    return json_str
