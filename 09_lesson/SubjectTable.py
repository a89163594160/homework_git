from sqlalchemy import create_engine
from sqlalchemy.sql import text


class SubjectTable:

    db_connection_string = "postgresql://postgres:Kubink%401@localhost:5432/QA"

    def __init__(self, connection_string):
        self.db = create_engine(connection_string)

    def create(self, title):
        sql = text(
            "INSERT INTO subject(\"subject_title\") VALUES (:new_title)")
        return self.db.execute(sql, new_title=title)

    def get_subject(self):
        return self.db.execute("SELECT * FROM subject").fetchall()

    def get_max_id(self):
        return self.db.execute(
            "SELECT MAX(\"subject_id\") FROM subject").fetchall()[-1][0]

    def create_new_subject(self, id, title):
        sql = text("INSERT INTO subject(subject_id, subject_title) VALUES \
                   (:new_id, :new_title)")
        return self.db.execute(sql, new_id=id, new_title=title)

    def delete(self, id):
        sql = text("DELETE FROM subject WHERE subject_id = :id_to_delete")
        return self.db.execute(sql, id_to_delete=id)

    def edit_subject(self, new_id, new_title):
        sql = text("UPDATE subject SET subject_title = :new_title WHERE \
                   subject_id = :new_id")
        return self.db.execute(sql, new_id=16, new_title="Updated")
