# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'font.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FontWindow(object):
    def setupUi(self, FontWindow):
        FontWindow.setObjectName("FontWindow")
        FontWindow.resize(370, 281)
        self.label = QtWidgets.QLabel(FontWindow)
        self.label.setGeometry(QtCore.QRect(210, 50, 67, 17))
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(FontWindow)
        self.line.setGeometry(QtCore.QRect(170, 10, 20, 201))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.fontComboBox = QtWidgets.QFontComboBox(FontWindow)
        self.fontComboBox.setGeometry(QtCore.QRect(30, 80, 141, 25))
        self.fontComboBox.setObjectName("fontComboBox")
        self.label_2 = QtWidgets.QLabel(FontWindow)
        self.label_2.setGeometry(QtCore.QRect(30, 50, 67, 17))
        self.label_2.setObjectName("label_2")
        self.line_2 = QtWidgets.QFrame(FontWindow)
        self.line_2.setGeometry(QtCore.QRect(0, 210, 371, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_3 = QtWidgets.QLabel(FontWindow)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 81, 17))
        self.label_3.setObjectName("label_3")
        self.fontColor = QtWidgets.QTextEdit(FontWindow)
        self.fontColor.setGeometry(QtCore.QRect(30, 160, 104, 21))
        self.fontColor.setObjectName("fontColor")
        self.pushButton = QtWidgets.QPushButton(FontWindow)
        self.pushButton.setGeometry(QtCore.QRect(130, 230, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.fontSize = QtWidgets.QComboBox(FontWindow)
        self.fontSize.setGeometry(QtCore.QRect(210, 80, 86, 25))
        self.fontSize.setObjectName("fontSize")
        self.checkBold = QtWidgets.QCheckBox(FontWindow)
        self.checkBold.setGeometry(QtCore.QRect(210, 140, 92, 23))
        self.checkBold.setObjectName("checkBold")

        self.retranslateUi(FontWindow)
        QtCore.QMetaObject.connectSlotsByName(FontWindow)

    def retranslateUi(self, FontWindow):
        _translate = QtCore.QCoreApplication.translate
        FontWindow.setWindowTitle(_translate("FontWindow", "Form"))
        self.label.setText(_translate("FontWindow", "Font Size:"))
        self.label_2.setText(_translate("FontWindow", "Font:"))
        self.label_3.setText(_translate("FontWindow", "Font Color:"))
        self.pushButton.setText(_translate("FontWindow", "Ok"))
        self.checkBold.setText(_translate("FontWindow", "Bold"))




