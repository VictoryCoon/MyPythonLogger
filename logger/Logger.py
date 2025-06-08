import os
import logging
import datetime
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler


def setup_logging():
    load_dotenv()

    name = os.getenv("LOG_NAME")
    level = int(os.getenv("LOG_LEVEL"))
    now = datetime.datetime.now()
    now_date = now.strftime("%Y-%m-%d")

    log_dir = 'logs'

    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    log_file_path = os.path.join(log_dir,f'{name}_{now_date}.log')

    # Object
    logger = logging.getLogger("VICTORY-RAG")
    console = logging.StreamHandler()
    output = RotatingFileHandler(
        log_file_path,
        maxBytes=1024*1024,  #1MB
        backupCount=5,
        encoding='utf-8'
    )

    # Level - DEBUG(10), INFO(20), WARN/WARNING(30), ERROR(40), FATAL/CRITICAL(50)
    logger.setLevel(level)
    console.setLevel(level)
    output.setLevel(level)

    # Format
    logger_format = logging.Formatter('[%(name)s] %(asctime)s - %(levelname)s : %(message)s')
    console.setFormatter(logger_format)
    output.setFormatter(logger_format)

    # Combine
    if not logger.handlers:
        logger.addHandler(console)
        logger.addHandler(output)

    return logger