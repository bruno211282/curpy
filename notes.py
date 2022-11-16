"""Script de inicialización de CurPy."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication

from data.db_access import DbManager
from view.main_window import WellcomeDialog

if __name__ == "__main__":
    """Ejecución de aplicación con interfaz gráfica."""
    app = QApplication(sys.argv)
    dbm = DbManager()
    login = WellcomeDialog(dbm=dbm)

    login.exec_()

    sys.exit(app.exec_())
