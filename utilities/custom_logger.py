import logging
import os
from utilities.dir_path_manager import DirPathManager as Path


def configure_logger(name):
    # Create a custom logger
    logger = logging.getLogger(name)

    # Set the log level
    logger.setLevel(logging.INFO)

    # Create handlers (console and file)
    c_handler = logging.StreamHandler()
    f_handler = logging.FileHandler(Path.get_relative_path('logs', 'automation.log'))

    # Create formatters and add it to handlers
    c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    c_handler.setFormatter(c_format)
    f_handler.setFormatter(f_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger
