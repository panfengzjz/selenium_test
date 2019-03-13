from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://cn.bing.com")
try:
    elem = WebDriverWait(driver, 3).until(EC.presence_of_element_located((By.ID, "hp_container")))
    print("hello world")
finally:
    driver.quit()