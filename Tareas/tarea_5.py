import sys
from PySide2.QtWidgets import QHBoxLayout,QGroupBox,QBoxLayout,QLabel,QFormLayout,QAction,QWidget,QApplication,QMainWindow,QDialog,QLineEdit,QPushButton, QVBoxLayout,QListWidget,QPlainTextEdit
from PySide2.QtCore import Slot
from Tareas.students import Students
from mongoengine import *
class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.initMainWindow()
        self.inputComponent()
        self.view()
        self.actionsButtons()
        self.db = connect('patds')
        self.obj = Students()
        self.temp=''

    def initMainWindow(self):
        self.resize(400, 400)
        self.setWindowTitle('Estudiantes')
        self.mainWidget = QWidget()
        self.mainLayout = QVBoxLayout(self.mainWidget)
        self.setCentralWidget(self.mainWidget)

    def initMenubar(self):
        self.menu = self.menuBar().addMenu('Prueba')
        self.action = QAction('Agragra')
        self.menu.addAction(self.action)
        self.action.triggered.connect(self.saludar)

    def inputComponent(self):
        self.inputName = QLineEdit()
        #self.inputName.placeholderText('Laura')
        self.inputEmail = QLineEdit()
        #self.inputEmail.placeholderText('Laura@cinvestav.mx')
        self.inputPassw = QLineEdit()
        #self.inputPassw.placeholderText('******')


        self.inputLayout = QFormLayout()
        self.inputLayout.addRow(QLabel('Nombre: '),self.inputName)
        self.inputLayout.addRow(QLabel('Email@: '), self.inputEmail)
        self.inputLayout.addRow(QLabel('Password: '), self.inputPassw)
        self.mainLayout.addLayout(self.inputLayout)
    def view(self):
        self.list = QListWidget()
        self.list.setAlternatingRowColors(True)
        self.list.setMaximumWidth(400)
        self.lisLayout= QVBoxLayout()
        self.mainLayout.addWidget(self.list)
        self.mainLayout.addLayout(self.lisLayout)
        self.list.itemClicked.connect(self.selectItem)



    def actionsButtons(self):
        self.buttonLayout = QHBoxLayout()
        self.guardarButton = QPushButton('Guardar')
        self.guardarButton.setMaximumWidth(100)
        self.consultarButton = QPushButton('Consultar')
        self.eliminarButton = QPushButton('Eliminar')
        self.actualizarButton = QPushButton('Actualizar')

        self.buttonLayout.addWidget(self.guardarButton)
        self.buttonLayout.addWidget(self.consultarButton)
        self.buttonLayout.addWidget(self.eliminarButton)
        self.buttonLayout.addWidget(self.actualizarButton)
        self.mainLayout.addLayout(self.buttonLayout)

        self.guardarButton.clicked.connect(self.create)
        self.consultarButton.clicked.connect(self.read)
        self.eliminarButton.clicked.connect(self.delete)
        self.actualizarButton.clicked.connect(self.update)

    def clearInput(self):
        self.inputName.clear()
        self.inputEmail.clear()
        self.inputPassw.clear()

    def setDataUI(self):
        t = self.obj.consultarByName(self.temp)
        self.inputName.setText(t.name)
        self.inputEmail.setText(t.email)
        self.inputPassw.setText(t.passw)

    @Slot()
    def selectItem(self):
        item = self.list.currentItem()
        self.temp=item.text()
        self.setDataUI()


    @Slot()
    def create(self):
        self.obj.guardarStudent(Students(name=self.inputName.text(),email=self.inputEmail.text(),passw=self.inputPassw.text()))
        self.read()
        self.clearInput()

    @Slot()
    def read(self):
        self.clearInput()
        self.list.clear()
        for i in self.obj.consultar():
            self.list.addItem(i.name)

    @Slot()
    def update(self):
        self.obj.actualizar(name=self.temp,student=Students(name=self.inputName.text(), email=self.inputEmail.text(), passw=self.inputPassw.text()))
        self.clearInput()
        self.read()

    @Slot()
    def delete(self):
        self.clearInput()
        self.obj.eliminar(name=self.temp)
        self.read()

def main():
    print('run')
    app = QApplication([])
    forma = MainWindow()
    forma.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
