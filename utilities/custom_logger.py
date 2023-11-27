import logging
from utilities.dir_path_manager import DirPathManager as Path


class CustomLogger:
    @staticmethod
    def configure_logger(name, level=logging.INFO):
        """
        Configure and return a logger with the given name and level.

        This method creates a logger with two handlers: one for console output
        and another for file output.

        :param name: The name of the logger.
        :param level: The logging level. Defaults to logging.INFO.
        :return: Configured logger instance.
        """
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

    @staticmethod
    def log_test_start(logger, test_case_id, test_case_name, browser):
        """
        Log the start of a test case.
        :param logger: The logger instance.
        :param test_case_id: The ID of the test case.
        :param test_case_name: The name of the test case.
        :param browser: The name of the browser.
        :return: None
        """
        # skip line for improved readability in the console output
        print()

        logger.info(f'**** {test_case_id}: {test_case_name} ****')
        logger.info(f'Browser: {browser}')

    @staticmethod
    def log_test_result(logger, test_case_id, status):
        """
        Log the result of a test case.
        :param logger: The logger instance.
        :param test_case_id: The ID of the test case.
        :param status: The result of the test case.
        :return: None
        """
        # skip line for improved readability in the console output
        print()

        logger.info(f'{test_case_id} == {status}')
