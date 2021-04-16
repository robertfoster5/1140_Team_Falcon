from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer
import sys

from ctc_main import ctc_qtui_test
from wayside_main import wayside_qtui_test
from tkm_main import tkm_test
from tnm_main import tnm_display
from tnm_main import tnm_failureTest
from tnc_main import TrainControllerMain
from time_main import TimeMain


#from t_time import timing
from signals import signals


class SystemEnvironment(QObject):
	def __init__(self):
		super().__init__()

		self.sec = 0
		self.mint = 0
		self.hr = 0
		self.check = 0
		self.time = 0

		self.ctc_thread = QThread()
		self.ctc = ctc_qtui_test()
		self.ctc.moveToThread(self.ctc_thread)
		self.ctc_thread.start()

		self.wayside_thread = QThread()
		self.wayside = wayside_qtui_test()
		self.wayside.moveToThread(self.wayside_thread)
		self.wayside_thread.start()

		self.tkm_thread = QThread()
		self.tkm = tkm_test()
		self.tkm.moveToThread(self.tkm_thread)
		self.tkm_thread.start()

		self.tnm_thread = QThread()
		self.tnm = tnm_display()
		self.tnm.moveToThread(self.tnm_thread)
		self.tnm_thread.start()

		self.tnm_thread_two = QThread()
		self.tnm = tnm_failureTest()
		self.tnm.moveToThread(self.tnm_thread_two)
		self.tnm_thread_two.start()

		self.tnc_thread = QThread()
		self.tnc = TrainControllerMain()
		self.tnc.moveToThread(self.tnc_thread)
		self.tnc_thread.start()

		self.time_ui_thread = QThread()
		self.time_ui = TimeMain()
		self.time_ui.moveToThread(self.time_ui_thread)
		self.time_ui_thread.start()


if __name__ == '__main__':

	app = QtWidgets.QApplication(sys.argv)

	system_environment = SystemEnvironment()

	app.exec_()


