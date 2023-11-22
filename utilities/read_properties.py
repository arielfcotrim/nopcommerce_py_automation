import configparser


config = configparser.RawConfigParser()
config.read('C:\\GitHub\\nopcommerce_py_automation\\configurations\\config.ini')


class ReadConfig:
    @staticmethod
    def get_url():
        url = config.get('basic access data', 'base_url')
        return url

    @staticmethod
    def get_username():
        username = config.get('basic access data', 'username')
        return username

    @staticmethod
    def get_password():
        password = config.get('basic access data', 'password')
        return password