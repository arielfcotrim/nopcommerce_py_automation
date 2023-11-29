import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from utilities.config_reader import ConfigReader


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
    # Access the metadata plugin
    metadata = config.pluginmanager.getplugin('metadata')

    # Check if the metadata plugin exists, if not, create it
    if metadata:
        from pytest_metadata.plugin import metadata_key

    # Create an instance of ConfigReader for the config.ini file
    parse_configs = ConfigReader('configurations', 'config.ini')

    # Retrieve the values from the config file
    project_name = parse_configs.get_config_value(section='test metadata', option='project_name')
    module_name = parse_configs.get_config_value(section='test metadata', option='module_name')
    tester_name = parse_configs.get_config_value(section='test metadata', option='tester_name')

    # Add the metadata to the metadata dictionary
    config.stash[metadata_key]['Project Name'] = project_name
    config.stash[metadata_key]['Module Name'] = module_name
    config.stash[metadata_key]['Tester Name'] = tester_name
    # config._metadata['Project Name'] = project_name
    # config._metadata['Module Name'] = module_name
    # config._metadata['Tester Name'] = tester_name

    # Set Metadata
    # Check if the metadata dictionary exists, if not, create it
    # if not hasattr(config, 'metadata'):
    #     config.metadata = {}
    # config.metadata['Project Name'] = project_name
    # config.metadata['Module Name'] = module_name
    # config.metadata['Tester Name'] = tester_name


@pytest.mark.optionalhook
def pytest_metadata(metadata):
    """
    An optional hook for modifying metadata for the test report.
    This is useful for removing or altering information that will appear in the report.

    :param metadata: A dictionary containing metadata information.
    """
    # Remove certain metadata entries that are not needed or should not be displayed in the report
    metadata.pop('JAVA HOME', None)     # Remove JAVA HOME information if it exists
    metadata.pop('Plugins', None)       # Remove Plugins information if it exists
