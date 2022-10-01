import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

class LaunchUrl(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("setup Method")
        cls.driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()

    def test_google(self):
        self.driver.get("https://www.google.com/")
        print(self.driver.title)
        print(self.driver.current_url)

    def test_bing(self):
        self.driver.get("https://www.bing.com")
        print(self.driver.title)
        print(self.driver.current_url)

    def test_facebook(self):
        self.driver.get("https://www.facebook.com")
        print(self.driver.title)
        print(self.driver.current_url)
    @classmethod
    def tearDownClass(cls):
        print("TearDown Method")
        cls.driver.close()
        cls.driver.quit()

if __name__ == '__main__':
    unittest.main()