from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Define a class for the login page
class LoginPage:
    # Define class-level variables to store element identifiers
    text_box_username_id = "Email"  # ID of the username input field
    text_box_password_id = "Password"  # ID of the password input field
    button_login_xpath = "//button[contains(text(),'Log in')]"  # XPath for the login button
    button_logout_linktext = "Logout"  # Link text for the logout button

    # Constructor method that initializes the class with a Selenium WebDriver instance
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # 10 seconds wait time

    # Method to set the username in the username input field
    def set_username(self, username):
        # Wait for the username input to be visible
        username_input = self.wait.until(EC.visibility_of_element_located((By.ID, self.text_box_username_id)))
        # Clear any existing text in the username input field
        username_input.clear()
        # Enter the provided username in the username input field
        username_input.send_keys(username)

    # Method to set the password in the password input field
    def set_password(self, password):
        # Wait for the password input to be visible
        password_input = self.wait.until(EC.visibility_of_element_located((By.ID, self.text_box_password_id)))
        # Clear any existing text in the password input field
        password_input.clear()
        # Enter the provided password in the password input field
        password_input.send_keys(password)

    # Method to click the login button
    def click_login_button(self):
        # Wait for the login button to be clickable
        login_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, self.button_login_xpath)))
        # Locate the login button using the defined XPath and click it
        login_button.click()

    # Method to click the logout button
    def click_logout_button(self):
        # Wait for the logout button to be clickable
        logout_button = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, self.button_logout_linktext)))
        # Locate the logout button by its link text and click it
        logout_button.click()
