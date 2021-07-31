from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import re


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(435, 393)
        mainWindow.setStyleSheet("background-color: rgb(85, 255, 255);\n"
"")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tocentimeters = QtWidgets.QPushButton(self.centralwidget)
        self.tocentimeters.setGeometry(QtCore.QRect(160, 100, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tocentimeters.setFont(font)
        self.tocentimeters.setObjectName("tocentimeters")
        self.formeters = QtWidgets.QLineEdit(self.centralwidget)
        self.formeters.setGeometry(QtCore.QRect(10, 100, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.formeters.setFont(font)
        self.formeters.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.formeters.setObjectName("formeters")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 50, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tometers = QtWidgets.QPushButton(self.centralwidget)
        self.tometers.setGeometry(QtCore.QRect(160, 240, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tometers.setFont(font)
        self.tometers.setObjectName("tometers")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 190, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.forcm = QtWidgets.QLineEdit(self.centralwidget)
        self.forcm.setGeometry(QtCore.QRect(10, 240, 131, 41))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.forcm.setFont(font)
        self.forcm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.forcm.setText("")
        self.forcm.setObjectName("forcm")
        self.incentimeters = QtWidgets.QPushButton(self.centralwidget)
        self.incentimeters.setGeometry(QtCore.QRect(300, 100, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.incentimeters.setFont(font)
        self.incentimeters.setText("")
        self.incentimeters.setObjectName("incentimeters")
        self.inmeters = QtWidgets.QPushButton(self.centralwidget)
        self.inmeters.setGeometry(QtCore.QRect(310, 230, 91, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.inmeters.setFont(font)
        self.inmeters.setText("")
        self.inmeters.setObjectName("inmeters")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 435, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)


        self.tocentimeters.clicked.connect(self.convertmeters)
        self.tometers.clicked.connect(self.convertcentimeters)

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)



    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Dimensions Converter"))
        self.tocentimeters.setText(_translate("mainWindow", "To Centimeters"))
        self.formeters.setToolTip(_translate("mainWindow", "<html><head/><body><p>Enter length in Meters</p></body></html>"))
        self.formeters.setPlaceholderText(_translate("mainWindow", "In Meters"))
        self.label.setText(_translate("mainWindow", "Convert from Meters to Centimeters"))
        self.tometers.setText(_translate("mainWindow", "To Meters"))
        self.label_2.setText(_translate("mainWindow", "Convert from Centimeters to Meters"))
        self.forcm.setToolTip(_translate("mainWindow", "<html><head/><body><p>Enter length in Centimeters</p></body></html>"))
        self.forcm.setPlaceholderText(_translate("mainWindow", "In Centimeters"))


    def error_string_input(self):
        self.incentimeters.setText("")
        msg = QMessageBox()
        msg.setWindowTitle("Message Box")
        msg.setText("Input Must be a number")
        msg.setIcon(QMessageBox.Warning)
        x=msg.exec_()

    def error_empty_input(self):
        self.incentimeters.setText("")
        msg = QMessageBox()
        msg.setWindowTitle("Message Box")
        msg.setText("Please fill in the field")
        msg.setIcon(QMessageBox.Warning)
        x=msg.exec_()



    def convertmeters(self):
        meter = str(self.formeters.text()) 
        if meter != "":
            try:
                a = []
                for word in meter.split():
                    try:
                        a.append(float(word))
                    except ValueError:
                        pass
                centimeters=a[0] * 100
                self.formeters.setText(str(a[0])+ " " + "M")
                self.incentimeters.setText(str(centimeters) + " " + "CM")
                self.incentimeters.adjustSize()
            except:
                self.error_string_input()
                self.formeters.setText("")

        else:
            self.error_empty_input()
            
        
        #self.formeters.setText("")

    def convertcentimeters(self):
        centimeters = self.forcm.text()
        
        if centimeters != "":
            try:
                b= []
                for word in centimeters.split():
                    try:
                        b.append(float(word))
                    except:
                        pass
                meters = b[0] /100
                self.inmeters.setText(str(meters) + " " + "M")
                self.inmeters.adjustSize()
                self.forcm.setText(str(b[0])+ " " + "CM")
            except:
                self.error_string_input()
                self.forcm.setText("")
        else:
            self.error_empty_input()
            self.inmeters.setText("")
            
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
