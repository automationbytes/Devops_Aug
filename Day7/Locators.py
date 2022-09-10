'''
id
name
class name
tag name
link text
partial link text
xpath
css
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://facebook.com")
driver.maximize_window()

driver.find_element(By.ID,"email").send_keys("username")
driver.find_element(By.ID,"pass").send_keys("passw123")
#driver.find_element(By.LINK_TEXT,"Forgotten password?").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"password?").click()

