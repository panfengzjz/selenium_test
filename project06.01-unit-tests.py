import unittest
import page
from selenium import webdriver

class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://www.python.org")
    
    def test_search_in_python_org(self):
        """
        Tests python.org search feature. Searches for the word "pycon" then verified that some results show up.
        Note that it does not look for any particular text in search results page. This test verifies that
        the results were not empty.
        """

        #Load the main page. In this case the home page of Python.org.
        main_page = page.MainPage(self.driver)
        assert main_page.is_title_matches(), "python.org title doesn't match"
        main_page.search_text_element = "pycon\n"
        #main_page.click_go_button()
        search_results_page = page.SearchResultsPage(self.driver)
        assert search_results_page.is_results_found(), "No results found."
    
    def tearDown(self):
        self.driver.close()
        print("test pass")

if __name__ == "__main__":
    unittest.main()