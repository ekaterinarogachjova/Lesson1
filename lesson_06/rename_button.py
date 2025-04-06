from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/textinput")


input_field = driver.find_element(By.ID, "newButtonName")
input_field.send_keys("SkyPro")
time.sleep(3)

button = driver.find_element(By.ID, "updatingButton")
button.click()

button_text = button.text
print(button_text)

driver.quit()
