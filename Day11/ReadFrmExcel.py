from ReadExcel import readExcel

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

driver.get(readExcel("Datasheet1.xlsx","Facebook","uRL"))
driver.find_element(By.NAME,"email").send_keys(readExcel("Datasheet1.xlsx","Facebook","Username"))
driver.find_element(By.NAME,"pass").send_keys(readExcel("Datasheet1.xlsx","Facebook","password"))
#driver.get(readExcel("Datasheet1.xlsx","Facebook","uRL"))
