import os
import pytest
from selenium import webdriver
from page_objects.login_page import LogInPage


class TestLogIn:
    baseURL = "https://admin.demo.nopcommerce.com/"
    username = os.environ.get('USERNAME')
    # username = "admin@yourstore.com"
    password = os.environ.get('PASSWORD')
    # password = "admin"

    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        expected_title = "Your store. Login"
        actual_title = self.driver.title
        self.driver.quit()

        if actual_title == expected_title:
            assert True

        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_home_page_title" + ".png")
            assert False

    def test_log_in(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.login_page = LogInPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login_button()
        expected_title = "Dashboard / nopCommerce administration"
        actual_title = self.driver.title
        self.driver.quit()

        if actual_title == expected_title:
            assert True

        else:
            assert False
