"""Script de inicialización de CurPy."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QApplication
from data.db_access import DbManager
from view.window import WindowController
import sys


if __name__ == "__main__":
    """Ejecución de aplicación con interfaz gráfica."""
    app = QApplication(sys.argv)
    dbm = DbManager()
    ui = WindowController(app, dbm)
    sys.exit(app.exec_())
