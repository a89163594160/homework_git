import pytest
from UI_page import LoginPage
from UI_page import ProgectPage
from UI_page import TaskPage
from selenium import webdriver
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


@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Авторизация в личном кабинете.")
@allure.story("Авторизация с валидными данными.")
@pytest.mark.ui
def test_login(driver):
    """Проверяет авторизацию в личном кабинете.
    :param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    UI_page = LoginPage(driver, ("https://ru.yougile.com/team/"))

    UI_page.open_login_page()
    UI_page.enter_value()
    profile = UI_page.profile_text()
    assert profile == "Мой профиль"


@allure.severity(allure.severity_level.MINOR)
@allure.title("Редактирование профиля: установка статуса")
@allure.story("Установка статуса 'в командировке' в профиле пользователя.")
@pytest.mark.ui
def test_update_profile(driver):
    """
    Проверяет редактирование профиля: установка статуса.
    param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    UI_page = LoginPage(driver, ("https://ru.yougile.com/team/"))
    UI_page.open_login_page()
    UI_page.enter_value()
    UI_page.add_profile_status()
    status_profile = UI_page.status_text()
    assert status_profile == "В командировке"
    UI_page.delete_profile_status()


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Добавление нового проекта")
@allure.story("Отображение проекта на странице после добавления.")
@pytest.mark.ui
def test_add_new_project(driver):
    """
    Проверяет корректность отображения проекта на странице после добавления.
    param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    UI_page = LoginPage(driver, ("https://ru.yougile.com/team/"))
    UI_page.open_login_page()
    UI_page.enter_value()
    UI_page = ProgectPage(driver, ("https://ru.yougile.com/team/projects"))
    UI_page.add_project()
    assert "Проект" in driver.page_source


@allure.severity(allure.severity_level.MINOR)
@allure.title("Редактирование проекта: перемещение в архив")
@allure.story("Перемещение проекта в раздел 'Архивированные проекты'.")
@pytest.mark.ui
def test_add_project_to_archive(driver):
    """
    Проверяет перемещение проекта в архив.
    param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    UI_page = LoginPage(driver, ("https://ru.yougile.com/team/"))
    UI_page.open_login_page()
    UI_page.enter_value()
    UI_page = ProgectPage(driver, ("https://ru.yougile.com/team/projects"))
    UI_page.add_project()
    UI_page.add_archive_project()
    assert "Проект" in driver.page_source


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Добавление списка задач.")
@allure.story("Добавление списка для ранжирования задач.")
@pytest.mark.ui
def test_add_task_list(driver):
    """
    Проверяет корректность добавления списка задач,
    его отображение на странице.
    param driver: WebDriver — объект драйвера, переданный фикстурой.
    """
    UI_page = LoginPage(driver, ("https://ru.yougile.com/team/"))
    UI_page.open_login_page()
    UI_page.enter_value()
    UI_page = TaskPage(driver, ("https://ru.yougile.com/team/my-tasks"))
    UI_page.add_task_list()
    task_list_name = UI_page.task_list_text()
    assert task_list_name == 'New list'
