"""Funcionalidades relacionadas a los sockets: RequestHandler y TCPServer"""
from socketserver import TCPServer, StreamRequestHandler
from PyQt5.QtCore import QObject, pyqtSignal


class RequestHandler(StreamRequestHandler):
    """
    Handler encargado de manejar cada request que llega al server TCP.

    Cuando se recibe un request, éste handler la toma para luego transferirla via el server
    mediante una señal del framework QT al thread principal para poder actualizar el
    comportamiento de la ventana acorde a la informacion recibida.
    """

    def handle(self):
        self.data = self.rfile.readline().strip()
        # aqui accedo a la señal para comunicar la data
        # recibida al thread principal.
        # Aqui `server` es la instancia del servidor TCP
        self.server.received.emit(self.data.decode())


class Server(QObject):
    """Servidor encargado de recibir los mensajes de registro e ingreso de usuarios al sistema.

    El servidor se encuentra implementado como un QObject dentro de un thread para no bloquear el
    thread principal donde corre el loop de la ventana (Interfaz de usuario).
    """
    finished = pyqtSignal()
    received = pyqtSignal(str)

    def __init__(self, port: int, *args, **kwargs):
        """Servidor encargado de recibir los mensajes de registro e ingreso de usuarios al sistema.

        Args:
            port (int): Puerto donde el server escuchará.
        """
        super().__init__(*args, **kwargs)
        self.port = port

    def run(self):
        """Iniciar el server."""
        HOST, PORT = "0.0.0.0", self.port

        with TCPServer((HOST, PORT), RequestHandler) as server:
            # aplico la signal al server para poder accederla luego
            setattr(server, "received", self.received)
            server.serve_forever()

        self.finished.emit()
