# lesson05_task4.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service)

try:

    url = "http://the-internet.herokuapp.com/login"
    driver.get(url)

    username_field = driver.find_element(By.ID, "username")
    username_field.send_keys("tomsmith")

    password_field = driver.find_element(By.ID, "password")
    password_field.send_keys("SuperSecretPassword!")
    time.sleep(5)

    login_button = driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']")
    login_button.click()
    time.sleep(5)

    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "flash"))
    )
    print(success_message.text)

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:

    driver.quit()
