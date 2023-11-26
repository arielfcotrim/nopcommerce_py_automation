import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager


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
    """
    A hook for adding or modifying pytest configuration settings.
    This is invoked for every test session.

    :param config: The pytest config object, which contains settings and options.
    """
    if hasattr(config, '_metadata'):
        # Check if the config object already has a '_metadata' attribute
        # If it does, update it with project-specific information
        config._metadata['Project Name'] = 'NOP Commerce'
        config._metadata['Module Name'] = 'Customers'
        config._metadata['Tester'] = 'Ariel'
    else:
        # If the '_metadata' attribute does not exist, create it
        # and initialize it with project-specific information
        config._metadata = {'Project Name': 'NOP Commerce', 'Module Name': 'Customers', 'Tester': 'Ariel'}


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
