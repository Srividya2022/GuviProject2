import self
from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

class EmployeePageElements:

    def __init__(self,driver):
        self.driver = driver
        self.pim_element_xpath = "//span[text()= 'PIM']"
        self.employpee_list_xpath = "//a[contains(text(),'Employee List')]"
        self.add_employee_tab_xpath = "//a[text() = 'Add Employee']"
        self.add_employee_button_xpath = "//button[normalize-space() = 'Add']"
        self.firstname_textbox_xpath = "//input[@name ='firstName']"
        self.lastname_textbox_xpath = "//input[@name ='lastName']"
        self.upload_image_xpath = "//button[contains(@class,'employee-image-action')]"
        self.toggle_login_detail_xpath = "//div[@class ='oxd-switch-wrapper']"
        self.newuser_xpath ="//label[contains(text(), 'Username')]/parent::div/following-sibling::div/input"
        self.newpassword_xpath = "//input[@type ='password']"
        self.confirmed_password_xpath ="//label[contains(text(), 'Confirm Password')]/parent::div/following-sibling::div/input"
        self.employee_tablist_xpath = "//div[@role ='tablist']/div/a"
        self.empsave_button_xpath = "//button[@type='submit']"
        #edit_image_xpath = "//button[2]/i"
        empid = "0038"
        self.edit_image_xpath = "//div[@role ='table']//div[contains(text(),'0038')]/../following-sibling::div[7]/div/button[2]"
        self.edit_Emp_firstname_textbox_xpath = "//input[@name ='firstName']"
        self.edit_Emp_lastname_textbox_xpath = "//input[@name ='lastName']"
        self.edit_emp_save_xpath = "//button[@type='submit']"
        self.delete_button_xpath ="//div[@role ='table']//div[contains(text(),'0038')]/../following-sibling::div[7]" \
                                  "/div/button[1]"
        self.delete_success_msg_xpath = "//button[contains(.,' Yes, Delete')]"
        #self.upload_image_xpath = "//button[@class ='oxd-icon-button employee-image-action']"
        #self.upload_image_xpath = "//img[@class ='employee-image']"

