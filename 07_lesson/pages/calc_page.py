from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage():
    DELAY_INPYT = (By.CSS_SELECTOR, "#delay")
    RESULT_SCREEN = (By.CSS_SELECTOR, ".screen")

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 50)

    def open_calc_page(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def delay_value(self):
        delay_input = self.wait.until(
            EC.presence_of_element_located(self.DELAY_INPYT))
        delay_input.clear()
        delay_input.send_keys(45)

    def enter_nums(self):
        buttons = ["7", "+", "8", "="]
        for button in buttons:
            xpath = f"//span[text()='{button}']"
            self.driver.find_element(By.XPATH, xpath).click()

    def final_value(self):
        self.wait.until(
            EC.text_to_be_present_in_element(self.RESULT_SCREEN, "15"))
        result_value = self.driver.find_element(*self.RESULT_SCREEN)
        return result_value.text
