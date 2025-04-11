from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")  # noqa: E501

    fields = {
        "first-name": "Иван",
        "last-name": "Петров",
        "address": "Ленина, 55-3",
        "e-mail": "test@skypro.com",
        "phone": "+7985899998787",
        "city": "Москва",
        "country": "Россия",
        "job-position": "QA",
        "company": "SkyPro"
    }

    for field_name, value in fields.items():
        WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.NAME, field_name))
        ).send_keys(value)

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "zip-code"))
    ).send_keys("")

    driver.find_element(By.XPATH, "//button[text()='Submit']").click()

    zip_code = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "zip-code"))
    )
    assert "alert-danger" in zip_code.get_attribute(
        "class"), "Поле почтового индекса не подсвечено красным"

    fields_to_check = ["first-name", "last-name", "address",
                       "e-mail", "phone", "city", "country", "job-position", "company"]  # noqa: E501
    for field in fields_to_check:
        input_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, field))
        )
        assert "alert-success" in input_field.get_attribute(
            "class"), f"Поле {field} не подсвечено зеленым"

finally:

    driver.quit()
