from datetime import datetime
import json
import socket


class LogSubscriber:
    """Observer que recibe mensajes del publisher.

    En particular se encarga de informar al server
    los eventos de login y signup.
    """

    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

    def inform_login(self, data: dict):
        data["type"] = "login"
        self.send_message(data)

    def inform_signup(self, data):
        data["type"] = "signup"
        self.send_message(data)

    def send_message(self, message):
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
    def __init__(self, events: list) -> None:
        """Observable que publica mensajes de acuerdo a
        diferentes eventos.

        Args:
            events (list): Lista de eventos soportados.

        {
            evento1 : {
                subscriber1: callable1,
                subscriber2: callable2
            },
            evento2 : {
                subscriber2: callable3
            }
        }
        """
        self.subscribers = {event: {} for event in events}

    def register(self, event: str, who: LogSubscriber, callback: callable):
        self.subscribers[event][who] = callback

    def dispatch(self, event: str, message: str):
        for _, callback in self.subscribers[event].items():
            callback(message)
