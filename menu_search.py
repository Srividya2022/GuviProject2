from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest
from selenium.webdriver.common.keys import Keys

from GuviOrangeHrmProject.PageObjects.loginpage_elements import LoginPageElements
from GuviOrangeHrmProject.PageObjects.menu_search_elements import MenuSearchElements



class MenuSearchTest(unittest.TestCase):
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


    #Validate the search textbox is displaying on the Admin Home page
    def test_search_box_display(self):
        driver =self.driver
        search = MenuSearchElements(driver)
        search_textbox = search.sidebar_search_displayed()
        if search_textbox.is_displayed():
            print("Search textbox is displaying on the Home page")
        else:
            print("Search textbox is not displaying on the Home page")

    # Validate the Menu options on the side pane are displaying on the Admin Page
    def test_menu_options(self):
        driver=self.driver
        menu_list = MenuSearchElements(driver)
        menu_list.menu_element_list()
        expected_menu_list =['Admin','PIM','Leave','Time','Recruitment','My Info','Performance','Dashboard','Directory','Maintenance','Buzz']
        actual_menu_list =[]
        for item in menu_list.menu_element_list():
            actual_menu_list.append(item.text)
        assert expected_menu_list ==actual_menu_list
        print(actual_menu_list )
        print("Menu options are displaying on the Admin Page")

    def test_search_by_lowercase(self):
        driver = self.driver
        s = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        expected_menu_list1 = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard',
                               'Directory', 'Maintenance', 'Buzz']

        for item in expected_menu_list1:
            s.send_keys(item.lower())
            assert driver.find_element(By.XPATH, "//ul[@class ='oxd-main-menu']/li/a/span").text == item
            s.send_keys(Keys.CONTROL + 'A', Keys.BACKSPACE)
        print("search menu in lower case")

    def test_search_by_uppercase(self):
        driver = self.driver
        s = driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        expected_menu_list1 = ['Admin', 'PIM', 'Leave', 'Time', 'Recruitment', 'My Info', 'Performance', 'Dashboard',
                               'Directory', 'Maintenance', 'Buzz']
        for item in expected_menu_list1:
            s.send_keys(item.upper())
            assert driver.find_element(By.XPATH, "//ul[@class ='oxd-main-menu']/li/a/span").text == item
            s.send_keys(Keys.CONTROL + 'a', Keys.BACKSPACE)
        print("search menu in upper case")
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")

