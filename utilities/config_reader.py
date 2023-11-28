import configparser
from utilities.dir_path_manager import DirPathManager as Path


# Initialize a RawConfigParser instance
config = configparser.RawConfigParser()

# Read the configuration file using a relative path
config.read(Path.get_relative_path('configurations', 'config.ini'))


class ConfigReader:
    @staticmethod
    def get_config_value(section, option):
        """
        Retrieve a specific configuration value from the config file.

        :param section: The section in the configuration file where the option is located.
        :param option: The option key whose value is to be fetched.
        :return: Value of the specified option from the specified section.
        """
        # Fetch the value from the specified section and option
        config_value = config.get(section, option)
        return config_value
