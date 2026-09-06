from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import allure


class CalcPage():
    """
    Класс страницы калькулятора.
    """
    DELAY_INPYT = (By.CSS_SELECTOR, "#delay")
    RESULT_SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver, url):
        """
        Конструктор класса CalcPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :param url: str, URL страницы сайта.
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 50)

    @allure.step("Открытие страницы калькулятора.")
    def open_calc_page(self):
        """
        Открывает страницу калькулятора.
        """
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    @allure.step("Установка задержки калькулятора.")
    def delay_value(self) -> int:
        """
        Устанавливает задержку калькулятора.
        """
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPYT))
        delay_input.clear()
        delay_input.send_keys(45)
        sleep(5)

    @allure.step("Нажатие кнопок калькулятора.")
    def enter_nums(self):
        """
        Нажимает на несколько кнопок калькулятора по очереди.
        :param buttons: list[str] — список текстов на кнопках,
        которые нужно нажать.
        """
        buttons = ["7", "+", "8", "="]
        for button in buttons:
            xpath = f"//span[text()='{button}']"
            self.driver.find_element(By.XPATH, xpath).click()

    def final_value(self) -> str:
        """
        Возвращает текущий результат с экрана калькулятора.

        :return: str — текст результата на экране калькулятора.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT_SCREEN, "15"))
        result_value = self.driver.find_element(*self.RESULT_SCREEN)
        return result_value.text
