from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from signals import signals

class mil_tim(object):
	def __init__(self,env):
		self.env = env
		self.sec = 0
		self.mint = 0
		self.hr = 0
		self.action = env.process(self.run())
		
		
	def run(self):
		check = 0
		while True:
			self.sec = self.env.now - (check*60)
			if self.sec == 60:
				 self.mint = self.mint+1
				 self.sec = 0
				 check = check+1
				 if self.mint ==  60:
					 self.hr = self.hr+1
					 self.mint = 0
					 if self.hr == 24:
						 self.hr = 0
			signals.time.emit(self.sec,self.mint,self.hr,self.env.now)
			yield self.env.timeout(1)
