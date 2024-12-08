import logging
import sys
from logging.handlers import RotatingFileHandler


def setup_logger(name):
    # Create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Create handlers
    console_handler = logging.StreamHandler(sys.stdout)
    file_handler = RotatingFileHandler(
        "bot.log", maxBytes=1024 * 1024, backupCount=5  # 1MB
    )

    # Create formatters and add it to handlers
    log_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    console_handler.setFormatter(log_format)
    file_handler.setFormatter(log_format)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
