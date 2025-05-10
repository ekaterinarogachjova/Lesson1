import unittest
import allure
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from CalculatorPage import CalculatorPage


class TestCalculator(unittest.TestCase):
    """
    Тестовый класс для проверки работы калькулятора.
    """

    def setUp(self) -> None:
        """
        Инициализация драйвера и открытие страницы калькулятора.
        """
        options = Options()
        options.add_argument("--blink-settings=imagesEnabled=false")
        service = ChromeService(
            executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)
        self.calculator_page = CalculatorPage(self.driver)
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"  # noqa: E501
        )

    @allure.title("Проверка сложения 7 + 8 с задержкой")
    @allure.description("Тест проверяет корректность работы калькулятора при сложении 7 и 8 с задержкой 45 секунд.")  # noqa: E501
    @allure.feature("Калькулятор")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_calculator_functionality(self) -> None:
        with allure.step("Установка задержки в 45 секунд"):
            self.calculator_page.set_delay("45")

        with allure.step("Нажатие кнопки '7'"):
            self.calculator_page.press_button_7()

        with allure.step("Нажатие кнопки '+'"):
            self.calculator_page.press_button_plus()

        with allure.step("Нажатие кнопки '8'"):
            self.calculator_page.press_button_8()

        with allure.step("Нажатие кнопки '='"):
            self.calculator_page.press_button_equals()

        with allure.step("Ожидание результата '15' на экране"):
            WebDriverWait(self.driver, 90).until(
                EC.text_to_be_present_in_element(
                    (By.CLASS_NAME, "screen"), "15")
            )

        with allure.step("Получение и проверка результата"):
            result = self.calculator_page.get_result()
            self.assertEqual(result, "15")

    def tearDown(self) -> None:
        """
        Закрывает браузер после теста.
        """
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
