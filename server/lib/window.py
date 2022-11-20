import json
from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QThread

from lib.libsrv import Server


class LogWindow(QtWidgets.QMainWindow):

    def __init__(self):
        """Controlador de la ventana principal de la aplicacion."""

        super().__init__()
        uic.loadUi("resource/logwindow.ui", self)

        self.button.clicked.connect(self.toggle_start_stop)

    def start_server(self):
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
        """
        data = {
            "type": "login",
            "name": "nombre",
            "when": "2022/11/20"
        }
        """
        data = json.loads(data)
        if data["type"] == "login":
            itm = QtWidgets.QListWidgetItem(
                f"{data['name']} ingreso en: {data['when']}")
            self.login_box.addItem(itm)
        elif data["type"] == "signup":
            itm = QtWidgets.QListWidgetItem(
                f"{data['name']} se unio e ingreso en: {data['when']}")
            self.signup_box.addItem(itm)

    def stop_server(self):
        self.sthread.quit()

    def toggle_start_stop(self):
        if self.button.text() == "Iniciar":
            self.button.setText("Parar")
            self.start_server()
        elif self.button.text() == "Parar":
            self.button.setText("Iniciar")
            self.stop_server()
