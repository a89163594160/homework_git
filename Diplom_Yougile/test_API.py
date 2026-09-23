from API_page import ProjectApi
import requests
from config import MY_LOGIN
from config import MY_PASSWORD
import allure
import pytest

api = ProjectApi("https://ru.yougile.com")
base_url = "https://ru.yougile.com"


@allure.severity(allure.severity_level.BLOCKER)
@allure.title("Получение ключа авторизации с валидным логином и паролем.")
@allure.story("Проверка корректности получения ключа авторизации.")
@pytest.mark.api
def test_get_token_positive(login=MY_LOGIN, password=MY_PASSWORD):
    """
    Тест проверяет корректность получения ключа авторизации.
    param login: str, логин пользователя,
    param password: str, пароль пользователя
    """
    creds = {'login': login, 'password': password}
    resp = requests.post(base_url+'/api-v2/auth/keys/get', json=creds)
    assert resp.status_code == 200


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Получение списка проектов.")
@allure.story("Корректность получения списка проектов с названием и id.")
@pytest.mark.api
def test_get_project_list_positive():
    """
    Проверяет корректность получения списка проектов,
    возвращает список проектов с названием и id.
    """
    result = api.get_project_list()
    assert result.status_code == 200


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Добавление задачи.")
@allure.story("Проверка добавления новой задачи.")
@pytest.mark.api
def test_add_new_task_positive():
    """
    Проверяет создание новой задачи по заголовку.
    """
    title = 'Новая задача'
    resp = api.create_task(title)
    new_id = resp.json()["id"]
    project = api.get_task_id(new_id)
    assert resp.status_code == 201
    assert project["title"] == "Новая задача"


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Удаление задачи.")
@allure.story("Проверка удаления новой задачи.")
@pytest.mark.api
def test_delete_task_positive():
    """
    Добавляет новую задачу и проверяет её удаление по id.
    """
    title = 'New task'
    result = api.create_task(title)
    new_id = result.json()["id"]
    edited = api.delete_task(new_id, title).json()
    assert edited["id"] == new_id
    assert result.status_code == 201


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Негативный тест: добавление задачи с пустым заголовком.")
@allure.story("Проверка добавления задачи без обязательного поля заголовок.")
@pytest.mark.api
def test_add_new_project_negative():
    """Негативный тест: проверяет добавление задачи с пустым обязательным
    полем заголовок.
    """
    title = ''
    resp = api.create_task(title)
    assert resp.status_code == 400
    result = resp.json()['error']
    assert result == 'Bad Request'


@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Негативный тест: получение списка задач без токена.")
@allure.story("Получение списка задач без обязательного токена.")
@pytest.mark.api
def test_get_task_list_negative():
    """Негативный тест: получение списка задач без обязательного
    ключа авторизации."""
    resp = api.get_task_list_without_token()
    assert resp.status_code == 401
    result = resp.json()['error']
    assert result == 'Unauthorized'
