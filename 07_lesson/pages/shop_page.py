from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginShopPage():
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOG_BTN = (By.ID, "login-button")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 25)

    def open_login_page(self):
        self.driver.get("https://www.saucedemo.com/")

    def login(self):
        username = self.wait.until(EC.presence_of_element_located(
            self.USERNAME))
        username.send_keys("standard_user")
        password = self.wait.until(EC.presence_of_element_located(
            self.PASSWORD))
        password.send_keys("secret_sauce")
        log_btn = self.wait.until(EC.presence_of_element_located(self.LOG_BTN))
        log_btn.click()


class GoodsShopPage():
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    SHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 20)

    def add_goods(self):
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
    SHOP_CART = (By.ID, "shopping_cart_container")
    CHECKOUT_BTN = (By.ID, "checkout")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 20)

    def checkout_shop_cart(self):
        shop_cart = self.wait.until(EC.presence_of_element_located(
            self.SHOP_CART))
        shop_cart.click()
        checkout_btn = self.wait.until(EC.presence_of_element_located(
            self.CHECKOUT_BTN))
        checkout_btn.click()


class FormShopPage():
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    ZIP_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    TOTAL_SUM = (By.CLASS_NAME, "summary_total_label")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 20)

    def fill_form(self):
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

    def get_total(self):
        self.wait.until(EC.presence_of_element_located(
            self.TOTAL_SUM
        ))

    def total_result(self):
        self.wait.until(EC.text_to_be_present_in_element(
            self.TOTAL_SUM, "Total: $58.29"))
        result_element = self.driver.find_element(*self.TOTAL_SUM)
        return result_element.text
