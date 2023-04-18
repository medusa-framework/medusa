import logging


def create_logger(log_name):
    logger = logging.getLogger(log_name)
    logger.setLevel(logging.DEBUG)
    
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    file_handler = logging.FileHandler(f"logs/{log_name}.log")

    logger.addHandler(ch)
    logger.addHandler(file_handler)

    return logger