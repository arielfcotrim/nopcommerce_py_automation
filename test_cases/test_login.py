import logging
import pytest
from page_objects.login_page import LoginPage
from utilities.config_reader import ConfigReader
from utilities.custom_logs import CustomLogs
from utilities.screen_cap_manager import ScreenCapture
from utilities.constants import PageTitles as Titles


class TestLogin:
    # Instantiate a ConfigReader instance to access configuration settings
    parse_configs = ConfigReader('configurations', 'config.ini')

    # Retrieve configuration values such as URL, username, and password
    base_url = parse_configs.get_config_value('basic access data', 'base_url')
    username = parse_configs.get_config_value('basic access data', 'username')
    password = parse_configs.get_config_value('basic access data', 'password')

    # Configure the logger for this test class
    logger = CustomLogs.configure_logger(__name__, level=logging.INFO)

    @pytest.mark.test_id_001
    @pytest.mark.parametrize("browser", ["chrome", "edge"])
    def test_home_page_title(self, driver_setup, browser):
        # # Declare variables to store information about the test case
        test_case_id = 'tc_001'
        test_case_name = 'test_home_page_title'

        # Call static method to log the start of the test case
        CustomLogs.log_test_start(self.logger, test_case_id, test_case_name, browser)

        # Initialize the WebDriver and open the base URL
        self.driver = driver_setup
        self.driver.get(self.base_url)

        # Declare variables to store the expected and actual page titles
        expected_result = Titles.HOME_PAGE
        actual_result = self.driver.title

        # Assert and log the result
        if actual_result == expected_result:
            CustomLogs.log_test_result(
                self.logger, test_case_id, 'PASSED',
                expected_result=expected_result, actual_result=actual_result
            )
            assert True

        else:
            ScreenCapture.save_screenshot(self.driver, f'{test_case_id}_{test_case_name}')
            CustomLogs.log_test_result(
                self.logger, test_case_id, 'FAILED',
                expected_result=expected_result, actual_result=actual_result
            )
            assert False

    @pytest.mark.test_id_002
    @pytest.mark.parametrize("browser", ["chrome", "edge"])
    def test_log_in(self, driver_setup, browser):
        # Declare variables to store information about the test case
        test_case_id = 'tc_002'
        test_case_name = 'test_log_in'

        # Call static method to log the start of the test case
        CustomLogs.log_test_start(self.logger, test_case_id, test_case_name, browser)

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
            CustomLogs.log_test_result(
                self.logger, test_case_id, 'PASSED',
                expected_result=expected_result, actual_result=actual_result
            )
            assert True

        else:
            ScreenCapture.save_screenshot(self.driver, f'{test_case_id}_{test_case_name}')
            CustomLogs.log_test_result(
                self.logger, test_case_id, 'FAILED',
                expected_result=expected_result, actual_result=actual_result
            )
            assert False
