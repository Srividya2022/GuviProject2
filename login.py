import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import unittest
from GuviOrangeHrmProject.PageObjects.loginpage_elements import LoginPageElements


class LoginTest(unittest.TestCase):
    driver = None
    cwd = os.getcwd()
    json_test_data_file_path ='%s%s' % (cwd,'\\TestData\\test_data.json')
    with open(json_test_data_file_path) as json_file:
         data_dict = json.load(json_file)
    print(data_dict)

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print("Application launched successfully")
        cls.driver.maximize_window()

    def test_invalid_password_login(self):
        driver = self.driver
        invalid_login = LoginPageElements(driver)
        username = self.data_dict.get('login_test_data').get('valid_username')
        invalid_login.enter_username(username)
        invalid_password = self.data_dict.get('login_test_data').get('invalid_password')
        invalid_login.enter_password(invalid_password)
        invalid_login.click_login()
        webpage_message = invalid_login.invalid_credential()
        assert webpage_message == 'Invalid credentials'

    def test_invalid_user_login(self):
        driver = self.driver
        invalid_login = LoginPageElements(driver)
        invalid_username = self.data_dict.get('login_test_data').get('invalid_username')
        invalid_login.enter_username(invalid_username)
        password = self.data_dict.get('login_test_data').get('valid_password')
        invalid_login.enter_password(password)
        invalid_login.click_login()
        webpage_message = invalid_login.invalid_credential()
        assert webpage_message == 'Invalid credentials'

    def test_valid_login(self):
        driver = self.driver
        valid_login = LoginPageElements(driver)
        username = self.data_dict.get('login_test_data').get('valid_username')
        valid_login.enter_username(username)
        password = self.data_dict.get('login_test_data').get('valid_password')
        valid_login.enter_password(password)
        valid_login.click_login()
        check_dashboard = driver.find_element(By.XPATH,"//h6[text()= 'Dashboard']").text
        assert check_dashboard == "Dashboard"
        print("Login pass")

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

