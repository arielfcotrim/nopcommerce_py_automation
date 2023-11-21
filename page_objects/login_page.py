class LoginPage:
    text_box_username_id = "Email"
    text_box_password_id = "Password"
    button_login_xpath = "//input[@value='Log in']"
    link_logout_button = "Logout"

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element_by_id(self.text_box_username_id).clear()
        self.driver.find_element_by_id(self.text_box_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_id(self.text_box_password_id).clear()
        self.driver.find_element_by_id(self.text_box_password_id).send_keys(password)

    def click_login_button(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def click_logout_button(self):
        self.driver.find_element_by_link_text(self.link_logout_button).click()
