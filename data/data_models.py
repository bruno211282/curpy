from datetime import datetime


class Note:
    """Representa un modelo de nota para mantener su informacion.
    """

    def __init__(self, noteid: str = '', title: str = '', body: str = ''):
        """Constructor de una Nota.

        Args:
            noteid (str, optional): [El ID de una nota]. Defaults to ''.
            title (str, optional): [Titulo para la nota]. Defaults to ''.
            body (str, optional): [El cuerpo de la nota]. Defaults to ''.
        """

        self.noteid = noteid
        self.title = title
        self.body = body
        self.created_at = datetime.today()

    def __str__(self):
        return self.title

    def is_note_in_db(self):
        return True if self.noteid is None else False
