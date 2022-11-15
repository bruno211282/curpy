"""Administrador de Base de Datos."""
import sqlite3

from data.data_models import Note, User
from logger.logger import log_try_exc_deco


class DbManager:
    """Administrador de Base de Datos SQL."""

    def __init__(self):
        """Conecta el objeto 'db' con la DB SQL y crea las tablas."""
        self.db = sqlite3.connect('db.sqlite3')
        self._create_tables()

    def __del__(self):
        """Cierra la DB."""
        self.db.close()

    @log_try_exc_deco("create database tables")
    def _create_tables(self) -> None:
        """Ejecuta las queries necesarias para crear las tablas requeridas."""
        with self.db as query:
            query.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    user_name TEXT,
                    user_paswd TEXT
                )"""
            )
            query.execute(
                """
                CREATE TABLE IF NOT EXISTS notes (
                    noteid INTEGER PRIMARY KEY,
                    title TEXT NOT NULL,
                    body TEXT,
                    author TEXT REFERENCES users(user_id) ON DELETE CASCADE
                )"""
            )

    @log_try_exc_deco("execute db query to create new note")
    def create_note(self, note: Note) -> None:
        """Ejecuta la Query necesaria para la creación de una nota.

        Args:
            Note: Objeto instancia del modelo Note.
        """
        with self.db as query:
            query.execute(
                """
                INSERT INTO notes
                    (title, body, author)
                VALUES
                    (:title, :body, :author)
                """,
                {
                    'title': note.title,
                    'body': note.body,
                    'author': note.author.user_id
                }
            )

    @log_try_exc_deco("execute db query to create new user")
    def create_user(self, user: User) -> None:
        """Ejecuta la Query necesaria para la creación de un usuario.

        Args:
            User: Objeto instancia del modelo User.
        """
        with self.db as query:
            query.execute(
                """
                INSERT INTO users
                    (user_name, user_paswd)
                VALUES
                    (:user_name, :user_paswd)
                """,
                {
                    'user_name': user.user_name,
                    'user_paswd': user.password
                }
            )

    @log_try_exc_deco("execute db query to update existing note")
    def update_note(self, note: Note) -> None:
        """Ejecuta la Query necesaria para actualizar una nota existente.

        Args:
            Note: Objeto instancia del modelo Note.
        """
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

    @log_try_exc_deco("execute db query to delete existing note")
    def delete_note(self, noteid: int) -> None:
        """Ejecuta la Query necesaria para eliminar una nota existente.

        Args:
            int: ID de la nota a eliminar.
        """
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

    @log_try_exc_deco("execute db query to get a single note")
    def get_note_from_id(self, noteid: int) -> Note:
        """Busca una nota en la base de datos y la devuelve.

        Args:
            int: ID de la nota a obtener.

        Returns:
            Note: Nota obtenida.
        """
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

    @log_try_exc_deco("execute db query to get the list of notes")
    def get_list_of_notes(self) -> list:
        """Retorna lista de notas cargadas en la DB.

        Returns:
            list: Lista de objetos Note almacenadas en la DB.
        """
        query = self.db.execute(
            """
            SELECT
                noteid, title, body
            FROM
                notes
            """
        )
        data = query.fetchall()
        return [Note(
            noteid=note[0],
            title=note[1],
            body=note[2]
        ) for note in data]

    @log_try_exc_deco("execute db query to get the list of users")
    def get_list_of_users(self) -> list:
        """Retorna lista de usuarios cargados en la DB.

        Returns:
            list: Lista de objetos User almacenados en la DB.
        """
        query = self.db.execute(
            """
            SELECT
                user_id, user_name
            FROM
                users
            """
        )
        data = query.fetchall()
        return [User(user_id=user[0], user_name=user[1]) for user in data]