#===============personal details elements============
        self.personal_detail_tab_xpath = "//a[contains(text(), 'Personal Details')]"
        self.emp_middle_name_xpath = "//input[@placeholder ='Middle Name']"
        self.employee_id_xpath = "//label[contains(text(),'Employee Id')]/parent::div/following-sibling::div/input"
        self.Employee_other_id_xpath = "//label[contains(text(), 'Other Id')]/parent::div/following-sibling::div/input"
        self.driver_license_no_xpath = "//label[contains(text(),'License Number')]/parent::div/following-sibling::div/input"
        self.license_expiry_xpath = "//label[contains(text(),'License Expiry Date')]/parent::div/following-sibling::div"\
                                    "//div/div/input "
        self.SSN_number_xpath = "//label[text()='SSN Number']/../following-sibling::div/input"
        self.SIN_number_xpath = "//label[text()='SIN Number']/../following-sibling::div/input"
        self.nationality_button_xpath = "//label[text()='Nationality']/../following-sibling::div/div//following-sibling::div"
        self.nationality_text_xpath = "//label[text()='Nationality']/../following-sibling::div/div/div/" \
                "div[@class ='oxd-select-text-input']"
        self.nationality_list_xpath = "//div[@role='option']"
        self.marital_status_button_xpath = "//label[text()='Marital Status']/../following-sibling::div/div//following-sibling::div"
        self.marital_status_text_xpath = "//label[text()='Marital Status']/../following-sibling::div/div/div/" \
                                         "div[@class ='oxd-select-text-input']"
        self.marital_status_list_xpath = "//div[@role='option']"
        self.date_of_brith_xpath = "//label[contains(text(),'Date of Birth')]/parent::div/following-sibling::div//div/div/input "
        self.gender_male_xpath = "//input[@value='1']/following-sibling::span"
        self.gender_female_xpath = "//input[@value='2']/following-sibling::span"
        self.military_service_xpath ="//label[contains(text(), 'Military Service')]/parent::div/following-sibling::div/input"
        self.custom_field_save_xpath = "//label[text()='Blood Type']/../../../../../following-sibling::div/button"
        self.employee_full_name_xpath = "//label[text()='Employee Name']/../following-sibling::div/div/div/input"
        self.employee_list_present_elements_xpath = "//div[@role='tab']/a"
        self.blood_type_button_xpath = "//label[text()='Blood Type']/../following-sibling::div/div//following-sibling::div"
        self.blood_type_xpath = "//label[text()='Blood Type']/../following-sibling::div/div/div/div[@class " \
                           "='oxd-select-text-input'] "
        self.blood_type_list_xpath = "//div[@role='option']"
        self.custom_field_save_xpath = "//label[text()='Blood Type']/../../../../../following-sibling::div/button"
        #=============Contact details==============================
        self.employee_contact_details_tap_xpath = "//a[text()='Contact Details']"
        self.street_1_input_box_xpath = "//label[text()='Street 1']/../following-sibling::div/input"
        self.city_input_box_xpath = "//label[text()='City']/../following-sibling::div/input"
        self.state_province_input_box_xpath = "//label[text()='State/Province']/../following-sibling::div/input"
        self.zip_code_input_box_xpath = "//label[text()='Zip/Postal Code']/../following-sibling::div/input"
        self.country_button_xpath = "//label[text()='Country']/../following-sibling::div/div//following-sibling::div"
        self.country_type_list_xpath = "//div[@role='option']"
        self.home_phone_no_xpath = "//label[text()='Home']/../following-sibling::div/input"
        self.mobile_no_xpath = "//label[text()='Mobile']/../following-sibling::div/input"
        self.work_phone_no_xpath = "//label[text()='Work']/../following-sibling::div/input"
        self.work_email_id_xpath = "//label[text()='Work Email']/../following-sibling::div/input"

#==============================Emergency Contacts===========================
        self.emergency_contact_tab_xpath = "// a[contains(text(), 'Emergency Contacts')]"
        self.emergency_contact_add_xpath ="//div[@class = 'orangehrm-action-header']/h6/../../div/button"
        self.emergency_contact_name_xpath = "//label[text()='Name']/../following-sibling::div/input"
        self.emergency_contact_relationship_xpath = "//label[text()='Relationship']/../following-sibling::div/input"
        self.emergency_contact_home_phone_xpath = "//label[text()='Home Telephone']/../following-sibling::div/input"
        self.emergency_contact_save_xpath = "//button[@type='submit']"
        self.emergency_relationship_dropdown_button_xpath = "//label[text()='Relationship']/../following-sibling::div/div/" \
                                             "/following-sibling::div"
        self.emergency_relationship_dropdown_list_XPATH = "//div[@role='option']"


        # ==============================Dependents===========================
        self.dependents_tab_xpath = "// a[contains(text(), 'Dependents')]"
        self.dependents_add_xpath = "//div[@class = 'orangehrm-action-header']/h6/../../div/button"
        self.dependents_name_xpath = "//label[text()='Name']/../following-sibling::div/input"
        self.dependents_relationship_button_xpath ="// label[text() = 'Relationship']/../following-sibling::div/div/div"
        self.dependents_relationship_xpath = "// label[text() = 'Relationship']/../following-sibling::div/div/div/" \
                "div[@class ='oxd-select-text-input']"
        self.dependents_DOB_xpath = "//label[contains(text(),'Date of Birth')]/parent::div/following-sibling::div//div/div/input"
        self.dependents_save_xpath = "//button[@type='submit']"

        # ==============================Job===========================
        self.employee_job_details_tap_xpath = "//a[text()='Job']"
        self.employee_join_date_xpath = "//label[contains(text(),'Joined Date')]/parent::div/following-sibling::div/" \
                                   "/div/div/input "
        self.employee_job_title_dropdown_button_xpath = "//label[text()='Job Title']/../following-sibling::div/div" \
                                                   "//following-sibling::div"
        self.employee_job_title_dropdown_list_xpath = "//div[@role='option']"
        self.employee_job_category_dropdown_button_xpath = "//label[text()='Job Category']/../following-sibling::div/div" \
                                                      "//following-sibling::div"
        self.employee_job_category_dropdown_list_xpath = "//div[@role='option']"
        self.employee_sub_unit_dropdown_button_xpath = "//label[text()='Sub Unit']/../following-sibling::div/div/" \
                                                  "/following-sibling::div"
        self.employee_sub_unit_dropdown_list_xpath = "//div[@role='option']"
        self.employee_location_dropdown_button_xpath = "//label[text()='Location']/../following-sibling::div/div/" \
                                                  "/following-sibling::div"
        self.employee_location_dropdown_list_xpath = "//div[@role='option']"
        self.employment_status_dropdown_button_xpath = "//label[text()='Employment Status']/../following-sibling::" \
                                                  "div/div//following-sibling::div"
        self.employment_status_dropdown_list_xpath = "//div[@role='option']"
        self.employee_contract_details_toggle_button_xpath = "//p[text()='Include Employment Contract Details']" \
                                                        "/following-sibling::div/label/span"
        self.employee_contract_start_date_xpath = "//label[contains(text(),'Contract Start Date')]/parent::div/" \
                                             "following-sibling::div//div/div/input "
        self.employee_contract_end_date_xpath = "//label[contains(text(),'Contract End Date')]/parent::div/" \
                                           "following-sibling::div//div/div/input "

        self.terminate_employment_and_activation_xpath = "//h6[text()='Employee Termination / Activiation']" \
                                                    "/following-sibling::button"
        self.termination_date_xpath = "//label[contains(text(),'Termination " \
                                 "Date')]/parent::div/following-sibling::div//div/div/input "
        self.termination_reason_dropdown_button_xpath = "//label[text()='Termination " \
                                                   "Reason']/../following-sibling::div/div//following-sibling::div "
        self.termination_reason_dropdown_list_xpath = "//div[@role='option']"
        self.required_save_button = "//p[text()=' * Required']/following-sibling::button[@type='submit']"
        self.job_save_xpath = "//button[@type='submit']"
        # ==============================Salary===========================
        self.employee_salary_tap_xpath = "//a[text()='Salary']"
        self.employee_salary_components_add_button_xpath = "//h6[text()='Assigned Salary Components']/following-sibling::button"
        self.employee_salary_component_input_box_xpath = "//label[text()='Salary Component']/../following-sibling::div/input"
        self.employee_pay_grade_dropdown_button_xpath = "//label[text()='Pay Grade']/../following-sibling::div/div" \
                                                   "//following-sibling::div "
        self.employee_pay_grade_list_xpath = "//div[@role='option']"
        self.employee_pay_frequency_dropdown_button_xpath = "//label[text()='Pay Frequency']/../following-sibling::div/div" \
                                                       "//following-sibling::div "
        self.employee_pay_frequency_list_xpath = "//div[@role='option']"
        self.currency_dropdown_button_xpath = "//label[text()='Currency']/../following-sibling::div/div" \
                                         "//following-sibling::div "
        self.currency_list_xpath = "//div[@role='option']"
        self.salary_amount_input_box_xpath = "//label[text()='Amount']/../following-sibling::div/input"
        self.bank_account_number_input_box_xpath = "//label[text()='Account Number']/../following-sibling::div/input"
        self.bank_account_type_dropdown_button_xpath = "//label[text()='Account Type']/../following-sibling::div/div" \
                                                  "//following-sibling::div "
        self.bank_account_type_list_xpath = "//div[@role='option']"
        self.bank_account_routing_number_input_box_xpath = "//label[text()='Routing Number']/../following-sibling::div/input"
        self.deposit_amount_input_box_xpath = "//label[text()='Routing Number']/../../.././following-sibling::div/div" \
                                         "/*/following-sibling::div/input "
        self.direct_deposit_details_toggle_button_xpath = "//p[text()='Include Direct Deposit Details']" \
                                                     "/following-sibling::div/label/span"
        self.visible_salary_component_xpath = "//div[text()='Salary Component']"
        self.federal_income_tax_status_dropdown_button_xpath = "//h6[text()='State Income " \
                                                          "Tax']/preceding-sibling::div/div/*/*/div/div/*/*/* "
        self.federal_income_tax_status_list_xpath = "//div[@role='option']"
        self.state_income_tax_status_dropdown_button_xpath = "//label[text()='Unemployment " \
                                                        "State']/../../../preceding-sibling::div[2]/div/div/div/*/*/* "
        self.state_income_tax_status_list_xpath = "//div[@role='option']"

        self.state_income_tax_state_dropdown_button_xpath = "//label[text()='State']/../following-sibling::div/*/*/*/*"
        self.state_income_tax_state_list_xpath = "//div[@role='option']"
        self.state_income_tax_unemployment_state_dropdown_button_xpath = "//label[text()='Unemployment " \
                                                                    "State']/../following-sibling::div/*/*/*/* "
        self.state_income_tax_unemployment_state_list_xpath = "//div[@role='option']"
        self.state_income_tax_work_state_dropdown_button_xpath = "//label[text()='Work State']/../following-sibling::div" \
                                                            "/*/*/*/* "
        self.state_income_tax_work_state_list_xpath = "//div[@role='option']"
        self.employee_tax_exemptions_tap_xpath = "//a[text()='Tax Exemptions']"



    #=======================================================================
    def pim_click(self):
        self.driver.find_element(By.XPATH,self.pim_element_xpath).click()
    def emp_list_click(self):
        self.driver.find_element(By.XPATH,self.employpee_list_xpath).click()
    def add_emp_tab_click(self):
        self.driver.find_element(By.XPATH,self.add_employee_tab_xpath).click()
    def click_add_button(self):
        self.driver.find_element(By.XPATH,self.add_employee_button_xpath).click()
    def add_employee(self, addfirstname, addlastname):
        self.driver.find_element(By.XPATH,self.add_employee_button_xpath).click()
        self.driver.find_element(By.XPATH, self.firstname_textbox_xpath).send_keys(addfirstname)
        self.driver.find_element(By.XPATH, self.lastname_textbox_xpath).send_keys(addlastname)
    def upload_image(self):
        self.driver.find_element(By.XPATH, self.upload_image_xpath).click()
        time.sleep(5)
        os.startfile("C:\\Users\\lenovo\\Desktop\\upload_image.exe")
       # self.driver.find_element(By.XPATH, self.upload_image_xpath).send_keys("D:/Downloads/1.png")
    def toggle_logindetail(self):
        self.driver.find_element(By.XPATH, self.toggle_login_detail_xpath).click()
    def username_textbox(self):
        self.driver.find_element(By.XPATH, self.newuser_xpath)
    def click_newuser_textbox(self,newusername,newpassword,confirmedpassword):
        #self.driver.find_element(By.XPATH, self.newuser_xpath).click()
        self.driver.find_element(By.XPATH, self.newuser_xpath).send_keys(newusername)
        #self.driver.find_element(By.XPATH, self.newpassword_xpath).click()
        self.driver.find_element(By.XPATH, self.newpassword_xpath).send_keys(newpassword)
        self.driver.find_element(By.XPATH, self.confirmed_password_xpath).send_keys(confirmedpassword)
    def employee_tab_list(self):
        a = self.driver.find_elements(By.XPATH, self.employee_tablist_xpath)
        return a
    def emp_save_button_click(self):
        self.driver.find_element(By.XPATH,self.empsave_button_xpath).click()
    def edit_image_click(self):
        self.driver.find_element(By.XPATH, self.edit_image_xpath).click()


    def edit_empfirstname_enter(self,editusername):
        self.driver.find_element(By.XPATH, self.edit_Emp_firstname_textbox_xpath).send_keys(editusername)
    def edit_emplastname_enter(self,editlastname):
        self.driver.find_element(By.XPATH, self.edit_Emp_lastname_textbox_xpath).send_keys(editlastname)
    def edit_emp_save_click(self):
        self.driver.find_element(By.XPATH, self.edit_emp_save_xpath).click()

    def delete_click(self):
        delete_emp_element = self.driver.find_element(By.XPATH, self.delete_button_xpath).click()
    def delete_emp_successmsg(self):
        delete_emp_success_element = self.driver.find_element(By.XPATH, self.delete_success_msg_xpath)


