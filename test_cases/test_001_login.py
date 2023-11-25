import logging
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import CustomLogger
from utilities.screen_cap_manager import ScreenCapture
from utilities.constants import PageTitles as Titles


class TestLogin:
    base_url = ReadConfig.get_config_value('basic access data', 'base_url')
    username = ReadConfig.get_config_value('basic access data', 'username')
    password = ReadConfig.get_config_value('basic access data', 'password')

    # logger = LogGeneration.log_gen()
    logger = CustomLogger.configure_logger(__name__, level=logging.INFO)

    @pytest.mark.test_id_001_01
    @pytest.mark.parametrize("browser", ["chrome", "edge"])
    def test_home_page_title(self, driver_setup, browser):
        print()
        self.logger.info('**** Test_001_Login ****')
        self.logger.info('Verifying Home Page Title')
        self.driver = driver_setup
        self.driver.get(self.base_url)

        expected_result = Titles.HOME_PAGE
        actual_result = self.driver.title

        if actual_result == expected_result:
            self.logger.info('Test_001: Home Page Title == PASSED')
            assert True

        else:
            ScreenCapture.save_screenshot(self.driver, 'test_home_page_title')
            self.logger.error('Test_001: Home Page Title == FAILED')
            assert False

    def test_log_in(self, driver_setup):
        self.logger.info('Attempting to Log-in...')
        self.driver = driver_setup
        self.driver.get(self.base_url)

        WebDriverWait(self.driver, 10)

        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login_button()

        expected_result = Titles.DASHBOARD
        actual_result = self.driver.title

        if actual_result == expected_result:
            self.logger.info('Test_001: Login == PASSED')
            assert True

        else:
            ScreenCapture.save_screenshot(self.driver, 'test_log_in')
            self.logger.error('Test_001: Login == FAILED')
            assert False
