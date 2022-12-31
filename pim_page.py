import json
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import unittest
from GuviOrangeHrmProject.PageObjects.loginpage_elements import LoginPageElements
from GuviOrangeHrmProject.PageObjects.pim_emp_page_elements import EmployeePageElements
import time



class PimTest(unittest.TestCase):
    driver = None
    # cwd = os.getcwd()
    # json_test_data_file_path = '%s%s' % (cwd, '\\TestData\\test_data.json')
    # with open(json_test_data_file_path) as json_file:
    #     data_dict = json.load(json_file)
    @classmethod
    def setUpClass(cls):
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

#create new user in PIM and user should see employee list page after the creation of the user
    def test_new_user(self):
        driver = self.driver
        employee_add = EmployeePageElements(driver)
        employee_add.pim_click()
        employee_add.emp_list_click()
        # first_name = self.data_dict.get('pim_test_data').get('firstname1')
        firstname = 'first1'
        lastname = 'Last1'
        employee_add.add_employee(firstname, lastname)
        expected_text = firstname + ' ' + lastname
        time.sleep(2)

        employee_add.toggle_logindetail()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(
            (By.XPATH, "//label[contains(text(), 'Username')]/parent::div/following-sibling::div/input")))
        #driver.find_element(By.XPATH,"//label[contains(text(),'Username')]/../following-sibling::div")

        employee_add.click_newuser_textbox('Users1_2', 'Users1_2','Users1_2')
        expected_text = firstname + ' ' + lastname
        employee_add.click_newuser_textbox('Users1_2', 'Users1_2','Users1_2')

        employee_add.emp_save_button_click()
        assert WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, "//div[@class='orangehrm-edit-employee-name']/h6"), expected_text))

        print("new user created ")

# Validate for all the tab list present in the Employee list page
    def test_tabs_employeelist(self):
        driver = self.driver
       # driver.find_element(By.XPATH, "//span[text()= 'PIM']").click()
       # driver.find_element(By.XPATH,"//a[contains(text(),'Employee List')]")
        tab_list = EmployeePageElements(driver)

        tab_list.employee_tab_list()
        expected_tab_list = ['Personal Details', 'Contact Details', 'Emergency Contacts', 'Dependents', 'Immigration',
                             'Job', 'Salary', 'Tax Exemptions',
                              'Report-to', 'Qualifications', 'Memberships']
        actual_tab_list = []
        for item in tab_list.employee_tab_list():
            actual_tab_list.append(item.text)
            print(item.text)
        assert expected_tab_list == actual_tab_list
        print(actual_tab_list)
        print("Tab lists  are displaying on the Employee List Page")

##validate Personal details
    def test_personal_details(self):
        driver = self.driver
        personal_details = EmployeePageElements(driver)
        personal_details.click_personal_detail_tab()
        personal_details.enter_driver_licence("1234567890XYZ")
        personal_details.enter_licence_expiry_date("2023-01-01")
        personal_details.enter_SSN_number("1234567")
        personal_details.enter_SIN_number("1234560")
        WebDriverWait(self.driver, 10).until(
             expected_conditions.presence_of_element_located((By.XPATH,"//label[contains(text(),'License Number')]/parent::div/following-sibling::div/input")))
        personal_details.enter_driver_licence("1234567890XYZ")
        WebDriverWait(self.driver, 10).until(
             expected_conditions.presence_of_element_located((By.XPATH,"//label[text()='Nationality']/../following-sibling::div/div/div/div[@class ='oxd-select-text-input']")))
        personal_details.select_nationality("Indian")

        WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, "//label[text()='Marital Status']/../following-sibling::div/div/div/div[@class ='oxd-select-text-input']")))
        personal_details.select_marital_status("Married")
        personal_details.enter_DOB("2000-01-01")
        personal_details.enter_gender("Female")
        personal_details.enter_military("12323232")
        personal_details.emp_save_button_click()

        ##validate contact details
    def test_contact_details(self):
        driver = self.driver
        contact_details = EmployeePageElements(driver)
        contact_details.click_contact_detail_tab()
        contact_details.enter_street1("Lake view road")
        contact_details.enter_city("Bangalore")
        contact_details.enter_state("KA")
        contact_details.enter_zip_code("560001")
        contact_details.select_country("Bangalore")
        contact_details.enter_home_phone("1234567890")
        contact_details.enter_mobile_no("1234567890")
        contact_details.enter_work_phone("1234567890")
        contact_details.enter_work_email("a@a.com")
        contact_details.emp_save_button_click()

    ##validate emergency contacts
    def test_emergency_contact(self):
        driver = self.driver
        emergency_contact = EmployeePageElements(driver)
        emergency_contact.emergency_contact_add_click()
        emergency_contact.emergency_contact_name_enter("name1")
        emergency_contact.emergency_contact_relationship_enter("friend")
        emergency_contact.emergency_contact_home_telephone_enter("1234567890")
        emergency_contact.emergency_contact_save()

    ##validate dependents
    def test_dependents(self):
        driver = self.driver
        dependents = EmployeePageElements(driver)
        dependents.dependents_add_click()
        dependents.dependents_name_enter("name1")
        dependents.dependents_relationship_enter("child")
        dependents.dependents_DOB_enter("2023-01-01")
        dependents.dependents_save()



    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
        print("Test Completed")


