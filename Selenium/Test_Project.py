import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        s = Service("D:\Chrome Driver\chromedriver.exe")
        self.driver = webdriver.Chrome(service=s)


    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.youtube.com/")
        self.assertIn("YouTube", driver.title)
        elem = driver.find_element(By.NAME, "search_query")
        elem.send_keys("Automation Testing for Beginner")
        elem.submit()
        driver.implicitly_wait(100)
        #elem.send_keys(Keys.RETURN)
        #self.assertNotIn("No results found.", driver.page_source)


   # def tearDown(self):
       # self.driver.close()

if __name__ == "__main__":
    unittest.main()