"""Controlador de ventana principal."""
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resource/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from view.new_user_window import NewUserController
from PyQt5 import QtCore, QtWidgets

from data.db_access import DbManager
from data.data_models import Note
from data.data_models import User


class WindowLayout:
    """Se definen los componentes de la ventana y su ubicacion.

    En la clase se definen todos los componentes de la ventana
    y como se ubican dentro de la misma.
    """

    def __init__(self) -> None:
        """Parámetros y objetos necesarios para ubicación de elementos UI."""
        # Main Window
        self.main_window = QtWidgets.QMainWindow()
        self.main_window.resize(912, 700)
        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 891, 641))

        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.notes_list = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.notes_list.setObjectName("notes_list")
        self.verticalLayout_2.addWidget(self.notes_list)

        spacerItem1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.verticalLayout_2.addItem(spacerItem1)

        self.btn_delete = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_delete.setObjectName("btn_delete")
        self.verticalLayout_2.addWidget(self.btn_delete)

        self.gridLayout.addLayout(self.verticalLayout_2, 3, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Minimum,
            QtWidgets.QSizePolicy.Expanding
        )
        self.gridLayout.addItem(spacerItem2, 3, 1, 1, 1)

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_filter = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_filter.setObjectName("label_filter")
        self.horizontalLayout_2.addWidget(self.label_filter)

        spacerItem3 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Preferred,
            QtWidgets.QSizePolicy.Minimum
        )
        self.horizontalLayout_2.addItem(spacerItem3)

        self.line_filter = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_filter.setObjectName("line_filter")
        self.horizontalLayout_2.addWidget(self.line_filter)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_new_user = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_new_user.setMinimumSize(QtCore.QSize(200, 0))
        self.btn_new_user.setObjectName("btn_new_user")
        self.horizontalLayout_3.addWidget(
            self.btn_new_user,
            0,
            QtCore.Qt.AlignLeft
        )

        self.btn_new = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_new.setMinimumSize(QtCore.QSize(200, 0))
        self.btn_new.setObjectName("btn_new")
        self.horizontalLayout_3.addWidget(
            self.btn_new,
            0,
            QtCore.Qt.AlignRight
        )
        self.gridLayout.addLayout(self.horizontalLayout_3, 1, 2, 1, 1)

        # Titulo de la nota
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_title = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_title.setObjectName("label_title")
        self.horizontalLayout_4.addWidget(self.label_title)

        self.note_title = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.note_title.setMinimumSize(QtCore.QSize(310, 0))
        self.note_title.setPlaceholderText("")
        self.note_title.setObjectName("note_title")
        self.horizontalLayout_4.addWidget(
            self.note_title,
            0,
            QtCore.Qt.AlignRight
        )
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.verticalLayout.addItem(spacerItem2)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_new_user = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_new_user.setObjectName("label_new_user")
        self.horizontalLayout_5.addWidget(
            self.label_new_user,
            0,
            QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )

        self.user_list = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.user_list.setMinimumSize(QtCore.QSize(310, 0))
        self.user_list.setIconSize(QtCore.QSize(16, 16))
        self.user_list.setObjectName("user_list")
        self.horizontalLayout_5.addWidget(
            self.user_list,
            0,
            QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter
        )
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        spacerItem4 = QtWidgets.QSpacerItem(
            40,
            10,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.verticalLayout.addItem(spacerItem4)
        self.notes_text = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.notes_text.setObjectName("notes_text")
        self.verticalLayout.addWidget(self.notes_text)

        spacerItem5 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.verticalLayout.addItem(spacerItem5)

        self.btn_save = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.btn_save.setObjectName("btn_save")
        self.verticalLayout.addWidget(self.btn_save)

        self.gridLayout.addLayout(self.verticalLayout, 3, 2, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(
            40,
            15,
            QtWidgets.QSizePolicy.Expanding,
            QtWidgets.QSizePolicy.Minimum
        )
        self.gridLayout.addItem(spacerItem6, 2, 2, 1, 1)

        self.main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 913, 20))
        self.menubar.setObjectName("menubar")
        self.main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.main_window)
        self.statusbar.setObjectName("statusbar")
        self.main_window.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(self.main_window)

        self.main_window.setWindowTitle("MainWindow")
        self.btn_delete.setText("Eliminar Nota Seleccionada")
        self.label_filter.setText("Filtrar Notas:")
        self.btn_new_user.setText("Nuevo Usuario")
        self.btn_new.setText("Nueva Nota")
        self.label_title.setText("Titulo de la Nota:")
        self.label_new_user.setText("Usuario:")
        self.btn_save.setText("Guardar Nota")


