import time

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By





@given('I navigate to the Home page')
def step_given_navigate_to_home_page(context):
     expected_title = "Your Store"
     assert context.driver.title.__eq__(expected_title)



@when('I enter a valid product into the search box')
def step_when_enter_valid_product(context):
    context.driver.find_element(By.NAME,"search").send_keys("HP")
    time.sleep(3)


@when('I enter an invalid product into the search box')
def step_when_enter_invalid_product(context):
    # Code to enter an invalid product into the search box
    context.driver.find_element(By.NAME, "search").send_keys("Honda")
    time.sleep(3)


@when('I don\'t enter anything into the search box')
def step_when_enter_nothing(context):
    # Code to ensure nothing is entered into the search box
    context.driver.find_element(By.NAME, "search").send_keys("")



@when('I click on the Search button')
def step_when_click_search_button(context):
    context.driver.find_element(By.XPATH,"//div[@id='search']//button").click()



@then('the valid product should be displayed in the search results')
def step_then_valid_product_displayed(context):
    assert context.driver.find_element(By.LINK_TEXT,"HP LP3065").is_displayed()
    time.sleep(3)




@then('a proper message should be displayed in the search results')
def step_then_proper_message_displayed(context):
    # Code to verify proper message in search results for invalid product
    expected_text = "There is no product that matches the search criteria."
    assert context.driver.find_element(By.XPATH,"//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)





@then('a "not found" message should be shown')
def step_then_not_found_message(context):
    # Code to verify "not found" message is shown
    pass
