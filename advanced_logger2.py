def set_logger(filename, file_mode='w', log_detail='INFO', console=False, silence_third_party=False):
    """
    Set up logging with:
      - File logging
      - Optional console output
      - Optional suppression of third-party logs

    Args:
        filename (str): Path to the log file
        file_mode (str): 'w' for overwrite, 'a' for append
        log_detail (str): 'DEBUG', 'INFO', etc.
        console (bool): Whether to also log to console
        silence_third_party (bool): Set True to silence non-local logs below WARNING
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

    if silence_third_party:
        for name in logging.root.manager.loggerDict:
            if not name.startswith('__main__') and not name.startswith('mylogger'):
                logging.getLogger(name).setLevel(logging.WARNING)

        # Additionally silence known verbose libraries
        for noisy_logger in ['httpx', 'openai', 'urllib3']:
            logging.getLogger(noisy_logger).setLevel(logging.WARNING)

    return logger
