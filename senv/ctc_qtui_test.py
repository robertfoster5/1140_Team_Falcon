# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Robert\QT_Designer\ctc_qtui_test.ui'
#
# Created by: PyQt5 UI code generator 5.15.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1048, 730)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 771, 251))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_transit = QtWidgets.QWidget()
        self.tab_transit.setObjectName("tab_transit")
        self.tabWidget.addTab(self.tab_transit, "")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget_2.setGeometry(QtCore.QRect(10, 290, 1031, 401))
        self.tabWidget_2.setTabBarAutoHide(False)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_schedule = QtWidgets.QWidget()
        self.tab_schedule.setObjectName("tab_schedule")
        self.tableView_schedule = QtWidgets.QTableView(self.tab_schedule)
        self.tableView_schedule.setGeometry(QtCore.QRect(20, 10, 991, 351))
        self.tableView_schedule.setObjectName("tableView_schedule")
        self.tabWidget_2.addTab(self.tab_schedule, "")
        self.tab_dispatch_green = QtWidgets.QWidget()
        self.tab_dispatch_green.setObjectName("tab_dispatch_green")
        self.label_3 = QtWidgets.QLabel(self.tab_dispatch_green)
        self.label_3.setGeometry(QtCore.QRect(20, 10, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.tab_dispatch_green)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 201, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.tab_dispatch_green)
        self.label_5.setGeometry(QtCore.QRect(20, 150, 201, 31))
        self.label_5.setObjectName("label_5")
        self.lineEditTime = QtWidgets.QLineEdit(self.tab_dispatch_green)
        self.lineEditTime.setGeometry(QtCore.QRect(240, 150, 201, 31))
        self.lineEditTime.setText("")
        self.lineEditTime.setObjectName("lineEditTime")
        self.btnDispatchMan = QtWidgets.QPushButton(self.tab_dispatch_green)
        self.btnDispatchMan.setGeometry(QtCore.QRect(110, 200, 241, 31))
        self.btnDispatchMan.setObjectName("btnDispatchMan")
        self.comboStation = QtWidgets.QComboBox(self.tab_dispatch_green)
        self.comboStation.setGeometry(QtCore.QRect(240, 100, 201, 31))
        self.comboStation.setObjectName("comboStation")
        self.comboStation.addItem("")
        self.comboStation.addItem("")
        self.comboStation.addItem("")
        self.comboStation.addItem("")
        self.comboStation.addItem("")
        self.comboStation.addItem("")
        self.comboStation.addItem("")
        self.comboStation.addItem("")
        self.comboStation.addItem("")
        self.comboStation.addItem("")
        self.comboStation.addItem("")
        self.comboStation.addItem("")
        self.comboStation.addItem("")
        self.comboStation.addItem("")
        self.label_16 = QtWidgets.QLabel(self.tab_dispatch_green)
        self.label_16.setGeometry(QtCore.QRect(540, 10, 471, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        self.label_18 = QtWidgets.QLabel(self.tab_dispatch_green)
        self.label_18.setGeometry(QtCore.QRect(490, 100, 201, 31))
        self.label_18.setObjectName("label_18")
        self.btnImportSchedFile = QtWidgets.QPushButton(self.tab_dispatch_green)
        self.btnImportSchedFile.setGeometry(QtCore.QRect(720, 100, 241, 31))
        self.btnImportSchedFile.setObjectName("btnImportSchedFile")
        self.labelSchedFile = QtWidgets.QLabel(self.tab_dispatch_green)
        self.labelSchedFile.setGeometry(QtCore.QRect(670, 150, 341, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelSchedFile.setFont(font)
        self.labelSchedFile.setObjectName("labelSchedFile")
        self.btnDispatchAuto = QtWidgets.QPushButton(self.tab_dispatch_green)
        self.btnDispatchAuto.setGeometry(QtCore.QRect(640, 200, 240, 30))
        self.btnDispatchAuto.setObjectName("btnDispatchAuto")
        self.comboTrain = QtWidgets.QComboBox(self.tab_dispatch_green)
        self.comboTrain.setGeometry(QtCore.QRect(240, 50, 201, 31))
        self.comboTrain.setObjectName("comboTrain")
        self.comboTrain.addItem("")
        self.label_20 = QtWidgets.QLabel(self.tab_dispatch_green)
        self.label_20.setGeometry(QtCore.QRect(20, 50, 201, 31))
        self.label_20.setObjectName("label_20")
        self.label_25 = QtWidgets.QLabel(self.tab_dispatch_green)
        self.label_25.setGeometry(QtCore.QRect(490, 150, 201, 31))
        self.label_25.setObjectName("label_25")
        self.labelManError = QtWidgets.QLabel(self.tab_dispatch_green)
        self.labelManError.setGeometry(QtCore.QRect(20, 240, 421, 31))
        self.labelManError.setAutoFillBackground(False)
        self.labelManError.setText("")
        self.labelManError.setObjectName("labelManError")
        self.labelAutoError = QtWidgets.QLabel(self.tab_dispatch_green)
        self.labelAutoError.setGeometry(QtCore.QRect(490, 240, 421, 31))
        self.labelAutoError.setAutoFillBackground(False)
        self.labelAutoError.setText("")
        self.labelAutoError.setObjectName("labelAutoError")
        self.tabWidget_2.addTab(self.tab_dispatch_green, "")
        self.tab_dispatch_red = QtWidgets.QWidget()
        self.tab_dispatch_red.setObjectName("tab_dispatch_red")
        self.label_10 = QtWidgets.QLabel(self.tab_dispatch_red)
        self.label_10.setGeometry(QtCore.QRect(20, 10, 501, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_10.setFont(font)
        self.label_10.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_10.setScaledContents(False)
        self.label_10.setObjectName("label_10")
        self.label_21 = QtWidgets.QLabel(self.tab_dispatch_red)
        self.label_21.setGeometry(QtCore.QRect(20, 50, 201, 31))
        self.label_21.setObjectName("label_21")
        self.label_17 = QtWidgets.QLabel(self.tab_dispatch_red)
        self.label_17.setGeometry(QtCore.QRect(540, 10, 471, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.label_11 = QtWidgets.QLabel(self.tab_dispatch_red)
        self.label_11.setGeometry(QtCore.QRect(20, 150, 201, 31))
        self.label_11.setObjectName("label_11")
        self.label_26 = QtWidgets.QLabel(self.tab_dispatch_red)
        self.label_26.setGeometry(QtCore.QRect(490, 150, 201, 31))
        self.label_26.setObjectName("label_26")
        self.label_22 = QtWidgets.QLabel(self.tab_dispatch_red)
        self.label_22.setGeometry(QtCore.QRect(490, 100, 201, 31))
        self.label_22.setObjectName("label_22")
        self.label_12 = QtWidgets.QLabel(self.tab_dispatch_red)
        self.label_12.setGeometry(QtCore.QRect(20, 100, 201, 31))
        self.label_12.setObjectName("label_12")
        self.lineEditTime_2 = QtWidgets.QLineEdit(self.tab_dispatch_red)
        self.lineEditTime_2.setGeometry(QtCore.QRect(240, 150, 201, 31))
        self.lineEditTime_2.setText("")
        self.lineEditTime_2.setObjectName("lineEditTime_2")
        self.btnImportSchedFile_2 = QtWidgets.QPushButton(self.tab_dispatch_red)
        self.btnImportSchedFile_2.setGeometry(QtCore.QRect(720, 100, 241, 31))
        self.btnImportSchedFile_2.setObjectName("btnImportSchedFile_2")
        self.btnDispatchMan_2 = QtWidgets.QPushButton(self.tab_dispatch_red)
        self.btnDispatchMan_2.setGeometry(QtCore.QRect(110, 200, 241, 31))
        self.btnDispatchMan_2.setObjectName("btnDispatchMan_2")
        self.comboStation_2 = QtWidgets.QComboBox(self.tab_dispatch_red)
        self.comboStation_2.setGeometry(QtCore.QRect(240, 100, 201, 31))
        self.comboStation_2.setObjectName("comboStation_2")
        self.comboStation_2.addItem("")
        self.comboStation_2.addItem("")
        self.comboStation_2.addItem("")
        self.comboStation_2.addItem("")
        self.comboStation_2.addItem("")
        self.comboStation_2.addItem("")
        self.comboStation_2.addItem("")
        self.comboStation_2.addItem("")
        self.comboStation_2.addItem("")
        self.btnDispatchAuto_2 = QtWidgets.QPushButton(self.tab_dispatch_red)
        self.btnDispatchAuto_2.setGeometry(QtCore.QRect(640, 200, 240, 30))
        self.btnDispatchAuto_2.setObjectName("btnDispatchAuto_2")
        self.comboTrain_2 = QtWidgets.QComboBox(self.tab_dispatch_red)
        self.comboTrain_2.setGeometry(QtCore.QRect(240, 50, 201, 31))
        self.comboTrain_2.setObjectName("comboTrain_2")
        self.comboTrain_2.addItem("")
        self.labelSchedFile_2 = QtWidgets.QLabel(self.tab_dispatch_red)
        self.labelSchedFile_2.setGeometry(QtCore.QRect(670, 150, 341, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelSchedFile_2.setFont(font)
        self.labelSchedFile_2.setObjectName("labelSchedFile_2")
        self.tabWidget_2.addTab(self.tab_dispatch_red, "")
        self.tab_maintenance = QtWidgets.QWidget()
        self.tab_maintenance.setObjectName("tab_maintenance")
        self.label_6 = QtWidgets.QLabel(self.tab_maintenance)
        self.label_6.setGeometry(QtCore.QRect(30, 0, 281, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.tab_maintenance)
        self.label_7.setGeometry(QtCore.QRect(390, 0, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.comboSwitch = QtWidgets.QComboBox(self.tab_maintenance)
        self.comboSwitch.setGeometry(QtCore.QRect(30, 80, 231, 31))
        self.comboSwitch.setEditable(False)
        self.comboSwitch.setObjectName("comboSwitch")
        self.comboSwitch.addItem("")
        self.comboSwitch.addItem("")
        self.comboSwitch.addItem("")
        self.comboSwitch.addItem("")
        self.comboSwitch.addItem("")
        self.comboSwitch.addItem("")
        self.label_8 = QtWidgets.QLabel(self.tab_maintenance)
        self.label_8.setGeometry(QtCore.QRect(30, 50, 291, 20))
        self.label_8.setObjectName("label_8")
        self.comboBlock = QtWidgets.QComboBox(self.tab_maintenance)
        self.comboBlock.setGeometry(QtCore.QRect(390, 80, 231, 31))
        self.comboBlock.setObjectName("comboBlock")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.comboBlock.addItem("")
        self.label_9 = QtWidgets.QLabel(self.tab_maintenance)
        self.label_9.setGeometry(QtCore.QRect(390, 50, 271, 20))
        self.label_9.setObjectName("label_9")
        self.btnToggleSwitch = QtWidgets.QPushButton(self.tab_maintenance)
        self.btnToggleSwitch.setGeometry(QtCore.QRect(30, 190, 151, 31))
        self.btnToggleSwitch.setObjectName("btnToggleSwitch")
        self.btnToggleBlock = QtWidgets.QPushButton(self.tab_maintenance)
        self.btnToggleBlock.setGeometry(QtCore.QRect(390, 190, 151, 31))
        self.btnToggleBlock.setObjectName("btnToggleBlock")
        self.tabWidget_2.addTab(self.tab_maintenance, "")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(850, 88, 161, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(860, 108, 161, 21))
        self.label_2.setObjectName("label_2")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setEnabled(True)
        self.label_19.setGeometry(QtCore.QRect(820, 130, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_19.setFont(font)
        self.label_19.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_19.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_19.setScaledContents(False)
        self.label_19.setAlignment(QtCore.Qt.AlignCenter)
        self.label_19.setObjectName("label_19")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1048, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_transit), _translate("MainWindow", "Transit System"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_schedule), _translate("MainWindow", "Schedule"))
        self.label_3.setText(_translate("MainWindow", "Dispatch Train (Manual):"))
        self.label_4.setText(_translate("MainWindow", "Destination Station:"))
        self.label_5.setText(_translate("MainWindow", "Arrival Time (2400):"))
        self.lineEditTime.setPlaceholderText(_translate("MainWindow", "Enter Arrival Time..."))
        self.btnDispatchMan.setText(_translate("MainWindow", "Dispatch Train"))
        self.comboStation.setItemText(0, _translate("MainWindow", "Edgebrook"))
        self.comboStation.setItemText(1, _translate("MainWindow", "Pioneer"))
        self.comboStation.setItemText(2, _translate("MainWindow", "Falcon"))
        self.comboStation.setItemText(3, _translate("MainWindow", "Whited"))
        self.comboStation.setItemText(4, _translate("MainWindow", "South Bank"))
        self.comboStation.setItemText(5, _translate("MainWindow", "Central"))
        self.comboStation.setItemText(6, _translate("MainWindow", "Inglewood"))
        self.comboStation.setItemText(7, _translate("MainWindow", "Overbrook"))
        self.comboStation.setItemText(8, _translate("MainWindow", "Yard"))
        self.comboStation.setItemText(9, _translate("MainWindow", "Glenbury"))
        self.comboStation.setItemText(10, _translate("MainWindow", "Dormont"))
        self.comboStation.setItemText(11, _translate("MainWindow", "Mt Lebanon"))
        self.comboStation.setItemText(12, _translate("MainWindow", "Poplar"))
        self.comboStation.setItemText(13, _translate("MainWindow", "Castle Shannon"))
        self.label_16.setText(_translate("MainWindow", "Dispatch Train (Automatic):"))
        self.label_18.setText(_translate("MainWindow", "Schedule File (.CSV):"))
        self.btnImportSchedFile.setText(_translate("MainWindow", "Import Schedule File"))
        self.labelSchedFile.setText(_translate("MainWindow", "..."))
        self.btnDispatchAuto.setText(_translate("MainWindow", "Dispatch Train"))
        self.comboTrain.setItemText(0, _translate("MainWindow", "New Train"))
        self.label_20.setText(_translate("MainWindow", "Outgoing Train:"))
        self.label_25.setText(_translate("MainWindow", "Chosen File:"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_dispatch_green), _translate("MainWindow", "Dispatch (Green)"))
        self.label_10.setText(_translate("MainWindow", "Dispatch Train (Manual):"))
        self.label_21.setText(_translate("MainWindow", "Outgoing Train:"))
        self.label_17.setText(_translate("MainWindow", "Dispatch Train (Automatic):"))
        self.label_11.setText(_translate("MainWindow", "Arrival Time (2400):"))
        self.label_26.setText(_translate("MainWindow", "Chosen File:"))
        self.label_22.setText(_translate("MainWindow", "Schedule File (.CSV):"))
        self.label_12.setText(_translate("MainWindow", "Destination Station:"))
        self.lineEditTime_2.setPlaceholderText(_translate("MainWindow", "Enter Arrival Time..."))
        self.btnImportSchedFile_2.setText(_translate("MainWindow", "Import Schedule File"))
        self.btnDispatchMan_2.setText(_translate("MainWindow", "Dispatch Train"))
        self.comboStation_2.setItemText(0, _translate("MainWindow", "Shadyside"))
        self.comboStation_2.setItemText(1, _translate("MainWindow", "Yard"))
        self.comboStation_2.setItemText(2, _translate("MainWindow", "Herron Ave"))
        self.comboStation_2.setItemText(3, _translate("MainWindow", "Swissville"))
        self.comboStation_2.setItemText(4, _translate("MainWindow", "Penn Station"))
        self.comboStation_2.setItemText(5, _translate("MainWindow", "Steel Plaza"))
        self.comboStation_2.setItemText(6, _translate("MainWindow", "First Ave"))
        self.comboStation_2.setItemText(7, _translate("MainWindow", "Station Square"))
        self.comboStation_2.setItemText(8, _translate("MainWindow", "South Hills Junction"))
        self.btnDispatchAuto_2.setText(_translate("MainWindow", "Dispatch Train"))
        self.comboTrain_2.setItemText(0, _translate("MainWindow", "New Train"))
        self.labelSchedFile_2.setText(_translate("MainWindow", "..."))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_dispatch_red), _translate("MainWindow", "Dispatch (Red)"))
        self.label_6.setText(_translate("MainWindow", "Toggle Switch:"))
        self.label_7.setText(_translate("MainWindow", "Toggle Block:"))
        self.comboSwitch.setItemText(0, _translate("MainWindow", "Switch (Block 13)"))
        self.comboSwitch.setItemText(1, _translate("MainWindow", "Switch (Block 29)"))
        self.comboSwitch.setItemText(2, _translate("MainWindow", "Switch (Block 57)"))
        self.comboSwitch.setItemText(3, _translate("MainWindow", "Switch (Block 63)"))
        self.comboSwitch.setItemText(4, _translate("MainWindow", "Switch (Block 77)"))
        self.comboSwitch.setItemText(5, _translate("MainWindow", "Switch (Block 85)"))
        self.label_8.setText(_translate("MainWindow", "Choose Switch:"))
        self.comboBlock.setItemText(0, _translate("MainWindow", "Block 1"))
        self.comboBlock.setItemText(1, _translate("MainWindow", "Block 2"))
        self.comboBlock.setItemText(2, _translate("MainWindow", "Block 3"))
        self.comboBlock.setItemText(3, _translate("MainWindow", "Block 4"))
        self.comboBlock.setItemText(4, _translate("MainWindow", "Block 5"))
        self.comboBlock.setItemText(5, _translate("MainWindow", "Block 6"))
        self.comboBlock.setItemText(6, _translate("MainWindow", "Block 7"))
        self.comboBlock.setItemText(7, _translate("MainWindow", "Block 8"))
        self.comboBlock.setItemText(8, _translate("MainWindow", "Block 9"))
        self.comboBlock.setItemText(9, _translate("MainWindow", "Block 10"))
        self.comboBlock.setItemText(10, _translate("MainWindow", "Block 11"))
        self.comboBlock.setItemText(11, _translate("MainWindow", "Block 12"))
        self.comboBlock.setItemText(12, _translate("MainWindow", "Block 13"))
        self.comboBlock.setItemText(13, _translate("MainWindow", "Block 14"))
        self.comboBlock.setItemText(14, _translate("MainWindow", "Block 15"))
        self.comboBlock.setItemText(15, _translate("MainWindow", "Block 16"))
        self.comboBlock.setItemText(16, _translate("MainWindow", "Block 17"))
        self.comboBlock.setItemText(17, _translate("MainWindow", "Block 18"))
        self.comboBlock.setItemText(18, _translate("MainWindow", "Block 19"))
        self.comboBlock.setItemText(19, _translate("MainWindow", "Block 20"))
        self.comboBlock.setItemText(20, _translate("MainWindow", "Block 21"))
        self.comboBlock.setItemText(21, _translate("MainWindow", "Block 22"))
        self.comboBlock.setItemText(22, _translate("MainWindow", "Block 23"))
        self.comboBlock.setItemText(23, _translate("MainWindow", "Block 24"))
        self.comboBlock.setItemText(24, _translate("MainWindow", "Block 25"))
        self.comboBlock.setItemText(25, _translate("MainWindow", "Block 26"))
        self.comboBlock.setItemText(26, _translate("MainWindow", "Block 27"))
        self.comboBlock.setItemText(27, _translate("MainWindow", "Block 28"))
        self.comboBlock.setItemText(28, _translate("MainWindow", "Block 29"))
        self.comboBlock.setItemText(29, _translate("MainWindow", "Block 30"))
        self.comboBlock.setItemText(30, _translate("MainWindow", "Block 31"))
        self.comboBlock.setItemText(31, _translate("MainWindow", "Block 32"))
        self.comboBlock.setItemText(32, _translate("MainWindow", "Block 33"))
        self.comboBlock.setItemText(33, _translate("MainWindow", "Block 34"))
        self.comboBlock.setItemText(34, _translate("MainWindow", "Block 35"))
        self.comboBlock.setItemText(35, _translate("MainWindow", "Block 36"))
        self.comboBlock.setItemText(36, _translate("MainWindow", "Block 37"))
        self.comboBlock.setItemText(37, _translate("MainWindow", "Block 38"))
        self.comboBlock.setItemText(38, _translate("MainWindow", "Block 39"))
        self.comboBlock.setItemText(39, _translate("MainWindow", "Block 40"))
        self.comboBlock.setItemText(40, _translate("MainWindow", "Block 41"))
        self.comboBlock.setItemText(41, _translate("MainWindow", "Block 42"))
        self.comboBlock.setItemText(42, _translate("MainWindow", "Block 43"))
        self.comboBlock.setItemText(43, _translate("MainWindow", "Block 44"))
        self.comboBlock.setItemText(44, _translate("MainWindow", "Block 45"))
        self.comboBlock.setItemText(45, _translate("MainWindow", "Block 46"))
        self.comboBlock.setItemText(46, _translate("MainWindow", "Block 47"))
        self.comboBlock.setItemText(47, _translate("MainWindow", "Block 48"))
        self.comboBlock.setItemText(48, _translate("MainWindow", "Block 49"))
        self.comboBlock.setItemText(49, _translate("MainWindow", "Block 50"))
        self.comboBlock.setItemText(50, _translate("MainWindow", "Block 51"))
        self.comboBlock.setItemText(51, _translate("MainWindow", "Block 52"))
        self.comboBlock.setItemText(52, _translate("MainWindow", "Block 53"))
        self.comboBlock.setItemText(53, _translate("MainWindow", "Block 54"))
        self.comboBlock.setItemText(54, _translate("MainWindow", "Block 55"))
        self.comboBlock.setItemText(55, _translate("MainWindow", "Block 56"))
        self.comboBlock.setItemText(56, _translate("MainWindow", "Block 57"))
        self.comboBlock.setItemText(57, _translate("MainWindow", "Block 58"))
        self.comboBlock.setItemText(58, _translate("MainWindow", "Block 59"))
        self.comboBlock.setItemText(59, _translate("MainWindow", "Block 60"))
        self.comboBlock.setItemText(60, _translate("MainWindow", "Block 61"))
        self.comboBlock.setItemText(61, _translate("MainWindow", "Block 62"))
        self.comboBlock.setItemText(62, _translate("MainWindow", "Block 63"))
        self.comboBlock.setItemText(63, _translate("MainWindow", "Block 64"))
        self.comboBlock.setItemText(64, _translate("MainWindow", "Block 65"))
        self.comboBlock.setItemText(65, _translate("MainWindow", "Block 66"))
        self.comboBlock.setItemText(66, _translate("MainWindow", "Block 67"))
        self.comboBlock.setItemText(67, _translate("MainWindow", "Block 68"))
        self.comboBlock.setItemText(68, _translate("MainWindow", "Block 69"))
        self.comboBlock.setItemText(69, _translate("MainWindow", "Block 70"))
        self.comboBlock.setItemText(70, _translate("MainWindow", "Block 71"))
        self.comboBlock.setItemText(71, _translate("MainWindow", "Block 72"))
        self.comboBlock.setItemText(72, _translate("MainWindow", "Block 73"))
        self.comboBlock.setItemText(73, _translate("MainWindow", "Block 74"))
        self.comboBlock.setItemText(74, _translate("MainWindow", "Block 75"))
        self.comboBlock.setItemText(75, _translate("MainWindow", "Block 76"))
        self.comboBlock.setItemText(76, _translate("MainWindow", "Block 77"))
        self.comboBlock.setItemText(77, _translate("MainWindow", "Block 78"))
        self.comboBlock.setItemText(78, _translate("MainWindow", "Block 79"))
        self.comboBlock.setItemText(79, _translate("MainWindow", "Block 80"))
        self.comboBlock.setItemText(80, _translate("MainWindow", "Block 81"))
        self.comboBlock.setItemText(81, _translate("MainWindow", "Block 82"))
        self.comboBlock.setItemText(82, _translate("MainWindow", "Block 83"))
        self.comboBlock.setItemText(83, _translate("MainWindow", "Block 84"))
        self.comboBlock.setItemText(84, _translate("MainWindow", "Block 85"))
        self.comboBlock.setItemText(85, _translate("MainWindow", "Block 86"))
        self.comboBlock.setItemText(86, _translate("MainWindow", "Block 87"))
        self.comboBlock.setItemText(87, _translate("MainWindow", "Block 88"))
        self.comboBlock.setItemText(88, _translate("MainWindow", "Block 89"))
        self.comboBlock.setItemText(89, _translate("MainWindow", "Block 90"))
        self.comboBlock.setItemText(90, _translate("MainWindow", "Block 91"))
        self.comboBlock.setItemText(91, _translate("MainWindow", "Block 92"))
        self.comboBlock.setItemText(92, _translate("MainWindow", "Block 93"))
        self.comboBlock.setItemText(93, _translate("MainWindow", "Block 94"))
        self.comboBlock.setItemText(94, _translate("MainWindow", "Block 95"))
        self.comboBlock.setItemText(95, _translate("MainWindow", "Block 96"))
        self.comboBlock.setItemText(96, _translate("MainWindow", "Block 97"))
        self.comboBlock.setItemText(97, _translate("MainWindow", "Block 98"))
        self.comboBlock.setItemText(98, _translate("MainWindow", "Block 99"))
        self.comboBlock.setItemText(99, _translate("MainWindow", "Block 100"))
        self.comboBlock.setItemText(100, _translate("MainWindow", "Block 101"))
        self.comboBlock.setItemText(101, _translate("MainWindow", "Block 102"))
        self.comboBlock.setItemText(102, _translate("MainWindow", "Block 103"))
        self.comboBlock.setItemText(103, _translate("MainWindow", "Block 104"))
        self.comboBlock.setItemText(104, _translate("MainWindow", "Block 105"))
        self.comboBlock.setItemText(105, _translate("MainWindow", "Block 106"))
        self.comboBlock.setItemText(106, _translate("MainWindow", "Block 107"))
        self.comboBlock.setItemText(107, _translate("MainWindow", "Block 108"))
        self.comboBlock.setItemText(108, _translate("MainWindow", "Block 109"))
        self.comboBlock.setItemText(109, _translate("MainWindow", "Block 110"))
        self.comboBlock.setItemText(110, _translate("MainWindow", "Block 111"))
        self.comboBlock.setItemText(111, _translate("MainWindow", "Block 112"))
        self.comboBlock.setItemText(112, _translate("MainWindow", "Block 113"))
        self.comboBlock.setItemText(113, _translate("MainWindow", "Block 114"))
        self.comboBlock.setItemText(114, _translate("MainWindow", "Block 115"))
        self.comboBlock.setItemText(115, _translate("MainWindow", "Block 116"))
        self.comboBlock.setItemText(116, _translate("MainWindow", "Block 117"))
        self.comboBlock.setItemText(117, _translate("MainWindow", "Block 118"))
        self.comboBlock.setItemText(118, _translate("MainWindow", "Block 119"))
        self.comboBlock.setItemText(119, _translate("MainWindow", "Block 120"))
        self.comboBlock.setItemText(120, _translate("MainWindow", "Block 121"))
        self.comboBlock.setItemText(121, _translate("MainWindow", "Block 122"))
        self.comboBlock.setItemText(122, _translate("MainWindow", "Block 123"))
        self.comboBlock.setItemText(123, _translate("MainWindow", "Block 124"))
        self.comboBlock.setItemText(124, _translate("MainWindow", "Block 125"))
        self.comboBlock.setItemText(125, _translate("MainWindow", "Block 126"))
        self.comboBlock.setItemText(126, _translate("MainWindow", "Block 127"))
        self.comboBlock.setItemText(127, _translate("MainWindow", "Block 128"))
        self.comboBlock.setItemText(128, _translate("MainWindow", "Block 129"))
        self.comboBlock.setItemText(129, _translate("MainWindow", "Block 130"))
        self.comboBlock.setItemText(130, _translate("MainWindow", "Block 131"))
        self.comboBlock.setItemText(131, _translate("MainWindow", "Block 132"))
        self.comboBlock.setItemText(132, _translate("MainWindow", "Block 133"))
        self.comboBlock.setItemText(133, _translate("MainWindow", "Block 134"))
        self.comboBlock.setItemText(134, _translate("MainWindow", "Block 135"))
        self.comboBlock.setItemText(135, _translate("MainWindow", "Block 136"))
        self.comboBlock.setItemText(136, _translate("MainWindow", "Block 137"))
        self.comboBlock.setItemText(137, _translate("MainWindow", "Block 138"))
        self.comboBlock.setItemText(138, _translate("MainWindow", "Block 139"))
        self.comboBlock.setItemText(139, _translate("MainWindow", "Block 140"))
        self.comboBlock.setItemText(140, _translate("MainWindow", "Block 141"))
        self.comboBlock.setItemText(141, _translate("MainWindow", "Block 142"))
        self.comboBlock.setItemText(142, _translate("MainWindow", "Block 143"))
        self.comboBlock.setItemText(143, _translate("MainWindow", "Block 144"))
        self.comboBlock.setItemText(144, _translate("MainWindow", "Block 145"))
        self.comboBlock.setItemText(145, _translate("MainWindow", "Block 146"))
        self.comboBlock.setItemText(146, _translate("MainWindow", "Block 147"))
        self.comboBlock.setItemText(147, _translate("MainWindow", "Block 148"))
        self.comboBlock.setItemText(148, _translate("MainWindow", "Block 149"))
        self.comboBlock.setItemText(149, _translate("MainWindow", "Block 150"))
        self.label_9.setText(_translate("MainWindow", "Choose Block:"))
        self.btnToggleSwitch.setText(_translate("MainWindow", "Toggle Switch"))
        self.btnToggleBlock.setText(_translate("MainWindow", "Toggle Block"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_maintenance), _translate("MainWindow", "Maintenance"))
        self.label.setText(_translate("MainWindow", "Passengers/Hour"))
        self.label_2.setText(_translate("MainWindow", "Throughput:"))
        self.label_19.setText(_translate("MainWindow", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
