'''

implicit wait
explicit wait

pageloadtimeout


'''

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
driver.implicitly_wait(90)

# wait = WebDriverWait(driver,15)
# wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[text()='OK']")))
#
# driver.find_element(By.XPATH,"//button[text()='OK']").click()


wait = WebDriverWait(driver,15,poll_frequency=2,ignored_exceptions="NoSuchElementException")
wait.until(expected_conditions.element_to_be_clickable((By.XPATH,"//button[text()='OK']")))

driver.find_element(By.XPATH,"//button[text()='OK']").click()


wait = WebDriverWait(driver,15,poll_frequency=2,ignored_exceptions="NoSuchElementException")
wait.until(expected_conditions.element_to_be_clickable((By.XPATH,'//label[@for="dateSpecific"]')))

#driver.find_element(By.ID,'availableBerth').click()
driver.find_element(By.XPATH,'//label[@for="dateSpecific"]').click()

