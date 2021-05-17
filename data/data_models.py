from datetime import datetime
from typing import Union


class Note:
    """Representa un modelo de nota para mantener su informacion.
    """

    def __init__(
        self,
        noteid: Union[int, None] = None,
        title: str = '',
        body: str = '',
        author: str = ''
    ):
        """Constructor de una Nota.

        Args:
            noteid (int, optional): [El ID de una nota]. Defaults to None.
            title (str, optional): [Titulo para la nota]. Defaults to ''.
            body (str, optional): [El cuerpo de la nota]. Defaults to ''.
            author (str, optional): [El autor de la nota]. Defaults to ''.
        """

        self.noteid = noteid
        self.title = title
        self.body = body
        self.author = author
        self.created_at = datetime.today()

    def __str__(self):
        return self.title

    def is_note_in_db(self):
        return False if self.noteid is None else True


class User:
    """Representa un modelo de Usuario cargado al sistema.
    """

    def __init__(
        self,
        user_id: Union[int, None] = None,
        user_name: str = ""
    ):
        """Constructor de un Usuario.

        Args:
            user_id (Union[int, None], optional): ID que asigna la DB al usuario.
                    Valor por defecto: None.
            user_name (str, optional): [description]. Nombre del usuario.
                    Valor por defecto: "".
        """

        self.user_id = user_id
        self.user_name = user_name

    def __str__(self) -> str:
        return self.user_name
