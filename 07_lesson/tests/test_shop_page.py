import pytest
from selenium import webdriver
from pages.shop_page import LoginShopPage
from pages.shop_page import GoodsShopPage
from pages.shop_page import CheckoutShopPage
from pages.shop_page import FormShopPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_page(driver):
    shop_page = LoginShopPage(driver, "https://www.saucedemo.com/")
    shop_page.open_login_page()
    shop_page.login()
    shop_page = GoodsShopPage(
        driver, "https://www.saucedemo.com/inventory.html")
    shop_page.add_goods()
    shop_page = CheckoutShopPage(
        driver, "https://www.saucedemo.com/cart.html")
    shop_page.checkout_shop_cart()
    shop_page = FormShopPage(
        driver, "https://www.saucedemo.com/checkout-step-one.html")
    shop_page.fill_form()

    assert shop_page.total_result() == "Total: $58.29"
