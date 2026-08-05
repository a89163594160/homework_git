from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 20)
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    first_name_form = wait.until(EC.presence_of_element_located(
        (By.NAME, "first-name")
    ))
    first_name_form.send_keys("Иван")

    last_name_form = wait.until(EC.presence_of_element_located(
        (By.NAME, "last-name")
    ))
    last_name_form.send_keys("Петров")

    address_form = wait.until(EC.presence_of_element_located(
        (By.NAME, "address")
    ))
    address_form.send_keys("Ленина, 55-3")

    city_form = wait.until(EC.presence_of_element_located(
        (By.NAME, "city")
    ))
    city_form.send_keys("Москва")

    country_form = wait.until(EC.presence_of_element_located(
        (By.NAME, "country")
    ))
    country_form.send_keys("Россия")

    email_form = wait.until(EC.presence_of_element_located(
        (By.NAME, "e-mail")
    ))
    email_form.send_keys("test@skypro.com")

    phone_form = wait.until(EC.presence_of_element_located(
        (By.NAME, "phone")
    ))
    phone_form.send_keys("+7985899998787")

    job_position_form = wait.until(EC.presence_of_element_located(
        (By.NAME, "job-position")
    ))
    job_position_form.send_keys("QA")

    company_form = wait.until(EC.presence_of_element_located(
        (By.NAME, "company")
    ))
    company_form.send_keys("SkyPro")

    submit_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "[type='submit']")
    ))
    submit_button.click()

    zip_code_form = driver.find_element(By.ID, "zip-code")
    color_zip_code = zip_code_form.value_of_css_property("border-color")
    assert "245, 194, 199" in color_zip_code

    forms = [
        ("first-name"),
        ("last-name"),
        ("address"),
        ("e-mail"),
        ("phone"),
        ("city"),
        ("country"),
        ("job-position"),
        ("company")
    ]

    for form_id in forms:
        form_element = wait.until(
            EC.visibility_of_element_located((By.ID, form_id)))
        border_color = form_element.value_of_css_property("border-color")
        assert "186, 219, 204" in border_color

    driver.quit()
