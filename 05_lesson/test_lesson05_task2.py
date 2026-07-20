from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()

    driver.get("https://httpbin.org/forms/post")
    driver.maximize_window()

    name_field = driver.find_element(By.NAME, "custname")
    name_field.send_keys("Елена")

    submit_button = driver.find_element(
        By.XPATH, "//button[text()='Submit order']")

    previous_url = driver.current_url

    submit_button.click()
    new_url = driver.current_url
    assert new_url != previous_url
    print(driver.current_url)

    driver.quit()
