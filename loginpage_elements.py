import self
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginPageElements:

    def __init__(self,driver):
        self.driver = driver

        self.username_textbox_name = "username"
        self.password_textbox_name = "password"
        self.login_button_xpath = "//button[@type ='submit']"
        self.invalid_credential_text_xpath = "//p[text()= 'Invalid credentials']"
        self.forgot_password_link_xpath = "//p[text()= 'Forgot your password? ']"

    def enter_username(self,username):
        self.driver.find_element(By.NAME, self.username_textbox_name).clear()
        self.driver.find_element(By.NAME, self.username_textbox_name).send_keys(username)

    def enter_password(self,password):
        self.driver.find_element(By.NAME, self.password_textbox_name).clear()
        self.driver.find_element(By.NAME,self.password_textbox_name).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def invalid_credential(self):
        msg = self.driver.find_element(By.XPATH, self.invalid_credential_text_xpath).text
        return msg

