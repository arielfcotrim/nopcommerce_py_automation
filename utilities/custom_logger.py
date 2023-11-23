import logging
from utilities.dir_path_manager import DirPathManager as Path


class LogGeneration:
    @staticmethod
    def log_gen():
        logging.basicConfig(
            filename=Path.get_relative_path('logs', 'automation.log'),
            level=logging.INFO,
            format='%(asctime)s : %(levelname)s : %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S %p'
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger
