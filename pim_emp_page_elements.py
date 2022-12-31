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
        self.delete_button_xpath ="//div[@role ='table']//div[contains(text(),'0038')]/../following-sibling::div[7]/div/button[1]"
        self.delete_success_msg_xpath = "//button[contains(.,' Yes, Delete')]"
        #self.upload_image_xpath = "//button[@class ='oxd-icon-button employee-image-action']"
        #self.upload_image_xpath = "//img[@class ='employee-image']"

#===============personal details elements============
        self.personal_detail_tab_xpath = "//a[contains(text(), 'Personal Details')]"
        self.emp_middle_name_xpath = "//input[@placeholder ='Middle Name']"
        self.employee_id_xpath = "//label[contains(text(),'Employee Id')]/parent::div/following-sibling::div/input"
        self.Employee_other_id_xpath = "//label[contains(text(), 'Other Id')]/parent::div/following-sibling::div/input"
        self.driver_license_no_xpath = "//label[contains(text(),'License Number')]/parent::div/following-sibling::div/input"
        self.license_expiry_xpath = "//label[contains(text(),'License Expiry Date')]/parent::div/following-sibling::div//div/div/input "
        self.SSN_number_xpath = "//label[text()='SSN Number']/../following-sibling::div/input"
        self.SIN_number_xpath = "//label[text()='SIN Number']/../following-sibling::div/input"
        self.nationality_button_xpath = "//label[text()='Nationality']/../following-sibling::div/div//following-sibling::div"
        self.nationality_text_xpath = "//label[text()='Nationality']/../following-sibling::div/div/div/div[@class ='oxd-select-text-input']"
        self.nationality_list_xpath = "//div[@role='option']"
        self.marital_status_button_xpath = "//label[text()='Marital Status']/../following-sibling::div/div//following-sibling::div"
        self.marital_status_text_xpath = "//label[text()='Marital Status']/../following-sibling::div/div/div/div[@class ='oxd-select-text-input']"
        self.marital_status_list_xpath = "//div[@role='option']"
        self.date_of_brith_xpath = "//label[contains(text(),'Date of Birth')]/parent::div/following-sibling::div//div/div/input "
        self.gender_male_xpath = "//input[@value='1']/following-sibling::span"
        self.gender_female_xpath = "//input[@value='2']/following-sibling::span"
        self.military_service_xpath ="//label[contains(text(), 'Military Service')]/parent::div/following-sibling::div/input"
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
        self.emergency_contact_relationship_xpath = "// label[text() = 'Relationship'] /../ following - sibling::div / input"
        self.emergency_contact_home_phone_xpath = "// label[text() = 'Home Telephone'] /../ following - sibling::div / input"
        self.emergency_contact_save_xpath = "//button[@type='submit']"

# ==============================Dependents===========================
        self.dependents_tab_xpath = "// a[contains(text(), 'Dependents')]"
        self.dependents_add_xpath = "//div[@class = 'orangehrm-action-header']/h6/../../div/button"
        self.dependents_name_xpath = "//label[text()='Name']/../following-sibling::div/input"
        self.dependents_relationship_button_xpath ="// label[text() = 'Relationship']/../following-sibling::div/div/div"
        self.dependents_relationship_xpath = "// label[text() = 'Relationship']/../following-sibling::div/div/div/div[@class ='oxd-select-text-input']"
        self.dependents_DOB_xpath = "//label[contains(text(),'Date of Birth')]/parent::div/following-sibling::div//div/div/input"
        self.dependents_save_xpath = "//button[@type='submit']"

        # ==============================Job===========================
        self.job_tab_xpath = "// a[contains(text(), 'Job')]"
        self.job_joined_date_xpath = "//label[contains(text(),'Joined Date')]/parent::div/following-sibling::div//div/div/input"
        self.job_title_xpath = "//label[text()='Job Title']/../following-sibling::div/div//following-sibling::div"
        self.job_title_list_xpath ="//label[text()='Job Title']/../following-sibling::div/div//following-sibling::div"
        self.job_specification_xpath = ""
        self.job_category_xpath = ""
        self.job_sub_unit_xpath = ""
        self.job_location_xpath = ""
        self.job_employee_status_xpath = ""
        self.job_save_xpath = "//button[@type='submit']"

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
