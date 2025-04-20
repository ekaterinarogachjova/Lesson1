from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from CartPage import CartPage
from CheckoutPage import CheckoutPage
from LoginPage import LoginPage
from MainPage import MainPage


def test_sauce_demo():
    options = Options()
    options.add_argument("--blink-settings=imagesEnabled=false")
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.get("https://www.saucedemo.com/")

        # Инициализация страниц
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        cart_page = CartPage(driver)
        checkout_page = CheckoutPage(driver)

        # Авторизация
        login_page.enter_username("standard_user")
        login_page.enter_password("secret_sauce")
        login_page.click_login()

        # Добавление товаров в корзину
        items_to_add = ["Sauce Labs Backpack",
                        "Sauce Labs Bolt T-Shirt", "Sauce Labs Onesie"]
        for item in items_to_add:
            main_page.add_item_to_cart(item)

        # Переход в корзину и оформление заказа
        main_page.go_to_cart()
        cart_page.click_checkout()

        # Заполнение формы оформления заказа
        checkout_page.fill_checkout_form("Екатерина", "Зубова", "357210")
        checkout_page.click_continue()

        # Проверка итоговой стоимости
        total_cost_value = checkout_page.get_total_cost()
        assert total_cost_value == 58.29, f"Итоговая сумма должна быть 58.29, но получено {total_cost_value}"  # noqa: E501

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        driver.quit()


test_sauce_demo()
