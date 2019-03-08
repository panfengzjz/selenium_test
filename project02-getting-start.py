from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://www.python.org")
print(driver.title)
print(driver.context)
driver.close()