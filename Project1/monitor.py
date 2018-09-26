# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitor.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import Adafruit_DHT

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 240, 81, 22))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 240, 81, 22))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 90, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(70, 160, 59, 14))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(250, 90, 59, 14))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(250, 160, 59, 14))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Refresh"))
        self.pushButton_3.setText(_translate("Dialog", "Quit"))
        self.label.setText(_translate("Dialog", "Temperature"))
        self.label_2.setText(_translate("Dialog", "Humidity"))
        self.pushButton.clicked.connect(self.displayValue)
        self.pushButton_3.clicked.connect(self.egjit)

    def displayValue(self):
        humidity, temperature = Adafruit_DHT.read_retry(22,4)
        if humidity is not None and temperature is not None:
            self.label_3.setText(str(temperature) + "C")
            self.label_4.setText(str(humidity) + "%" ) 

    def egjit(self):
        exit()


