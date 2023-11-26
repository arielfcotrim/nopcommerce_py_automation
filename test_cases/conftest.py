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
