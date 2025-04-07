from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome()

try:

    driver.get("http://uitestingplayground.com/textinput")

    input_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )
    input_field.send_keys("SkyPro")

    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "updatingButton"))
    )
    button.click()

    WebDriverWait(driver, 20).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )
    print(button.text)

finally:
    
    driver.quit()
