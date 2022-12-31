import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import unittest

from GuviOrangeHrmProject.PageObjects.loginpage_elements import LoginPageElements
from GuviOrangeHrmProject.PageObjects.adminpage_elements import AdminPageElements

class AdminTest(unittest.TestCase):
    driver = None


    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        print("Application launched successfully")
        cls.driver.maximize_window()

        driver = cls.driver
        valid_login = LoginPageElements(driver)
        valid_login.enter_username("Admin")
        valid_login.enter_password("admin123")
        valid_login.click_login()
        print("login pass")


    #validate uer role and status dropdown values in the User management in Admin module
    def test_admin_user_management(self):
        driver = self.driver
        admin_user_management = AdminPageElements(driver)
        admin_user_management.click_admin()
        admin_user_management.click_user_management()
        admin_user_management.click_user()
        user_role_list = admin_user_management.click_user_role_dropdown()
        expected_user_role_list = ["-- Select --", "Admin", "ESS"]
        actual_user_role_list = []
        for list_of_item in user_role_list:
            actual_user_role_list.append(list_of_item.text)
        assert expected_user_role_list == actual_user_role_list
        print("User role list:")
        print(actual_user_role_list)
        status_list = admin_user_management.click_status_dropdown()
        expected_status_list = ["-- Select --", "Enabled", "Disabled"]
        actual_status_list = []
        for list_of_item in status_list:
            actual_status_list.append(list_of_item.text)
        assert expected_status_list == actual_status_list
        print("Status list:")
        print(actual_status_list)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

