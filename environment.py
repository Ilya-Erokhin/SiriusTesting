from selenium import webdriver
from utilities import ConfigReader

def before_scenario(context, driver):
    browser_name = ConfigReader.read_configuration("basic info", "browser")

    if browser_name == "chrome":
        context.driver = webdriver.Chrome()
    elif browser_name == "firefox":
        context.driver = webdriver.Firefox()
    elif browser_name == "edge":
        context.driver = webdriver.Edge()

def after_scenario(context, driver):
    context.driver.quit()
