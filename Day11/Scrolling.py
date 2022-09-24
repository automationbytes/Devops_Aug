'''

3 ways scrolling
1) scrollby -> x and y axis
2) scrollto -> either top or bottom of the page
3) scrollintoview -> scrolls to particular webelement
'''

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
phnnum = driver.find_element(By.XPATH,'//input[@id="smsTXTBOX"]')
driver.execute_script("arguments[0].scrollIntoView(true);",phnnum)
#
# time.sleep(10)
# driver.execute_script("window.scrollBy(0,1000);")
#
#
# time.sleep(10)
# driver.execute_script("window.scrollBy(0,1000);")
#
#
# time.sleep(10)
# driver.execute_script("window.scrollBy(0,-1500);")
#
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
# time.sleep(10)
#
#
# driver.execute_script("window.scrollTo(0,-document.body.scrollHeight);")
