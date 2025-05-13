from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class CartPage:
    """
    Класс для работы со страницей корзины.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация элементов страницы.

        :param driver: WebDriver - экземпляр Selenium WebDriver.
        """
        self.driver = driver
        self.checkout_button = (By.ID, "checkout")

    @allure.step("Нажать кнопку оформления заказа")
    def click_checkout(self) -> None:
        """
        Нажимает кнопку оформления заказа.
        """
        checkout_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.checkout_button)
        )
        checkout_button.click()
