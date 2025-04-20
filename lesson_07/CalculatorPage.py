from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.ID, "delay")
        self.button_7 = (By.XPATH, "//span[text()='7']")
        self.button_plus = (By.XPATH, "//span[text()='+']")
        self.button_8 = (By.XPATH, "//span[text()='8']")
        self.button_equals = (By.XPATH, "//span[text()='=']")
        self.result_output = (By.CLASS_NAME, "screen")

    def set_delay(self, delay):
        delay_field = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.delay_input)
        )
        delay_field.clear()
        delay_field.send_keys(delay)

    def press_button_7(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_7)
        )
        button.click()

    def press_button_plus(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_plus)
        )
        button.click()

    def press_button_8(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_8)
        )
        button.click()

    def press_button_equals(self):
        button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.button_equals)
        )
        button.click()

    def get_result(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.result_output)
        ).text
