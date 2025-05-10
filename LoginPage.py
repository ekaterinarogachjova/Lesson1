from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import allure


class LoginPage:
    """
    Класс для работы со страницей авторизации.
    """

    def __init__(self, driver: WebDriver) -> None:
        """
        Инициализация элементов страницы.

        :param driver: WebDriver - экземпляр Selenium WebDriver.
        """
        self.driver = driver
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя.

        :param username: str - имя пользователя.
        """
        self.driver.find_element(*self.username_field).send_keys(username)

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> None:
        """
        Вводит пароль.

        :param password: str - пароль.
        """
        self.driver.find_element(*self.password_field).send_keys(password)

    @allure.step("Нажать кнопку входа")
    def click_login(self) -> None:
        """
        Нажимает кнопку входа.
        """
        self.driver.find_element(*self.login_button).click()
