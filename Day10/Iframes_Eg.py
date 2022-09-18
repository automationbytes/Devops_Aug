from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.XPATH,'//a[@onclick="retheme()"]').click()
#we can switch in 3 ways
'''
name/id
index
locators

'''

#driver.switch_to.frame("iframeResult")
driver.switch_to.frame(driver.find_element(By.XPATH,'//iframe[@name="iframeResult"]'))

driver.find_element(By.XPATH,"//button[text()='Try it']").click()
print(driver.switch_to.alert.text)
driver.switch_to.alert.send_keys("Tom")
driver.switch_to.alert.dismiss()


#driver.switch_to.default_content()
driver.switch_to.parent_frame()
driver.find_element(By.XPATH,'//a[@onclick="retheme()"]').click()
