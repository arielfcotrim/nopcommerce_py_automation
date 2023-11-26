import configparser
from utilities.dir_path_manager import DirPathManager as Path


config = configparser.RawConfigParser()
config.read(Path.get_relative_path('configurations', 'config.ini'))


class ReadConfig:
    @staticmethod
    def get_config_value(section, option):
        config_value = config.get(section, option)
        return config_value
