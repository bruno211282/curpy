"""Script de inicialización de CurPy."""
# !/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication

from data.db_access import DbManager
from logger.pubsub import LogSubscriber, Publisher
from view.main_window import WellcomeDialog

if __name__ == "__main__":
    """Ejecución de aplicación con interfaz gráfica."""
    app = QApplication(sys.argv)
    if len(sys.argv) == 1:
        host = "127.0.0.1"
        port = 9999
    elif len(sys.argv) == 3:
        host = sys.argv[1]
        port = sys.argv[2]
    else:
        print(
            """Missing arguments...
How to run:

1. python notes.py <- With no arguments HOST and PORT take the default values.
2. python notes.py 10.0.0.15 5689 <- Specifying HOST and PORT in arguments.

Default values:
    HOST: 127.0.0.1
    PORT: 9999"""
        )
        sys.exit(1)

    dbm = DbManager()

    sub = LogSubscriber(host, port)

    pub = Publisher(["login", "signup"])
    pub.register("login", sub, sub.inform_login)
    pub.register("signup", sub, sub.inform_signup)

    login = WellcomeDialog(dbm=dbm, pub=pub)
    login.exec_()

    sys.exit(app.exec_())
