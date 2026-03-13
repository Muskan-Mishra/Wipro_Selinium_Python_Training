import logging
import os

def get_logger():

    log_dir = "Logs"
    os.makedirs(log_dir, exist_ok=True)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    file_handler = logging.FileHandler(f"{log_dir}/automation.log")
    formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(message)s")

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger