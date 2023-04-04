import inspect
import logging
from medusa.config.app import Config


class CustomLogger:
    def __init__(self):
        super().__init__()

    # TODO: figure out why custom fields aren't working-
    # probably shouldn't have to build a big fstring here
    def log_builder(self, message, status):
        model = inspect.stack()[
            2][0].f_locals["self"].__class__.__name__.upper()
        function = inspect.stack()[2][0].f_code.co_name.upper()
        return f"[{model}-{function}: {status}] {message}"

    def log_debug(self, message, status):
        logger = self.build_logger()
        logger.debug(self.log_builder(message, status))

    def log_info(self, message, status):
        logger = self.build_logger()
        logger.info(self.log_builder(message, status))

    def log_warning(self, message, status):
        logger = self.build_logger()
        logger.warning(self.log_builder(message, status))

    def log_error(self, message, status):
        logger = self.build_logger()
        logger.error(self.log_builder(message, status))

    def build_logger(self):
        logger = logging.getLogger("MEDUSALOGGER")
        formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] %(message)s')
        file_handler = logging.FileHandler(Config.LOG_FILE)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        logger.setLevel(logging.DEBUG)
        return logger


CustomLogger()
