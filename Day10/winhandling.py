import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.set_page_load_timeout(60)
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.XPATH,"//button[text()='OK']").click()
try:
    wait = WebDriverWait(driver,15)
    wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[text()='Later']")))

    if driver.find_element(By.XPATH,"//button[text()='Later']").size['width']>0 :
        driver.find_element(By.XPATH,"//button[text()='Later']").click()
except:
    print("No popup")
wait = WebDriverWait(driver,15)
wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//a[text()=' BUSES ']")))

driver.find_element(By.XPATH,"//a[text()=' BUSES ']").click()
driver.find_element(By.XPATH,"//a[text()=' FLIGHTS ']").click()
driver.find_element(By.XPATH,"//a[text()=' HOTELS ']").click()

parentwindow = driver.current_window_handle
print(parentwindow)

allopenwindows = driver.window_handles
print(allopenwindows)
print(type(allopenwindows))

for a in allopenwindows:
    if a!= parentwindow:
        time.sleep(5)
        driver.switch_to.window(a)
        print(driver.current_url)
        if "air"  in driver.current_url:
            driver.find_element(By.ID,'ltc').click()
            break

