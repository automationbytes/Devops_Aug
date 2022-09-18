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

driver.set_page_load_timeout(60)
driver.get("https://www.timeanddate.com/worldclock/india/new-delhi")
driver.maximize_window()
driver.implicitly_wait(30)

act = ActionChains(driver)
act.move_to_element(driver.find_element(By.XPATH,'//ul[@id="site-nav"]//a[text()="Calendar"]'))
time.sleep(3)
act.move_to_element(driver.find_element(By.XPATH,"//a[text()='Calendar 2022']"))
act.click(driver.find_element(By.XPATH,"//a[text()='Calendar 2022']")).perform()



