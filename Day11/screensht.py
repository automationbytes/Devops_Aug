import calendar
import datetime
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

driver.get("https://www.redbus.in/")
driver.implicitly_wait(30)

print(datetime.datetime.now())
curtime = str(datetime.datetime.now()).replace(":","-")
gmtime = time.gmtime()
print(gmtime)
print(calendar.timegm(gmtime))


driver.save_full_page_screenshot("c:/java/redbus"+curtime+".jpg")

driver.get_screenshot_as_png()
driver.get_screenshot_as_file("screenshot"+curtime+".jpg")