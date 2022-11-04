"""Controlador de ventana principal."""
# -*- coding: utf-8 -*-


from PyQt5 import uic
from view.new_user_window import NewUserController
from PyQt5 import QtWidgets


from data.data_models import Note
from data.data_models import User


class WindowController:
    """Se definen los metodos de control de la ventana.

    En esta clase, por medio de la herencia se agregan al
    layout de la ventana los metodos necesarios para el
    control de la misma.
    """

    def __init__(self, app, dbm):
        """Inicialización de DbManager y elementos de UI."""

        self.app = app
        self.dbm = dbm

        self.layout = uic.loadUi("view/resource/main.ui")
        self.layout.show()

        self.update_user_list()
        self.update_note_list()
        self.note = None

        self.layout.user_list.setCurrentIndex(0)
        self.user = User(
            user_name=self.layout.user_list.currentData(0),
            user_id=self.layout.user_list.currentData(1)
        )

        self.layout.btn_save.clicked.connect(self.save_note)
        self.layout.btn_new.clicked.connect(self.new_note)
        self.layout.btn_new_user.clicked.connect(self.new_user)
        self.layout.btn_delete.clicked.connect(self.delete_selected_note)
        self.layout.notes_list.itemClicked.connect(self.load_selected_note)
        self.layout.user_list.currentIndexChanged.connect(self.user_changed)

    def save_note(self):
        """Guarda Nota nueva o la actualiza si ya existe en la DB."""
        # Get Values from window
        body = self.layout.notes_text.toPlainText()
        title = self.layout.note_title.text()

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
        self.layout.notes_text.setPlainText('')
        self.layout.note_title.setText('')

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
        self.layout.notes_list.clear()
        for note in notes:
            itm = QtWidgets.QListWidgetItem(note.title)
            itm.setData(1, note.noteid)
            self.layout.notes_list.addItem(itm)
            print(f'Updating List with Note: {note.title}')

    def update_user_list(self):
        """Actualización de listado de usuarios en la DB."""
        users = self.dbm.get_list_of_users()
        self.layout.user_list.clear()
        for index, user in enumerate(users):
            self.layout.user_list.addItem(user.user_name)
            self.layout.user_list.setItemData(index, user.user_id, role=1)

        print('Updating User List')

    def user_changed(self):
        """Actualiza el usuario seleccionado dentro del controlador."""
        user_name = self.layout.user_list.currentData(0)
        user_id = self.layout.user_list.currentData(1)
        self.user = User(user_id, user_name)
        print(f'Selected User: {user_name} with id: {user_id}')

    def load_selected_note(self):
        """Carga el contenido y los datos de la nota seleccionada en la UI."""
        selected = self.layout.notes_list.selectedItems()[0]
        note = self.dbm.get_note_from_id(
            selected.data(1)
        )
        self.note = note
        self.layout.notes_text.setPlainText(note.body)
        self.layout.note_title.setText(note.title)
        print(f'Loading Note: {note.title}')

    def delete_selected_note(self):
        """Elimina de la DB la nota seleccionada."""
        try:
            selected = self.layout.notes_list.selectedItems()[0]
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
