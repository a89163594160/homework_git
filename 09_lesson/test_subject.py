from sqlalchemy import create_engine
from SubjectTable import SubjectTable

db_connection_string = "postgresql://postgres:Kubink%401@localhost:5432/QA"
db = SubjectTable("postgresql://postgres:Kubink%401@localhost:5432/QA")


def test_db_connection():
    create_engine(db_connection_string)


def test_select():
    db = create_engine(db_connection_string)
    rows = db.execute("SELECT * FROM subject").fetchall()
    row1 = rows[0]

    assert row1["subject_title"] == "English"


def test_create_new_subject():
    max_id = db.get_max_id()
    id = max_id + 1
    title = 'Physical education'
    db.create_new_subject(id, title)
    rows = db.get_subject()
    row1 = rows[-1]
    id_to_delete = db.get_max_id()
    db.delete(id_to_delete)
    assert row1["subject_title"] == title


def test_edit_subject():
    max_id = db.get_max_id()
    new_id = max_id + 1
    title = "Art"
    db.create_new_subject(new_id, title)
    new_title = "Updated"
    db.edit_subject(new_id, new_title)
    rows = db.get_subject()
    row1 = rows[-1]
    db.delete(new_id)
    assert row1["subject_title"] == new_title


def test_delete_subject():
    max_id = db.get_max_id()
    id = max_id + 1
    title = 'Physical education'
    db.create_new_subject(id, title)
    db.delete(id)
    rows = db.get_subject()
    row1 = rows[-1]
    assert row1["subject_title"] != title
