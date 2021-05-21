"""Script de inicialización de CurPy."""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication
from view.window import WindowController
import sys


if __name__ == "__main__":
    """Ejecución de aplicación con interfaz gráfica."""
    app = QApplication(sys.argv)
    ui = WindowController()
    ui.main_window.show()
    sys.exit(app.exec_())
