# chatgpt adaptation of my baseline logger

import logging

def set_logger(filename, file_mode='w', log_detail='INFO', silence_third_party=True):
    """
    Set up logging with control over local and third-party log levels.
    
    Parameters:
    - filename: Log file path
    - file_mode: 'a' for append, 'w' for write
    - log_detail: 'DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'
    - silence_third_party: If True, suppress third-party logs below WARNING
    """

    level = getattr(logging, log_detail.upper(), logging.INFO)  # Failsafe to INFO

    # Clear all root logger handlers
    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # Create file handler for local logger
    file_handler = logging.FileHandler(filename, mode=file_mode)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(formatter)

    # Set up your script's logger
    local_logger = logging.getLogger('__main__')  # Or use __name__ if inside a module
    local_logger.setLevel(level)
    local_logger.addHandler(file_handler)
    local_logger.propagate = False  # Prevent double logging via root

    if silence_third_party:
        for name in logging.root.manager.loggerDict:
            if not name.startswith("__main__"):
                logging.getLogger(name).setLevel(logging.WARNING)

    # Optionally return the logger if you want to use it directly
    return local_logger
