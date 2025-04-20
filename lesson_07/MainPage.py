from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver

    def add_item_to_cart(self, item_name):
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@class='inventory_item' and .//div[contains(text(), '{item_name}')]]//button"))  # noqa: E501
        )
        add_button.click()

    def go_to_cart(self):
        cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_link.click()
