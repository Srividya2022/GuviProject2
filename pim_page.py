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
    def test_employee_job_details_page(self):
        driver = self.driver
        employee_job_details_page = EmployeePageElements(driver)
        employee_job_details_page.click_employee_job_details()
        employee_job_details_page.enter_joint_date("2022-02-02")
        employee_job_details_page.select_job_title_dropdown("QA Lead")
        employee_job_details_page.select_job_category_dropdown("Professionals")
        employee_job_details_page.select_sub_unit_dropdown("Quality Assurance")
        employee_job_details_page.select_location_dropdown("New York Sales Office")
        employee_job_details_page.select_employment_status_dropdown("Full-Time Permanent")
        employee_job_details_page.click_employee_contract_toggle_button()
        employee_job_details_page.enter_employee_contract_start_end_date("2023-01-01", "2023-12-12")
        employee_job_details_page.job_save()


    def test_validate_employee_job_details_termination_page(self):
        driver = self.driver
        termination_and_activation_page = EmployeePageElements(driver)
        termination_and_activation_page.click_employee_termination_and_activation_button()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                        ((By.XPATH, "//label[contains(text(),'TerminationDate')]/parent::div/" \
                                          "following-sibling::div//div/div/input ")))
        termination_and_activation_page.enter_employee_termination_date("2023-05-05")
        termination_and_activation_page.select_employee_termination_reason_dropdown("Contract Not Renewed")
        termination_and_activation_page.click_employee_required_save()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, "//h6[text()='Employee Termination / Activiation']/following-sibling::button"), "Activate Employment"))
        visible_activation_button = driver.find_element(By.XPATH,"//h6[text()='Employee Termination / Activiation']" \
                                                    " /following-sibling::button").text

        assert visible_activation_button == "Activate Employment"

    def test_activation_employment_page(self):
        driver = self.driver
        activation_employment = EmployeePageElements(driver)
        activation_employment.click_employee_termination_and_activation_button()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH,"//h6[text()='Employee Termination / Activiation']/following-sibling::button"), "Terminate Employment"))
        visible_terminate_employment_button = driver.find_element(By.XPATH,"//h6[text()='Employee Termination / Activiation']" \
                                                                  "/following-sibling::button") .text
        assert visible_terminate_employment_button == "Terminate Employment"

    def test_validate_employee_salary_page(self):
        driver = self.driver
        employee_salary_page = EmployeePageElements(driver)
        employee_salary_page.click_employee_salary_component_tap()
        employee_salary_page.click_assigned_salary_component()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, "//h6[text()=' Add Salary Component ']"), "Add Salary Component"))
        employee_salary_page.enter_employee_salary_component("XXX")
        employee_salary_page.select_pay_grade_dropdown("Grade 1")
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                        ((By.XPATH,"//label[text()='Currency']/../following-sibling::div/div" \
                                         "//following-sibling::div ")))
        employee_salary_page.select_pay_frequency_dropdown("Monthly")
        employee_salary_page.select_currency_dropdown("Indian Rupee")
        employee_salary_page.enter_employee_salary_amount("5000")
        employee_salary_page.click_direct_deposit_details_toggle_button()
        employee_salary_page.enter_bank_account_number("AC-123456789")
        employee_salary_page.select_bank_account_type_dropdown("Savings")
        employee_salary_page.enter_bank_routing_number("123456789")
        employee_salary_page.enter_deposit_amount("5000")
        employee_salary_page.click_employee_required_save()
        WebDriverWait(driver, 10).until(expected_conditions.text_to_be_present_in_element(
            (By.XPATH, "//div[text()='Salary Component']"), "Salary Component"))
        record_found = driver.find_element(By.XPATH, "//div[text()='Salary Component']")
        assert record_found.text == "Salary Component"

    def test_11_validate_tax_exemptions_page(self):  # Test Case ID TC_PIM_13
        driver = self.driver
        tax_exemptions_page = EmployeePageElements(driver)
        tax_exemptions_page.click_employee_stax_exemptions_tap()
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located
                                        ((By.XPATH,"//label[text()='Unemployment " \
                                                      "State']/../../../preceding-sibling::div[2]/div/div/div/*/*/* ")))
        tax_exemptions_page.select_federal_income_tax_status_dropdown("Married")
        tax_exemptions_page.select_state_income_tax_state_dropdown("Alaska")
        tax_exemptions_page.select_state_income_tax_status_dropdown("Married")
        tax_exemptions_page.select_state_income_tax_unemployment_state_dropdown("Alabama")
        tax_exemptions_page.select_state_income_tax_work_state_dropdown("Alabama")
        tax_exemptions_page.click_save_button()

