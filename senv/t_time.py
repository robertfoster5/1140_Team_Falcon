import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer
from signals import signals


class timing(QObject):
	def __init__(self):
		super().__init__()

		self.sec = 0
		self.mint = 0
		self.hr = 0
		self.check = 0
		self.time = 0

		self.timer = QTimer()
		self.timer.setInterval(1000)
		self.timer.start()

		self.timer.timeout.connect(self.time_incr)
		signals.time_multiplier.connect(self.set_multiplier)


	def time_incr(self):
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

	def set_multiplier(self,mult):
		self.timer.setInterval(1000/mult)



if __name__ == '__main__':
	t = timing()
