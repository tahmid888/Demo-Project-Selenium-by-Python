import time

from selenium.webdriver.common.by import By


class Login_Admin_Page:
    textbox_username_id = "formEmail"
    textbox_password_id = "formPassword"
    btn_login_xpath = "//button[normalize-space()='Login']"
    account_text_xpath = "//span[normalize-space()='Account']"
    logout_xpath = "//button[normalize-space()='Logout']"
    login_xpath = "//*[normalize-space()='Log in']"


    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def click_logout(self):
        self.driver.find_element(By.XPATH, self.account_text_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.logout_xpath).click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, self.login_xpath).click()
        time.sleep(5)
