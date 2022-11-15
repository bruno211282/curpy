"""Controlador de ventana principal."""
# -*- coding: utf-8 -*-


from PyQt5 import QtWidgets, uic

from data.data_models import Note, User
from data.db_access import DbManager
from logger.logger import log_try_exc_deco


class WellcomeDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("view/resource/wellcome.ui", self)

    def accept(self):
        # currentIndex = 1 -> signup
        if self.tab.currentIndex():
            usr = self.new_user_name.text()
            paswd = self.new_user_pass_1.text()
            conf = self.new_user_pass_2.text()

            if usr == "" or paswd == "" or conf == "":
                self.sig_error.setText(
                    "Debe ingresar toda la informacion requerida"
                )
            elif " " in paswd:
                self.sig_error.setText("No se admiten espacios en la clave")
            elif paswd != conf:
                self.sig_error.setText("Las claves no coinciden!")
            elif not usr.isalnum():
                self.sig_error.setText(
                    "Usuario invalido. "
                    "Solo se admiten caracteres alfanuméricos"
                )
            else:
                print("Estamos creando una cuenta!!!")
                self.done(1)

        # currentIndex = 0 -> login
        else:
            usr = self.login_user_name.text()
            paswd = self.login_user_pass.text()
            if usr == "" or paswd == "":
                self.log_error.setText(
                    "Debe ingresar toda la informacion requerida"
                )
            else:
                print("Estamos ingresando al sitio...")
                self.done(1)

    def reject(self):
        print("Reject")
        self.done(0)


class WindowController(QtWidgets.QMainWindow):
    """Se definen los metodos de control de la ventana."""

    def __init__(self, dbm: DbManager):
        """Controlador de la ventana principal de la aplicacion."""

        super().__init__()
        self.dbm = dbm

        uic.loadUi("view/resource/main.ui", self)

        self.update_note_list()
        self.note = None

        self.user = "Temp User..."  # Must be a User instance...

        self.btn_save.clicked.connect(self.save_note)
        self.btn_new.clicked.connect(self.new_note)
        self.btn_delete.clicked.connect(self.delete_selected_note)
        self.notes_list.itemClicked.connect(self.load_selected_note)

        self.username.setText(self.user)

    @ log_try_exc_deco("save a note to database")
    def save_note(self, *args):
        """Guarda Nota nueva o la actualiza si ya existe en la DB."""
        # Get Values from window
        body = self.notes_text.toPlainText()
        title = self.note_title.text()

        if self.note is None:
            print(f'Saving new note with title: {title}')
            self.note = Note(
                title=title,
                body=body,
                author=self.user
            )
            self.note.body = (
                f'{body} \n\n\n\nAuthored by {self.note.author} at'
                f' {self.note.created_at}.'
            )
            self.dbm.create_note(self.note)
        else:
            print(f'Updating old note with title: {title}')
            self.note.title = title
            self.note.body = body
            self.note.author = self.user
            self.dbm.update_note(self.note)

        self.update_note_list()

    @log_try_exc_deco("create a note")
    def new_note(self, *args):
        """Reinicia los elementos de la UI para poder crear una nota nueva.

        Al presionar el botón de nueva nota, se limpian los
        campos de título y cuerpo del texto, y se actualizan los
        usuarios disponibles.
        """
        print('New note!!')
        self.note = None
        self.notes_text.setPlainText('')
        self.note_title.setText('')

    @log_try_exc_deco("retrieve notes from database")
    def update_note_list(self, *args):
        """Actualización de listado de notas en la DB."""
        notes = self.dbm.get_list_of_notes()
        self.notes_list.clear()
        for note in notes:
            itm = QtWidgets.QListWidgetItem(note.title)
            itm.setData(1, note.noteid)
            self.notes_list.addItem(itm)
            print(f'Updating List with Note: {note.title}')

    @log_try_exc_deco("load note")
    def load_selected_note(self, *args):
        """Carga el contenido y los datos de la nota seleccionada en la UI."""
        selected = self.notes_list.selectedItems()[0]
        note = self.dbm.get_note_from_id(
            selected.data(1)
        )
        self.note = note
        self.notes_text.setPlainText(note.body)
        self.note_title.setText(note.title)
        print(f'Loading Note: {note.title}')

    @log_try_exc_deco("delete selected note")
    def delete_selected_note(self, *args):
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
