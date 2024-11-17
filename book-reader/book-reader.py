from PyQt5 import QtWidgets, QtCore, QtGui, QtSerialPort
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from PyQt5.QtCore import QTimer, QEventLoop
from TextEditor import Ui_MainWindow
from Controlfont import ControlFont
import sys
import os

class Control(QtWidgets.QMainWindow, Ui_MainWindow):
    edit = None
    saveloc = ""
    def __init__(self):
        super(Control, self).__init__()
        self.setupUi(self)
        self.actionFonts.triggered.connect(self.fontWindow)
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave_as.triggered.connect(self.saveFile)
        self.actionSave.triggered.connect(self.save)
        self.actionExit.triggered.connect(self.exitProg)
        self.edit = self.plainTextEdit
        self.timer = QTimer(self)
        self.setFixedSize(1024, 800)
        
        self.serial = QtSerialPort.QSerialPort(
            '/dev/tty1',
            baudRate=QtSerialPort.QSerialPort.Baud9600,
            readyRead=self.Receive)

        self.Emotion = ""

        #Delete previous font data
        try:
            os.remove('.fontdata')
        except FileNotFoundError:
            pass
        
        self.center()

    def center(self):
        # geometry of the main window
        qr = self.frameGeometry()

        # center point of screen
        cp = QDesktopWidget().availableGeometry().center()

        # move rectangle's center point to screen's center point
        qr.moveCenter(cp)

        # top left of rectangle becomes top left of window centering it
        self.move(qr.topLeft())


    def openFile(self):
        
        options = QtWidgets.QFileDialog.Options()
        loc, _ = QtWidgets.QFileDialog.getOpenFileName(None,"Open File", "","All Files (*);;Python Files (*.py)", options=options)
        if not(loc == ''):
            self.plainTextEdit.clear()
            with open(loc , 'r') as f:
                lines = f.read().splitlines()
            for str in lines:
                self.plainTextEdit.appendPlainText(str)
            f.close()
        self.plainTextEdit.verticalScrollBar().setValue(0)
        if not self.serial.isOpen():
            self.serial.open(QtCore.QIODevice.ReadWrite)
            self.timer.timeout.connect(self.readEmotions)
            self.timer.start(200)
            


    @QtCore.pyqtSlot()
    def Receive(self):
        print("Receive")
        self.Emotion = self.serial.readAll().data().decode()


    def Delay(self, msec):
        loop = QEventLoop()
        QTimer.singleShot(msec, loop.quit)
        loop.exec_()
        
        
    def readEmotions(self):
        #self.Emotion = ""

        if self.Emotion == "happy":
            print("happy")
            self.plainTextEdit.verticalScrollBar().setValue(2)    
        elif self.Emotion == "surprise":
            print("surprise")
            self.plainTextEdit.verticalScrollBar().setValue(0)
        else:
            pass
        self.Emotion = ""

    
    def saveFile(self):
        #Save as Function
        options = QtWidgets.QFileDialog.Options()
        loc, _ = QtWidgets.QFileDialog.getSaveFileName(None,"Save File", "","All Files (*);;Python Files (*.py)", options=options)
        self.saveloc = loc
        lines = self.plainTextEdit.toPlainText()
        if not loc == '':
            with open(loc, 'w') as data:
                for str in lines:
                    data.write(str)
            data.close()


    def save(self):
        #Save function
        #Check if Save As function has been used previously
        if self.saveloc == "":
            self.saveFile()
        else:
            lines = self.plainTextEdit.toPlainText()
            with open(self.saveloc, 'w') as data:
                for str in lines:
                    data.write(str)
            data.close()


    def fontWindow(self):
        #Open the font choosing window
        self.openFont = ControlFont(self.plainTextEdit)
        self.openFont.show()


    def exitProg(self):
        exit() 

if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    form = Control()
    form.show()
    sys.exit(app.exec_())
