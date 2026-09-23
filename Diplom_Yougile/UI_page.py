from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure
from config import MY_LOGIN
from config import MY_PASSWORD


class LoginPage():
    """
    Класс страницы авторизации.
    """
    LOGIN_INPYT = By.CSS_SELECTOR, ("[autocomplete='email']")
    PASSWORD_INPUT = (By.CSS_SELECTOR, "[autocomplete='current-password']")
    ENTER_BUTTON = (By.CSS_SELECTOR, ".bg-action-default[role='button']")
    MY_PROFILE_BUTTON = (By.CSS_SELECTOR, ".truncate.ml-6.text-14.leading-4")
    RES_STATUS = (By.XPATH, "(//div[@class='mb-24'])[1]")
    ADD_STATUS = (By.XPATH, "//span[contains(text(),'Установить статус')]")
    VALUE_STATUS = (By.XPATH, "//span[contains(text(),'В командировке')]")
    SAVE_STATUS = (By.XPATH, "//div[contains(text(),'Сохранить')]")
    DELETE_STATUS = (By.XPATH, "(//*[name()='svg'][@type='ui'])[3]")

    def __init__(self, driver, url):
        """
        Конструктор класса LoginPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :param url: str, URL страницы сайта.
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step("Открытие страницы авторизации.")
    def open_login_page(self):
        """
        Открывает страницу авторизации.
        """
        self.driver.get("https://ru.yougile.com/team/")

    @allure.step("Ввод логина и пароля.")
    def enter_value(self):
        """
        Вводит данные пользователя для авторизации.
        """
        self.wait.until(
            EC.presence_of_element_located(
                self.LOGIN_INPYT)).send_keys(MY_LOGIN)
        self.wait.until(
            EC.presence_of_element_located(
                self.PASSWORD_INPUT)).send_keys(MY_PASSWORD)
        self.wait.until(EC.presence_of_element_located(
                        self.ENTER_BUTTON)).click()

    @allure.step("Проверка успешной авторизации на странице")
    def profile_text(self) -> str:
        """Возвращает текст с кнопки перехода в профиль.

        :return: str — текст.
        """
        self.wait.until(
            EC.text_to_be_present_in_element(
                self.MY_PROFILE_BUTTON, "Мой профиль"))
        result_profile = self.driver.find_element(*self.MY_PROFILE_BUTTON)
        return result_profile.text

    @allure.step("Редактирование профиля: добавление статуса 'в командировке'")
    def add_profile_status(self):
        """Редактирует профиль, устанавливает статус профиля 'в командировке'.
        """
        self.wait.until(
            EC.presence_of_element_located((self.MY_PROFILE_BUTTON))).click()
        self.wait.until(
            EC.presence_of_element_located(self.ADD_STATUS)).click()
        self.wait.until(
            EC.presence_of_element_located(self.VALUE_STATUS)).click()
        self.wait.until(
            EC.presence_of_element_located(self.SAVE_STATUS)).click()

    @allure.step("Проверка успешного редактирования профиля.")
    def status_text(self) -> str:
        """Возвращает текст с кнопки статуса.

        :return: str — текст."""
        self.wait.until(
                    EC.text_to_be_present_in_element(
                        self.RES_STATUS, "В командировке"))
        result_status = self.driver.find_element(*self.RES_STATUS)
        return result_status.text

    @allure.step("Удаление статуса профиля.")
    def delete_profile_status(self):
        """
        Удаляет статус профиля
        """
        self.wait.until(
            EC.presence_of_element_located(self.DELETE_STATUS)).click()


class ProgectPage():
    """
    Класс страницы проектов.
    """
    MY_COMPANY_BUTTON = (By.XPATH, "//div[contains(text(),'Моя компания')]")
    PROJECT_BUTTON = (By.XPATH, "//span[contains(text(),'Добавить проект')]")
    PROJECT_WITH_TASK = (
        By.XPATH, "//div[contains(text(),'Проект с задачами')]")
    PROJECT_NAME_FORM = (
        By.CSS_SELECTOR, "input[placeholder='Введите название проекта…']")
    ADD_PROJECT_BUTTON = (
        By.XPATH, "//div[contains(text(),'Добавить проект с задачами')]")
    PANEL_PROJECT = (
        By.CSS_SELECTOR, "div[data-testid='panel-company-projects']")
    COMPANY_BTN = (By.XPATH, "//div[contains(text(),'Моя компания')]")
    PROJECT_BTN = (By.XPATH, "(//*[name()='svg'][@type='ui'])[13]")
    ADD_ARCHIVE_BTN = (By.XPATH, "//div[contains(text(),'Поместить в архив')]")
    ARCHIVE_BOX = (By.CSS_SELECTOR, "div[class='flex-none mr-4']")
    ARCHIVE_PANEL = (By.XPATH, "//div[@class='pt-8']")

    def __init__(self, driver, url):
        """
        Конструктор класса ProgectPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :param url: str, URL страницы сайта.
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step("Открытие страницы проектов.")
    def open_project_page(self):
        """
        Открывает страницу проектов.
        """
        self.driver.get("https://ru.yougile.com/team/projects")

    @allure.step("Добавление нового проекта.")
    def add_project(self):
        """
        Добавляет новый проект.
        """
        self.wait.until(
            EC.presence_of_element_located(self.MY_COMPANY_BUTTON)).click()
        self.wait.until(
            EC.presence_of_element_located(self.PROJECT_BUTTON)).click()
        self.wait.until(
            EC.presence_of_element_located(self.PROJECT_WITH_TASK)).click()
        self.wait.until(
            EC.presence_of_element_located(
                self.PROJECT_NAME_FORM)).send_keys("Проект")
        self.wait.until(
            EC.presence_of_element_located(self.ADD_PROJECT_BUTTON)).click()
        self.wait.until(
            EC.presence_of_element_located(self.MY_COMPANY_BUTTON)).click()
        self.wait.until(EC.presence_of_element_located(self.PANEL_PROJECT))

    @allure.step("Перемещение проекта в архив.")
    def add_archive_project(self):
        """Перемещает проект в папку 'Архив'
        """
        self.wait.until(
            EC.presence_of_element_located(self.COMPANY_BTN)).click()
        self.wait.until(
            EC.presence_of_element_located(self.PROJECT_BTN)).click()
        self.wait.until(
            EC.presence_of_element_located(self.ADD_ARCHIVE_BTN)).click()
        self.wait.until(
            EC.presence_of_element_located(self.ARCHIVE_BOX)).click()
        self.wait.until(EC.presence_of_element_located(self.ARCHIVE_PANEL))


