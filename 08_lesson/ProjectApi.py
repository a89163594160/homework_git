import requests
from config import MY_LOGIN
from config import MY_PASSWORD


class ProjectApi():
    def __init__(self, url):
        self.url = url

    def get_token(self, login=MY_LOGIN, password=MY_PASSWORD):
        creds = {'login': login, 'password': password}
        resp = requests.post(self.url+'/api-v2/auth/keys/get', json=creds)
        return resp.json()[0]["key"]

    def create_project(self, title):
        my_token = self.get_token()
        my_headers = {
           'Content-Type': 'application/json',
           'Authorization': 'Bearer ' + my_token}
        new_project = {
            "title": title
            }
        resp = requests.post(self.url + '/api-v2/projects', json=new_project,
                             headers=my_headers)
        return resp

    def update_project(self, id, new_title):
        my_token = self.get_token()
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + my_token
        }
        new_project = {
            "title": new_title
        }
        resp = requests.put(self.url + f'/api-v2/projects/{id}',
                            json=new_project, headers=my_headers)
        return resp

    def get_project_id(self, id):
        my_token = self.get_token()
        my_headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + my_token
        }
        resp = requests.get(self.url + f'/api-v2/projects/{id}',
                            headers=my_headers)
        return resp.json()
