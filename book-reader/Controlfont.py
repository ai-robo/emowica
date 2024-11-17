from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QApplication
from font import Ui_FontWindow
import sys
import os

class ControlFont(QtWidgets.QMainWindow, Ui_FontWindow):
    
    def __init__(self, edit):
        super(ControlFont, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.setFont)

        #Set available font size
        for i in range(2, 51):
            self.fontSize.addItem(str(i))
        self.classEdit = edit
        self.label_3.setText('Font color:')
        self.fontSize.setCurrentIndex(9)
        self.fontColor.setText('0,0,0')
        self.pushButton.setText('Apply')

        #Set the saved data when the window was previously opened
        self.setData()

        #Set window to the screen center
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
      
    def setData(self):


        try:

            #Open .fontdata file and store each line into dat list
            dat=[]
            with open('.fontdata', 'r') as data:
                for line in data:
                    dat.append(line[:-1])
            data.close()
    
            #Set properties of the font window
            index = self.fontComboBox.findText(dat[0], QtCore.Qt.MatchFixedString)
            self.fontComboBox.setCurrentIndex(index)
            self.fontSize.setCurrentIndex(int(dat[1])-2)
            self.fontColor.setPlainText(dat[3])
            
            if dat[2] == 'True':
                self.checkBold.setChecked(True)
            else:
                self.checkBold.setChecked(False)

        except FileNotFoundError:
            pass

    def setFont(self):
        
        #Check if the user wants bold fonts or not
        bol = False
        if self.checkBold.isChecked():
            bol = True

        # Set Font properties
        font = QtGui.QFont()
        font.setPointSize(int(str(self.fontSize.currentText())))
        font.setFamily(self.fontComboBox.currentText())
        font.setBold(bol)
        self.classEdit.setStyleSheet("color: rgb("+str(self.fontColor.toPlainText())+")")
        self.classEdit.setFont(font)

        #Remove previous Font data
        try:
            os.remove('.fontdata')
        except FileNotFoundError:
            pass

        #Add the new data into .fontdata
        with open('.fontdata', 'w') as data:
            data.write(str(self.fontComboBox.currentText()+'\n'))
            data.write(str(self.fontSize.currentText()+'\n'))
            data.write(str(bol)+'\n')
            data.write(str(self.fontColor.toPlainText()+'\n'))
        data.close()
        self.close()