import inspect
import logging
from medusa.config.app import Config


class CustomLogger:
    def __init__(self):
        self.logger = logging.getLogger("MEDUSALOGGER")
        formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(message)s')
        file_handler = logging.FileHandler(Config.LOG_PATH)
        file_handler.setFormatter(formatter)
        self.logger.addHandler(file_handler)
        self.logger.setLevel(logging.DEBUG)

    # TODO: figure out why custom fields aren't working-
    # probably shouldn't have to build a big fstring here
    def builder(self, message, status):
        model = inspect.stack()[
            2][0].f_locals["self"].__class__.__name__.upper()
        function = inspect.stack()[2][0].f_code.co_name.upper()
        return f"[{model}-{function}: {status}] {message}"

    # TODO: debug outputs to log file, but not console
    def debug(self, message, status):
        built_message = self.builder(message, status)
        self.logger.debug(built_message)

    def info(self, message, status):
        built_message = self.builder(message, status)
        self.logger.info(built_message)

    def warning(self, message, status):
        built_message = self.builder(message, status)
        self.logger.warning(built_message)

    def error(self, message, status):
        built_message = self.builder(message, status)
        self.logger.error(built_message)
