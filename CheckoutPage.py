from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class CheckoutPage:
    """
    Класс для работы со страницей оформления заказа.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация элементов страницы.

        :param driver: WebDriver - экземпляр Selenium WebDriver.
        """
        self.driver = driver
        self.first_name_field = (By.ID, "first-name")
        self.last_name_field = (By.ID, "last-name")
        self.postal_code_field = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.total_cost_label = (By.CLASS_NAME, "summary_total_label")

    @allure.step("Заполнить форму оформления заказа: {first_name} {last_name}, почтовый индекс {postal_code}")  # noqa: E501
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:  # noqa: E501
        """
        Заполняет форму оформления заказа.

        :param first_name: str - имя.
        :param last_name: str - фамилия.
        :param postal_code: str - почтовый индекс.
        """
        self.driver.find_element(*self.first_name_field).send_keys(first_name)
        self.driver.find_element(*self.last_name_field).send_keys(last_name)
        self.driver.find_element(
            *self.postal_code_field).send_keys(postal_code)

    @allure.step("Нажать кнопку продолжить оформление")
    def click_continue(self) -> None:
        """
        Нажимает кнопку продолжения оформления заказа.
        """
        self.driver.find_element(*self.continue_button).click()

    @allure.step("Получить итоговую стоимость заказа")
    def get_total_cost(self) -> float:
        """
        Получает итоговую стоимость заказа.

        :return: float - итоговая сумма.
        """
        total_cost = self.driver.find_element(*self.total_cost_label).text
        return float(total_cost.split("$")[1])
