import requests
from config import MY_LOGIN
from config import MY_PASSWORD
import allure


class ProjectApi():
    """
    Класс страницы проектов.
    """
    def __init__(self, url):
        """Конструктор класса ProjectApi.
        :param url: str, URL страницы сайта.
        """
        self.url = url

    @allure.step("Получение токена авторизации.")
    def get_token(self, login=MY_LOGIN, password=MY_PASSWORD) -> str:
        """Отправляет в теле запроса логин и пароль
          и возвращает в ответе ключ авторизации.
          :param login: str, логин пользователя,
          :param password: str, пароль пользователя.
          """
        creds = {'login': login, 'password': password}
        resp = requests.post(self.url+'/api-v2/auth/keys/get', json=creds)
        return resp.json()[0]["key"]

    @allure.step("Получение списка проектов.")
    def get_project_list(self) -> list:
        """Возвращает список проектов."""
        my_token = self.get_token()
        my_headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + my_token}
        resp = requests.get(self.url + '/api-v2/projects', headers=my_headers)
        return resp

    @allure.step("Получение списка задач без ключа авторизации.")
    def get_task_list_without_token(self) -> str:
        """
        Отправляет запрос на получение списка без ключа авторизации,
        возвращает ошибку 401.
        """
        my_headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '}
        resp = requests.get(self.url + '/api-v2/task-list', headers=my_headers)
        return resp

    @allure.step("Создание новой задачи.")
    def create_task(self, title) -> str:
        """Создает новую задачу.
        :param title: str, название задачи.
        """
        my_token = self.get_token()
        my_headers = {
           'Content-Type': 'application/json',
           'Authorization': 'Bearer ' + my_token}
        new_task = {
            "title": title
            }
        resp = requests.post(self.url + '/api-v2/tasks', json=new_task,
                             headers=my_headers)
        return resp

    @allure.step("Удаление задачи.")
    def delete_task(self, id, del_task) -> str:
        """Удаляет созданную задачу, возвращает id удаленной задачи.
        :param id: str, id задачи,
        :param del_task: str, запрос на удаление задачи.
        """
        my_token = self.get_token()
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + my_token
        }
        del_task = {
            "deleted": True
        }
        resp = requests.put(
            self.url + (
                f'//api-v2/tasks/{id}'), json=del_task, headers=my_headers)
        return resp

    @allure.step("Получение задачи по id.")
    def get_task_id(self, id) -> str:
        """
        Возвращает id созданной задачи.
        :param id: str, id созданной задачи,
        """
        my_token = self.get_token()
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + my_token
        }
        resp = requests.get(self.url + f'/api-v2/tasks/{id}',
                            headers=my_headers)
        return resp.json()
