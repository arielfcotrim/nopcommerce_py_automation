import pytest
from page_objects.login_page import LoginPage
from utilities.read_properties import ReadConfig


class TestLogIn:
    base_url = ReadConfig.get_url()
    username = ReadConfig.get_username()
    password = ReadConfig.get_password()

    def test_home_page_title(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        expected_title = "Your store. Login"
        actual_title = self.driver.title

        if actual_title == expected_title:
            assert True

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_home_page_title" + ".png")
            assert False

    def test_log_in(self, setup):
        self.driver = setup
        self.driver.get(self.base_url)

        self.login_page = LoginPage(self.driver)
        self.login_page.set_username(self.username)
        self.login_page.set_password(self.password)
        self.login_page.click_login_button()

        expected_title = "Dashboard / nopCommerce administration"
        actual_title = self.driver.title

        if actual_title == expected_title:
            assert True

        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_log_in" + ".png")
            assert False
