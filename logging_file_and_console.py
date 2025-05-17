import logging
import datetime as dt

def set_logger(filename, file_mode='w', log_detail='INFO', console=False):
    """
    Basic logging function:
      - Logs to a file
      - Also prints to console
    """
    level = getattr(logging, log_detail.upper(), logging.INFO)

    logger = logging.getLogger()
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    logging.basicConfig(
        filename=filename,
        level=level,
        filemode=file_mode,
        format='%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    if console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_formatter = logging.Formatter('%(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    return logger


def set_ts_logger(filename, log_detail='INFO'): 
    """
    Basic logging function which outputs to a timestamped file:
      filename: filename string to save in current dir or pass a full '/path/to/filename.log'
      log_detail: log_detail: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
    """
    
    level = getattr(logging, log_detail.upper(), logging.INFO) #default/failsafe is INFO
  
    logger = logging.getLogger()
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    logging.basicConfig(
                    filename= f'{filename}_{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}',
                    level=level,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

    if console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_formatter = logging.Formatter('%(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)
        logger.addHandler(console_handler)

    return logger

