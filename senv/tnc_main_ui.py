# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\lieri\Documents\School_Folder\Junior\1140\train_controller_qtui.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(529, 684)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.train_num = QtWidgets.QComboBox(self.centralwidget)
        self.train_num.setMinimumSize(QtCore.QSize(505, 0))
        self.train_num.setMaximumSize(QtCore.QSize(505, 16777215))
        self.train_num.setObjectName("train_num")
        self.train_num.addItem("")
        self.train_num.addItem("")
        self.train_num.addItem("")
        self.train_num.addItem("")
        self.train_num.addItem("")
        self.train_num.addItem("")
        self.train_num.addItem("")
        self.train_num.addItem("")
        self.train_num.addItem("")
        self.train_num.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.SpanningRole, self.train_num)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setMinimumSize(QtCore.QSize(250, 250))
        self.widget.setMaximumSize(QtCore.QSize(250, 250))
        self.widget.setStyleSheet("background-color: white;\n"
"border-width: 2px;\n"
"border-style:  solid;\n"
"border-color: black; ")
        self.widget.setObjectName("widget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.widget)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setMinimumSize(QtCore.QSize(250, 200))
        self.widget_6.setMaximumSize(QtCore.QSize(250, 200))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.widget_6.setFont(font)
        self.widget_6.setStyleSheet("background-color: none; border: none;")
        self.widget_6.setObjectName("widget_6")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.widget_6)
        self.gridLayout_5.setContentsMargins(3, 3, 3, 3)
        self.gridLayout_5.setSpacing(3)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.announce_text = QtWidgets.QPlainTextEdit(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(29)
        self.announce_text.setFont(font)
        self.announce_text.setStyleSheet("background-color: none; border: none;")
        self.announce_text.setObjectName("announce_text")
        self.gridLayout_5.addWidget(self.announce_text, 1, 0, 1, 1)
        self.gridLayout_3.addWidget(self.widget_6, 1, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(250, 50))
        self.label_4.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: lightgrey;")
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setMinimumSize(QtCore.QSize(250, 250))
        self.widget_2.setMaximumSize(QtCore.QSize(250, 250))
        self.widget_2.setStyleSheet("background-color: white;\n"
"border-width: 2px;\n"
"border-style:  solid;\n"
"border-color: black; ")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setMinimumSize(QtCore.QSize(250, 50))
        self.label_2.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: lightgrey;")
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.widget_2)
        self.frame.setStyleSheet("background-color: none; border: none;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.right_door_check = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.right_door_check.setFont(font)
        self.right_door_check.setStyleSheet("")
        self.right_door_check.setAutoRepeat(False)
        self.right_door_check.setObjectName("right_door_check")
        self.gridLayout.addWidget(self.right_door_check, 0, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_5 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 1)
        self.left_door_check = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.left_door_check.setFont(font)
        self.left_door_check.setStyleSheet("")
        self.left_door_check.setAutoRepeat(False)
        self.left_door_check.setObjectName("left_door_check")
        self.gridLayout.addWidget(self.left_door_check, 1, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_6 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 2, 0, 1, 1)
        self.in_light_check = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.in_light_check.setFont(font)
        self.in_light_check.setStyleSheet("")
        self.in_light_check.setAutoRepeat(False)
        self.in_light_check.setObjectName("in_light_check")
        self.gridLayout.addWidget(self.in_light_check, 2, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_7 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)
        self.tunnel_light_check = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.tunnel_light_check.setFont(font)
        self.tunnel_light_check.setStyleSheet("")
        self.tunnel_light_check.setAutoRepeat(False)
        self.tunnel_light_check.setObjectName("tunnel_light_check")
        self.gridLayout.addWidget(self.tunnel_light_check, 3, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_10 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)
        self.beam_light_check = QtWidgets.QCheckBox(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.beam_light_check.setFont(font)
        self.beam_light_check.setStyleSheet("")
        self.beam_light_check.setAutoRepeat(False)
        self.beam_light_check.setObjectName("beam_light_check")
        self.gridLayout.addWidget(self.beam_light_check, 4, 1, 1, 1, QtCore.Qt.AlignHCenter)
        self.gridLayout_2.addWidget(self.frame, 1, 0, 1, 1)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setMinimumSize(QtCore.QSize(250, 350))
        self.widget_3.setMaximumSize(QtCore.QSize(250, 350))
        self.widget_3.setStyleSheet("background-color: white;\n"
"border-width: 2px;\n"
"border-style:  solid;\n"
"border-color: black; ")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.widget_3)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setMinimumSize(QtCore.QSize(250, 50))
        self.label_3.setMaximumSize(QtCore.QSize(250, 50))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: lightgrey;")
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 0, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.widget_3)
        self.frame_2.setStyleSheet("background-color: none; border: none;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 14))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.gridLayout_9.addWidget(self.label_9, 3, 0, 1, 1)
        self.power_text = QtWidgets.QTextBrowser(self.frame_4)
        self.power_text.setMaximumSize(QtCore.QSize(70, 25))
        self.power_text.setStyleSheet("background-color: white;\n"
"border-width: 1px;\n"
"border-style:  solid;\n"
"border-color: black; ")
        self.power_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.power_text.setObjectName("power_text")
        self.gridLayout_9.addWidget(self.power_text, 6, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_8 = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_9.addWidget(self.label_8, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_9.addItem(spacerItem, 7, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.frame_4)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.gridLayout_9.addWidget(self.label_12, 8, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.auto_check = QtWidgets.QCheckBox(self.frame_4)
        self.auto_check.setMaximumSize(QtCore.QSize(70, 25))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.auto_check.setFont(font)
        self.auto_check.setObjectName("auto_check")
        self.gridLayout_9.addWidget(self.auto_check, 9, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.max_speed_text = QtWidgets.QTextBrowser(self.frame_4)
        self.max_speed_text.setMaximumSize(QtCore.QSize(70, 25))
        self.max_speed_text.setStyleSheet("background-color: white;\n"
"border-width: 1px;\n"
"border-style:  solid;\n"
"border-color: black; ")
        self.max_speed_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.max_speed_text.setObjectName("max_speed_text")
        self.gridLayout_9.addWidget(self.max_speed_text, 4, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.label_11 = QtWidgets.QLabel(self.frame_4)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout_9.addWidget(self.label_11, 5, 0, 1, 1, QtCore.Qt.AlignHCenter)
        self.curr_speed_text = QtWidgets.QTextBrowser(self.frame_4)
        self.curr_speed_text.setMaximumSize(QtCore.QSize(70, 25))
        self.curr_speed_text.setStyleSheet("background-color: white;\n"
"border-width: 1px;\n"
"border-style:  solid;\n"
"border-color: black; ")
        self.curr_speed_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.curr_speed_text.setObjectName("curr_speed_text")
        self.gridLayout_9.addWidget(self.curr_speed_text, 2, 0, 1, 1)
        self.gridLayout_7.addWidget(self.frame_4, 0, 1, 1, 1)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.set_speed_text = QtWidgets.QTextBrowser(self.frame_3)
        self.set_speed_text.setMaximumSize(QtCore.QSize(70, 25))
        self.set_speed_text.setStyleSheet("background-color: white;\n"
"border-width: 1px;\n"
"border-style:  solid;\n"
"border-color: black; ")
        self.set_speed_text.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.set_speed_text.setObjectName("set_speed_text")
        self.gridLayout_10.addWidget(self.set_speed_text, 2, 0, 1, 6, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.listWidget = QtWidgets.QListWidget(self.frame_3)
        self.listWidget.setMinimumSize(QtCore.QSize(30, 0))
        self.listWidget.setMaximumSize(QtCore.QSize(20, 16777215))
        self.listWidget.setSizeIncrement(QtCore.QSize(1, 0))
        font = QtGui.QFont()
        font.setFamily("8514oem")
        font.setPointSize(10)
        self.listWidget.setFont(font)
        self.listWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.listWidget.setResizeMode(QtWidgets.QListView.Fixed)
        self.listWidget.setWordWrap(False)
        self.listWidget.setObjectName("listWidget")
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget.addItem(item)
        self.gridLayout_10.addWidget(self.listWidget, 4, 3, 1, 1, QtCore.Qt.AlignLeft)
        self.label_17 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setObjectName("label_17")
        self.gridLayout_10.addWidget(self.label_17, 1, 0, 1, 7, QtCore.Qt.AlignHCenter)
        self.speed_slider = QtWidgets.QSlider(self.frame_3)
        self.speed_slider.setStyleSheet("")
        self.speed_slider.setMaximum(45)
        self.speed_slider.setOrientation(QtCore.Qt.Vertical)
        self.speed_slider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.speed_slider.setTickInterval(5)
        self.speed_slider.setObjectName("speed_slider")
        self.gridLayout_10.addWidget(self.speed_slider, 4, 1, 1, 1, QtCore.Qt.AlignRight)
        self.gridLayout_7.addWidget(self.frame_3, 0, 0, 1, 1)
        self.gridLayout_4.addWidget(self.frame_2, 1, 0, 1, 1)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.widget_3)
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setMinimumSize(QtCore.QSize(250, 350))
        self.widget_4.setMaximumSize(QtCore.QSize(250, 350))
        self.widget_4.setAutoFillBackground(False)
        self.widget_4.setStyleSheet("background-color: white;\n"
"border-width: 2px;\n"
"border-style:  solid;\n"
"border-color: black; ")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.widget_4)
        self.gridLayout_8.setObjectName("gridLayout_8")
        spacerItem1 = QtWidgets.QSpacerItem(20, 67, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem1, 2, 1, 1, 1)
        self.brake_fail_led = QtWidgets.QPushButton(self.widget_4)
        self.brake_fail_led.setMinimumSize(QtCore.QSize(30, 30))
        self.brake_fail_led.setMaximumSize(QtCore.QSize(30, 30))
        self.brake_fail_led.setStyleSheet("border: 2px solid #555;border-radius: 15px;border-style: outset;background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,radius: 1.35, stop: 0 #fff, stop: 1 #888);padding: 5px; background-color: rgb(122, 0, 0);")
        self.brake_fail_led.setText("")
        self.brake_fail_led.setObjectName("brake_fail_led")
        self.gridLayout_8.addWidget(self.brake_fail_led, 0, 4, 1, 1)
        self.pass_brake_led = QtWidgets.QPushButton(self.widget_4)
        self.pass_brake_led.setMinimumSize(QtCore.QSize(30, 30))
        self.pass_brake_led.setMaximumSize(QtCore.QSize(30, 30))
        self.pass_brake_led.setStyleSheet("border: 2px solid #555;border-radius: 15px;border-style: outset;background: qradialgradient(cx: 0.3, cy: -0.4, fx: 0.3, fy: -0.4,radius: 1.35, stop: 0 #fff, stop: 1 #888);padding: 5px; background-color: rgb(122, 0, 0);")
        self.pass_brake_led.setText("")
        self.pass_brake_led.setObjectName("pass_brake_led")
        self.gridLayout_8.addWidget(self.pass_brake_led, 1, 4, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 103, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_8.addItem(spacerItem2, 4, 0, 1, 1)
        self.brake_button = QtWidgets.QPushButton(self.widget_4)
        self.brake_button.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.brake_button.setFont(font)
        self.brake_button.setStyleSheet("background-color: red; color: white;")
        self.brake_button.setObjectName("brake_button")
        self.gridLayout_8.addWidget(self.brake_button, 5, 0, 1, 5)
        self.brake_button_2 = QtWidgets.QPushButton(self.widget_4)
        self.brake_button_2.setMinimumSize(QtCore.QSize(0, 70))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.brake_button_2.setFont(font)
        self.brake_button_2.setStyleSheet("background-color: gray; color: white;")
        self.brake_button_2.setObjectName("brake_button_2")
        self.gridLayout_8.addWidget(self.brake_button_2, 3, 0, 1, 5)
        self.label_16 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("background-color: none; border: none;")
        self.label_16.setObjectName("label_16")
        self.gridLayout_8.addWidget(self.label_16, 1, 0, 1, 4, QtCore.Qt.AlignLeft)
        self.label_13 = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet("background-color: none; border: none;")
        self.label_13.setObjectName("label_13")
        self.gridLayout_8.addWidget(self.label_13, 0, 0, 1, 4, QtCore.Qt.AlignLeft)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.widget_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 529, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.train_num.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.train_num.setItemText(0, _translate("MainWindow", "Train 1"))
        self.train_num.setItemText(1, _translate("MainWindow", "Train 2"))
        self.train_num.setItemText(2, _translate("MainWindow", "Train 3"))
        self.train_num.setItemText(3, _translate("MainWindow", "Train 4"))
        self.train_num.setItemText(4, _translate("MainWindow", "Train 5"))
        self.train_num.setItemText(5, _translate("MainWindow", "Train 6"))
        self.train_num.setItemText(6, _translate("MainWindow", "Train 7"))
        self.train_num.setItemText(7, _translate("MainWindow", "Train 8"))
        self.train_num.setItemText(8, _translate("MainWindow", "Train 8"))
        self.train_num.setItemText(9, _translate("MainWindow", "Train 10"))
        self.label_4.setText(_translate("MainWindow", "Announcements"))
        self.label_2.setText(_translate("MainWindow", "Controls"))
        self.label.setText(_translate("MainWindow", "Right Door"))
        self.right_door_check.setText(_translate("MainWindow", "Closed"))
        self.label_5.setText(_translate("MainWindow", "Left Door"))
        self.left_door_check.setText(_translate("MainWindow", "Closed"))
        self.label_6.setText(_translate("MainWindow", "Interior Lights"))
        self.in_light_check.setText(_translate("MainWindow", "Off"))
        self.label_7.setText(_translate("MainWindow", "Tunnel Lights"))
        self.tunnel_light_check.setText(_translate("MainWindow", "Off"))
        self.label_10.setText(_translate("MainWindow", "Beam Lights"))
        self.beam_light_check.setText(_translate("MainWindow", "Off"))
        self.label_3.setText(_translate("MainWindow", "Speed"))
        self.label_9.setText(_translate("MainWindow", "Max Speed"))
        self.power_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "Current\n"
"Speed"))
        self.label_12.setText(_translate("MainWindow", "Automatic\n"
"Mode"))
        self.auto_check.setText(_translate("MainWindow", "Off"))
        self.max_speed_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "Power"))
        self.curr_speed_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.25pt;\"><br /></p></body></html>"))
        self.set_speed_text.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:9.75pt;\"><br /></p></body></html>"))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(1)
        item.setText(_translate("MainWindow", "40"))
        item = self.listWidget.item(3)
        item.setText(_translate("MainWindow", "30"))
        item = self.listWidget.item(5)
        item.setText(_translate("MainWindow", "20"))
        item = self.listWidget.item(7)
        item.setText(_translate("MainWindow", "10"))
        item = self.listWidget.item(9)
        item.setText(_translate("MainWindow", "0"))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_17.setText(_translate("MainWindow", "Set Speed"))
        self.brake_button.setText(_translate("MainWindow", "EMERGENCY BRAKE"))
        self.brake_button_2.setText(_translate("MainWindow", "Service Brake"))
        self.label_16.setText(_translate("MainWindow", "Passenger Brake"))
        self.label_13.setText(_translate("MainWindow", "Train Failure"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
