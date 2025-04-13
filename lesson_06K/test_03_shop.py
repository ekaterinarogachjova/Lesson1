from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def test_sauce_demo():
    options = Options()
    options.add_argument("--blink-settings=imagesEnabled=false")
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://www.saucedemo.com/")

        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "password")
        login_button = driver.find_element(By.ID, "login-button")

        username_field.send_keys("standard_user")
        password_field.send_keys("secret_sauce")
        login_button.click()

        items_to_add = ["Sauce Labs Backpack", "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]  # noqa: E501

        for item_name in items_to_add:
            add_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, f"//div[@class='inventory_item' and .//div[contains(text(), '{item_name}')]]//button"))  # noqa: E501
            )
            add_button.click()

        cart_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_link.click()

        checkout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "checkout"))
        )
        checkout_button.click()

        first_name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "first-name"))
        )
        last_name_field = driver.find_element(By.ID, "last-name")
        postal_code_field = driver.find_element(By.ID, "postal-code")

        first_name_field.send_keys("Екатерина")
        last_name_field.send_keys("Зубова")
        postal_code_field.send_keys("357210")

        continue_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.ID, "continue"))
        )
        continue_button.click()

        time.sleep(2)
        total_cost = driver.find_element(By.CLASS_NAME, "summary_total_label").text  # noqa: E501
        total_cost_value = float(total_cost.split("$")[1])  # noqa: E501

        assert total_cost_value == 58.29, f"Итоговая сумма должна быть 58.29, но получено {total_cost_value}"  # noqa: E501
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


test_sauce_demo()
