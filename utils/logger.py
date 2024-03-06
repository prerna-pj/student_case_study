import logging


def setup_logger(log_file="log/log_file_name.log", log_level="INFO"):
    """
    Setup the logging instance
    PARAMETERS:
    - log_file: Set the name of the log file to be created
    - log_level: Set the log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    """
    # Create a logger instance
    logger = logging.getLogger(__name__)

    # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    # logger.setLevel(logging.log_level)
    # Convert log_level string to corresponding constant
    numeric_level = getattr(logging, log_level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {log_level}")

    # Set the logging level
    logger.setLevel(numeric_level)

    # Create a file handler and set the level to INFO
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)

    # Create a console handler and set the level to DEBUG
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)

    # Create a formatter and add it to the handlers
    formatter = logging.Formatter(
        "%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
    )
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
