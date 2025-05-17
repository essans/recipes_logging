import logging
import datetime as dt

def set_logger(filename, file_mode='w', log_detail='INFO'):

    """
    Basic logging function accepting user inputs:
      filename: filename string to save in current dir or pass a full '/path/to/filename.log'
      file_mode : 'a' for append, 'w' for write
      log_detail: 'INFO' or 'DEBUG'
    """
    
    level = getattr(logging, log_detail.upper(), logging.INFO) #default/failsafe is INFO

    # Get and clear existing handlers for safe re-calling
    logger = logging.getLogger()
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    logging.basicConfig(
                    filename=filename,
                    level=level,
                    filemode=file_mode,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')



def set_ts_logger(filename, log_detail='INFO'):
    
    """
    Basic logging function which outputs to a timestamped file:
      filename: filename string to save in current dir or pass a full '/path/to/filename.log'
      log_detail: 'INFO' or 'DEBUG'
    """

    
    level = getattr(logging, log_detail.upper(), logging.INFO) #default/failsafe is INFO
  
    # Get and clear existing handlers for safe re-calling
    logger = logging.getLogger()
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)

    logging.basicConfig(
                    filename= f'{filename}_{dt.datetime.now().strftime('%Y%m%d_%H%M%S')}',
                    level=level,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

