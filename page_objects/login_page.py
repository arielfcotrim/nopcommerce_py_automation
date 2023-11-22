from selenium.webdriver.common.by import By


# Define a class for the login page
class LogInPage:
    # Define class-level variables to store element identifiers
    text_box_username_id = "Email"  # ID of the username input field
    text_box_password_id = "Password"  # ID of the password input field
    button_login_xpath = "//button[contains(text(),'Log in')]"  # XPath for the login button
    button_logout_linktext = "Logout"  # Link text for the logout button

    # Constructor method that initializes the class with a Selenium WebDriver instance
    def __init__(self, driver):
        self.driver = driver

    # Method to set the username in the username input field
    def set_username(self, username):
        # Clear any existing text in the username input field
        self.driver.find_element(By.ID, self.text_box_username_id).clear()
        # Enter the provided username in the username input field
        self.driver.find_element(By.ID, self.text_box_username_id).send_keys(username)

    # Method to set the password in the password input field
    def set_password(self, password):
        # Clear any existing text in the password input field
        self.driver.find_element(By.ID, self.text_box_password_id).clear()
        # Enter the provided password in the password input field
        self.driver.find_element(By.ID, self.text_box_password_id).send_keys()

    # Method to click the login button
    def click_login_button(self):
        # Locate the login button using the defined XPath and click it
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()

    # Method to click the logout button
    def click_logout_button(self):
        # Locate the logout button by its link text and click it
        self.driver.find_element(By.LINK_TEXT, self.button_logout_linktext).click()
