from selenium.webdriver.remote.webdriver import WebDriver
from utilities.dir_path_manager import DirPathManager as Path


class ScreenCapture:
    @staticmethod
    def save_screenshot(driver: WebDriver, test_name: str):
        """
        Save a screenshot of the current state of the browser.

        :param driver: The WebDriver instance controlling the browser.
        :param test_name: The name of the test, used to name the screenshot file.
        """
        # Construct the file path for the screenshot and save it in the 'screenshots' directory with the test_name
        screenshot_path = Path.get_relative_path('screenshots', test_name + '.png')

        # Use the WebDriver to save the screenshot to the specified path
        driver.save_screenshot(screenshot_path)
