from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_shop():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 20)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")

    username = wait.until(EC.presence_of_element_located(
        (By.ID, "user-name")
    ))
    username.send_keys("standard_user")

    password = wait.until(EC.presence_of_element_located(
        (By.ID, "password")
    ))
    password.send_keys("secret_sauce")

    log_btn = wait.until(EC.element_to_be_clickable(
        (By.ID, "login-button")))
    log_btn.click()

    backpack = driver.find_element(By.NAME, "add-to-cart-sauce-labs-backpack")
    backpack.click()
    shirt = driver.find_element(By.NAME, "add-to-cart-sauce-labs-bolt-t-shirt")
    shirt.click()
    onesie = driver.find_element(By.NAME, "add-to-cart-sauce-labs-onesie")
    onesie.click()

    shop_cart = driver.find_element(By.ID, "shopping_cart_container")
    shop_cart.click()

    checkout_btn = driver.find_element(By.ID, "checkout")
    checkout_btn.click()

    first_name = driver.find_element(By.ID, "first-name")
    first_name.send_keys("Елена")
    last_name = driver.find_element(By.ID, "last-name")
    last_name.send_keys("Старкова")
    zip_code = driver.find_element(By.ID, "postal-code")
    zip_code.send_keys("123456")

    continue_btn = driver.find_element(By.ID, "continue")
    continue_btn.click()

    total_sum = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_sum.text
    expected_total = "Total: $58.29"
    assert total_text == expected_total

    driver.quit()