class WindowController(WindowLayout):
    """Se definen los metodos de control de la ventana.

    En esta clase, por medio de la herencia se agregan al
    layout de la ventana los metodos necesarios para el
    control de la misma.
    """

    def __init__(self) -> None:
        """Inicialización de DbManager y elementos de UI."""
        super().__init__()
        self.dbm = DbManager()

        self.update_user_list()
        self.update_note_list()
        self.note = None

        self.user_list.setCurrentIndex(0)
        self.user = User(
            user_name=self.user_list.currentData(0),
            user_id=self.user_list.currentData(1)
        )

        self.btn_save.clicked.connect(self.save_note)
        self.btn_new.clicked.connect(self.new_note)
        self.btn_new_user.clicked.connect(self.new_user)
        self.btn_delete.clicked.connect(self.delete_selected_note)
        self.notes_list.itemPressed.connect(self.load_selected_note)
        self.user_list.currentIndexChanged.connect(self.user_changed)

    def save_note(self):
        """Guarda Nota nueva o la actualiza si ya existe en la DB."""
        # Get Values from window
        body = self.notes_text.toPlainText()
        title = self.note_title.text()

        # Validar que el titulo sea solo alfanumérico
        if not title.isalnum():
            print('Invalid characters in note title.')
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Error en Título ingresado!")
            msg.setInformativeText(
                'El Título de una nota puede contener solo caracteres'
                + ' alfanuméricos.'
            )
            msg.setWindowTitle("ERROR")
            msg.exec_()
        else:
            if self.note is None:
                print(f'Saving new note with title: {title}')
                self.note = Note(
                    title=title,
                    body=body,
                    author=self.user
                )
                self.note.body = (
                    f'{body} \n\n\n\nAuthored by {self.note.author} at'
                    + f' {self.note.created_at}.'
                )
                self.dbm.create_note(self.note)
            else:
                print(f'Updating old note with title: {title}')
                self.note.title = title
                self.note.body = body
                self.note.author = self.user
                self.dbm.update_note(self.note)

            self.update_note_list()

    def new_note(self):
        """Reinicia los elementos de la UI para poder crear una nota nueva.

        Al presionar el botón de nueva nota, se limpian los
        campos de título y cuerpo del texto, y se actualizan los
        usuarios disponibles.
        """
        print('New note!!')
        self.note = None
        self.notes_text.setPlainText('')
        self.note_title.setText('')

    def new_user(self):
        """Inicializa una nueva ventana para creación de usuario.

        Al presionar el botón de nuevo usuario, se presenta
        la ventana de diálogo para ingresar el nombre.
        """
        print('New user')
        self.new_user_win = NewUserController()
        self.new_user_win.update_user_list = self.update_user_list
        self.new_user_win.dialog.show()

    def update_note_list(self):
        """Actualización de listado de notas en la DB."""
        notes = self.dbm.get_list_of_notes()
        self.notes_list.clear()
        for note in notes:
            itm = QtWidgets.QListWidgetItem(note.title)
            itm.setData(1, note.noteid)
            self.notes_list.addItem(itm)
            print(f'Updating List with Note: {note.title}')

    def update_user_list(self):
        """Actualización de listado de usuarios en la DB."""
        users = self.dbm.get_list_of_users()
        self.user_list.clear()
        for index, user in enumerate(users):
            self.user_list.addItem(user.user_name)
            self.user_list.setItemData(index, user.user_id, role=1)

        print('Updating User List')

    def user_changed(self):
        """Actualiza el usuario seleccionado dentro del controlador."""
        user_name = self.user_list.currentData(0)
        user_id = self.user_list.currentData(1)
        self.user = User(user_id, user_name)
        print(f'Selected User: {user_name} with id: {user_id}')

    def load_selected_note(self):
        """Carga el contenido y los datos de la nota seleccionada en la UI."""
        selected = self.notes_list.selectedItems()[0]
        note = self.dbm.get_note_from_id(
            selected.data(1)
        )
        self.note = note
        self.notes_text.setPlainText(note.body)
        self.note_title.setText(note.title)
        print(f'Loading Note: {note.title}')

    def delete_selected_note(self):
        """Elimina de la DB la nota seleccionada."""
        try:
            selected = self.notes_list.selectedItems()[0]
            self.dbm.delete_note(int(selected.data(1)))
            print(f'Deleting Note: {selected.text()}')
            self.update_note_list()
        except IndexError:
            print('No note selected.')
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Critical)
            msg.setText("Ninguna nota seleccionada!")
            msg.setInformativeText(
                'Debe seleccionar una nota para eliminar.'
            )
            msg.setWindowTitle("ERROR")
            msg.exec_()
