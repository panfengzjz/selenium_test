from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox()
driver.get("https://www.python.org")
elem = driver.find_element_by_name("q")
# return result is
#   <input id="id-search-field" name="q" type="search" role="textbox" \
#   class="search-field" placeholder="Search" value="" tabindex="1">
# so element named "q" is the search-field class
# be careful the API should be find_element_by_name without 's'

elem.clear()
elem.send_keys("pycon")
# find 'pycon' from search-field in www.python.org
elem.send_keys(Keys.RETURN)
print(driver.page_source)
driver.close()