############PERSONAL DETAILS##################
    def click_personal_detail_tab(self):
        self.driver.find_element(By.XPATH,self.personal_detail_tab_xpath).click()
    def enter_driver_licence(self,driver_licence):
        #self.driver.find_element(By.XPATH,self.driver_license_no_xpath).click()
        self.driver.find_element(By.XPATH,self.driver_license_no_xpath).send_keys(driver_licence)
    def enter_licence_expiry_date(self,licence_expiry_date):
        self.driver.find_element(By.XPATH,self.license_expiry_xpath).send_keys(licence_expiry_date)
    def enter_SSN_number(self, SSN):
        self.driver.find_element(By.XPATH, self.SSN_number_xpath).send_keys(SSN)
    def enter_SIN_number(self, SIN):
        self.driver.find_element(By.XPATH, self.SIN_number_xpath).send_keys(SIN)
    def select_nationality(self,nationality):
        self.driver.find_element(By.XPATH, self.nationality_button_xpath).click()
        self.driver.find_element(By.XPATH, self.nationality_text_xpath).click()
        self.driver.find_element(By.XPATH, self.nationality_list_xpath).send_keys(nationality)
    def load_nationality(self):
        self.driver.find_element(By.XPATH, self.nationality_text_xpath).click()
    def select_marital_status(self, marital_status):
        self.driver.find_element(By.XPATH, self.marital_status_button_xpath).click()
        self.driver.find_element(By.XPATH, self.marital_status_text_xpath).click()
        self.driver.find_element(By.XPATH, self.marital_status_list_xpath).send_keys(marital_status)
    def enter_DOB(self, DOB):
        self.driver.find_element(By.XPATH, self.date_of_brith_xpath).send_keys(DOB)
    def enter_gender(self, gender):
        self.driver.find_element(By.XPATH, self.gender_female_xpath).send_keys(gender)
    def enter_military(self, military):
        self.driver.find_element(By.XPATH, self.military_service_xpath).send_keys(military)
    def click_custom_save(self, nationality):
        self.driver.find_element(By.XPATH, self.custom_field_save_xpath).click()



 #=============Contact details==============================
    def click_contact_detail_tab(self):
        self.driver.find_element(By.XPATH, self.employee_contact_details_tap_xpath).click()
    def enter_street1(self, street1):
        self.driver.find_element(By.XPATH, self.street_1_input_box_xpath).send_keys(street1)
    def enter_city(self, city):
        self.driver.find_element(By.XPATH, self.city_input_box_xpath).send_keys(city)
    def enter_state(self, state):
        self.driver.find_element(By.XPATH, self.state_province_input_box_xpath).send_keys(state)
    def enter_zip_code(self, zip_code):
        self.driver.find_element(By.XPATH, self.zip_code_input_box_xpath).send_keys(zip_code)
    def enter_home_phone(self, home_phone):
        self.driver.find_element(By.XPATH, self.home_phone_no_xpath).send_keys(home_phone)
    def enter_mobile_no(self, mobile_no):
        self.driver.find_element(By.XPATH, self.mobile_no_xpath).send_keys(mobile_no)
    def enter_work_phone(self, work_phone):
        self.driver.find_element(By.XPATH, self.work_phone_no_xpath).send_keys(work_phone)
    def enter_work_email(self, work_email):
        self.driver.find_element(By.XPATH, self.work_email_id_xpath).send_keys(work_email)
    def select_country(self, country):
        self.driver.find_element(By.XPATH, self.country_button_xpath).click()
        self.driver.find_element(By.XPATH, self.country_type_list_xpath).send_keys(country)

