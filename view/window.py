from data.db_access import DbManager
from data.data_models import Note
from PyQt5 import QtCore, QtGui, QtWidgets


class WindowLayout:

    def __init__(self) -> None:

        # Main Window
        self.main_window = QtWidgets.QMainWindow()
        self.main_window.resize(912, 700)
        self.centralwidget = QtWidgets.QWidget(self.main_window)
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 891, 641))
        self.main_layout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.main_layout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(3)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.main_layout.addItem(spacerItem, 3, 1, 1, 1)

        # Titulo de la nota
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.label_title = QtWidgets.QLabel(self.gridLayoutWidget)
        self.horizontalLayout_4.addWidget(self.label_title)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.note_title = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.note_title.setPlaceholderText("Título de la Nota")
        self.horizontalLayout_4.addWidget(self.note_title)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)

        # Cuerpo de la nota
        self.notes_text = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
        self.verticalLayout.addWidget(self.notes_text)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        self.btn_save = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.verticalLayout.addWidget(self.btn_save)
        self.main_layout.addLayout(self.verticalLayout, 3, 2, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.main_layout.addItem(spacerItem4, 2, 0, 1, 3)


        # Filtro de notas
        self.hlayout_filter = QtWidgets.QHBoxLayout()
        self.label_filter = QtWidgets.QLabel(self.gridLayoutWidget)
        self.hlayout_filter.addWidget(self.label_filter)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.hlayout_filter.addItem(spacerItem5)
        self.line_filter = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.line_filter.setPlaceholderText("Comience a escribir para filtrar...")
        self.hlayout_filter.addWidget(self.line_filter)
        self.main_layout.addLayout(self.hlayout_filter, 1, 0, 1, 1)

        # Boton Nueva Nota
        self.hlayout_new_note = QtWidgets.QHBoxLayout()
        self.btn_new = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.hlayout_new_note.addWidget(self.btn_new)
        self.main_layout.addLayout(self.hlayout_new_note, 1, 2, 1, 1)

        # Lista de notas
        self.vlayout_notes_list = QtWidgets.QVBoxLayout()
        self.notes_list = QtWidgets.QListWidget(self.gridLayoutWidget)
        self.vlayout_notes_list.addWidget(self.notes_list)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.vlayout_notes_list.addItem(spacerItem6)
        self.btn_delete = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.vlayout_notes_list.addWidget(self.btn_delete)
        self.main_layout.addLayout(self.vlayout_notes_list, 3, 0, 1, 1)

        self.main_window.setCentralWidget(self.centralwidget)
        QtCore.QMetaObject.connectSlotsByName(self.main_window)

        self.main_window.setWindowTitle("Mis Notas!!!")
        self.label_title.setText("Titulo de la Nota:")
        self.btn_save.setText("Guardar Nota")
        self.label_filter.setText("Filtrar Notas:")
        self.btn_new.setText("Nueva Nota")
        self.btn_delete.setText("Eliminar Nota Seleccionada")



class WorkingWindow(WindowLayout):

    def __init__(self) -> None:
        super().__init__()

        self.note = None
        self.dbm = DbManager()
        self.btn_save.clicked.connect(self.save_note)
        self.btn_new.clicked.connect(self.new_note)
        self.btn_delete.clicked.connect(self.delete_selected_note)
        self.notes_list.itemPressed.connect(self.load_selected_note)
        self.update_list()

    def save_note(self):

        # Get Values from window
        body = self.notes_text.toPlainText()
        title = self.note_title.text()

        if self.note is None:
            print(f'Saving new note with title: {title}')
            self.note = Note(
                title=title,
                body=body
            )
            self.dbm.create_note(self.note)
        else:
            print(f'Updating old note with title: {title}')
            self.note.title = title
            self.note.body = body
            self.dbm.update_note(self.note)

        self.update_list()


    def new_note(self):
        print('New note!!')
        self.note = None
        self.notes_text.setPlainText('')
        self.note_title.setText('')


    def update_list(self):
        notes = self.dbm.get_list_of_notes()
        self.notes_list.clear()
        for note in notes:
            itm = QtWidgets.QListWidgetItem(note.title)
            itm.setData(1, note.noteid)
            self.notes_list.addItem(itm)
            print(f'Updating List with Note: {note.title}')


    def load_selected_note(self):
        selected = self.notes_list.selectedItems()[0]
        note = self.dbm.get_note_from_id(
            selected.data(1)
        )
        self.note = note
        self.notes_text.setPlainText(note.body)
        self.note_title.setText(note.title)
        print(f'Loading Note: {note.title}')


    def delete_selected_note(self):
        selected = self.notes_list.selectedItems()[0]
        self.dbm.delete_note(int(selected.data(1)))
        print(f'Deletinging Note: {selected.text()}')
        self.update_list()

