
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()

try:

    driver.get("http://uitestingplayground.com/classattr")

    time.sleep(3)

    blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")

    blue_button.click()

    time.sleep(8)

finally:

    driver.quit()
