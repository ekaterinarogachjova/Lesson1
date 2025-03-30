from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
import time


service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:

    url = "http://the-internet.herokuapp.com/inputs"
    driver.get(url)

    input_field = driver.find_element(By.XPATH, "//input[@type='number']")

    input_field.send_keys("Sky")
    time.sleep(5)

    input_field.clear()

    input_field.send_keys("Pro")
    time.sleep(5)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:

    driver.quit()
