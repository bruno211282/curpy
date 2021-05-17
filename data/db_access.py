import sqlite3
from data.data_models import Note, User

class DbManager:
    def __init__(self):
        self.db = sqlite3.connect('db.sqlite3')
        self._create_tables()

    def __del__(self):
        self.db.close()


    def _create_tables(self):
        with self.db as query:
            query.execute(
                """CREATE TABLE IF NOT EXISTS notes (
                    noteid INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    body TEXT
                    author TEXT
                )
                """
            )
            query.execute(
                """CREATE TABLE IF NOT EXISTS users (
                    user_name TEXT PRIMARY KEY
                )
                """
            )

    def create_note(self, note:Note):
        with self.db as query:
            query.execute(
                """
                INSERT INTO notes
                    (title, body)
                VALUES
                    (:title, :body)
                """,
                {'title': note.title, 'body': note.body}
            )

    def create_user(self, user:User):
        with self.db as query:
            query.execute(
                """
                INSERT INTO users
                    (user_name)
                VALUES
                    (:user_name)
                """,
                {'user_name': user.user_name}
            )

    def update_note(self, note:Note):
        with self.db as query:
            query.execute(
                """
                UPDATE
                    notes
                SET
                    title = :title,
                    body = :body
                WHERE
                    noteid = :noteid
                """,
                {'title': note.title, 'body': note.body, 'noteid': note.noteid}
            )

    def delete_note(self, noteid:int):
        with self.db as query:
            query.execute(
                """
                DELETE FROM
                    notes
                WHERE
                    noteid = :noteid
                """,
                {'noteid': noteid}
            )

    def get_note_from_id(self, noteid):
        query = self.db.execute(
            """
            SELECT
                title, body
            FROM
                notes
            WHERE
                noteid = :noteid
            """,
            {'noteid': noteid}
        )
        data = query.fetchone()
        return Note(
            noteid=noteid,
            title=data[0],
            body=data[1]
        )

    def get_list_of_notes(self):
        query = self.db.execute(
            """
            SELECT
                noteid, title, body
            FROM
                notes
            """
        )
        data = query.fetchall()
        notes = [
            Note(
                noteid=note[0],
                title=note[1],
                body=note[2]) for note in data
        ]
        return notes
    
    def get_list_of_users(self):
        query = self.db.execute(
            """
            SELECT
                user_name
            FROM
                users
            """
        )
        data = query.fetchall()
        users = [
            User(
                user_name=user[0]
            ) for user in data
        ]
        return users
