from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class MainPage:
    """
    Класс для работы с главной страницей магазина.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация страницы.

        :param driver: WebDriver - экземпляр Selenium WebDriver.
        """
        self.driver = driver

    @allure.step("Добавить товар '{item_name}' в корзину")
    def add_item_to_cart(self, item_name: str) -> None:
        """
        Добавляет товар с указанным именем в корзину.

        :param item_name: str - название товара.
        """
        add_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 f"//div[@class='inventory_item' and .//div[contains(text(), '{item_name}')]]//button")  # noqa: E501
            )
        )
        add_button.click()

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> None:
        """
        Переходит на страницу корзины.
        """
        cart_link = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link"))
        )
        cart_link.click()
