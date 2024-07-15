import time
from datetime import datetime

from behave import given, when, then

from selenium import webdriver
from selenium.webdriver.common.by import By


@given('I navigate to the Register page')
def step_given_navigate_to_register_page(context):
    # Code to navigate to the register page
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    context.driver.get("https://tutorialsninja.com/demo/")
    context.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
    context.driver.find_element(By.LINK_TEXT,"Register").click()
    time.sleep(5)


@when('I enter the mandatory fields')
def step_when_enter_mandatory_fields(context):
    # Code to enter mandatory fields
    context.driver.find_element(By.ID,"input-firstname").send_keys("Arun")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Mooturi")

    time_stamp = datetime.now().strftime("%Y_%m_%H_%M_%S")
    new_email = "ujwl" + time_stamp + "@gmail.com"
    context.driver.find_element(By.ID, "input-email").send_keys(new_email)
    context.driver.find_element(By.ID,"input-telephone").send_keys("121213")
    context.driver.find_element(By.ID,"input-password").send_keys("121313")
    context.driver.find_element(By.ID, "input-confirm").send_keys("121313")




@when('I select privacy Policy option')
def step_when_enter_mandatory_fields(context):
    context.driver.find_element(By.NAME,"agree").click()
    time.sleep(3)




@when('I enter all fields')
def step_when_enter_all_fields(context):
    # Code to enter all fields
    pass


@when('I enter details into all fields except the email field')
def step_when_enter_all_fields_except_email(context):
    # Code to enter details into all fields except email
    context.driver.find_element(By.ID, "input-firstname").send_keys("Arun")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Mooturi")

    time_stamp = datetime.now().strftime("%Y_%m_%H_%M_%S")
    # new_email = "ujwl" + time_stamp + "@gmail.com"
    # context.driver.find_element(By.ID, "input-email").send_keys(new_email)
    context.driver.find_element(By.ID, "input-telephone").send_keys("121213")
    context.driver.find_element(By.ID, "input-password").send_keys("121313")
    context.driver.find_element(By.ID, "input-confirm").send_keys("121313")


@when('I enter an existing account\'s email into the email field')
def step_when_enter_existing_email(context):
    # Code to enter an existing email
    pass


@when('I don\'t enter anything into the fields')
def step_when_enter_nothing(context):
    # Code to ensure no details are entered
    pass


@when('I click on the Continue button')
def step_when_click_continue_button(context):
    # Code to click the continue button
    time.sleep(3)
    context.driver.find_element(By.XPATH,"//input[@value='Continue']").click()

    time.sleep(3)





@then('the account should get created')
def step_then_account_created(context):
    # Code to verify account creation

    expected_text = "Your Account Has Been Created"
    assert context.driver.find_element(By.XPATH,"//div[@id='content']/h1").text.__eq__(expected_text)

    context.driver.quit()




@then('a proper warning message informing about the duplicate account should be displayed')
def step_then_warning_message_duplicate_account(context):
    # Code to verify warning message for duplicate account
    pass

@then('proper warning messages for every mandatory field should be displayed')
def step_then_warning_messages_mandatory_fields(context):
    # Code to verify warning messages for mandatory fields
    expected_warning_message = "E-Mail Address does not appear to be valid!"

    assert context.driver.find_element(By.XPath,"")
