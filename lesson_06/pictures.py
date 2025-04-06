from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")  # noqa: E501

waiter = WebDriverWait(driver, 40)

waiter.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#award")))

print(driver.find_element(By.CSS_SELECTOR, "#award").get_dom_attribute("src"))

driver.quit()
