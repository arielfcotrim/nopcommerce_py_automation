import logging
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from page_objects.login_page import LoginPage
from utilities.config_parser import ReadConfig
from utilities.custom_logger import CustomLogger
from utilities.screen_cap_manager import ScreenCapture
from utilities.constants import PageTitles as Titles


class TestLogin:
    # Retrieve configuration values such as URL, username, and password
    base_url = ReadConfig.get_config_value('basic access data', 'base_url')
    username = ReadConfig.get_config_value('basic access data', 'username')
    password = ReadConfig.get_config_value('basic access data', 'password')

    # Configure the logger for this test class
    logger = CustomLogger.configure_logger(__name__, level=logging.INFO)

    @pytest.mark.test_id_001
    @pytest.mark.parametrize("browser", ["chrome", "edge"])
    def test_home_page_title(self, driver_setup, browser):
        # Declare variables to store information about the test case
        tc_id = 'tc_001'
        tc_name = 'test_home_page_title'

        # skip line for improved readability in the console output
        print()
        # Log the start of the test
        self.logger.info(f'**** {tc_id}: {tc_name} ****')
        self.logger.info(f'Browser: {browser}')

        # Initialize the WebDriver and open the base URL
        self.driver = driver_setup
        self.driver.get(self.base_url)

        # Declare variables to store the expected and actual page titles
        expected_result = Titles.HOME_PAGE
        actual_result = self.driver.title

        # Assert and log the result
        if actual_result == expected_result:
            self.logger.info(f'{tc_id} == PASSED')
            assert True

        else:
            ScreenCapture.save_screenshot(self.driver, f'{tc_id}_{tc_name}')
            self.logger.error(f'{tc_id} == FAILED')
            assert False

    @pytest.mark.test_id_002
    @pytest.mark.parametrize("browser", ["chrome", "edge"])
    def test_log_in(self, driver_setup, browser):
        # Declare variables to store information about the test case
        tc_id = 'tc_002'
        tc_name = 'test_log_in'

        # skip line for improved readability in the console output
        print()
        # Log the start of the test
        self.logger.info(f'**** {tc_id}: {tc_name} ****')
        self.logger.info(f'Browser: {browser}')

        # Initialize the WebDriver and open the base URL
        self.driver = driver_setup
        self.driver.get(self.base_url)

        # Initialize the login page object and perform login
        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login_button()

        # Declare variables to store the expected and actual page titles
        expected_result = Titles.DASHBOARD
        actual_result = self.driver.title

        # Assert and log the result
        if actual_result == expected_result:
            self.logger.info(f'{tc_id} == PASSED')
            assert True

        else:
            ScreenCapture.save_screenshot(self.driver, f'{tc_id}_{tc_name}')
            self.logger.error(f'{tc_id} == FAILED')
            assert False
