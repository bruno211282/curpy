"""Registro de mensajes de acceso al sistema y generacion de usuarios."""
from datetime import datetime
import json
import socket


class LogSubscriber:
    """Observer que recibe mensajes del publisher.

    Este Subscriber en particular se encarga de informar al server los eventos de login y signup.
    El observer (subscriber) recibe los mensajes del observable (publisher) mediante
    dos diferentes callables: `inform_login` e `inform_signup`

    Ambos aceptan un diccionario como argumento mediante el cual se pasa la informacion necesaria
    que luego se envia al server de registro.
    Si el server no se encuentra escuchando eventos el error es ignorado completamente.
    """

    def __init__(self, host: str, port: int) -> None:
        """Observer que recibe mensajes del publisher.

        Args:
            host (str): Direccion IP del server
            port (int): Puerto del server
        """

        self.host = host
        self.port = port

    def inform_login(self, data: dict):
        """Método mediante el cual se informa un evento de login.

        Args:
            data (dict): Debe contener los ítems: 'name' y 'result' como mínimo.
            Se acepta cualquier otro ítem adicional.
        """
        data["type"] = "login"
        self._send_message(data)

    def inform_signup(self, data):
        """Método mediante el cual se informa un evento de signup.

        Args:
            data (dict): Debe contener los ítems: 'name' y 'result' como mínimo.
            Se acepta cualquier otro ítem adicional.
        """
        data["type"] = "signup"
        self._send_message(data)

    def _send_message(self, message):
        message["when"] = f"{datetime.now().strftime('%Y-%m-%d %H:%M')}"
        data = json.dumps(message)

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
                # Connect to server and send data
                sock.connect((self.host, self.port))
                sock.sendall(bytes(data + "\n", "utf-8"))
        except ConnectionRefusedError:
            print("Server is not listening...")


class Publisher:
    """Observable que publica mensajes de acuerdo a diferentes eventos.

    Al instanciar el Publisher se define una lista de eventos a los cuales
    cada subscriptor puede luego subscribirse.
    Cada subscriptor se registra utilizando el método `register`.
    Cuando se quiere informar de un evento, se utiliza el método `dispatch`.
    """

    def __init__(self, events: list) -> None:
        """Observable que publica mensajes de acuerdo a diferentes eventos.

        Args:
            events (list): Lista de eventos para los cuales el publisher ofrece actualizaciones.
        """
        self.subscribers = {event: {} for event in events}

    def register(self, event: str, who: LogSubscriber, callback: callable):
        """Registra un Subscriptor en la lista de subscriptores.

        Args:
            event (str): Evento al cual el subscriptor se subscribe.
            who (Subscriber): Subscriptor.
            callback (callable): callback que el publisher utilizará cuando
            deba informar al subscriptor.
        """
        self.subscribers[event][who] = callback

    def dispatch(self, event: str, message: str):
        """Informa de un evento en particular a los subscriptores registrados.

        Args:
            event (str): Evento del que se está informando. Debe ser uno del eventos soportados.
            message (str): Mensaje mediante el cual se informa del evento ocurrido.
        """
        for _, callback in self.subscribers[event].items():
            callback(message)
