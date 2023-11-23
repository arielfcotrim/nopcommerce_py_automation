import logging
from utilities.dir_path_manager import DirPathManager as Path


class CustomLogger:
    @staticmethod
    def configure_logger(name, level=logging.INFO):
        """ Configure and return a logger with the given name and level. """
        # Create a custom logger
        logger = logging.getLogger(name)

        # Set the log level
        logger.setLevel(level)

        # Check if the logger already has handlers to avoid duplicate logs
        if not logger.handlers:
            # Create handlers (console and file)
            console_handler = logging.StreamHandler()
            file_handler = logging.FileHandler(Path.get_relative_path('logs', 'automation.log'))

            # Create formatters and add them to handlers
            console_format = logging.Formatter(
                '%(name)s - %(levelname)s - %(message)s'
            )

            file_format = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                datefmt='%Y-%m-%d %H:%M:%S'
            )

            console_handler.setFormatter(console_format)
            file_handler.setFormatter(file_format)

            # Add handlers to the logger
            logger.addHandler(console_handler)
            logger.addHandler(file_handler)

        return logger
