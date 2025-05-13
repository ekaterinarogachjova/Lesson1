from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class CalculatorPage:
    """
    Класс-обертка для взаимодействия с калькулятором на странице.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализирует элементы страницы калькулятора.

        :param driver: WebDriver - экземпляр Selenium WebDriver.
        """
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.result_output = (By.CLASS_NAME, "screen")

    @allure.step("Установить задержку: {delay}")
    def set_delay(self, delay: str) -> None:
        """
        Устанавливает задержку вычисления.

        :param delay: str - значение задержки в секундах.
        """
        delay_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.delay_input)
        )
        delay_field.clear()
        delay_field.send_keys(delay)

    @allure.step("Нажать кнопку '7'")
    def press_button_7(self) -> None:
        """
        Нажимает кнопку '7' на калькуляторе.
        """
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_7)
        )
        button.click()

    @allure.step("Нажать кнопку '+'")
    def press_button_plus(self) -> None:
        """
        Нажимает кнопку '+' на калькуляторе.
        """
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_plus)
        )
        button.click()

    @allure.step("Нажать кнопку '8'")
    def press_button_8(self) -> None:
        """
        Нажимает кнопку '8' на калькуляторе.
        """
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_8)
        )
        button.click()

    @allure.step("Нажать кнопку '='")
    def press_button_equals(self) -> None:
        """
        Нажимает кнопку '=' для получения результата.
        """
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_equals)
        )
        button.click()

    @allure.step("Получить результат вычисления")
    def get_result(self) -> str:
        """
        Получает результат вычисления с экрана калькулятора.

        :return: str - результат вычисления.
        """
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.result_output)
        ).text
