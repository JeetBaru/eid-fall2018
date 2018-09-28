# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'monitorv3.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import Adafruit_DHT
import datetime
import numpy
import time
import matplotlib.pyplot as plt

temp = [0] * 100
hum = [0] * 100
timestp = [0] * 100
count = 0

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(389, 415)
        self.RefreshButton = QtWidgets.QPushButton(Dialog)
        self.RefreshButton.setGeometry(QtCore.QRect(40, 370, 81, 22))
        self.RefreshButton.setObjectName("RefreshButton")
        self.QuitButton = QtWidgets.QPushButton(Dialog)
        self.QuitButton.setGeometry(QtCore.QRect(270, 370, 81, 22))
        self.QuitButton.setObjectName("QuitButton")
        self.TempHeader = QtWidgets.QLabel(Dialog)
        self.TempHeader.setGeometry(QtCore.QRect(50, 100, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.TempHeader.setFont(font)
        self.TempHeader.setObjectName("TempHeader")
        self.HumHeader = QtWidgets.QLabel(Dialog)
        self.HumHeader.setGeometry(QtCore.QRect(250, 100, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setUnderline(True)
        self.HumHeader.setFont(font)
        self.HumHeader.setObjectName("HumHeader")
        self.CurrTempVal = QtWidgets.QLabel(Dialog)
        self.CurrTempVal.setGeometry(QtCore.QRect(60, 140, 91, 16))
        self.CurrTempVal.setObjectName("CurrTempVal")
        self.CurrHumVal = QtWidgets.QLabel(Dialog)
        self.CurrHumVal.setGeometry(QtCore.QRect(240, 140, 111, 16))
        self.CurrHumVal.setObjectName("CurrHumVal")
        self.TempBar = QtWidgets.QProgressBar(Dialog)
        self.TempBar.setGeometry(QtCore.QRect(40, 260, 118, 23))
        self.TempBar.setProperty("value", 0)
        self.TempBar.setObjectName("TempBar")
        self.HumBar = QtWidgets.QProgressBar(Dialog)
        self.HumBar.setGeometry(QtCore.QRect(230, 260, 118, 23))
        self.HumBar.setProperty("value", 0)
        self.HumBar.setObjectName("HumBar")
        self.GraphButton = QtWidgets.QPushButton(Dialog)
        self.GraphButton.setGeometry(QtCore.QRect(160, 370, 81, 22))
        self.GraphButton.setObjectName("GraphButton")
        self.ConnStatus = QtWidgets.QLabel(Dialog)
        self.ConnStatus.setGeometry(QtCore.QRect(20, 40, 221, 21))
        self.ConnStatus.setObjectName("ConnStatus")
        self.TimeStamp = QtWidgets.QLabel(Dialog)
        self.TimeStamp.setGeometry(QtCore.QRect(230, 40, 101, 21))
        self.TimeStamp.setObjectName("TimeStamp")
        self.AvgTempVal = QtWidgets.QLabel(Dialog)
        self.AvgTempVal.setGeometry(QtCore.QRect(60, 180, 91, 16))
        self.AvgTempVal.setObjectName("AvgTempVal")
        self.AvgHumVal = QtWidgets.QLabel(Dialog)
        self.AvgHumVal.setGeometry(QtCore.QRect(240, 180, 111, 16))
        self.AvgHumVal.setObjectName("AvgHumVal")
        self.TempLowLimit = QtWidgets.QSpinBox(Dialog)
        self.TempLowLimit.setGeometry(QtCore.QRect(40, 290, 48, 23))
        self.TempLowLimit.setProperty("value", 10)
        self.TempLowLimit.setObjectName("TempLowLimit")
        self.TempHighLimit = QtWidgets.QSpinBox(Dialog)
        self.TempHighLimit.setGeometry(QtCore.QRect(110, 290, 48, 23))
        self.TempHighLimit.setProperty("value", 40)
        self.TempHighLimit.setObjectName("TempHighLimit")
        self.HumLowLimit = QtWidgets.QSpinBox(Dialog)
        self.HumLowLimit.setGeometry(QtCore.QRect(230, 290, 48, 23))
        self.HumLowLimit.setObjectName("HumLowLimit")
        self.HumHighLimit = QtWidgets.QSpinBox(Dialog)
        self.HumHighLimit.setGeometry(QtCore.QRect(300, 290, 48, 23))
        self.HumHighLimit.setProperty("value", 99)
        self.HumHighLimit.setObjectName("HumHighLimit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(140, 320, 111, 16))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "TempHumMonitor"))
        self.RefreshButton.setText(_translate("Dialog", "Refresh"))
        self.QuitButton.setText(_translate("Dialog", "Quit"))
        self.TempHeader.setText(_translate("Dialog", "Temperature"))
        self.HumHeader.setText(_translate("Dialog", "Humidity"))
        self.CurrTempVal.setText(_translate("Dialog", "Press Refresh"))
        self.CurrHumVal.setText(_translate("Dialog", "Press Refresh"))
        self.GraphButton.setText(_translate("Dialog", "Graph"))
        self.ConnStatus.setText(_translate("Dialog", "Sensor Connection Status"))
        self.TimeStamp.setText(_translate("Dialog", "    Timestamp    "))
        self.AvgTempVal.setText(_translate("Dialog", "Press Refresh"))
        self.AvgHumVal.setText(_translate("Dialog", "Press Refresh"))
        self.label.setText(_translate("Dialog", "        No Alert"))
        
        self.RefreshButton.clicked.connect(self.refresh)
        self.QuitButton.clicked.connect(self.quit)
        self.GraphButton.clicked.connect(self.graph)
        self.TempLowLimit.valueChanged.connect(self.valuechange)
        self.TempHighLimit.valueChanged.connect(self.valuechange)
        self.HumLowLimit.valueChanged.connect(self.valuechange)
        self.HumHighLimit.valueChanged.connect(self.valuechange)

    def valuechange(self):
        if count > 0:
            self.TempBar.setValue((temp[count-1]-self.TempLowLimit.value())/(0.01*(self.TempHighLimit.value()-self.TempLowLimit.value())))
            self.HumBar.setValue((hum[count-1]-self.HumLowLimit.value())/(0.01*(self.HumHighLimit.value()-self.HumLowLimit.value())))
            if temp[count-1] > self.TempHighLimit.value():
                self.label.setText('Temp Too High!')
            elif temp[count-1] < self.TempLowLimit.value():
                self.label.setText('Temp Too Low!')
            elif hum[count-1] > self.HumHighLimit.value():
                self.label.setText('Hum Too High!')
            elif hum[count-1] < self.HumLowLimit.value():
                self.label.setText('Hum Too low!')
            else:
                self.label.setText('    No Alert!')		

    def mean(self, arr, l):
        return sum(arr)/(l+1)
    
    def refresh(self):
        global temp
        global hum
        global timestp
        global count

        temp[count],hum[count] = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22,4)

        if temp[count] is not None and hum[count] is not None:
            avgtemp = self.mean(temp,count)
            avghum = self.mean(hum,count)
            self.ConnStatus.setText('    Sensor Connected')
            self.TimeStamp.setText(datetime.datetime.now().strftime("%H:%M %d-%m-%y"))
            timestp[count] = time.time()
            self.CurrTempVal.setText('Curr: ' + '{0:0.2f} C'.format(temp[count]))
            self.CurrHumVal.setText('Curr: ' + '{0:0.2f}%'.format(hum[count]))
            self.AvgTempVal.setText('Avg: ' + '{0:0.2f} C'.format(avgtemp))
            self.AvgHumVal.setText('Avg: ' + '{0:0.2f}%'.format(avghum))
            self.TempBar.setValue((temp[count]-self.TempLowLimit.value())/(0.01*(self.TempHighLimit.value()-self.TempLowLimit.value())))
            self.HumBar.setValue((hum[count]-self.HumLowLimit.value())/(0.01*(self.HumHighLimit.value()-self.HumLowLimit.value())))
            if temp[count] > self.TempHighLimit.value():
                self.label.setText('Temp Too High!')
            elif temp[count] < self.TempLowLimit.value():
                self.label.setText('Temp Too Low!')
            elif hum[count] > self.HumHighLimit.value():
                self.label.setText('Hum Too High!')
            elif hum[count] < self.HumLowLimit.value():
                self.label.setText('Hum Too low!')
            else:
                self.label.setText('    No Alert!')

            count = count + 1
            if count == 99:
                count = 0
                temp = [0] * 100
                hum = [0] * 100
                timestp = [0] * 100
        else:
            self.ConnStatus.setText('Sensor Not Connected')

    
    def quit(self):
        exit()

    def graph(self):
         
        global temp
        global hum
        global timestp
        global count
        
        if count is not 0: 

            avgtemparr = [self.mean(temp,count)] * count
            avghumarr = [self.mean(hum,count)] * count          

            plt.subplot(2,1,1)
            plt.plot(timestp[0:(count-1)],temp[0:(count-1)])
            plt.plot(timestp[0:(count-1)],avgtemparr[0:(count-1)])

            plt.subplot(2,1,2)
            plt.plot(timestp[0:(count-1)],hum[0:(count-1)])
            plt.plot(timestp[0:(count-1)],avghumarr[0:(count-1)])

            plt.show()

