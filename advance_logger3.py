def set_logger(
    filename,
    file_mode='w',
    log_detail='DEBUG',
    console=False,
    console_level='INFO',
    silence_third_party_console=True,
    local_modules=['__main', 'src', 'scripts']
):
    """
    Args:
        local_modules (list): Module name prefixes considered 'local' for console logs.
    """
    if local_modules is None:
        local_modules = ['__main__']

    file_log_level = getattr(logging, log_detail.upper(), logging.DEBUG)
    screen_log_level = getattr(logging, console_level.upper(), logging.INFO)

    root_logger = logging.getLogger()
    for handler in root_logger.handlers[:]:
        root_logger.removeHandler(handler)

    # --- File handler ---
    file_handler = logging.FileHandler(filename, mode=file_mode)
    file_handler.setLevel(file_log_level)
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(name)s - %(message)s',
                                       datefmt='%Y-%m-%d %H:%M:%S')
    file_handler.setFormatter(file_formatter)
    root_logger.addHandler(file_handler)

    # --- Console handler ---
    if console:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(screen_log_level)
        console_formatter = logging.Formatter('%(levelname)s - %(message)s')
        console_handler.setFormatter(console_formatter)

        if silence_third_party_console:
            def is_local_log(record):
                return any(record.name.startswith(prefix) for prefix in local_modules)
            console_handler.addFilter(is_local_log)

        root_logger.addHandler(console_handler)

    root_logger.setLevel(min(file_log_level, screen_log_level))

    return root_logger
