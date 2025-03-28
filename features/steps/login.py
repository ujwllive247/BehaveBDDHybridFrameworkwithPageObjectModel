from datetime import datetime
import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

from features import environment
from features.pages.AccountPage import AccountPage
from features.pages.Homepage import HomePage
from features.pages.loginPage import LoginPage


@given('I navigate to the Login page')
def step_given_navigate_to_login_page(context):
    # Code to navigate to the login page
    context.home_page = HomePage(context.driver)
    context.home_page.click_on_my_account()
    context.home_page.select_login_option()

    # context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    # context.driver.find_element(By.LINK_TEXT, 'Login').click()


@when('I enter a valid email address and a valid password into the fields')
def step_when_enter_valid_credentials(context):
    # Code to enter valid email and password
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address("ujwllive247@gmail.com")
    context.login_page.enter_password("Kangaroo@123")


    # context.driver.find_element(By.ID, "input-email").send_keys("ujwllive247@gmail.com")
    # context.driver.find_element(By.ID, "input-password").send_keys("Kangaroo@123")
    # time.sleep(5)


@when('I enter an invalid email and a valid password into the fields')
def step_when_enter_invalid_email_valid_password(context):
    # Code to enter invalid email and valid password
    # Generate random email address
    time_stamp = datetime.now().strftime("%Y_%m_%H_%M_%S")
    invalid_email = "ujwl" + time_stamp + "@gmail.com"
    context.login_page = LoginPage(context.driver)
    context.login_page.enter_email_address(invalid_email)
    context.login_page.enter_password("Kangaroo@123")

    # time_stamp = datetime.now().strftime("%Y_%m_%H_%M_%S")
    # invalid_email = "ujwl" + time_stamp + "@gmail.com"
    # context.driver.find_element(By.ID, "input-email").send_keys(invalid_email)
    # context.driver.find_element(By.ID, "input-password").send_keys("Kangaroo@123")
    # time.sleep(5)

@when('I enter a valid email and an invalid password into the fields')
def step_when_enter_valid_email_invalid_password(context):
    # Code to enter valid email and invalid password
    context.driver.find_element(By.ID, "input-email").send_keys("ujwl247@gmail.com")
    context.driver.find_element(By.ID, "input-password").send_keys("garoo@123")
    time.sleep(5)


@when('I enter an invalid email and an invalid password into the fields')
def step_when_enter_invalid_credentials(context):
    # Code to enter invalid email and invalid password
    time_stamp = datetime.now().strftime("%Y_%m_%H_%M_%S")
    invalid_email = "ujwl" + time_stamp + "@gmail.com"
    context.driver.find_element(By.ID, "input-email").send_keys(invalid_email)
    context.driver.find_element(By.ID, "input-password").send_keys("aroo@123")
    time.sleep(5)


@when('I don\'t enter anything into the email and password fields')
def step_when_enter_nothing(context):
    # Code to ensure no email and password are entered
    context.driver.find_element(By.ID, "input-email").send_keys("")
    context.driver.find_element(By.ID, "input-password").send_keys("")
    time.sleep(5)

@when('I click on the Login button')
def step_when_click_login_button(context):
    # Code to click the login button

    context.login_page.click_on_login_button()
    # context.driver.find_element(By.XPATH, "//input[@value='Login']").click()


@then('I should get logged in')
def step_then_logged_in(context):
    # Code to verify user is logged in

    account_page = AccountPage(context.driver)
    assert account_page.display_status_of_edit_your_account_information_option()
    # assert context.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()
    # time.sleep(3)




@then('I should get a proper warning message')
def step_then_warning_message(context):
    # Code to verify warning message is displayed
    expected_warning_message = "Warning: No match for E-Mail Address and/or Password."
    assert context.login_page.display_status_of_warning_message(expected_warning_message)

    # assert context.driver.find_element(By.XPATH,"//div[@id='account-login']div[1]").text.__contains__(expected_warning_message)