import configparser
from utilities.dir_path_manager import DirPathManager as Path


class ConfigReader:
    def __init__(self, directory_name, file_name):
        """
        Initialize a RawConfigParser instance.
        :param directory_name:
        :param file_name:
        """
        self.my_config = configparser.RawConfigParser()

        # Read the configuration file using a relative path
        self.my_config.read(Path.get_relative_path(directory_name, file_name))

    def get_config_value(self, section, option):
        """
        Retrieve a specific configuration value from the config file.

        :param section: The section in the configuration file where the option is located.
        :param option: The option key whose value is to be fetched.
        :return: Value of the specified option from the specified section.
        """
        # Fetch the value from the specified section and option
        config_value = self.my_config.get(section, option)

        return config_value
