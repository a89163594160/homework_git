import pytest
from selenium import webdriver
from pages.calc_page import CalcPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calc(driver):
    calc_page = CalcPage(
        driver,
        (
         "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        ))
    calc_page.open_calc_page()
    calc_page.delay_value()
    calc_page.enter_nums()
    calc_page.final_value()
    assert calc_page.final_value() == "15"
