# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tkm_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1037, 929)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(10, 820, 71, 41))
        self.graphicsView.setObjectName("graphicsView")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(670, 170, 231, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(670, 220, 251, 31))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(670, 285, 271, 31))
        self.checkBox_3.setObjectName("checkBox_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(670, 380, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(670, 100, 261, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(670, 130, 81, 16))
        self.label_18.setObjectName("label_18")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(780, 380, 171, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(0, 120, 321, 581))
        self.tableView.setObjectName("tableView")
        self.tableView_S = QtWidgets.QTableView(self.centralwidget)
        self.tableView_S.setGeometry(QtCore.QRect(320, 120, 311, 231))
        self.tableView_S.setObjectName("tableView_S")
        self.tableView_T = QtWidgets.QTableView(self.centralwidget)
        self.tableView_T.setGeometry(QtCore.QRect(320, 380, 311, 321))
        self.tableView_T.setObjectName("tableView_T")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(660, 91, 291, 341))
        self.textBrowser.setObjectName("textBrowser")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(820, 160, 42, 22))
        self.spinBox.setObjectName("spinBox")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(820, 130, 91, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(880, 170, 35, 10))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(0, 90, 141, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.enterB = QtWidgets.QPushButton(self.centralwidget)
        self.enterB.setGeometry(QtCore.QRect(140, 90, 181, 31))
        self.enterB.setObjectName("enterB")
        self.lineEdit_s = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_s.setGeometry(QtCore.QRect(320, 90, 161, 31))
        self.lineEdit_s.setText("")
        self.lineEdit_s.setObjectName("lineEdit_s")
        self.enterS = QtWidgets.QPushButton(self.centralwidget)
        self.enterS.setGeometry(QtCore.QRect(480, 90, 151, 31))
        self.enterS.setObjectName("enterS")
        self.enterT = QtWidgets.QPushButton(self.centralwidget)
        self.enterT.setGeometry(QtCore.QRect(480, 350, 151, 31))
        self.enterT.setObjectName("enterT")
        self.lineEdit_t = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_t.setGeometry(QtCore.QRect(320, 350, 161, 31))
        self.lineEdit_t.setText("")
        self.lineEdit_t.setObjectName("lineEdit_t")
        self.lineEdit_f = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_f.setGeometry(QtCore.QRect(280, 0, 181, 31))
        self.lineEdit_f.setText("")
        self.lineEdit_f.setObjectName("lineEdit_f")
        self.enterF = QtWidgets.QPushButton(self.centralwidget)
        self.enterF.setGeometry(QtCore.QRect(460, 0, 181, 31))
        self.enterF.setObjectName("enterF")
        self.lineEdit_v = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_v.setGeometry(QtCore.QRect(280, 50, 181, 31))
        self.lineEdit_v.setText("")
        self.lineEdit_v.setObjectName("lineEdit_v")
        self.enterV = QtWidgets.QPushButton(self.centralwidget)
        self.enterV.setGeometry(QtCore.QRect(460, 50, 181, 31))
        self.enterV.setObjectName("enterV")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, -10, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textBrowser.raise_()
        self.checkBox.raise_()
        self.checkBox_2.raise_()
        self.checkBox_3.raise_()
        self.pushButton.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.pushButton_2.raise_()
        self.tableView.raise_()
        self.tableView_S.raise_()
        self.tableView_T.raise_()
        self.graphicsView.raise_()
        self.spinBox.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.lineEdit.raise_()
        self.enterB.raise_()
        self.lineEdit_s.raise_()
        self.enterS.raise_()
        self.enterT.raise_()
        self.lineEdit_t.raise_()
        self.lineEdit_f.raise_()
        self.enterF.raise_()
        self.lineEdit_v.raise_()
        self.enterV.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1037, 18))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.checkBox.setText(_translate("MainWindow", "Broken Rail"))
        self.checkBox_2.setText(_translate("MainWindow", "Power Failure"))
        self.checkBox_3.setText(_translate("MainWindow", "Track Circuit Failure"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.label_17.setText(_translate("MainWindow", "For the Selected Block"))
        self.label_18.setText(_translate("MainWindow", "Select Errors"))
        self.pushButton_2.setText(_translate("MainWindow", "Track Heater"))
        self.label.setText(_translate("MainWindow", "Set Temp"))
        self.label_2.setText(_translate("MainWindow", "F"))
        self.enterB.setText(_translate("MainWindow", "Enter"))
        self.enterS.setText(_translate("MainWindow", "Enter"))
        self.enterT.setText(_translate("MainWindow", "Enter"))
        self.enterF.setText(_translate("MainWindow", "Enter"))
        self.enterV.setText(_translate("MainWindow", "Enter"))
        self.label_3.setText(_translate("MainWindow", "Select Line to View"))
        self.label_4.setText(_translate("MainWindow", "Select File to Load"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
