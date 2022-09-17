from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://www.redbus.in/")
driver.maximize_window()
driver.implicitly_wait(30)

driver.find_element(By.ID,'src').send_keys("Kol")

fromdrpdwn = driver.find_elements(By.XPATH,'//ul[@class="autoFill homeSearch"]/li')
for f in fromdrpdwn:
    print(f.text)
    if 'Airport, Kolkata' == f.text:
        f.click()
        break


driver.find_element(By.ID,'dest').send_keys("Bang")
todrpdwn = driver.find_elements(By.XPATH,'//ul[@class="autoFill homeSearch"]/li')
for t in todrpdwn:
    print(t.text)
    if 'Bangladesh' in t.text:
        t.click()
        break


date_cal = driver.find_elements(By.XPATH,'//table[@class="rb-monthTable first last"]//td')
for d in date_cal:
    print(d.text)
    if '27' == d.text:
        d.click()
        break
