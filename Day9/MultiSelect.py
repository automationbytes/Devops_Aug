from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://demo.mobiscroll.com/select/multiple-select")
driver.maximize_window()
driver.implicitly_wait(30)
#driver.find_element(By.XPATH,'//a[@data-testid="open-registration-form-button"]').click()


multidrp = Select(driver.find_element(By.ID,'multiple-select-select'))
multidrp.select_by_value("1")
multidrp.select_by_value("4")
