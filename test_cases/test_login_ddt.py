import pytest
from page_objects.login_page import LoginPage
from utilities.config_reader import ConfigReader
from utilities.custom_logs import CustomLogs
from utilities.dir_path_manager import DirPathManager as Path
from utilities import excel_utilities as Excel
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Test002LoginDDT:
    # Instantiate a ConfigReader instance to access configuration settings
    parse_configs = ConfigReader('configurations', 'config.ini')

    # Get url from config.ini
    base_url = parse_configs.get_config_value('basic access data', 'base_url')
    # Get username and password from Excel file
    data_file = Path.get_relative_path('test_data', 'login_data.xlsx')

    # Configure the logger for this test class
    logger = CustomLogs.configure_logger(__name__)

    @pytest.mark.test_id_003
    @pytest.mark.parametrize("browser", ["chrome", "edge"])
    def test_login_ddt(self, driver_setup, browser):
        # Declare variables to store information about the test case
        test_case_id = 'tc_003'
        test_case_name = 'test_login_ddt'

        # Call static method to log the start of the test case
        CustomLogs.log_test_start(self.logger, test_case_id, test_case_name, browser)

        # Initialize the WebDriver and open the base URL
        self.driver = driver_setup
        self.driver.get(self.base_url)

        # Instantiate a LoginPage object
        self.login_page = LoginPage(self.driver)

        # Call the set_username method to enter the username
        self.rows = Excel.get_row_count(self.data_file, 'Sheet1')

        list_status = []  # Empty list to append the results of each iteration
        for row in range(2, self.rows + 1):
            self.username = Excel.read_data(self.data_file, 'Sheet1', row, 1)
            self.password = Excel.read_data(self.data_file, 'Sheet1', row, 2)
            self.expected_result = Excel.read_data(self.data_file, 'Sheet1', row, 3)

            self.login_page.set_username(self.username)
            self.login_page.set_password(self.password)
            self.login_page.click_login_button()

            # Declare variables to store the expected and actual page titles
            expected_result = 'Dashboard / nopCommerce administration'
            actual_result = self.driver.title

            if actual_result == expected_result:
                if self.expected_result == 'Pass':
                    CustomLogs.log_test_result(
                        self.logger, test_case_id, 'PASSED PARTIALLY',
                        expected_result=expected_result, actual_result=actual_result
                    )
                    list_status.append('Pass')
                    self.login_page.click_logout_button()

                elif self.expected_result == 'Fail':
                    CustomLogs.log_test_result(
                        self.logger, test_case_id, 'FAILED PARTIALLY',
                        expected_result=expected_result, actual_result=actual_result
                    )
                    list_status.append('Fail')
                    self.login_page.click_logout_button()

            elif actual_result != expected_result:
                if self.expected_result == 'Pass':
                    CustomLogs.log_test_result(
                        self.logger, test_case_id, 'FAILED PARTIALLY',
                        expected_result=expected_result, actual_result=actual_result
                    )
                    list_status.append('Fail')

                elif self.expected_result == 'Fail':
                    CustomLogs.log_test_result(
                        self.logger, test_case_id, 'PASSED PARTIALLY',
                        expected_result=expected_result, actual_result=actual_result
                    )
                    list_status.append('Pass')

        if 'Fail' not in list_status:
            CustomLogs.log_test_result(
                self.logger, test_case_id, 'PASSED',
                expected_result='Pass', actual_result='Pass'
            )
            assert True
        else:
            CustomLogs.log_test_result(
                self.logger, test_case_id, 'FAILED',
                expected_result='Pass', actual_result='Fail'
            )
            assert False
