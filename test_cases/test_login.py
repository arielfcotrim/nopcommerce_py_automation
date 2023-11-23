import logging
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig
from utilities.custom_logger import CustomLogger
from utilities.media_manager import MediaManager


class TestLogIn:
    base_url = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    # logger = LogGeneration.log_gen()
    logger = CustomLogger.configure_logger(__name__, level=logging.INFO)

    def test_home_page_title(self, setup):
        self.logger.info('**** Test_001_Login ****')
        self.logger.info('Verifying Home Page Title')
        self.driver = setup
        self.driver.get(self.base_url)

        expected_title = "Your store. Login"
        actual_title = self.driver.title

        if actual_title == expected_title:
            self.logger.info('Test_001: Home Page Title == PASSED')
            assert True

        else:
            MediaManager.save_screenshot(self.driver, 'test_home_page_title')
            self.logger.error('Test_001: Home Page Title == FAILED')
            assert False

    def test_log_in(self, setup):
        self.logger.info('Attempting to Log-in...')
        self.driver = setup
        self.driver.get(self.base_url)

        WebDriverWait(self.driver, 10)

        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login_button()

        expected_title = "Dashboard / nopCommerce administration"
        actual_title = self.driver.title

        if actual_title == expected_title:
            self.logger.info('Test_001: Login == PASSED')
            assert True

        else:
            MediaManager.save_screenshot(self.driver, 'test_log_in')
            self.logger.error('Test_001: Login == FAILED')
            assert False