#==============================Emergency Contacts==========================
    def emergency_contact_tab_click(self):
        self.driver.find_element(By.XPATH,self.emergency_contact_tab_xpath).click()
    def emergency_contact_add_click(self):
        self.driver.find_element(By.XPATH,self.emergency_contact_add_xpath).click()
    def emergency_contact_name_enter(self,name):
        self.driver.find_element(By.XPATH, self.emergency_contact_name_xpath).send_keys(name)
    def emergency_contact_relationship_enter(self,relationship):
        self.driver.find_element(By.XPATH, self.emergency_contact_relationship_xpath).send_keys(relationship)
    def emergency_contact_home_telephone_enter(self, home_telephone):
        self.driver.find_element(By.XPATH, self.emergency_contact_home_phone_xpath).send_keys(home_telephone)
    def emergency_contact_save(self):
        self.driver.find_element(By.XPATH, self.emergency_contact_save_xpath).click()

    # ==============================dependents==========================
    def dependents_tab_click(self):
        self.driver.find_element(By.XPATH, self.dependents_tab_xpath).click()
    def dependents_add_click(self):
        self.driver.find_element(By.XPATH, self.dependents_add_xpath).click()
    def dependents_name_enter(self, name):
        self.driver.find_element(By.XPATH, self.emergency_contact_name_xpath).send_keys(name)
    def dependents_relationship_enter(self, relationship):
        self.driver.find_element(By.XPATH, self.dependents_relationship_button_xpath).click()
        self.driver.find_element(By.XPATH, self.dependents_relationship_xpath).send_keys(relationship)
    def dependents_DOB_enter(self, dob):
        self.driver.find_element(By.XPATH, self.dependents_DOB_xpath).send_keys(dob)
    def dependents_save(self):
        self.driver.find_element(By.XPATH, self.dependents_save_xpath).click()

    # ==============================Job==========================
    def job_tab_click(self):
        self.driver.find_element(By.XPATH, self.employee_job_details_tap_xpath).click()
    def enter_joint_date(self, join_date):
        self.driver.find_element(By.XPATH, self.employee_join_date_xpath).send_keys(join_date)

    def select_job_title_dropdown(self, job_title):
        self.driver.find_element(By.XPATH, self.employee_job_title_dropdown_button_xpath).click()
        job_title_dropdown_list = self.driver.find_elements(By.XPATH,self.employee_job_title_dropdown_list_xpath)
        for job_title_list in job_title_dropdown_list:
            if job_title == job_title_list.text:
                job_title_list.click()
                break

    def select_job_category_dropdown(self, job_category):
        self.driver.find_element(By.XPATH, self.employee_job_category_dropdown_button_xpath).click()
        job_category_dropdown_list = self.driver.find_elements(By.XPATH,self.employee_job_category_dropdown_list_xpath)
        for job_category_list in job_category_dropdown_list:
            if job_category == job_category_list.text:
                job_category_list.click()
                break

    def select_sub_unit_dropdown(self, sub_unit):
        self.driver.find_element(By.XPATH, self.employee_sub_unit_dropdown_button_xpath).click()
        sub_unit_dropdown_list = self.driver.find_elements(By.XPATH,self.employee_sub_unit_dropdown_list_xpath)
        for sub_unit_list in sub_unit_dropdown_list:
            if sub_unit == sub_unit_list.text:
                sub_unit_list.click()
                break

    def select_location_dropdown(self, location):
        self.driver.find_element(By.XPATH,self.employee_location_dropdown_button_xpath).click()
        location_dropdown_list = self.driver.find_elements(By.XPATH, self.employee_location_dropdown_list_xpath)
        for location_list in location_dropdown_list:
            if location == location_list.text:
                location_list.click()
                break

    def select_employment_status_dropdown(self, status):
        self.driver.find_element(By.XPATH,self.employment_status_dropdown_button_xpath).click()
        employment_status_dropdown_list = self.driver.find_elements(By.XPATH,self.employment_status_dropdown_list_xpath)
        for employment_status_list in employment_status_dropdown_list:
            if status == employment_status_list.text:
                employment_status_list.click()
                break

    def click_employee_contract_toggle_button(self):
        self.driver.find_element(By.XPATH, self.employee_contract_details_toggle_button_xpath).click()

    def enter_employee_contract_start_end_date(self, start_date, end_date):
        self.driver.find_element(By.XPATH, self.employee_contract_start_date_xpath).send_keys(start_date)
        self.driver.find_element(By.XPATH, self.employee_contract_end_date_xpath).send_keys(end_date)

    def click_employee_job_details(self):
        self.driver.find_element(By.XPATH, self.employee_job_details_tap_xpath).click()

    def click_employee_termination_and_activation_button(self):
        self.driver.find_element(By.XPATH, self.terminate_employment_and_activation_xpath).click()

    def enter_employee_termination_date(self, date):
        self.driver.find_element(By.XPATH, self.termination_date_xpath).send_keys(date)

    def select_employee_termination_reason_dropdown(self, reason):
        self.driver.find_element(By.XPATH, self.termination_reason_dropdown_button_xpath).click()
        employee_termination_reason_dropdown_list = self.driver.find_elements(By.XPATH, self.
                                                                              termination_reason_dropdown_list_xpath)
        for employee_termination_reason_list in employee_termination_reason_dropdown_list:
            if reason == employee_termination_reason_list.text:
                employee_termination_reason_list.click()
                break

    def click_employee_required_save(self):
        self.driver.find_element(By.XPATH,self.required_save_button).click()

    def job_save(self):
        self.driver.find_element(By.XPATH, self.job_save_xpath).click()

    #===========================Salary===========================================
    def click_employee_salary_component_tap(self):
        self.driver.find_element(By.XPATH, self.employee_salary_tap_xpath).click()

    def click_assigned_salary_component(self):
        self.driver.find_element(By.XPATH, self.employee_salary_components_add_button_xpath).click()

    def enter_employee_salary_component(self, component):
        self.driver.find_element(By.XPATH,self.employee_salary_component_input_box_xpath).send_keys(component)

    def select_pay_grade_dropdown(self, pay_grade):
        self.driver.find_element(By.XPATH, self.employee_pay_grade_dropdown_button_xpath).click()
        pay_grade_dropdown_list = self.driver.find_elements(By.XPATH, self.employee_pay_grade_list_xpath)
        for pay_grade_list in pay_grade_dropdown_list:
            if pay_grade == pay_grade_list.text:
                pay_grade_list.click()
                break

    def select_pay_frequency_dropdown(self, duration):
        self.driver.find_element(By.XPATH, self.employee_pay_frequency_dropdown_button_xpath).click()
        pay_frequency_dropdown_list = self.driver.find_elements(By.XPATH,self.employee_pay_frequency_list_xpath)
        for pay_frequency_list in pay_frequency_dropdown_list:
            if duration == pay_frequency_list.text:
                pay_frequency_list.click()
                break

    def select_currency_dropdown(self, currency):
        self.driver.find_element(By.XPATH, self.currency_dropdown_button_xpath).click()
        currency_dropdown_list = self.driver.find_elements(By.XPATH, self.currency_dropdown_button_xpath)
        for currency_list in currency_dropdown_list:
            if currency == currency_list.text:
                currency_list.click()
                break

    def enter_employee_salary_amount(self, amount):
        self.driver.find_element(By.XPATH, self.salary_amount_input_box_xpath).send_keys(amount)

    def click_direct_deposit_details_toggle_button(self):
        self.driver.find_element(By.XPATH, self.direct_deposit_details_toggle_button_xpath).click()

    def enter_bank_account_number(self, ac_number):
        self.driver.find_element(By.XPATH, self.bank_account_number_input_box_xpath).send_keys(ac_number)

    def select_bank_account_type_dropdown(self, ac_type):
        self.driver.find_element(By.XPATH,self.bank_account_type_dropdown_button_xpath).click()
        bank_account_type_dropdown_list = self.driver.find_elements(By.XPATH,self.bank_account_type_list_xpath)
        for bank_account_list in bank_account_type_dropdown_list:
            if ac_type == bank_account_list.text:
                bank_account_list.click()
                break

    def enter_bank_routing_number(self, route_number):
        self.driver.find_element(By.XPATH, self.bank_account_routing_number_input_box_xpath).send_keys(route_number)

    def enter_deposit_amount(self, amount):
        self.driver.find_element(By.XPATH, self.deposit_amount_input_box_xpath).send_keys(amount)

    def select_federal_income_tax_status_dropdown(self, status):
        self.driver.find_element(By.XPATH,self.federal_income_tax_status_dropdown_button_xpath).click()
        federal_income_tax_status_dropdown_list=self.driver.find_elements(By.XPATH,self.federal_income_tax_status_list_xpath)
        for federal_income_tax_status_list in federal_income_tax_status_dropdown_list:
            if status == federal_income_tax_status_list.text:
                federal_income_tax_status_list.click()
                break

    def select_state_income_tax_state_dropdown(self, state):
        self.driver.find_element(By.XPATH, self.state_income_tax_state_dropdown_button_xpath).click()
        state_income_tax_status_dropdown_list =self.driver.find_elements(By.XPATH,self.state_income_tax_state_list_xpath)
        for state_income_tax_state_list in state_income_tax_status_dropdown_list:
            if state == state_income_tax_state_list.text:
                state_income_tax_state_list.click()
                break

    def select_state_income_tax_status_dropdown(self, status):
        self.driver.find_element(By.XPATH,self.state_income_tax_status_dropdown_button_xpath).click()
        state_income_tax_status_dropdown_list=self.driver.find_elements(By.XPATH,self.state_income_tax_status_list_xpath)
        for state_income_tax_status_list in state_income_tax_status_dropdown_list:
            if status == state_income_tax_status_list.text:
                state_income_tax_status_list.click()
                break

    def select_state_income_tax_unemployment_state_dropdown(self, state):
        self.driver.find_element(By.XPATH, self.state_income_tax_unemployment_state_dropdown_button_xpath) \
            .click()
        state_income_tax_unemployment_state_dropdown_list = self.driver. \
            find_elements(By.XPATH,self.state_income_tax_unemployment_state_list_xpath)
        for state_income_tax_unemployment_state_list in state_income_tax_unemployment_state_dropdown_list:
            if state == state_income_tax_unemployment_state_list.text:
                state_income_tax_unemployment_state_list.click()
                break

    def select_state_income_tax_work_state_dropdown(self, state):
        self.driver.find_element(By.XPATH,self.state_income_tax_work_state_dropdown_button_xpath).click()
        state_income_tax_work_state_dropdown_list = self.driver.find_elements(By.XPATH, self.
                                                                              state_income_tax_work_state_list_xpath)
        for state_income_tax_work_state_list in state_income_tax_work_state_dropdown_list:
            if state == state_income_tax_work_state_list.text:
                state_income_tax_work_state_list.click()
                break

    def click_employee_stax_exemptions_tap(self):
        self.driver.find_element(By.XPATH, self.employee_tax_exemptions_tap_xpath).click()
