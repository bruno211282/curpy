from PyQt5.QtWidgets import QApplication
import sys


from lib.window import LogWindow


if __name__ == "__main__":
    """Ejecución de aplicación con interfaz gráfica."""
    app = QApplication(sys.argv)

    window = LogWindow()
    window.show()

    sys.exit(app.exec_())
