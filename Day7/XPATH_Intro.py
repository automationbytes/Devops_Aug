'''
xml path

absolute xpath - /
relative xpath - //


//tagname[@attribute = 'value']
//input[@data-testid="royal_email"]
//input[@aria-label="Email address or phone number"]

//tagname[@attribute1 = 'value1' and @attribute2 = 'value2']
//input[@type="text" and @name="email"]

//tagname[contains(@attribute, 'val')]
//input[contains(@aria-label,"address or phone")]

//tagname[text()='value']
//a[text()='Forgotten password?']

//tagname[contains(text(),'va')]
//a[contains(text(),'Forgotten passwo')]

//ul/li - ul - parent-> li- child

'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
driver.get("https://facebook.com")
driver.maximize_window()

driver.find_element(By.XPATH,'//input[contains(@aria-label,"number")]').send_keys("username")
