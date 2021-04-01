from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer
import sys

from ctc_main import ctc_qtui_test
from wayside_main import wayside_qtui_test
from tkm_main import tkm_test
from tnm_main import tnm_display
from tnc_main import TrainControllerMain


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

		self.tnc_thread = QThread()
		self.tnc = TrainControllerMain()
		self.tnc.moveToThread(self.tnc_thread)
		self.tnc_thread.start()
		
		self.time_thread = QThread()
		self.timer = QTimer()
		self.timer.setInterval(1000);
		self.timer.moveToThread(self.time_thread)

		self.time_thread.started.connect(self.timer.start)
		self.timer.timeout.connect(self.timing)

		self.time_thread.start()

	def timing(self):
		self.sec = self.time - (self.check*60)
		if self.sec == 60:
			self.mint = self.mint+1
			self.sec = 0
			self.check = self.check+1
			if self.mint ==  60:
				self.hr = self.hr+1
				self.mint = 0
				if self.hr == 24:
					self.hr = 0
		print('The time is ' + str(self.hr)+ ':' + str(self.mint) + ':' +str(self.sec))
		signals.time.emit(self.sec,self.mint,self.hr,self.time)
		self.time += 1

if __name__ == '__main__':

	app = QtWidgets.QApplication(sys.argv)

	system_environment = SystemEnvironment()

	app.exec_()


