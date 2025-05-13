import unittest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from CartPage import CartPage
from CheckoutPage import CheckoutPage
from LoginPage import LoginPage
from MainPage import MainPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.feature("Покупка товаров")
class TestSauceDemo(unittest.TestCase):
    """
    Тестовый класс для проверки покупки товаров на сайте SauceDemo.
    """

    def setUp(self) -> None:
        """
        Инициализация драйвера и открытие главной страницы.
        """
        options = Options()
        options.add_argument("--blink-settings=imagesEnabled=false")
        service = ChromeService(
            executable_path=ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service, options=options)

    @allure.title("Проверка покупки товаров")
    @allure.description("Тест проверяет полный сценарий покупки нескольких товаров на сайте SauceDemo.")  # noqa: E501
    @allure.severity(allure.severity_level.CRITICAL)
    def test_sauce_demo(self) -> None:
        driver = self.driver
        with allure.step("Открыть страницу авторизации"):
            driver.get("https://www.saucedemo.com/")

        # Инициализация страниц
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        with allure.step("Авторизация пользователя"):
            login_page.enter_username("standard_user")
            login_page.enter_password("secret_sauce")
            login_page.click_login()
            #Ожидание алерта
            #WebDriverWait(driver, 20).until(EC.alert_is_present())
            #alert = driver.switch_to.alert
            #alert.accept()

        with allure.step("Добавление товаров в корзину"):
            items_to_add = [
                "Sauce Labs Backpack",
                "Sauce Labs Bolt T-Shirt",
                "Sauce Labs Onesie"
            ]
            for item in items_to_add:
                main_page.add_item_to_cart(item)

        with allure.step("Переход в корзину и оформление заказа"):
            main_page.go_to_cart()
            cart_page.click_checkout()

        with allure.step("Заполнение формы оформления заказа"):
            checkout_page.fill_checkout_form("Екатерина", "Зубова", "357210")
            checkout_page.click_continue()

        with allure.step("Проверка итоговой стоимости заказа"):
            total_cost_value = checkout_page.get_total_cost()
            expected_cost = 58.29
            self.assertEqual(
                total_cost_value,
                expected_cost,
                f"Итоговая сумма должна быть {expected_cost}, но получено {total_cost_value}"  # noqa: E501
            )

    def tearDown(self) -> None:
        """
        Закрывает браузер после теста.
        """
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
