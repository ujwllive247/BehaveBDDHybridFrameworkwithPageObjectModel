import time
from datetime import datetime

from behave import given, when, then

from selenium import webdriver
from selenium.webdriver.common.by import By




@given('I navigate to the Register page')
def step_given_navigate_to_register_page(context):
    # Code to navigate to the register page

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




# @when('I enter all fields')
# def step_when_enter_all_fields(context):
#     # Code to enter all fields
#     pass


@when('I enter details into all fields except the email field')
def step_when_enter_all_fields_except_email(context):
    # Code to enter details into all fields except email
    context.driver.find_element(By.ID, "input-firstname").send_keys("Arun")
    context.driver.find_element(By.ID, "input-lastname").send_keys("Mooturi")

    context.driver.find_element(By.ID, "input-telephone").send_keys("121213")
    context.driver.find_element(By.ID, "input-password").send_keys("121313")
    context.driver.find_element(By.ID, "input-confirm").send_keys("121313")
    context.driver.find_element(By.XPATH,"//input[@name='newsletter'][@value='1']").click()


@when('I enter an existing account\'s email into the email field')
def step_when_enter_existing_email(context):
    # Code to enter an existing email
    context.driver.find_element(By.ID,"input-email").send_keys("ujwllive247@gmail.com")


@when('I don\'t enter anything into the fields')
def step_when_enter_nothing(context):
    # Code to ensure no details are entered
    context.driver.find_element(By.ID, "input-firstname").send_keys("")
    context.driver.find_element(By.ID, "input-lastname").send_keys("")
    context.driver.find_element(By.ID, "input-email").send_keys("")
    context.driver.find_element(By.ID, "input-telephone").send_keys("")
    context.driver.find_element(By.ID, "input-password").send_keys("")
    context.driver.find_element(By.ID, "input-confirm").send_keys("")


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






@then('a proper warning message informing about the duplicate account should be displayed')
def step_then_warning_message_duplicate_account(context):
    # Code to verify warning message for duplicate account
    expected_warning = "Warning: E-Mail Address is already registered!"
    assert context.driver.find_element(By.XPATH,"//div[@id='account-register']/div[1]")\
    .text__contains__(expected_warning)



@then('proper warning messages for every mandatory field should be displayed')
def step_then_warning_messages_mandatory_fields(context):
    # Code to verify warning messages for mandatory fields
    expected_privacy_policy_warning = "Warning: You must agree to the Privacy Policy!"
    expected_first_name_warning ="First Name must be between 1 and 32 characters!"
    expected_last_name_warning = "Last Name must be between 1 and 32 characters!"
    expected_email_warning = "E-Mail Address does not appear to be valid!"
    expected_telephone_warning = "Telephone must be between 3 and 32 characters!"
    expected_password_warning = "Password must be between 4 and 20 characters!"

    assert context.driver.find_element(By.XPATH,"//div[@id='account-register']/div[1]")\
    .text.__contains__(expected_privacy_policy_warning)

    assert context.driver.find_element(By.XPATH,"//input[@id='input-firstname']/following-sibling::div")\
    .text.__eq__(expected_first_name_warning)

    assert context.driver.find_element(By.XPATH,"//input[@id='input-lastname']/following-sibling::div")\
    .text.__eq__(expected_last_name_warning)

    assert context.driver.find_element(By.XPATH, "//input[@id='input-email']/following-sibling::div") \
        .text.__eq__(expected_last_name_warning)

    assert context.driver.find_element(By.XPATH, "//input[@id='input-lastname']/following-sibling::div") \
        .text.__eq__(expected_email_warning)

    assert context.driver.find_element(By.XPATH, "//input[@id='input-telephone']/following-sibling::div") \
        .text.__eq__(expected_telephone_warning)

    assert context.driver.find_element(By.XPATH, "//input[@id='input-password']/following-sibling::div") \
        .text.__eq__(expected_password_warning)



