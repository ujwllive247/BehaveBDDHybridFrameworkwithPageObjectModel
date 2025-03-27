from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self,driver):

        self.driver = driver

    email_address_field_id = "input-email"
    password_field_id = "input-password"
    login_button_xpath = "//input[@value='Login']"
    warning_message_xpath = "//div[@id='account-login']/div[1]"



    def enter_email_address(self,email_text):
        self.driver.find_element(By.ID,self.email_address_field_id).send_keys(email_text)



    def enter_password(self,password_text):
        self.driver.find_element(By.ID,self.password_field_id).send_keys(password_text)


    def click_on_login_button(self):
        self.driver.find_element(By.XPATH,self.login_button_xpath).click()

    def display_status_of_warning_message(self,expected_warning_text):
        self.driver.find_element(By.XPATH,self.warning_message_xpath).text.__contains__(expected_warning_text)
