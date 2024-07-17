# from selenium import webdriver
#
# from utilities import ConfigReader
#
#
# def before_scenario(context,driver):
#     browser_name = ConfigReader.read_configuration("basic info","broswer")
#
#     if browser_name.__eq__("chrome"):
#         context.driver= webdriver.Chrome()
#
#     elif browser_name.__eq__("firefox"):
#          context.driver = webdriver.Firefox()
#
#     elif browser_name.__eq__("edge"):
#          context.driver = webdriver.Edge()
#
#     context.driver = webdriver.Firefox()
#     context.driver.maximize_window()
#     context.driver.get(ConfigReader.read_configuration("basic info","url"))
#
#
#
# def after_scenario(context,driver):
#     context.driver.quit()
import time

#________ChatGpt____

# from selenium import webdriver
# from utilities import ConfigReader
#
# def before_scenario(context, scenario):
#
#
#     browser_name = ConfigReader.read_configuration("basic info", "browser")
#
#     if browser_name == "chrome":
#         context.driver = webdriver.Chrome()
#     elif browser_name == "firefox":
#         context.driver = webdriver.Firefox()
#     elif browser_name == "edge":
#         context.driver = webdriver.Edge()
#     else:
#         raise Exception(f"Browser '{browser_name}' is not supported")
#
#     context.driver.maximize_window()
#     context.driver.get(ConfigReader.read_configuration("basic info", "url"))
#
# def after_scenario(context, scenario):
#     context.driver.quit()



# environment.py
# from selenium import webdriver
# from utilities import ConfigReader
#
# def before_scenario(context, scenario):
#     browser_name = ConfigReader.read_configuration("basic info", "browser")
#
#     if browser_name == "chrome":
#         context.driver = webdriver.Chrome()
#     elif browser_name == "firefox":
#         context.driver = webdriver.Firefox()
#     elif browser_name == "edge":
#         context.driver = webdriver.Edge()
#     else:
#         raise Exception(f"Browser '{browser_name}' is not supported")
#
#     context.driver.maximize_window()
#     context.driver.get(ConfigReader.read_configuration("basic info", "url"))
#
# def after_scenario(context, scenario):
#     context.driver.quit()



from selenium import webdriver

from utilities import ConfigReader


def before_scenario(context,driver):
    context.driver = webdriver.Firefox()
    context.driver.maximize_window()
    context.driver.get(ConfigReader.read_configuration("basic info","url"))
    time.sleep(5)


def after_scenario(context,driver):

    context.driver.quit()