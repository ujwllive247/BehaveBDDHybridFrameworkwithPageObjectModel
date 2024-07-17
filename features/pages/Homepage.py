from selenium.webdriver.common.by import By


class HomePage:


    def __init__(self,driver):
        self.driver = driver

    my_account_option_xpath = "//span[text()='My Account']"
    login_option_link_text = "Login"


    def click_on_my_account(self):

        self.driver.find_element(By.XPATH,self.my_account_option_xpath).click()


    def select_login_option(self):
        self.driver.find_element(By.LINK_TEXT,self.login_option_link_text)