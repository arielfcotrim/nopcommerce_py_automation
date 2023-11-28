import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import configparser
from utilities.config_reader import ConfigReader
from utilities.dir_path_manager import DirPathManager


def pytest_addoption(parser):
    """
    Adds a command-line option to pytest.
    This allows the user to specify the browser to be used for tests.
    """
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture()
def browser(request):
    """
    Pytest fixture to retrieve the browser type from the pytest command-line option.
    """
    return request.config.getoption("--browser")


@pytest.fixture()
def driver_setup(browser):
    """
    Pytest fixture to initialize and quit the WebDriver based on the browser type.
    This fixture takes the 'browser' fixture as an input to determine which browser
    WebDriver to initiate.
    """
    if browser == "edge":
        print('Launching Edge...')
        driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
        yield driver
        driver.quit()

    elif browser == "firefox":
        print('Launching Firefox...')
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        yield driver
        driver.quit()

    else:
        print('Launching Chrome...')
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        yield driver
        driver.quit()


# PyTest HTML Report
def pytest_configure(config):
    # Read from config.ini
    config_parser = configparser.ConfigParser()
    config_parser.read(DirPathManager.get_relative_path('configurations', 'config.ini'))
    ConfigReader.get_config_value(section='test metadata', option='project_name')
    project_name = config_parser.get('test metadata', 'project_name')
    module_name = config_parser.get('test metadata', 'module_name')
    tester_name = config_parser.get('test metadata', 'tester_name')

    # Set Metadata
    # Check if the metadata dictionary exists, if not, create it
    if not hasattr(config, 'metadata'):
        config.metadata = {}
    config.metadata['Project Name'] = project_name
    config.metadata['Module Name'] = module_name
    config.metadata['Tester Name'] = tester_name


# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     """
#     An optional hook for modifying metadata for the test report.
#     This is useful for removing or altering information that will appear in the report.
#
#     :param metadata: A dictionary containing metadata information.
#     """
#     # Remove certain metadata entries that are not needed or should not be displayed in the report
#     metadata.pop('JAVA HOME', None)     # Remove JAVA HOME information if it exists
#     metadata.pop('Plugins', None)       # Remove Plugins information if it exists
