from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal

from ctc_main import ctc_qtui_test
from wayside_main import wayside_qtui_test
from tkm_main import tkm_test
from tnm_main import tnm_display
from tnc_main import TrainControllerMain

from t_time import timing


class SystemEnvironment(QObject):
    def __init__(self):
        super().__init__()

        self.ctc_thread = QThread()
        self.ctc = ctc_qtui_test()
        self.ctc.moveToThread(self.ctc_thread)

        self.wayside_thread = QThread()
        self.wayside = wayside_qtui_test()
        self.wayside.moveToThread(self.wayside_thread)

        self.tkm_thread = QThread()
        self.tkm = tkm_test()
        self.tkm.moveToThread(self.tkm_thread)

        self.tnm_thread = QThread()
        self.tnm = tnm_display()
        self.tnm.moveToThread(self.tnm_thread)

        self.tnc_thread = QThread()
        self.tnc = TrainControllerMain()
        self.tnc.moveToThread(self.tnc_thread)

        self.time_thread = QThread()
        self.time = timing()
        self.time.moveToThread(self.time_thread)

        self.ctc_thread.start()
        self.wayside_thread.start()
        self.tkm_thread.start()
        self.tnm_thread.start()
        self.tnc_thread.start()
        self.time_thread.start()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    system_environment = SystemEnvironment()

    app.exec_()


