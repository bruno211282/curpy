from PyQt5 import QtWidgets, uic


class LogWindow(QtWidgets.QMainWindow):

    def __init__(self):
        """Controlador de la ventana principal de la aplicacion."""

        super().__init__()
        uic.loadUi("resource/logwindow.ui", self)

        self.button.clicked.connect(self.toggle_start_stop)

    def start_server(self):
        pass

    def toggle_start_stop(self):
        if self.button.text() == "Iniciar":
            self.button.setText("Parar")
        elif self.button.text() == "Parar":
            self.button.setText("Iniciar")