class TaskPage():
    """
    Класс страницы задач.
    """
    TASK_TEXT = (By.XPATH, "//div[normalize-space()='New list']")
    MY_TASK_BTN = (By.XPATH, "//div[contains(text(),'Мои задачи')]")
    ADD_LIST = (By.XPATH, "//span[contains(text(),'Добавить список')]")
    LIST_NAME = (By.XPATH, "//input[@placeholder='Название списка']")

    def __init__(self, driver, url):
        """
        Конструктор класса TaskPage.
        :param driver: WebDriver — объект драйвера Selenium.
        :param url: str, URL страницы сайта.
        """
        self.driver = driver
        self.url = url
        self.wait = WebDriverWait(self.driver, 20)

    @allure.step("Открытие страницы задач.")
    def open_task_page(self):
        """
        Открывает страницу с задачами.
        """
        self.driver.get("https://ru.yougile.com/team/my-tasks")

    @allure.step("Добавление списка задач.")
    def add_task_list(self):
        """
        Добавляет список для ранжирования задач.
        """
        self.wait.until(
            EC.presence_of_element_located(self.MY_TASK_BTN)).click()
        self.wait.until(EC.presence_of_element_located(self.ADD_LIST)).click()
        self.wait.until(
            EC.presence_of_element_located(self.LIST_NAME)).send_keys(
                "New list")

    @allure.step("Проверка текстового значения в поле 'название списка'")
    def task_list_text(self) -> str:
        """Возвращает текст поля 'название списка'.
        :return: str — текст.
        """
        self.wait.until(EC.text_to_be_present_in_element(
            self.TASK_TEXT, "New list"))
        result_task = self.driver.find_element(*self.TASK_TEXT)
        return result_task.text
