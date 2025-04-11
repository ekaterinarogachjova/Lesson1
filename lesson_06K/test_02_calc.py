from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.add_argument("--blink-settings=imagesEnabled=false")
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")  # noqa: E501

    delay_input = driver.find_element(By.ID, "delay")
    delay_input.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()  # 7
    driver.find_element(By.XPATH, "//span[text()='+']").click()  # +
    driver.find_element(By.XPATH, "//span[text()='8']").click()  # 8
    driver.find_element(By.XPATH, "//span[text()='=']").click()  # =

    try:
        WebDriverWait(driver, 90).until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
    except Exception as e:
        print(f"Timeout or exception occurred: {e}")
        print("Page source:")
        print(driver.page_source)

    try:
        result = driver.find_element(By.CLASS_NAME, "screen").text
        assert result == "15"
    except AssertionError:
        print("ошибка ")
finally:
    driver.quit()
