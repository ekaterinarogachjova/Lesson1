from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Открытие страницы
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    WebDriverWait(driver, 40).until(EC.visibility_of_element_located((By.NAME, "first-name"))).send_keys("Иван")
driver.find_element(By.NAME, "last-name").send_keys("Петров")
driver.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
driver.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
driver.find_element(By.NAME, "phone").send_keys("+7985899998787")
driver.find_element(By.NAME, "zip-code").send_keys("")  # оставляем пустым
driver.find_element(By.NAME, "city").send_keys("Москва")
driver.find_element(By.NAME, "country").send_keys("Россия")
driver.find_element(By.NAME, "job-position").send_keys("QA")
driver.find_element(By.NAME, "company").send_keys("SkyPro")

 # Нажимаем кнопку Отправить
    driver.find_element(By.XPATH, "//button[text()='Отправить']").click()

    # Проверяем, что поле почтовый индекс подсвечено красным
    zip-code = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "zip-code")))
    assert "red" in zip-code.get_attribute("style"), "Поле почтового индекса не подсвечено красным"

    # Проверяем, что остальные поля подсвечены зеленым
    fields = ["first-name", "last-name", "address", "e-mail", "phone", "city", "country", "job-position", "company"]
    for field in fields:
        input_field = driver.find_element(By.NAME, field)
        assert "green" in input_field.get_attribute("style"), f"Поле {field} не подсвечено зеленым"

finally:
    # Закрываем драйвер
    driver.quit()
