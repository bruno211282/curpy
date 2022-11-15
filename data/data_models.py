"""Modelos de datos para almacenar Notas y Usuarios."""
from datetime import datetime
from typing import Union


class User:
    """Representa un modelo de Usuario cargado al sistema."""

    def __init__(
        self,
        user_id: Union[int, None] = None,
        user_name: str = "",
        password: str = ""
    ):
        """Método constructor de un Usuario.

        Args:
            user_id (Union[int, None], optional): ID que asigna la DB al user.
                    Valor por defecto: None.
            user_name (str, optional): [description]. Nombre del usuario.
                    Valor por defecto: "".
            password (str, optional): [description]. Clave para el usuario.
                    Valor por defecto: "".
        """
        self.user_id = user_id
        self.user_name = user_name
        self.password = password

    def __str__(self) -> str:
        """Devuelve nombre del usuario.

        Returns:
            str: Nombre del usuario.
        """
        return self.user_name


class Note:
    """Representa un modelo de nota para mantener su información."""

    def __init__(
        self,
        noteid: Union[int, None] = None,
        title: str = '',
        body: str = '',
        author: Union[User, None] = None
    ):
        """Método constructor de una Nota.

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
        self.created_at = datetime.now()

    def __str__(self) -> str:
        """Devuelve el título de la nota.

        Returns:
            str: Título de la nota.
        """
        return self.title

    def is_note_in_db(self) -> bool:
        """Indica si la nota tiene asignado un ID de la Base de Datos.

        Returns:
            bool: True si está guardada.
        """
        return self.noteid is not None
