import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):
    # initialization
    # be called before every test function in this test case class
    def setUp(self):
        self.driver = webdriver.Firefox()
    
    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found" not in driver.page_source
    
    # be called after every test method
    # to do all cleanup actions
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()