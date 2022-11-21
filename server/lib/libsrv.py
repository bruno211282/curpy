
from socketserver import TCPServer, StreamRequestHandler
from PyQt5.QtCore import QObject, pyqtSignal


class RequestHandler(StreamRequestHandler):
    """
    The request handler class for log server.
    """

    def handle(self):
        self.data = self.rfile.readline().strip()
        # aqui accedo a la señal para comunicar la data
        # recibida al thread principal.
        self.server.received.emit(self.data.decode())


class Server(QObject):
    # Definicion de signals para luego comunicar lo que sucede
    finished = pyqtSignal()
    received = pyqtSignal(str)

    def __init__(self, port: int, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.port = port

    def run(self):
        """Start the server."""
        HOST, PORT = "0.0.0.0", self.port

        with TCPServer((HOST, PORT), RequestHandler) as server:
            # aplico la signal al server para poder accederla luego
            setattr(server, "received", self.received)
            server.serve_forever()

        self.finished.emit()
