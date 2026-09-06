import pytest
from selenium import webdriver
from shop_page import LoginShopPage
from shop_page import GoodsShopPage
from shop_page import CheckoutShopPage
from shop_page import FormShopPage
import allure


@pytest.fixture
def driver():
    """
    Фикстура для инициализации и завершения работы драйвера.
    """
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Тестирование работы интернет-магазина")
@allure.description("Тест проверяет корректность работы основных функций "
                    "интернет-магазина")
@allure.feature("Оформление заказа")
def test_shop_page(driver):
    """Тест проверяет работу функций: авторизация, добавление товаров,
       заполнение формы доставки и формирование итоговой суммы.
       :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    shop_page = LoginShopPage(driver, "https://www.saucedemo.com/")
    with allure.step("Открытие страницы сайта"):
        shop_page.open_login_page()
    with allure.step("Ввод данных пользователя"):
        shop_page.login()
    shop_page = GoodsShopPage(
        driver, "https://www.saucedemo.com/inventory.html")
    with allure.step("Добавление товаров"):
        shop_page.add_goods()
    shop_page = CheckoutShopPage(
        driver, "https://www.saucedemo.com/cart.html")
    with allure.step("Подтверждение корзины"):
        shop_page.checkout_shop_cart()
    shop_page = FormShopPage(
        driver, "https://www.saucedemo.com/checkout-step-one.html")
    with allure.step("Заполнение формы доставки и получение "
                     "суммы покупок."):
        shop_page.fill_form()
    with allure.step("Сравнение суммы покупок с ожидаемым результатом"):
        assert shop_page.total_result() == "Total: $58.29"
