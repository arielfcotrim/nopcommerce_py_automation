import logging


class LogGeneration:
    @staticmethod
    def log_gen():
        logging.basicConfig(
            filename='C:\\GitHub\\nopcommerce_py_automation\\logs\\' +
                     'automation.log',
            format='%(asctime)s : %(levelname)s : %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S %p'
        )

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)

        return logger
