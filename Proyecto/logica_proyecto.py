import sys
from PySide2.QtWidgets import QFileDialog,QHBoxLayout,QGroupBox,QLabel,QAction,QWidget,QApplication,QMainWindow,QLineEdit,QPushButton, QVBoxLayout
from PySide2.QtCore import Slot,QDir
import  socket as s
from Proyecto.estudiante import Estudiante
import pickle
import time
from threading import  Thread
class MainWindow(QMainWindow):

    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.initMainWindow()
        self.inputComponentServer()
        self.inputComponentStudet()
        self.fileComponentInput()
        self.statusComponentServer()
        self.clienteTCP = s.socket()
        self.t = Thread(target=self.servicesDataTranfer)



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
        self.buttonConectServer.clicked.connect(self.conectOrDisconect)

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
        statusLabelLayout.addWidget(QLabel('Data Transfer Status:'))
        self.statsDataTransfer = QLabel('Developer data')
        statusLabelLayout.addWidget(self.statsDataTransfer)
        inpintMainboxStatuslayout.addLayout(statusLabelLayout)

    def servicesDataTranfer(self):
        while True:
            self.data = self.clienteTCP.recv(1024)
            print(self.data.decode())


    @Slot()
    def sendFileToServer(self):
        inicio='iniciozip'.encode()
        fin ='finzip'.encode()
        self.clienteTCP.send(inicio)
        self.file = open(self.path[0], "rb")
        self.bytes = self.file.read(500)
        while len(self.bytes)>0 and self.bytes!=-1:
            self.clienteTCP.send(self.bytes)
            self.bytes = self.file.read(500)
            print(f'tmaño:{len(self.bytes)}->{self.bytes}\n')

        self.file.close()
        self.clienteTCP.send(fin)
        #file = open("tester/prueba.zip", "wb")
        #file.write(self.bytes)
        #file.close()
    @Slot()
    def conectOrDisconect(self):
        if self.buttonConectServer.text() == 'Conectar':
            self.conectServer()
        else:
            self.disconectServer()
    @Slot()
    def disconectServer(self):
        self.buttonConectServer.setText('Conectar')
        self.statusConectLabel.setText('Desconect')
        self.clienteTCP.close()


    @Slot()
    def conectServer(self):
        self.ip = self.inputIP.text()
        self.port  = int(self.inputPort.text())
        self.clienteTCP.connect((self.ip,self.port))
        self.statusConectLabel.setText('Connect')
        self.buttonConectServer.setText('Desconectar')
        #self.t.start()


    @Slot()
    def sendStudent(self):
        student = Estudiante(self.inputNameStudet.text(),self.inputEmailStudet.text(),self.inputPasswStudet.text())
        dataByte = pickle.dumps(student)
        self.clienteTCP.send(dataByte)

    @Slot()
    def findFile(self):
        self.path = QFileDialog.getOpenFileName(self, "Cargar", QDir.currentPath(), "*.*");
        self.inputFileSend.setText(self.path[0])





def main():
    print('run')
    app = QApplication([])
    forma = MainWindow()
    forma.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
