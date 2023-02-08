from flask_login import current_user
import logging
from datetime import datetime
from flask import request
from astro.log.models.log import Log


class ConsoleLog:
    action = None
    status = None
    user = None
    level = None
    message = None

    def build_output(self, json):
        output = [
            "[" + json.get("ip_address") + "]",
            json.get("action").upper(),
            json.get("class_name"),
            json.get("status") + ":",
            json.get("message")
        ]
        return " ".join(output)

    def log_error(self, action, status, message):
        output = self.build_output(action, status, message)
        logging.error(output)
        return output

    def log_info(self, json):
        if current_user.is_authenticated:
            json["user"] = current_user.id
        json["level"] = "info"
        output = self.build_output(json)
        logging.info(output)
        Log().create(json=json)
        return output

    def log_warn(self, action, status, message):
        output = self.build_output(action, status, message)
        logging.warn(output)
        return output

    def log_debug(self, action, status, message):
        output = self.build_output(action, status, message)
        logging.debug(output)
        return output

    def log_critical(self, action, status, message):
        output = self.build_output(action, status, message)
        logging.critical(output)
        return output
