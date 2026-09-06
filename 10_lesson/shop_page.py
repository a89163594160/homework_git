from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class LoginShopPage():
    """
    Класс авторизации на странице магазина.
    """
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOG_BTN = (By.ID, "login-button")

    def __init__(self, driver, url):
        """Инициализация конструктора класса LoginShopPage.
           :param driver: WebDriver — объект драйвера Selenium.
           :param url: str, URL страницы сайта.
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 25)

    @allure.step("Открыть страницу авторизации")
    def open_login_page(self):
        """
        Открывает страницу авторизации пользователя.
        """
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Ввести пароль и логин, перейти на страницу товаров.")
    def login(self):
        """
        Вводит данные в форму и авторизует пользователя на сайте.
        """
        username = self.wait.until(EC.presence_of_element_located(
            self.USERNAME))
        username.send_keys("standard_user")
        password = self.wait.until(EC.presence_of_element_located(
            self.PASSWORD))
        password.send_keys("secret_sauce")
        log_btn = self.wait.until(EC.presence_of_element_located(self.LOG_BTN))
        log_btn.click()


class GoodsShopPage():
    """
    Класс страницы добавления товаров.
    """
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    SHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")

    def __init__(self, driver, url):
        """Инициализация конструктора класса GoodsShopPage.
            :param driver: WebDriver — объект драйвера Selenium.
            :param url: str, URL страницы сайта.
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step("Добавить товары в корзину.")
    def add_goods(self):
        """
        Добавление товара в корзину.
        """
        backpack = self.wait.until(EC.presence_of_element_located(
            self.BACKPACK))
        backpack.click()
        shirt = self.wait.until(EC.presence_of_element_located(
            self.SHIRT))
        shirt.click()
        onesie = self.wait.until(EC.presence_of_element_located(
            self.ONESIE))
        onesie.click()


class CheckoutShopPage():
    """
    Класс управления содержимым корзины.
    """
    SHOP_CART = (By.ID, "shopping_cart_container")
    CHECKOUT_BTN = (By.ID, "checkout")

    def __init__(self, driver, url):
        """Инициализация конструктора класса CheckoutShopPage.
            :param driver: WebDriver — объект драйвера Selenium.
            :param url: str, URL страницы сайта.
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step("Подтверждаем покупку и переходим на страницу данных "
                 "покупателя")
    def checkout_shop_cart(self):
        """
        Проверка и подтверждение содержания корзины.
        """
        shop_cart = self.wait.until(EC.presence_of_element_located(
            self.SHOP_CART))
        shop_cart.click()
        checkout_btn = self.wait.until(EC.presence_of_element_located(
            self.CHECKOUT_BTN))
        checkout_btn.click()


class FormShopPage():
    """
    Класс формы заполнения данных покупателя, содержит
    итоговую сумму покупки.
    """
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    TOTAL_SUM = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver, url):
        """Инициализация конструктора класса FormShopPage.
            :param driver: WebDriver — объект драйвера Selenium.
            :param url: str, URL страницы сайта.
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step("Заполнить данные покупателя.")
    def fill_form(self):
        """Заполнение формы данных покупателя.
        """
        first_name = self.wait.until(EC.presence_of_element_located(
            self.FIRST_NAME))
        first_name.send_keys("Елена")
        last_name = self.wait.until(EC.presence_of_element_located(
            self.LAST_NAME))
        last_name.send_keys("Старкова")
        zip_code = self.wait.until(EC.presence_of_element_located(
            self.ZIP_CODE))
        zip_code.send_keys("123456")
        continue_btn = self.wait.until(EC.presence_of_element_located(
            self.CONTINUE_BTN))
        continue_btn.click()

    @allure.step("Ждём появления итоговой суммы покупки.")
    def get_total(self):
        """Ожидание появление на странице общей суммы покупки.
        """
        self.wait.until(EC.presence_of_element_located(
            self.TOTAL_SUM
        ))

    @allure.step("Сравниваем полученную сумму покупки с ожидаемой")
    def total_result(self) -> str:
        """Функция возвращает общую сумму покупки.
           :return: str, результат сложения стоимости товаров.
        """
        self.wait.until(EC.text_to_be_present_in_element(
            self.TOTAL_SUM, "Total: $58.29"))
        result_element = self.driver.find_element(*self.TOTAL_SUM)
        return result_element.text
