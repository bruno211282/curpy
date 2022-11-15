"""Script de inicialización de CurPy."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication

from data.db_access import DbManager
from view.main_window import WellcomeDialog, WindowController

if __name__ == "__main__":
    """Ejecución de aplicación con interfaz gráfica."""
    app = QApplication(sys.argv)
    dbm = DbManager()
    login = WellcomeDialog()

    if login.exec_():
        main = WindowController(dbm=dbm)
        main.show()

    sys.exit(app.exec_())
