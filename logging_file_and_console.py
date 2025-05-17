import logging
import datetime as dt

import logging

def set_logger(filename, file_mode='w', log_detail='INFO', conole=False):
    """
    Basic logging function:
      - Logs to a file
      - Also prints to console
    """
    level = getattr(logging, log_detail.upper(), logging.INFO)

    logger = logging.getLogger()
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    # Configure file logging
    logging.basicConfig(
        filename=filename,
        level=level,
        filemode=file_mode,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Add console (stream) handler
    if console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_formatter = logging.Formatter('%(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    return logger


