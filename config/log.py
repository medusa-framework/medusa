import os


class LogConfig():
    LOG_NAME = os.environ.get("LOG_NAME", "medusa")
    LOG_DIR = os.environ.get("LOG_DIR", "/logs")
    LOG_FILE = os.environ.get("LOG_FILE", f"{LOG_DIR}/{LOG_NAME}.log")
