import sys
from PySide2.QtWidgets import QFileDialog,QHBoxLayout,QGroupBox,QBoxLayout,QLabel,QFormLayout,QAction,QWidget,QApplication,QMainWindow,QDialog,QLineEdit,QPushButton, QVBoxLayout,QListWidget,QPlainTextEdit
from PySide2.QtCore import Slot,QDir
import  socket
class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.initMainWindow()
        self.inputComponentServer()
        self.inputComponentStudet()
        self.fileComponentInput()
        self.statusComponentServer()


    def initMainWindow(self):
        self.resize(400, 400)
        self.setWindowTitle('Oliver R')
        self.mainWidget = QWidget()
        self.mainLayout = QVBoxLayout(self.mainWidget)
        self.setCentralWidget(self.mainWidget)

    def initMenubar(self):
        self.menu = self.menuBar().addMenu('Prueba')
        self.action = QAction('Agragra')
        self.menu.addAction(self.action)
        self.action.triggered.connect(self.saludar)

    def inputComponentServer(self):
        boxInput = QGroupBox('Servidor')
        inpintMainboxlayout = QVBoxLayout()
        boxInput.setLayout(inpintMainboxlayout)
        self.mainLayout.addWidget(boxInput)

        self.inputIP = QLineEdit()
        #self.inputName.setMinimumWidth(300)
        self.inputIP.setPlaceholderText('10.10.0.1')
        self.inputPort = QLineEdit()
        self.inputPort.setPlaceholderText('8080')

        inputLayout = QHBoxLayout()
        inputLayout.addWidget(QLabel('IP: '))
        inputLayout.addWidget(self.inputIP)
        inputLayout.addWidget(QLabel('Puerto: '))
        inputLayout.addWidget(self.inputPort)
        inpintMainboxlayout.addLayout(inputLayout)

        self.buttonConectServer = QPushButton('Conectar')
        inpintMainboxlayout.addWidget(self.buttonConectServer)
        self.buttonConectServer.clicked.connect(self.conectServer)

    def inputComponentStudet(self):
        boxInputStudet = QGroupBox('Estudiante')
        inpintMainboxStudetlayout = QVBoxLayout()
        boxInputStudet.setLayout(inpintMainboxStudetlayout)
        self.mainLayout.addWidget(boxInputStudet)

        nameLayout = QHBoxLayout()
        nameLayout.addWidget(QLabel('Nombre: '))
        self.inputNameStudet = QLineEdit()
        self.inputNameStudet.setPlaceholderText('Nombre')
        nameLayout.addWidget(self.inputNameStudet)
        inpintMainboxStudetlayout.addLayout(nameLayout)

        emailLayout = QHBoxLayout()
        emailLayout.addWidget(QLabel('Email@: '))
        self.inputEmailStudet = QLineEdit()
        self.inputEmailStudet.setPlaceholderText('Email@cinvestav.mx')
        emailLayout.addWidget(self.inputEmailStudet)
        inpintMainboxStudetlayout.addLayout(emailLayout)

        passwLayout = QHBoxLayout()
        passwLayout.addWidget(QLabel('Passw: '))
        self.inputPasswStudet = QLineEdit()
        self.inputPasswStudet.setPlaceholderText('*************')
        passwLayout.addWidget(self.inputPasswStudet)
        inpintMainboxStudetlayout.addLayout(passwLayout)

        self.buttonSendStudent = QPushButton('Enviar')
        self.buttonSendStudent.clicked.connect(self.sendStudent)
        inpintMainboxStudetlayout.addWidget(self.buttonSendStudent)

    def fileComponentInput(self):
        boxInputFile = QGroupBox('File')
        inpintMainboxFilelayout = QVBoxLayout()
        boxInputFile.setLayout(inpintMainboxFilelayout)
        self.mainLayout.addWidget(boxInputFile)

        fileFindLayout = QHBoxLayout()
        buttonFindFile = QPushButton('Buscar')
        buttonFindFile.clicked.connect(self.findFile)
        fileFindLayout.addWidget(buttonFindFile)
        self.inputFileSend = QLineEdit()
        self.inputFileSend.setPlaceholderText('Ruta de archivo')
        fileFindLayout.addWidget(self.inputFileSend)
        inpintMainboxFilelayout.addLayout(fileFindLayout)
        buttonSendFile = QPushButton('Enviar')
        buttonSendFile.clicked.connect(self.sendFileToServer)
        inpintMainboxFilelayout.addWidget(buttonSendFile)


    def statusComponentServer(self):
        boxStatus = QGroupBox('Status Server')
        inpintMainboxStatuslayout = QVBoxLayout()
        boxStatus.setLayout(inpintMainboxStatuslayout)
        self.mainLayout.addWidget(boxStatus)

        statusLabelLayout = QHBoxLayout()
        statusLabelLayout.addWidget(QLabel('Connection Status: '))
        self.statusConectLabel = QLabel('Developer connect')
        statusLabelLayout.addWidget(self.statusConectLabel)
        statusLabelLayout.addWidget(QLabel('Data Transfer Status'))
        self.statsDataTransfer = QLabel('Developer data')
        statusLabelLayout.addWidget(self.statsDataTransfer)
        inpintMainboxStatuslayout.addLayout(statusLabelLayout)




    @Slot()
    def sendFileToServer(self):
        print('Send File')


    @Slot()
    def conectServer(self):
        print('Conect Server')

    @Slot()
    def findFile(self):
        self.path = QFileDialog.getOpenFileName(self, "Cargar", QDir.currentPath(), "*.*");
        self.inputFileSend.setText(self.path[0])
        file = open(self.path[0],"rb")
        self.bytes = file.read()
        file.close()
        file = open("tester/prueba.zip","wb")
        file.write(self.bytes)
        file.close()


    @Slot()
    def sendStudent(self):
        print('Send Studen')

def main():
    print('run')
    app = QApplication([])
    forma = MainWindow()
    forma.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
