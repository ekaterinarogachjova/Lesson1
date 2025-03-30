from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:

    driver.get("http://uitestingplayground.com/dynamicid")

    time.sleep(2)

    button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")
    button.click()

    time.sleep(2)

finally:

    driver.quit()
