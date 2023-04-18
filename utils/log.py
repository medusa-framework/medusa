import getpass
import logging
import os
import socket
import coloredlogs


def create_logger(log_name):
    logger = logging.getLogger(log_name)
    logger.propagate = False
    logger.setLevel(logging.DEBUG)
    
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter(
        '%(asctime)s %(hostname)s %(username)s %(name)s %(levelname)s %(message)s'.format())
    formatter.datefmt = '%Y-%m-%d %H:%M:%S'
    ch.setFormatter(formatter)

    coloredlogs.install(
        level='DEBUG',
        logger=logger,
        fmt='%(asctime)s %(hostname)s %(username)s %(name)s %(levelname)s %(message)s'.format(
        datefmt='%Y-%m-%d %H:%M:%S'))


    file_handler = logging.FileHandler(f"logs/{log_name}.log")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger
