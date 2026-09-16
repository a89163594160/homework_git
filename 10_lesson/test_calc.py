import pytest
from selenium import webdriver
from calc_page import CalcPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тестирование работы калькулятора с задержкой")
@allure.description("Тест проверяет корректность работы калькулятора")
@allure.feature("Калькулятор")
def test_calc(driver):
    """
    Тест проверяет работу калькулятора с различными операциями.
    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    :return: str, результат арифметического действия.
    """
    calc_page = CalcPage(
        driver,
        (
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        ))
    with allure.step("Открыть страницу калькулятора"):
        calc_page.open_calc_page()
    with allure.step("Установить задержку калькулятора"):
        calc_page.delay_value()
    with allure.step("Ввести значения"):
        calc_page.enter_nums()
    with allure.step("Ожидание результата"):
        calc_page.final_value()
    with allure.step("Проверка результата"):
        assert calc_page.final_value() == "15"
