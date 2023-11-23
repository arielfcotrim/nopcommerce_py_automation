import os
from selenium.webdriver.remote.webdriver import WebDriver
from utilities.dir_path_manager import DirPathManager as Path


class MediaManager:
    @staticmethod
    def save_screenshot(driver: WebDriver, test_name: str):
        screenshot_path = Path.get_relative_path('screenshots', test_name + '.png')
        driver.save_screenshot(screenshot_path)
