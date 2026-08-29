from ProjectApi import ProjectApi

api = ProjectApi("https://ru.yougile.com")


def test_add_new_project_positive():
    title = 'Новый проект'
    resp = api.create_project(title)
    new_id = resp.json()["id"]
    project = api.get_project_id(new_id)
    assert resp.status_code == 201
    assert project["title"] == "Новый проект"


def test_rename_project_positive():
    title = 'Проект'
    result = api.create_project(title)
    new_id = result.json()["id"]
    new_title = 'Измененный проект'
    edited = api.update_project(new_id, new_title).json()
    assert edited["id"] == new_id
    assert result.status_code == 201


def test_get_project_id_positive():
    title = 'New'
    result = api.create_project(title)
    new_id = result.json()["id"]
    print(new_id)
    id_project = api.get_project_id(new_id)
    print(id_project)
    assert id_project["id"] == new_id
    assert result.status_code == 201


def test_add_new_project_negative():
    title = ''
    resp = api.create_project(title)
    assert resp.status_code == 400
    result = resp.json()['error']
    assert result == 'Bad Request'


def test_rename_project_negative():
    title = 'Проект'
    api.create_project(title)
    new_title = 'Измененный проект'
    invalid_id = 'abc'
    resp = api.update_project(invalid_id, new_title)
    message = resp.json()['error']
    assert message == 'Not Found'
    assert resp.status_code == 404


def test_get_project_id_negative():
    title = 'New'
    result = api.create_project(title).json()["id"]
    print(result)
    invalid_id = ' '
    resp = api.get_project_id(invalid_id)
    message = resp['error']
    assert message == 'Not Found'
