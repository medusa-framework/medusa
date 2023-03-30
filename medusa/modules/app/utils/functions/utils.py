from datetime import datetime
import json


def validate_int(id):
    """
    Validates whether a value is an integer.

    Args:
        id (str or int): The value to validate.

    Returns:
        int or None: The value as an integer, or None if it could not be converted to an integer.
    """
    if isinstance(id, str) and id.isdigit():
        return int(id)
    elif isinstance(id, int):
        return id
    else:
        return None


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


def kwargs_get(json, key):
    """
    Retrieves the value of a key from a JSON object.

    Args:
        json (dict): The JSON object.
        key (str): The key to retrieve.

    Returns:
        str or None: The value of the key, or None if the key is not found.
    """
    if json.get(key):
        return json.get(key)
    else:
        if "json" in json.keys():
            return kwargs_get(json.get("json"), key)
