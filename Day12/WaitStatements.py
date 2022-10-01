import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

starttime = time.time()
driver.set_page_load_timeout(60)
driver.get("https://www.irctc.co.in/nget/train-search")
print(driver.title)
driver.implicitly_wait(600)
driver.find_element(By.XPATH,"//button[text()='OK']").click()

try:
    # wait = WebDriverWait(driver,10)
    # wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[text()='Later']")))
    driver.find_element(By.XPATH,"//button[text()='Later']").click()

except:
    pass
endtime = time.time()
print(endtime-starttime)