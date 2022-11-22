"""Funcionalidades relacionadas a la lógica de control de la ventana principal de la aplicación."""
import json
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread, Qt

from lib.libsrv import Server


class LogWindow(QtWidgets.QMainWindow):

    def __init__(self):
        """Controlador de la ventana principal de la aplicacion."""

        super().__init__()
        uic.loadUi("resource/logwindow.ui", self)

        self.button.clicked.connect(self._toggle_start_stop)

    def start_server(self):
        """Inicia la ejecucion del thread con el server TCP."""

        port = int(self.port_number.text())
        self.sthread = QThread()
        self.server = Server(port)
        self.server.moveToThread(self.sthread)
        # Connect signals and slots
        self.sthread.started.connect(self.server.run)
        self.server.finished.connect(self.sthread.quit)
        self.server.finished.connect(self.server.deleteLater)
        self.server.received.connect(self.process_data)
        self.sthread.finished.connect(self.sthread.deleteLater)
        self.sthread.start()

    def process_data(self, data):
        """Publica los mensajes recibidos en la ventana principal de la aplicación.

        Args:
            data (dict): Diccionario con la informacion a publicar. Ej:

        data = {
            "type": "login",
            "name": "nombre",
            "result": "success"
            "when": "2022/11/20"
        }
        """
        data = json.loads(data)

        try:
            desc = data['desc']
        except KeyError:
            desc = ""

        messages = {
            "signup": {
                "success": f"[{data['when']}] -> [Se acaba de generar el usuario {data['name']}]",
                "error": f"[{data['when']}] -> [Generacion de usuario erroneo: {desc}"
            },
            "login": {
                "success": f"[{data['when']}] -> [Acaba de ingresar el usuario {data['name']}]",
                "error": f"[{data['when']}] -> [Ingreso de usuario erroneo: {desc}"
            }
        }

        itm = QtWidgets.QListWidgetItem(
            messages[data["type"]][data["result"]]
        )

        if data["result"] == "error":
            itm.setForeground(Qt.red)

        if data["type"] == "login":
            self.login_box.addItem(itm)
        elif data["type"] == "signup":
            self.signup_box.addItem(itm)

    def stop_server(self):
        """Finaliza la ejecucion del server."""
        self.sthread.quit()

    def _toggle_start_stop(self):
        if self.button.text() == "Iniciar":
            self.button.setText("Parar")
            self.start_server()
        elif self.button.text() == "Parar":
            self.button.setText("Iniciar")
            self.stop_server()
