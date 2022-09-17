from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager


driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://facebook.com")
driver.maximize_window()
driver.implicitly_wait(30)
driver.find_element(By.XPATH,'//a[@data-testid="open-registration-form-button"]').click()

monthdropdown = Select(driver.find_element(By.NAME,'birthday_month'))
#monthdropdown.select_by_value("3")
monthdropdown.select_by_visible_text('Jun')

yearDropdown = Select(driver.find_element(By.ID,'year'))
yearDropdown.select_by_index(5)
yearDropdown.select_by_index(7)

for y in yearDropdown.options:
    print(y.text)


driver.find_element(By.XPATH,"//label[text()='Male']").click()