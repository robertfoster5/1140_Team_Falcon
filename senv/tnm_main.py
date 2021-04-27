#Main file for Train Model, taking in classes and functions to operate
#python code for QT Ui here
import sys
import time

from tnm_functions import EmergencyBraking
from tnm_functions import set_curr_speed
from tnm_functions import temp_control
from tnm_functions import pass_crew_count
from tnm_functions import stopping_dist
from tnm_functions import KilotoMile
from tnm_functions import meterToMile
from tnm_functions import MiletoMeter
from tnm_functions import AppendBeacon
from tnm_functions import GreenBeacon
from tnm_functions import RedBeacon

from PyQt5 import uic
from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from tnm_display import Ui_MainWindow
from tnm_failureTest import Ui_Test
from signals import signals
from t_time import timing


#_______________________________________________________________________
#Failure Test State for Train Model Interface
class tnm_failureTest(QObject):
	def __init__(self):
		super().__init__()
		self.TestUi = QtWidgets.QMainWindow()
		self.ui = Ui_Test()
		
		#display main program
		self.ui.setupUi(self.TestUi)
		self.TestUi.show()
		

		#Signals defined
		tnm_ebrake = pyqtSignal(bool, int)
		tnm_sendyard = pyqtSignal(bool, int)			#Track Model and Track Controller
		
		#define variables to be used in the Failure Interface
		self.car1_status1, self.car1_status2, self.car1_status3,self.car1_status4, self.car1_status5, self.car1_status6, self.car1_status7, self.car1_status8 = True,True,True,True,True,True,True,True
		self.car2_status1, self.car2_status2, self.car2_status3,self.car2_status4, self.car2_status5, self.car2_status6, self.car2_status7, self.car2_status8 = True,True,True,True,True,True,True,True
		self.car3_status1, self.car3_status2, self.car3_status3,self.car3_status4, self.car3_status5, self.car3_status6, self.car3_status7, self.car3_status8 = True,True,True,True,True,True,True,True
		self.car4_status1, self.car4_status2, self.car4_status3,self.car4_status4, self.car4_status5, self.car4_status6, self.car4_status7, self.car4_status8 = True,True,True,True,True,True,True,True
		self.car5_status1, self.car5_status2, self.car5_status3,self.car5_status4, self.car5_status5, self.car5_status6, self.car5_status7, self.car5_status8 = True,True,True,True,True,True,True,True
		self.train1_status, self.train2_status, self.train3_status, self.train4_status, self.train5_status, self.train6_status, self.train7_status, self.train8_status = True,True,True,True,True,True,True,True
		self.sendYard1, self.sendYard2, self.sendYard3, self.sendYard4, self.sendYard5, self.sendYard6, self.sendYard7, self.sendYard8 = False,False,False,False,False,False,False,False
		self.trainNum = 0
		self.routeLine = 0
		self.train1, self.train2, self.train3, self.train4, self.train5, self.train6, self.train7, self.train8 = "Train 1 Status", "Train 2 Status", "Train 3 Status", "Train 4 Status", "Train 5 Status", "Train 6 Status", "Train 7 Status","Train 8 Status"
		self.trainNum1, self.trainNum2, self.trainNum3, self.trainNum4, self.trainNum5, self.trainNum6, self.trainNum7, self.trainNum8 = 0,0,0,0,0,0,0,0
		self.eBrakeTest1, self.eBrakeTest2, self.eBrakeTest3, self.eBrakeTest4, self.eBrakeTest5, self.eBrakeTest6, self.eBrakeTest7, self.eBrakeTest1 = False,False,False,False,False,False,False,False
		signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
		signals.tkm_get_train_num.connect(self.setTrainInfo)
		
		#Defining Actions for specific UI Interactions
		signals.time.connect(self.update_Info)
		#self.pushButton.clicked.connect(self.update_Info)
		
		self.ui.lineEdit.editingFinished.connect(self.brake_fail_act)
		self.ui.lineEdit_2.editingFinished.connect(self.brake_fail_act)
		self.ui.lineEdit_3.editingFinished.connect(self.brake_fail_act)
		self.ui.lineEdit_4.editingFinished.connect(self.brake_fail_act)
		self.ui.lineEdit_5.editingFinished.connect(self.brake_fail_act)
		
		self.ui.lineEdit_7.editingFinished.connect(self.engine_fail_act)
		self.ui.lineEdit_12.editingFinished.connect(self.engine_fail_act)
		self.ui.lineEdit_13.editingFinished.connect(self.engine_fail_act)
		self.ui.lineEdit_14.editingFinished.connect(self.engine_fail_act)
		self.ui.lineEdit_15.editingFinished.connect(self.engine_fail_act)
		
		self.ui.lineEdit_21.editingFinished.connect(self.signalP_fail_act)

#_______________________________________________________________________
	#function to update Train Failure interface Info
	def update_Info(self):
		#Update Train Number based on Route Line
		if(self.trainNum1 == 1):
			self.ui.label.setText(self.train1)
		elif(self.trainNum2 == 1):
			self.ui.label.setText(self.train2)
		elif(self.trainNum3 == 1):
			self.ui.label.setText(self.train3)
		elif(self.trainNum4 == 1):
			self.ui.label.setText(self.train4)
		elif(self.trainNum5 == 1):
			self.ui.label.setText(self.train5)
		elif(self.trainNum6 == 1):
			self.ui.label.setText(self.train6)
		elif(self.trainNum7 == 1):
			self.ui.label.setText(self.train7)
		elif(self.trainNum8 == 1):
			self.ui.label.setText(self.train8)
		
		
		#Don't let Status LineEdits to be edited
		self.ui.lineEdit_6.setReadOnly(True)		#Brake Status's
		self.ui.lineEdit_11.setReadOnly(True)		
		self.ui.lineEdit_8.setReadOnly(True)		
		self.ui.lineEdit_9.setReadOnly(True)			
		self.ui.lineEdit_10.setReadOnly(True)	
		self.ui.lineEdit_16.setReadOnly(True)		#Engine Status's	
		self.ui.lineEdit_17.setReadOnly(True)	
		self.ui.lineEdit_18.setReadOnly(True)	
		self.ui.lineEdit_19.setReadOnly(True)		
		self.ui.lineEdit_20.setReadOnly(True)		
		self.ui.lineEdit_26.setReadOnly(True)		#Signal Pickup Status

#_______________________________________________________________________
	#function to delegate variables when Emergency Brake triggered
	def EmergencyBrakingTest(self):
		if(self.trainNum1 == 1 and self.eBrakeTest1 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest1, 1)
		elif(self.trainNum2 == 1 and self.eBrakeTest2 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest2, 2)
		elif(self.trainNum3 == 1 and self.eBrakeTest3 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest3, 3)
		elif(self.trainNum4 == 1 and self.eBrakeTest4 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest4, 4)
		elif(self.trainNum5 == 1 and self.eBrakeTest5 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest5, 5)
		elif(self.trainNum6 == 1 and self.eBrakeTest6 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest6, 6)
		elif(self.trainNum7 == 1 and self.eBrakeTest7 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest7, 7)
		elif(self.trainNum8 == 1 and self.eBrakeTest8 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest8, 8)			
			
#_______________________________________________________________________
	#function to set Emergency Brake from tnc
	def SetEBrakeTest(self, eBrakeTNC):
		if(self.trainNum1 == 1):
			self.eBrakeTest1 = eBrakeTNC
		elif(self.trainNum2 == 1):
			self.eBrakeTest2 = eBrakeTNC
		elif(self.trainNum3 == 1):
			self.eBrakeTest3 = eBrakeTNC
		elif(self.trainNum4 == 1):
			self.eBrakeTest4 = eBrakeTNC
		elif(self.trainNum5 == 1):
			self.eBrakeTest5 = eBrakeTNC
		elif(self.trainNum6 == 1):
			self.eBrakeTest6 = eBrakeTNC
		elif(self.trainNum7 == 1):
			self.eBrakeTest7 = eBrakeTNC
		elif(self.trainNum8 == 1):
			self.eBrakeTest8 = eBrakeTNC
		
#_______________________________________________________________________
	#function to address Brake Failure Status's
	def brake_fail_act(self):
		if(self.trainNum1 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui.lineEdit.text() == "Off" or self.ui.lineEdit.text() == "OFF" or self.ui.lineEdit.text() == "off"):	
				self.car1_status1 = True
				self.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False ,1)	
			elif(self.ui.lineEdit.text() == "On" or self.ui.lineEdit.text() == "ON" or self.ui.lineEdit.text() == "on"):
				self.car1_status1 = False	
				self.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True, 1)
			else:
				self.car1_status1 = True
				self.ui.lineEdit.setText("Off")
				self.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui.lineEdit_2.text() == "Off" or self.ui.lineEdit_2.text() == "OFF" or self.ui.lineEdit_2.text() == "off"):
				self.car2_status1 = True	
				self.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui.lineEdit_2.text() == "On" or self.ui.lineEdit_2.text() == "ON" or self.ui.lineEdit_2.text() == "on"):
				self.car2_status1 = False	
				self.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True,1)				
			else:
				self.car2_status1 = True
				self.ui.lineEdit_2.setText("Off")
				self.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui.lineEdit_3.text() == "Off" or self.ui.lineEdit_3.text() == "OFF" or self.ui.lineEdit_3.text() == "off"):		
				self.car3_status1 = True
				self.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui.lineEdit_3.text() == "On" or self.ui.lineEdit_3.text() == "ON" or self.ui.lineEdit_3.text() == "on"):
				self.car3_status1 = False
				self.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True		
				signals.tnm_sendyard.emit(True,1)			
			else:
				self.car3_status1 = True
				self.ui.lineEdit_3.setText("Off")
				self.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui.lineEdit_4.text() == "Off" or self.ui.lineEdit_4.text() == "OFF" or self.ui.lineEdit_4.text() == "off"):									
				self.car4_status1 = True
				self.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui.lineEdit_4.text() == "On" or self.ui.lineEdit_4.text() == "ON" or self.ui.lineEdit_4.text() == "on"):
				self.car4_status1 = False
				self.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True,1)							
			else:
				self.car4_status1 = True
				self.ui.lineEdit_4.setText("Off")
				self.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui.lineEdit_5.text() == "Off" or self.ui.lineEdit_5.text() == "OFF" or self.ui.lineEdit_5.text() == "off"):										
				self.car5_status1 = True
				self.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui.lineEdit_5.text() == "On" or self.ui.lineEdit_5.text() == "ON" or self.ui.lineEdit_5.text() == "on"):
				self.car5_status1 = False
				self.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True,1)					
			else:
				self.car5_status1 = True
				self.ui.lineEdit_5.setText("Off")
				self.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			#_______________________________________________________________________
		elif(self.trainNum2 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui.lineEdit.text() == "Off" or self.ui.lineEdit.text() == "OFF" or self.ui.lineEdit.text() == "off"):	
				self.car1_status2 = True
				self.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False ,2)	
			elif(self.ui.lineEdit.text() == "On" or self.ui.lineEdit.text() == "ON" or self.ui.lineEdit.text() == "on"):
				self.car1_status2 = False	
				self.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True, 2)
			else:
				self.car1_status2 = True
				self.ui.lineEdit.setText("Off")
				self.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui.lineEdit_2.text() == "Off" or self.ui.lineEdit_2.text() == "OFF" or self.ui.lineEdit_2.text() == "off"):
				self.car2_status2 = True	
				self.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui.lineEdit_2.text() == "On" or self.ui.lineEdit_2.text() == "ON" or self.ui.lineEdit_2.text() == "on"):
				self.car2_status2 = False	
				self.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True,2)				
			else:
				self.car2_status2 = True
				self.ui.lineEdit_2.setText("Off")
				self.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui.lineEdit_3.text() == "Off" or self.ui.lineEdit_3.text() == "OFF" or self.ui.lineEdit_3.text() == "off"):		
				self.car3_status2 = True
				self.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui.lineEdit_3.text() == "On" or self.ui.lineEdit_3.text() == "ON" or self.ui.lineEdit_3.text() == "on"):
				self.car3_status2 = False
				self.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True		
				signals.tnm_sendyard.emit(True,2)			
			else:
				self.car3_status2 = True
				self.ui.lineEdit_3.setText("Off")
				self.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui.lineEdit_4.text() == "Off" or self.ui.lineEdit_4.text() == "OFF" or self.ui.lineEdit_4.text() == "off"):									
				self.car4_status2 = True
				self.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui.lineEdit_4.text() == "On" or self.ui.lineEdit_4.text() == "ON" or self.ui.lineEdit_4.text() == "on"):
				self.car4_status2 = False
				self.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True,2)							
			else:
				self.car4_status2 = True
				self.ui.lineEdit_4.setText("Off")
				self.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui.lineEdit_5.text() == "Off" or self.ui.lineEdit_5.text() == "OFF" or self.ui.lineEdit_5.text() == "off"):										
				self.car5_status2 = True
				self.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui.lineEdit_5.text() == "On" or self.ui.lineEdit_5.text() == "ON" or self.ui.lineEdit_5.text() == "on"):
				self.car5_status2 = False
				self.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True,2)					
			else:
				self.car5_status2 = True
				self.ui.lineEdit_5.setText("Off")
				self.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			#__________________________________________________________________
		elif(self.trainNum3 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui.lineEdit.text() == "Off" or self.ui.lineEdit.text() == "OFF" or self.ui.lineEdit.text() == "off"):	
				self.car1_status3 = True
				self.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False ,3)	
			elif(self.ui.lineEdit.text() == "On" or self.ui.lineEdit.text() == "ON" or self.ui.lineEdit.text() == "on"):
				self.car1_status3 = False	
				self.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True, 3)
			else:
				self.car1_status3 = True
				self.ui.lineEdit.setText("Off")
				self.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui.lineEdit_2.text() == "Off" or self.ui.lineEdit_2.text() == "OFF" or self.ui.lineEdit_2.text() == "off"):
				self.car2_status3 = True	
				self.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui.lineEdit_2.text() == "On" or self.ui.lineEdit_2.text() == "ON" or self.ui.lineEdit_2.text() == "on"):
				self.car2_status3 = False	
				self.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True,3)				
			else:
				self.car2_status3 = True
				self.ui.lineEdit_2.setText("Off")
				self.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui.lineEdit_3.text() == "Off" or self.ui.lineEdit_3.text() == "OFF" or self.ui.lineEdit_3.text() == "off"):		
				self.car3_status3 = True
				self.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui.lineEdit_3.text() == "On" or self.ui.lineEdit_3.text() == "ON" or self.ui.lineEdit_3.text() == "on"):
				self.car3_status3 = False
				self.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True		
				signals.tnm_sendyard.emit(True,3)			
			else:
				self.car3_status3 = True
				self.ui.lineEdit_3.setText("Off")
				self.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui.lineEdit_4.text() == "Off" or self.ui.lineEdit_4.text() == "OFF" or self.ui.lineEdit_4.text() == "off"):									
				self.car4_status3 = True
				self.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui.lineEdit_4.text() == "On" or self.ui.lineEdit_4.text() == "ON" or self.ui.lineEdit_4.text() == "on"):
				self.car4_status3 = False
				self.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True,3)							
			else:
				self.car4_status3 = True
				self.ui.lineEdit_4.setText("Off")
				self.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui.lineEdit_5.text() == "Off" or self.ui.lineEdit_5.text() == "OFF" or self.ui.lineEdit_5.text() == "off"):										
				self.car5_status3 = True
				self.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui.lineEdit_5.text() == "On" or self.ui.lineEdit_5.text() == "ON" or self.ui.lineEdit_5.text() == "on"):
				self.car5_status3 = False
				self.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True,3)					
			else:
				self.car5_status3 = True
				self.ui.lineEdit_5.setText("Off")
				self.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			#_________________________________________________________________
		elif(self.trainNum4 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui.lineEdit.text() == "Off" or self.ui.lineEdit.text() == "OFF" or self.ui.lineEdit.text() == "off"):	
				self.car1_status4 = True
				self.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False ,4)	
			elif(self.ui.lineEdit.text() == "On" or self.ui.lineEdit.text() == "ON" or self.ui.lineEdit.text() == "on"):
				self.car1_status4 = False	
				self.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True, 4)
			else:
				self.car1_status4 = True
				self.ui.lineEdit.setText("Off")
				self.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui.lineEdit_2.text() == "Off" or self.ui.lineEdit_2.text() == "OFF" or self.ui.lineEdit_2.text() == "off"):
				self.car2_status4 = True	
				self.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui.lineEdit_2.text() == "On" or self.ui.lineEdit_2.text() == "ON" or self.ui.lineEdit_2.text() == "on"):
				self.car2_status4 = False	
				self.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True,4)				
			else:
				self.car2_status4 = True
				self.ui.lineEdit_2.setText("Off")
				self.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui.lineEdit_3.text() == "Off" or self.ui.lineEdit_3.text() == "OFF" or self.ui.lineEdit_3.text() == "off"):		
				self.car3_status4 = True
				self.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui.lineEdit_3.text() == "On" or self.ui.lineEdit_3.text() == "ON" or self.ui.lineEdit_3.text() == "on"):
				self.car3_status4 = False
				self.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True		
				signals.tnm_sendyard.emit(True,4)			
			else:
				self.car3_status4 = True
				self.ui.lineEdit_3.setText("Off")
				self.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui.lineEdit_4.text() == "Off" or self.ui.lineEdit_4.text() == "OFF" or self.ui.lineEdit_4.text() == "off"):									
				self.car4_status4 = True
				self.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui.lineEdit_4.text() == "On" or self.ui.lineEdit_4.text() == "ON" or self.ui.lineEdit_4.text() == "on"):
				self.car4_status4 = False
				self.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True,4)							
			else:
				self.car4_status4 = True
				self.ui.lineEdit_4.setText("Off")
				self.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui.lineEdit_5.text() == "Off" or self.ui.lineEdit_5.text() == "OFF" or self.ui.lineEdit_5.text() == "off"):										
				self.car5_status4 = True
				self.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui.lineEdit_5.text() == "On" or self.ui.lineEdit_5.text() == "ON" or self.ui.lineEdit_5.text() == "on"):
				self.car5_status4 = False
				self.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True,4)					
			else:
				self.car5_status4 = True
				self.ui.lineEdit_5.setText("Off")
				self.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			#__________________________________________________________________
		elif(self.trainNum5 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui.lineEdit.text() == "Off" or self.ui.lineEdit.text() == "OFF" or self.ui.lineEdit.text() == "off"):	
				self.car1_status5 = True
				self.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False ,5)	
			elif(self.ui.lineEdit.text() == "On" or self.ui.lineEdit.text() == "ON" or self.ui.lineEdit.text() == "on"):
				self.car1_status5 = False	
				self.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True, 5)
			else:
				self.car1_status5 = True
				self.ui.lineEdit.setText("Off")
				self.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui.lineEdit_2.text() == "Off" or self.ui.lineEdit_2.text() == "OFF" or self.ui.lineEdit_2.text() == "off"):
				self.car2_status5 = True	
				self.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui.lineEdit_2.text() == "On" or self.ui.lineEdit_2.text() == "ON" or self.ui.lineEdit_2.text() == "on"):
				self.car2_status5 = False	
				self.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True,5)				
			else:
				self.car2_status5 = True
				self.ui.lineEdit_2.setText("Off")
				self.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui.lineEdit_3.text() == "Off" or self.ui.lineEdit_3.text() == "OFF" or self.ui.lineEdit_3.text() == "off"):		
				self.car3_status5 = True
				self.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui.lineEdit_3.text() == "On" or self.ui.lineEdit_3.text() == "ON" or self.ui.lineEdit_3.text() == "on"):
				self.car3_status5 = False
				self.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True		
				signals.tnm_sendyard.emit(True,5)			
			else:
				self.car3_status5 = True
				self.ui.lineEdit_3.setText("Off")
				self.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui.lineEdit_4.text() == "Off" or self.ui.lineEdit_4.text() == "OFF" or self.ui.lineEdit_4.text() == "off"):									
				self.car4_status5 = True
				self.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui.lineEdit_4.text() == "On" or self.ui.lineEdit_4.text() == "ON" or self.ui.lineEdit_4.text() == "on"):
				self.car4_status5 = False
				self.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True,5)							
			else:
				self.car4_status5 = True
				self.ui.lineEdit_4.setText("Off")
				self.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui.lineEdit_5.text() == "Off" or self.ui.lineEdit_5.text() == "OFF" or self.ui.lineEdit_5.text() == "off"):										
				self.car5_status5 = True
				self.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui.lineEdit_5.text() == "On" or self.ui.lineEdit_5.text() == "ON" or self.ui.lineEdit_5.text() == "on"):
				self.car5_status5 = False
				self.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True,5)					
			else:
				self.car5_status5 = True
				self.ui.lineEdit_5.setText("Off")
				self.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			#___________________________________________________________________
		elif(self.trainNum6 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui.lineEdit.text() == "Off" or self.ui.lineEdit.text() == "OFF" or self.ui.lineEdit.text() == "off"):	
				self.car1_status6 = True
				self.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False ,6)	
			elif(self.ui.lineEdit.text() == "On" or self.ui.lineEdit.text() == "ON" or self.ui.lineEdit.text() == "on"):
				self.car1_status6 = False	
				self.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True, 6)
			else:
				self.car1_status6 = True
				self.ui.lineEdit.setText("Off")
				self.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui.lineEdit_2.text() == "Off" or self.ui.lineEdit_2.text() == "OFF" or self.ui.lineEdit_2.text() == "off"):
				self.car2_status6 = True	
				self.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui.lineEdit_2.text() == "On" or self.ui.lineEdit_2.text() == "ON" or self.ui.lineEdit_2.text() == "on"):
				self.car2_status6 = False	
				self.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True,6)				
			else:
				self.car2_status6 = True
				self.ui.lineEdit_2.setText("Off")
				self.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui.lineEdit_3.text() == "Off" or self.ui.lineEdit_3.text() == "OFF" or self.ui.lineEdit_3.text() == "off"):		
				self.car3_status6 = True
				self.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui.lineEdit_3.text() == "On" or self.ui.lineEdit_3.text() == "ON" or self.ui.lineEdit_3.text() == "on"):
				self.car3_status6 = False
				self.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True		
				signals.tnm_sendyard.emit(True,6)			
			else:
				self.car3_status6 = True
				self.ui.lineEdit_3.setText("Off")
				self.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui.lineEdit_4.text() == "Off" or self.ui.lineEdit_4.text() == "OFF" or self.ui.lineEdit_4.text() == "off"):									
				self.car4_status6 = True
				self.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui.lineEdit_4.text() == "On" or self.ui.lineEdit_4.text() == "ON" or self.ui.lineEdit_4.text() == "on"):
				self.car4_status6 = False
				self.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True,6)							
			else:
				self.car4_status6 = True
				self.ui.lineEdit_4.setText("Off")
				self.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui.lineEdit_5.text() == "Off" or self.ui.lineEdit_5.text() == "OFF" or self.ui.lineEdit_5.text() == "off"):										
				self.car5_status6 = True
				self.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui.lineEdit_5.text() == "On" or self.ui.lineEdit_5.text() == "ON" or self.ui.lineEdit_5.text() == "on"):
				self.car5_status6 = False
				self.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True,6)					
			else:
				self.car5_status6 = True
				self.ui.lineEdit_5.setText("Off")
				self.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			#______________________________________________________________________
		elif(self.trainNum7 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui.lineEdit.text() == "Off" or self.ui.lineEdit.text() == "OFF" or self.ui.lineEdit.text() == "off"):	
				self.car1_status7 = True
				self.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False ,7)	
			elif(self.ui.lineEdit.text() == "On" or self.ui.lineEdit.text() == "ON" or self.ui.lineEdit.text() == "on"):
				self.car1_status7 = False	
				self.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)
			else:
				self.car1_status7 = True
				self.ui.lineEdit.setText("Off")
				self.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui.lineEdit_2.text() == "Off" or self.ui.lineEdit_2.text() == "OFF" or self.ui.lineEdit_2.text() == "off"):
				self.car2_status7 = True	
				self.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui.lineEdit_2.text() == "On" or self.ui.lineEdit_2.text() == "ON" or self.ui.lineEdit_2.text() == "on"):
				self.car2_status7 = False	
				self.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)				
			else:
				self.car2_status7 = True
				self.ui.lineEdit_2.setText("Off")
				self.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui.lineEdit_3.text() == "Off" or self.ui.lineEdit_3.text() == "OFF" or self.ui.lineEdit_3.text() == "off"):		
				self.car3_status7 = True
				self.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui.lineEdit_3.text() == "On" or self.ui.lineEdit_3.text() == "ON" or self.ui.lineEdit_3.text() == "on"):
				self.car3_status7 = False
				self.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True		
				signals.tnm_sendyard.emit(True,7)			
			else:
				self.car3_status7 = True
				self.ui.lineEdit_3.setText("Off")
				self.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui.lineEdit_4.text() == "Off" or self.ui.lineEdit_4.text() == "OFF" or self.ui.lineEdit_4.text() == "off"):									
				self.car4_status7 = True
				self.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui.lineEdit_4.text() == "On" or self.ui.lineEdit_4.text() == "ON" or self.ui.lineEdit_4.text() == "on"):
				self.car4_status7 = False
				self.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)							
			else:
				self.car4_status7 = True
				self.ui.lineEdit_4.setText("Off")
				self.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui.lineEdit_5.text() == "Off" or self.ui.lineEdit_5.text() == "OFF" or self.ui.lineEdit_5.text() == "off"):										
				self.car5_status7 = True
				self.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui.lineEdit_5.text() == "On" or self.ui.lineEdit_5.text() == "ON" or self.ui.lineEdit_5.text() == "on"):
				self.car5_status7 = False
				self.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)					
			else:
				self.car5_status7 = True
				self.ui.lineEdit_5.setText("Off")
				self.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			#____________________________________________________________________
		elif(self.trainNum8 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui.lineEdit.text() == "Off" or self.ui.lineEdit.text() == "OFF" or self.ui.lineEdit.text() == "off"):	
				self.car1_status8 = True
				self.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False ,8)	
			elif(self.ui.lineEdit.text() == "On" or self.ui.lineEdit.text() == "ON" or self.ui.lineEdit.text() == "on"):
				self.car1_status8 = False	
				self.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)
			else:
				self.car1_status8 = True
				self.ui.lineEdit.setText("Off")
				self.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui.lineEdit_2.text() == "Off" or self.ui.lineEdit_2.text() == "OFF" or self.ui.lineEdit_2.text() == "off"):
				self.car2_status8 = True	
				self.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui.lineEdit_2.text() == "On" or self.ui.lineEdit_2.text() == "ON" or self.ui.lineEdit_2.text() == "on"):
				self.car2_status8 = False	
				self.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)				
			else:
				self.car2_status8 = True
				self.ui.lineEdit_2.setText("Off")
				self.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui.lineEdit_3.text() == "Off" or self.ui.lineEdit_3.text() == "OFF" or self.ui.lineEdit_3.text() == "off"):		
				self.car3_status8 = True
				self.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui.lineEdit_3.text() == "On" or self.ui.lineEdit_3.text() == "ON" or self.ui.lineEdit_3.text() == "on"):
				self.car3_status8 = False
				self.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True		
				signals.tnm_sendyard.emit(True,8)			
			else:
				self.car3_status8 = True
				self.ui.lineEdit_3.setText("Off")
				self.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui.lineEdit_4.text() == "Off" or self.ui.lineEdit_4.text() == "OFF" or self.ui.lineEdit_4.text() == "off"):									
				self.car4_status8 = True
				self.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui.lineEdit_4.text() == "On" or self.ui.lineEdit_4.text() == "ON" or self.ui.lineEdit_4.text() == "on"):
				self.car4_status8 = False
				self.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)							
			else:
				self.car4_status8 = True
				self.ui.lineEdit_4.setText("Off")
				self.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui.lineEdit_5.text() == "Off" or self.ui.lineEdit_5.text() == "OFF" or self.ui.lineEdit_5.text() == "off"):										
				self.car5_status8 = True
				self.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui.lineEdit_5.text() == "On" or self.ui.lineEdit_5.text() == "ON" or self.ui.lineEdit_5.text() == "on"):
				self.car5_status8 = False
				self.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)					
			else:
				self.car5_status8 = True
				self.ui.lineEdit_5.setText("Off")
				self.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
		
#_______________________________________________________________________
	#function to address Engine Failure Status's
	def engine_fail_act(self):
		if(self.trainNum1 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui.lineEdit_7.text() == "Off" or self.ui.lineEdit_7.text() == "OFF" or self.ui.lineEdit_7.text() == "off"):	
				self.car1_status1 = True
				self.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui.lineEdit_7.text() == "On" or self.ui.lineEdit_7.text() == "ON" or self.ui.lineEdit_7.text() == "on"):
				self.car1_status1 = False	
				self.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True,1)				
			else:
				self.car1_status1 = True
				self.ui.lineEdit_7.setText("Off")
				self.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui.lineEdit_12.text() == "Off" or self.ui.lineEdit_12.text() == "OFF" or self.ui.lineEdit_12.text() == "off"):
				self.car2_status1 = True	
				self.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui.lineEdit_12.text() == "On" or self.ui.lineEdit_12.text() == "ON" or self.ui.lineEdit_12.text() == "on"):
				self.car2_status1 = False	
				self.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True	
				signals.tnm_sendyard.emit(True,1)				
			else:
				self.car2_status1 = True
				self.ui.lineEdit_12.setText("Off")
				self.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui.lineEdit_13.text() == "Off" or self.ui.lineEdit_13.text() == "OFF" or self.ui.lineEdit_13.text() == "off"):		
				self.car3_status1 = True
				self.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui.lineEdit_13.text() == "On" or self.ui.lineEdit_13.text() == "ON" or self.ui.lineEdit_13.text() == "on"):
				self.car3_status1 = False
				self.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True,1)					
			else:
				self.car3_status1 = True
				self.ui.lineEdit_13.setText("Off")
				self.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui.lineEdit_14.text() == "Off" or self.ui.lineEdit_14.text() == "OFF" or self.ui.lineEdit_14.text() == "off"):									
				self.car4_status1 = True
				self.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui.lineEdit_14.text() == "On" or self.ui.lineEdit_14.text() == "ON" or self.ui.lineEdit_14.text() == "on"):
				self.car4_status1 = False
				self.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True,1)					
			else:
				self.car4_status1 = True
				self.ui.lineEdit_14.setText("Off")
				self.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui.lineEdit_15.text() == "Off" or self.ui.lineEdit_15.text() == "OFF" or self.ui.lineEdit_15.text() == "off"):										
				self.car5_status1 = True
				self.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui.lineEdit_15.text() == "On" or self.ui.lineEdit_15.text() == "ON" or self.ui.lineEdit_15.text() == "on"):
				self.car5_status1 = False
				self.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True,1)					
			else:
				self.car5_status1 = True
				self.ui.lineEdit_15.setText("Off")
				self.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			#__________________________________________________________________
		elif(self.trainNum2 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui.lineEdit_7.text() == "Off" or self.ui.lineEdit_7.text() == "OFF" or self.ui.lineEdit_7.text() == "off"):	
				self.car1_status2 = True
				self.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui.lineEdit_7.text() == "On" or self.ui.lineEdit_7.text() == "ON" or self.ui.lineEdit_7.text() == "on"):
				self.car1_status2 = False	
				self.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True,2)				
			else:
				self.car1_status2 = True
				self.ui.lineEdit_7.setText("Off")
				self.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui.lineEdit_12.text() == "Off" or self.ui.lineEdit_12.text() == "OFF" or self.ui.lineEdit_12.text() == "off"):
				self.car2_status2 = True	
				self.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui.lineEdit_12.text() == "On" or self.ui.lineEdit_12.text() == "ON" or self.ui.lineEdit_12.text() == "on"):
				self.car2_status2 = False	
				self.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True	
				signals.tnm_sendyard.emit(True,2)				
			else:
				self.car2_status2 = True
				self.ui.lineEdit_12.setText("Off")
				self.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui.lineEdit_13.text() == "Off" or self.ui.lineEdit_13.text() == "OFF" or self.ui.lineEdit_13.text() == "off"):		
				self.car3_status2 = True
				self.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui.lineEdit_13.text() == "On" or self.ui.lineEdit_13.text() == "ON" or self.ui.lineEdit_13.text() == "on"):
				self.car3_status2 = False
				self.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True,2)					
			else:
				self.car3_status2 = True
				self.ui.lineEdit_13.setText("Off")
				self.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui.lineEdit_14.text() == "Off" or self.ui.lineEdit_14.text() == "OFF" or self.ui.lineEdit_14.text() == "off"):									
				self.car4_status2 = True
				self.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui.lineEdit_14.text() == "On" or self.ui.lineEdit_14.text() == "ON" or self.ui.lineEdit_14.text() == "on"):
				self.car4_status2 = False
				self.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True,2)					
			else:
				self.car4_status2 = True
				self.ui.lineEdit_14.setText("Off")
				self.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui.lineEdit_15.text() == "Off" or self.ui.lineEdit_15.text() == "OFF" or self.ui.lineEdit_15.text() == "off"):										
				self.car5_status2 = True
				self.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui.lineEdit_15.text() == "On" or self.ui.lineEdit_15.text() == "ON" or self.ui.lineEdit_15.text() == "on"):
				self.car5_status2 = False
				self.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True,2)					
			else:
				self.car5_status2 = True
				self.ui.lineEdit_15.setText("Off")
				self.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			#____________________________________________________________________
		elif(self.trainNum3 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui.lineEdit_7.text() == "Off" or self.ui.lineEdit_7.text() == "OFF" or self.ui.lineEdit_7.text() == "off"):	
				self.car1_status3 = True
				self.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui.lineEdit_7.text() == "On" or self.ui.lineEdit_7.text() == "ON" or self.ui.lineEdit_7.text() == "on"):
				self.car1_status3 = False	
				self.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True,3)				
			else:
				self.car1_status3 = True
				self.ui.lineEdit_7.setText("Off")
				self.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui.lineEdit_12.text() == "Off" or self.ui.lineEdit_12.text() == "OFF" or self.ui.lineEdit_12.text() == "off"):
				self.car2_status3 = True	
				self.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui.lineEdit_12.text() == "On" or self.ui.lineEdit_12.text() == "ON" or self.ui.lineEdit_12.text() == "on"):
				self.car2_status3 = False	
				self.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True	
				signals.tnm_sendyard.emit(True,3)				
			else:
				self.car2_status3 = True
				self.ui.lineEdit_12.setText("Off")
				self.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui.lineEdit_13.text() == "Off" or self.ui.lineEdit_13.text() == "OFF" or self.ui.lineEdit_13.text() == "off"):		
				self.car3_status3 = True
				self.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui.lineEdit_13.text() == "On" or self.ui.lineEdit_13.text() == "ON" or self.ui.lineEdit_13.text() == "on"):
				self.car3_status3 = False
				self.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True,3)					
			else:
				self.car3_status3 = True
				self.ui.lineEdit_13.setText("Off")
				self.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui.lineEdit_14.text() == "Off" or self.ui.lineEdit_14.text() == "OFF" or self.ui.lineEdit_14.text() == "off"):									
				self.car4_status3 = True
				self.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui.lineEdit_14.text() == "On" or self.ui.lineEdit_14.text() == "ON" or self.ui.lineEdit_14.text() == "on"):
				self.car4_status3 = False
				self.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True,3)					
			else:
				self.car4_status3 = True
				self.ui.lineEdit_14.setText("Off")
				self.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui.lineEdit_15.text() == "Off" or self.ui.lineEdit_15.text() == "OFF" or self.ui.lineEdit_15.text() == "off"):										
				self.car5_status3 = True
				self.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui.lineEdit_15.text() == "On" or self.ui.lineEdit_15.text() == "ON" or self.ui.lineEdit_15.text() == "on"):
				self.car5_status3 = False
				self.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True,3)					
			else:
				self.car5_status3 = True
				self.ui.lineEdit_15.setText("Off")
				self.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			#__________________________________________________________________
		elif(self.trainNum4 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui.lineEdit_7.text() == "Off" or self.ui.lineEdit_7.text() == "OFF" or self.ui.lineEdit_7.text() == "off"):	
				self.car1_status4 = True
				self.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui.lineEdit_7.text() == "On" or self.ui.lineEdit_7.text() == "ON" or self.ui.lineEdit_7.text() == "on"):
				self.car1_status4 = False	
				self.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True,4)				
			else:
				self.car1_status4 = True
				self.ui.lineEdit_7.setText("Off")
				self.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui.lineEdit_12.text() == "Off" or self.ui.lineEdit_12.text() == "OFF" or self.ui.lineEdit_12.text() == "off"):
				self.car2_status4 = True	
				self.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui.lineEdit_12.text() == "On" or self.ui.lineEdit_12.text() == "ON" or self.ui.lineEdit_12.text() == "on"):
				self.car2_status4 = False	
				self.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True	
				signals.tnm_sendyard.emit(True,4)				
			else:
				self.car2_status4 = True
				self.ui.lineEdit_12.setText("Off")
				self.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui.lineEdit_13.text() == "Off" or self.ui.lineEdit_13.text() == "OFF" or self.ui.lineEdit_13.text() == "off"):		
				self.car3_status4 = True
				self.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui.lineEdit_13.text() == "On" or self.ui.lineEdit_13.text() == "ON" or self.ui.lineEdit_13.text() == "on"):
				self.car3_status4 = False
				self.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True,4)					
			else:
				self.car3_status4 = True
				self.ui.lineEdit_13.setText("Off")
				self.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui.lineEdit_14.text() == "Off" or self.ui.lineEdit_14.text() == "OFF" or self.ui.lineEdit_14.text() == "off"):									
				self.car4_status4 = True
				self.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui.lineEdit_14.text() == "On" or self.ui.lineEdit_14.text() == "ON" or self.ui.lineEdit_14.text() == "on"):
				self.car4_status4 = False
				self.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True,4)					
			else:
				self.car4_status4 = True
				self.ui.lineEdit_14.setText("Off")
				self.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui.lineEdit_15.text() == "Off" or self.ui.lineEdit_15.text() == "OFF" or self.ui.lineEdit_15.text() == "off"):										
				self.car5_status4 = True
				self.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui.lineEdit_15.text() == "On" or self.ui.lineEdit_15.text() == "ON" or self.ui.lineEdit_15.text() == "on"):
				self.car5_status4 = False
				self.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True,4)					
			else:
				self.car5_status4 = True
				self.ui.lineEdit_15.setText("Off")
				self.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			#____________________________________________________________________
		elif(self.trainNum5 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui.lineEdit_7.text() == "Off" or self.ui.lineEdit_7.text() == "OFF" or self.ui.lineEdit_7.text() == "off"):	
				self.car1_status5 = True
				self.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui.lineEdit_7.text() == "On" or self.ui.lineEdit_7.text() == "ON" or self.ui.lineEdit_7.text() == "on"):
				self.car1_status5 = False	
				self.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True,5)				
			else:
				self.car1_status5 = True
				self.ui.lineEdit_7.setText("Off")
				self.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui.lineEdit_12.text() == "Off" or self.ui.lineEdit_12.text() == "OFF" or self.ui.lineEdit_12.text() == "off"):
				self.car2_status5 = True	
				self.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui.lineEdit_12.text() == "On" or self.ui.lineEdit_12.text() == "ON" or self.ui.lineEdit_12.text() == "on"):
				self.car2_status5 = False	
				self.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True	
				signals.tnm_sendyard.emit(True,5)				
			else:
				self.car2_status5 = True
				self.ui.lineEdit_12.setText("Off")
				self.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui.lineEdit_13.text() == "Off" or self.ui.lineEdit_13.text() == "OFF" or self.ui.lineEdit_13.text() == "off"):		
				self.car3_status5 = True
				self.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui.lineEdit_13.text() == "On" or self.ui.lineEdit_13.text() == "ON" or self.ui.lineEdit_13.text() == "on"):
				self.car3_status5 = False
				self.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True,5)					
			else:
				self.car3_status5 = True
				self.ui.lineEdit_13.setText("Off")
				self.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui.lineEdit_14.text() == "Off" or self.ui.lineEdit_14.text() == "OFF" or self.ui.lineEdit_14.text() == "off"):									
				self.car4_status5 = True
				self.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui.lineEdit_14.text() == "On" or self.ui.lineEdit_14.text() == "ON" or self.ui.lineEdit_14.text() == "on"):
				self.car4_status5 = False
				self.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True,5)					
			else:
				self.car4_status5 = True
				self.ui.lineEdit_14.setText("Off")
				self.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui.lineEdit_15.text() == "Off" or self.ui.lineEdit_15.text() == "OFF" or self.ui.lineEdit_15.text() == "off"):										
				self.car5_status5 = True
				self.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui.lineEdit_15.text() == "On" or self.ui.lineEdit_15.text() == "ON" or self.ui.lineEdit_15.text() == "on"):
				self.car5_status5 = False
				self.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True,5)					
			else:
				self.car5_status5 = True
				self.ui.lineEdit_15.setText("Off")
				self.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			#____________________________________________________________________
		elif(self.trainNum6 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui.lineEdit_7.text() == "Off" or self.ui.lineEdit_7.text() == "OFF" or self.ui.lineEdit_7.text() == "off"):	
				self.car1_status6 = True
				self.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui.lineEdit_7.text() == "On" or self.ui.lineEdit_7.text() == "ON" or self.ui.lineEdit_7.text() == "on"):
				self.car1_status6 = False	
				self.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True,6)				
			else:
				self.car1_status6 = True
				self.ui.lineEdit_7.setText("Off")
				self.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui.lineEdit_12.text() == "Off" or self.ui.lineEdit_12.text() == "OFF" or self.ui.lineEdit_12.text() == "off"):
				self.car2_status6 = True	
				self.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui.lineEdit_12.text() == "On" or self.ui.lineEdit_12.text() == "ON" or self.ui.lineEdit_12.text() == "on"):
				self.car2_status6 = False	
				self.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True	
				signals.tnm_sendyard.emit(True,6)				
			else:
				self.car2_status6 = True
				self.ui.lineEdit_12.setText("Off")
				self.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui.lineEdit_13.text() == "Off" or self.ui.lineEdit_13.text() == "OFF" or self.ui.lineEdit_13.text() == "off"):		
				self.car3_status6 = True
				self.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui.lineEdit_13.text() == "On" or self.ui.lineEdit_13.text() == "ON" or self.ui.lineEdit_13.text() == "on"):
				self.car3_status6 = False
				self.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True,6)					
			else:
				self.car3_status6 = True
				self.ui.lineEdit_13.setText("Off")
				self.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui.lineEdit_14.text() == "Off" or self.ui.lineEdit_14.text() == "OFF" or self.ui.lineEdit_14.text() == "off"):									
				self.car4_status6 = True
				self.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui.lineEdit_14.text() == "On" or self.ui.lineEdit_14.text() == "ON" or self.ui.lineEdit_14.text() == "on"):
				self.car4_status6 = False
				self.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True,6)					
			else:
				self.car4_status6 = True
				self.ui.lineEdit_14.setText("Off")
				self.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui.lineEdit_15.text() == "Off" or self.ui.lineEdit_15.text() == "OFF" or self.ui.lineEdit_15.text() == "off"):										
				self.car5_status6 = True
				self.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui.lineEdit_15.text() == "On" or self.ui.lineEdit_15.text() == "ON" or self.ui.lineEdit_15.text() == "on"):
				self.car5_status6 = False
				self.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True,6)					
			else:
				self.car5_status6 = True
				self.ui.lineEdit_15.setText("Off")
				self.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			#_____________________________________________________________________
		elif(self.trainNum7 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui.lineEdit_7.text() == "Off" or self.ui.lineEdit_7.text() == "OFF" or self.ui.lineEdit_7.text() == "off"):	
				self.car1_status7 = True
				self.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui.lineEdit_7.text() == "On" or self.ui.lineEdit_7.text() == "ON" or self.ui.lineEdit_7.text() == "on"):
				self.car1_status7 = False	
				self.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)				
			else:
				self.car1_status7 = True
				self.ui.lineEdit_7.setText("Off")
				self.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui.lineEdit_12.text() == "Off" or self.ui.lineEdit_12.text() == "OFF" or self.ui.lineEdit_12.text() == "off"):
				self.car2_status7 = True	
				self.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui.lineEdit_12.text() == "On" or self.ui.lineEdit_12.text() == "ON" or self.ui.lineEdit_12.text() == "on"):
				self.car2_status7 = False	
				self.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True	
				signals.tnm_sendyard.emit(True,7)				
			else:
				self.car2_status7 = True
				self.ui.lineEdit_12.setText("Off")
				self.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui.lineEdit_13.text() == "Off" or self.ui.lineEdit_13.text() == "OFF" or self.ui.lineEdit_13.text() == "off"):		
				self.car3_status7 = True
				self.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui.lineEdit_13.text() == "On" or self.ui.lineEdit_13.text() == "ON" or self.ui.lineEdit_13.text() == "on"):
				self.car3_status7 = False
				self.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)					
			else:
				self.car3_status7 = True
				self.ui.lineEdit_13.setText("Off")
				self.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui.lineEdit_14.text() == "Off" or self.ui.lineEdit_14.text() == "OFF" or self.ui.lineEdit_14.text() == "off"):									
				self.car4_status7 = True
				self.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui.lineEdit_14.text() == "On" or self.ui.lineEdit_14.text() == "ON" or self.ui.lineEdit_14.text() == "on"):
				self.car4_status7 = False
				self.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)					
			else:
				self.car4_status7 = True
				self.ui.lineEdit_14.setText("Off")
				self.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui.lineEdit_15.text() == "Off" or self.ui.lineEdit_15.text() == "OFF" or self.ui.lineEdit_15.text() == "off"):										
				self.car5_status7 = True
				self.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui.lineEdit_15.text() == "On" or self.ui.lineEdit_15.text() == "ON" or self.ui.lineEdit_15.text() == "on"):
				self.car5_status7 = False
				self.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)					
			else:
				self.car5_status7 = True
				self.ui.lineEdit_15.setText("Off")
				self.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			#__________________________________________________________________
		elif(self.trainNum8 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui.lineEdit_7.text() == "Off" or self.ui.lineEdit_7.text() == "OFF" or self.ui.lineEdit_7.text() == "off"):	
				self.car1_status8 = True
				self.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui.lineEdit_7.text() == "On" or self.ui.lineEdit_7.text() == "ON" or self.ui.lineEdit_7.text() == "on"):
				self.car1_status8 = False	
				self.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)				
			else:
				self.car1_status8 = True
				self.ui.lineEdit_7.setText("Off")
				self.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui.lineEdit_12.text() == "Off" or self.ui.lineEdit_12.text() == "OFF" or self.ui.lineEdit_12.text() == "off"):
				self.car2_status8 = True	
				self.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui.lineEdit_12.text() == "On" or self.ui.lineEdit_12.text() == "ON" or self.ui.lineEdit_12.text() == "on"):
				self.car2_status8 = False	
				self.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True	
				signals.tnm_sendyard.emit(True,8)				
			else:
				self.car2_status8 = True
				self.ui.lineEdit_12.setText("Off")
				self.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui.lineEdit_13.text() == "Off" or self.ui.lineEdit_13.text() == "OFF" or self.ui.lineEdit_13.text() == "off"):		
				self.car3_status8 = True
				self.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui.lineEdit_13.text() == "On" or self.ui.lineEdit_13.text() == "ON" or self.ui.lineEdit_13.text() == "on"):
				self.car3_status8 = False
				self.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)					
			else:
				self.car3_status8 = True
				self.ui.lineEdit_13.setText("Off")
				self.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui.lineEdit_14.text() == "Off" or self.ui.lineEdit_14.text() == "OFF" or self.ui.lineEdit_14.text() == "off"):									
				self.car4_status8 = True
				self.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui.lineEdit_14.text() == "On" or self.ui.lineEdit_14.text() == "ON" or self.ui.lineEdit_14.text() == "on"):
				self.car4_status8 = False
				self.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)					
			else:
				self.car4_status8 = True
				self.ui.lineEdit_14.setText("Off")
				self.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui.lineEdit_15.text() == "Off" or self.ui.lineEdit_15.text() == "OFF" or self.ui.lineEdit_15.text() == "off"):										
				self.car5_status8 = True
				self.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui.lineEdit_15.text() == "On" or self.ui.lineEdit_15.text() == "ON" or self.ui.lineEdit_15.text() == "on"):
				self.car5_status8 = False
				self.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)					
			else:
				self.car5_status8 = True
				self.ui.lineEdit_15.setText("Off")
				self.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)

	
#_______________________________________________________________________
	#function to address Signal Pickup Failure Status's
	def signalP_fail_act(self):
		if(self.trainNum1 == 1):
			#train 1 Status Change
			#True means train 1 is functional
			if(self.ui.lineEdit_21.text() == "Off" or self.ui.lineEdit_21.text() == "OFF" or self.ui.lineEdit_21.text() == "off"):	
				self.train1_status = True
				self.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui.lineEdit_21.text() == "On" or self.ui.lineEdit_21.text() == "ON" or self.ui.lineEdit_21.text() == "on"):
				self.train1_status = False	
				self.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True,1)			
			else:
				self.train1_status = True
				self.ui.lineEdit_21.setText("Off")
				self.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			#________________________________________________________________
		elif(self.trainNum2 == 1):
			#train 2 Status Change
			#True means train 2 is functional
			if(self.ui.lineEdit_21.text() == "Off" or self.ui.lineEdit_21.text() == "OFF" or self.ui.lineEdit_21.text() == "off"):	
				self.train2_status = True
				self.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui.lineEdit_21.text() == "On" or self.ui.lineEdit_21.text() == "ON" or self.ui.lineEdit_21.text() == "on"):
				self.train2_status = False	
				self.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True,2)			
			else:
				self.train2_status = True
				self.ui.lineEdit_21.setText("Off")
				self.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			#______________________________________________________________________
		elif(self.trainNum3 == 1):
			#train 3 Status Change
			#True means train 3 is functional
			if(self.ui.lineEdit_21.text() == "Off" or self.ui.lineEdit_21.text() == "OFF" or self.ui.lineEdit_21.text() == "off"):	
				self.train3_status = True
				self.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui.lineEdit_21.text() == "On" or self.ui.lineEdit_21.text() == "ON" or self.ui.lineEdit_21.text() == "on"):
				self.train3_status = False	
				self.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True,3)			
			else:
				self.train3_status = True
				self.ui.lineEdit_21.setText("Off")
				self.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			#_________________________________________________________________
		elif(self.trainNum4 == 1):
			#train 4 Status Change
			#True means train 4 is functional
			if(self.ui.lineEdit_21.text() == "Off" or self.ui.lineEdit_21.text() == "OFF" or self.ui.lineEdit_21.text() == "off"):	
				self.train4_status = True
				self.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui.lineEdit_21.text() == "On" or self.ui.lineEdit_21.text() == "ON" or self.ui.lineEdit_21.text() == "on"):
				self.train4_status = False	
				self.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True,4)			
			else:
				self.train4_status = True
				self.ui.lineEdit_21.setText("Off")
				self.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			#_____________________________________________________________________
		elif(self.trainNum5 == 1):
			#train 5 Status Change
			#True means train 5 is functional
			if(self.ui.lineEdit_21.text() == "Off" or self.ui.lineEdit_21.text() == "OFF" or self.ui.lineEdit_21.text() == "off"):	
				self.train5_status = True
				self.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui.lineEdit_21.text() == "On" or self.ui.lineEdit_21.text() == "ON" or self.ui.lineEdit_21.text() == "on"):
				self.train5_status = False	
				self.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True,5)			
			else:
				self.train5_status = True
				self.ui.lineEdit_21.setText("Off")
				self.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			#_____________________________________________________________________
		elif(self.trainNum6 == 1):
			#train 6 Status Change
			#True means train 6 is functional
			if(self.ui.lineEdit_21.text() == "Off" or self.ui.lineEdit_21.text() == "OFF" or self.ui.lineEdit_21.text() == "off"):	
				self.train6_status = True
				self.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui.lineEdit_21.text() == "On" or self.ui.lineEdit_21.text() == "ON" or self.ui.lineEdit_21.text() == "on"):
				self.train6_status = False	
				self.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True,6)			
			else:
				self.train6_status = True
				self.ui.lineEdit_21.setText("Off")
				self.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			#___________________________________________________________________
		elif(self.trainNum7 == 1):
			#train 7 Status Change
			#True means train 7 is functional
			if(self.ui.lineEdit_21.text() == "Off" or self.ui.lineEdit_21.text() == "OFF" or self.ui.lineEdit_21.text() == "off"):	
				self.train7_status = True
				self.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui.lineEdit_21.text() == "On" or self.ui.lineEdit_21.text() == "ON" or self.ui.lineEdit_21.text() == "on"):
				self.train7_status = False	
				self.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)			
			else:
				self.train7_status = True
				self.ui.lineEdit_21.setText("Off")
				self.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			#____________________________________________________________________
		elif(self.trainNum8 == 1):
			#train 8 Status Change
			#True means train 8 is functional
			if(self.ui.lineEdit_21.text() == "Off" or self.ui.lineEdit_21.text() == "OFF" or self.ui.lineEdit_21.text() == "off"):	
				self.train8_status = True
				self.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui.lineEdit_21.text() == "On" or self.ui.lineEdit_21.text() == "ON" or self.ui.lineEdit_21.text() == "on"):
				self.train8_status = False	
				self.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)			
			else:
				self.train8_status = True
				self.ui.lineEdit_21.setText("Off")
				self.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
	

	#Function to check which line the train is on
	def setTrainInfo(self, tkmTrainNum, tkmTrainLine):
		#Set train Number
		self.trainNum = tkmTrainNum
		if(self.trainNum == 1):
			self.trainNum1 = 1
		elif(self.trainNum == 2):
			self.trainNum2 = 1
		elif(self.trainNum == 3):
			self.trainNum3 = 1
		elif(self.trainNum == 4):
			self.trainNum4 = 1
		elif(self.trainNum == 5):
			self.trainNum5 = 1
		elif(self.trainNum == 6):
			self.trainNum6 = 1
		elif(self.trainNum == 7):
			self.trainNum7 = 1
		elif(self.trainNum == 8):
			self.trainNum8 = 1
		
		#Set route line
		if(tkmTrainLine == "Red"):
			self.routeLine = 0
		elif(tkmTrainLine == "Green"):
			self.routeLine = 1
		
#_____________________________________________________________________________________________________________		
#_____________________________________________________________________________________________________________
#Main Window for Train Model Interface
class tnm_display(QObject):
	def __init__(self):
		#Ui_MainWindow.__init__(self)
		print("running train model")
		super().__init__()
		self.MainWindow = QtWidgets.QMainWindow()
		self.ui = Ui_MainWindow()
		
		#display main program
		self.ui.setupUi(self.MainWindow)
		self.MainWindow.show()
		
		#Signals defined here
		tnm_comm_speed = pyqtSignal(float, int)		#All signals for Track Controller
		tnm_curr_speed = pyqtSignal(float, int)
		tnm_authority = pyqtSignal(bool, int)
		tnm_beaconID = pyqtSignal(int, int)
		tnm_ebrake = pyqtSignal(bool, int)
		tnm_cab_temp = pyqtSignal(int)
		tnm_sendYard = pyqtSignal(int, int)
		tnm_block_finished_green = pyqtSignal(int)
		tnm_block_finished_red = pyqtSignal(int)
		tnm_curr_station = pyqtSignal(str, int)
		tnm_TrainDir = pyqtSignal(bool, int)
		tnm_train_stop_num = pyqtSignal(int)

#Define variables to be used in tnm_display
		self.TrainNum = 0
		self.TrainName1, self.TrainName2, self.TrainName3, self.TrainName4, self.TrainName5, self.TrainName6, self.TrainName7, self.TrainName8 = " -- Information"," -- Information"," -- Information"," -- Information"," -- Information"," -- Information"," -- Information"," -- Information"
		self.train1, self.train2, self.train3, self.train4, self.train5, self.train6, self.train7, self.train8 = "Train 1 Information", "Train 2 Information", "Train 3 Information", "Train 4 Information", "Train 5 Information", "Train 6 Information", "Train 7 Information", "Train 8 Information"
		#Train Number x - 0 if not added, 1 if on the track
		self.TrainNum1, self.TrainNum2, self.TrainNum3, self.TrainNum4, self.TrainNum5, self.TrainNum6, self.TrainNum7, self.TrainNum8 = 0,0,0,0,0,0,0,0	
		self.timeSeconds = 0
		signals.tkm_get_train_num.connect(self.setTrainStart)
	#authority connected from tkm
		self.block_authority1, self.block_authority2, self.block_authority3, self.block_authority4, self.block_authority5, self.block_authority6, self.block_authority7, self.block_authority8 = False,False,False,False,False,False,False,False
		signals.tkm_get_train_auth.connect(self.SetAuthority)
	#power connected from tnc
		self.curr_power1, self.curr_power2, self.curr_power3, self.curr_power4, self.curr_power5, self.curr_power6, self.curr_power7, self.curr_power8 = 0,0,0,0,0,0,0,0
		signals.tnc_power.connect(self.SetPower)
		self.curr_speed1, self.curr_speed2, self.curr_speed3, self.curr_speed4, self.curr_speed5, self.curr_speed6, self.curr_speed7, self.curr_speed8 = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
		self.curr_accl1, self.curr_accl2, self.curr_accl3, self.curr_accl4, self.curr_accl5, self.curr_accl6, self.curr_accl7, self.curr_accl8 = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
		self.comm_speed1, self.comm_speed2, self.comm_speed3, self.comm_speed4, self.comm_speed5, self.comm_speed6, self.comm_speed7, self.comm_speed8 = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
		signals.tkm_get_speed.connect(self.SetCommSpeed)
		#train starts at rest v		-> #Used as value for inital speed for curr_speed calculation. Then is set to curr_speed for next calculation
		self.SpeedN11, self.SpeedN12, self.SpeedN13, self.SpeedN14, self.SpeedN15, self.SpeedN16, self.SpeedN17, self.SpeedN18 = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0				
		self.AcclN11, self.AcclN12, self.AcclN13, self.AcclN14, self.AcclN15, self.AcclN16, self.AcclN17, self.AcclN18 = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
	#Block length connected from tkm
		self.block_length1, self.block_length2, self.block_length3, self.block_length4, self.block_length5, self.block_length6, self.block_length7, self.block_length8 = 1,1,1,1,1,1,1,1
		self.block_num1, self.block_num2, self.block_num3, self.block_num4, self.block_num5, self.block_num6, self.block_num7, self.block_num8 = 0,0,0,0,0,0,0,0
		self.block_finished1, self.block_finished2, self.block_finished3, self.block_finished4, self.block_finished5, self.block_finished6, self.block_finished7, self.block_finished8 = False,False,False,False,False,False,False,False
		self.timeBlock = 0
		self.dist_traveled1, self.dist_traveled2, self.dist_traveled3, self.dist_traveled4, self.dist_traveled5, self.dist_traveled6, self.dist_traveled7, self.dist_traveled8  = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
		signals.tkm_get_blength.connect(self.blockLen)
		signals.tkm_get_block.connect(self.blockNum)
	#brake states
		self.Brake1, self.Brake2, self.Brake3, self.Brake4, self.Brake5, self.Brake6, self.Brake7, self.Brake8  = False,False,False,False,False,False,False,False
		self.eBrake1, self.eBrake2, self.eBrake3, self.eBrake4, self.eBrake5, self.eBrake6, self.eBrake7, self.eBrake8 = False,False,False,False,False,False,False,False
		signals.tnc_emergency_brake.connect(self.SetEBrake)
		signals.tnc_service_brake.connect(self.SetServiceBrake)
	#Occupancy 
		self.pass_count1, self.pass_count2, self.pass_count3, self.pass_count4, self.pass_count5, self.pass_count6, self.pass_count7, self.pass_count8 = 0,0,0,0,0,0,0,0
		signals.tkm_get_pass_count.connect(self.SetOccupancy)
		self.crew_count = 3
	#Route Information
		self.Mass_Empty = (5*40.9)								#Tons with no passengers/crew
		self.Occupancy1, self.Occupancy2, self.Occupancy3, self.Occupancy4, self.Occupancy5, self.Occupancy6, self.Occupancy7, self.Occupancy8 = 3,3,3,3,3,3,3,3
		self.RouteName1, self.RouteName2, self.RouteName3, self.RouteName4, self.RouteName5, self.RouteName6, self.RouteName7, self.RouteName8, = " --- "," --- "," --- "," --- "," --- "," --- "," --- "," --- "
		self.TrainDirection1, self.TrainDirection2, self.TrainDirection3, self.TrainDirection4, self.TrainDirection5, self.TrainDirection6, self.TrainDirection7, self.TrainDirection8 = 1,1,1,1,1,1,1,1
		#internal direction for train on the red line
		self.TNMdirectionR1, self.TNMdirectionR2, self.TNMdirectionR3, self.TNMdirectionR4, self.TNMdirectionR5, self.TNMdirectionR6, self.TNMdirectionR7, self.TNMdirectionR8 = 1,1,1,1,1,1,1,1
		#internal direction for train on the green line
		self.TNMdirectionG1, self.TNMdirectionG2, self.TNMdirectionG3, self.TNMdirectionG4, self.TNMdirectionG5, self.TNMdirectionG6, self.TNMdirectionG7, self.TNMdirectionG8 = 1,1,1,1,1,1,1,1
		self.CurrStation1, self.CurrStation2, self.CurrStation3, self.CurrStation4, self.CurrStation5, self.CurrStation6, self.CurrStation7, self.CurrStation8 = "Yard","Yard","Yard","Yard","Yard","Yard","Yard","Yard"
		self.NextStation1, self.NextStation2, self.NextStation3, self.NextStation4, self.NextStation5, self.NextStation6, self.NextStation7, self.NextStation8 = " --- "," --- "," --- "," --- "," --- "," --- "," --- "," --- "
		self.DoorStatus1, self.DoorStatus2, self.DoorStatus3, self.DoorStatus4, self.DoorStatus5, self.DoorStatus6, self.DoorStatus7, self.DoorStatus8 = False,False,False,False,False,False,False,False
		self.LeftDoor1, self.LeftDoor2, self.LeftDoor3, self.LeftDoor4, self.LeftDoor5, self.LeftDoor6, self.LeftDoor7, self.LeftDoor8 = False,False,False,False,False,False,False,False
		self.RightDoor1, self.RightDoor2, self.RightDoor3, self.RightDoor4, self.RightDoor5, self.RightDoor6, self.RightDoor7, self.RightDoor8 = False,False,False,False,False,False,False,False
		signals.tnc_left_door.connect(self.setRightDoor)
		signals.tnc_right_door.connect(self.setLeftDoor)
	#Beacon ID connected from tkm
		self.beacon_bin1, self.beacon_bin1, self.beacon_bin1, self.beacon_bin1, self.beacon_bin1, self.beacon_bin1, self.beacon_bin1, self.beacon_bin1  = 0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000
		#self.BeaconID = 00000000								#bit1 (red vs green) bit2 (UG vs Station) bit3 (Left side (62->63) vs Right side(63->64))
		signals.tkm_get_beacon.connect(self.SetBeaconID)
		self.BeaconIDStatus = True
	#Internal control status's
		self.lights_Cab1, self.lights_Cab2, self.lights_Cab3, self.lights_Cab4, self.lights_Cab5, self.lights_Cab6, self.lights_Cab7, self.lights_Cab8 = True,True,True,True,True,True,True,True
		self.lights_High1, self.lights_High2, self.lights_High3, self.lights_High4, self.lights_High5, self.lights_High6, self.lights_High7, self.lights_High8 = False,False,False,False,False,False,False,False
		self.lights_Tun1, self.lights_Tun2, self.lights_Tun3, self.lights_Tun4, self.lights_Tun5, self.lights_Tun6, self.lights_Tun7, self.lights_Tun8  = False,False,False,False,False,False,False,False
		signals.tnc_cab_light.connect(self.setCabLight)
		signals.tnc_tunnel_light.connect(self.setTunLight)
		signals.tnc_high_beam_light.connect(self.setHighLight)
		#degrees Fahrenheit
		self.set_temp1, self.set_temp2, self.set_temp3, self.set_temp4, self.set_temp5, self.set_temp6, self.set_temp7, self.set_temp8 = 68,68,68,68,68,68,68,68
		self.curr_temp1, self.curr_temp2, self.curr_temp3, self.curr_temp4, self.curr_temp5, self.curr_temp6, self.curr_temp7, self.curr_temp8 = 68,68,68,68,68,68,68,68	
		self.announce1, self.announce2, self.announce3, self.announce4, self.announce5, self.announce6, self.announce7, self.announce8  = "Watch your step. Have a great day!","Watch your step. Have a great day!","Watch your step. Have a great day!","Watch your step. Have a great day!","Watch your step. Have a great day!","Watch your step. Have a great day!","Watch your step. Have a great day!","Watch your step. Have a great day!"
		signals.tnc_announcement.connect(self.SetAnnounce)


		#Defining Actions for specific UI Interactions
		signals.time.connect(self.SetCommSpeed)
		signals.time.connect(self.update_MoveStat)						#Update Movement Statistics
		
		signals.time.connect(self.update_TrainStat)						#Update Train Statistics
		
		signals.time.connect(self.update_RouteInfo)						#Update Route Information
		
		signals.time.connect(self.DispAnnounce)							#Display current Announcements
		
		signals.time.connect(self.getTime)
		
		if(signals.time.connect(self.GetDatetime)):							#Display running time
			self.ui.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
			self.ui.dateTimeEdit.setDisplayFormat("MM/dd/yyyy hh:mm:ss")
		
		self.ui.pushButton.clicked.connect(self.EmergencyBraking)			#Verify eBrake is pressed
		
		self.ui.lineEdit_17.editingFinished.connect(self.Temperature)		#Update Temperature interface
		
	
#_______________________________________________________________________
	#function to update Movement Statistics
	def update_MoveStat(self):
		
		#Check if current trains are still running
		signals.tkm_get_destroy.connect(self.setDestroyTrain)
		#Calculate based on current train number
		if(self.TrainNum1 == 1):
			#Address Authority Here
			signals.tnm_authority.emit(self.block_authority1,1)
			#Address Commanded Speed
			signals.tnm_comm_speed.emit(self.comm_speed1,1)
			
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed1, self.current_accl1 = set_curr_speed(self.timeSeconds, self.eBrake1, self.Brake1, self.block_authority1, self.curr_power1, self.Occupancy1, self.SpeedN11, self.AcclN11, self.comm_speed1)

			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN11 = self.curr_speed1
			self.AcclN11 = self.current_accl1
			
			#Update current speed given power value
			self.ui.lineEdit.setText(str(self.curr_speed1) + " mph")
			#Send the new calculated current speed to Train Controller
			signals.tnm_curr_speed.emit(self.curr_speed1,1)
			
			#Variable to check speed, then calculate when block changes based on speed
			curr_speed_mps = 0.0
			#calculations of current distance
			curr_speed_mps = MiletoMeter(self.curr_speed1)					#MPH to mps
			self.dist_traveled1 = (self.dist_traveled1 + curr_speed_mps*(1))		#distance in meters m/s *s = m
			#If distance > length, change blocks and emit signal
			if(curr_speed_mps > 0.0):
				if(self.dist_traveled1 >= self.block_length1):
					self.block_finished1 = True
					print(str(self.block_finished1) + " 1 change blocks")
					
					self.dist_traveled1 = 0
					if(self.RouteName1 == "Red Line"):
						signals.tnm_block_finished_red.emit(1)
					elif(self.RouteName1 == "Green Line"):
						signals.tnm_block_finished_green.emit(1)
					signals.tkm_get_blength.connect(self.blockLen)
				
			#Update brake status
			if (self.Brake1 == True or self.eBrake1 == True):
				self.ui.lineEdit_2.setText("On")
			else:
				self.ui.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		elif(self.TrainNum2 == 1):
			#Address Authority Here
			signals.tnm_authority.emit(self.block_authority2,2)
			#Address Commanded Speed
			signals.tnm_comm_speed.emit(self.comm_speed2,2)
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed2, self.current_accl2 = set_curr_speed(self.timeSeconds, self.eBrake2, self.Brake2, self.block_authority2, self.curr_power2, self.Occupancy2, self.SpeedN12, self.AcclN12, self.comm_speed2)

			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN12 = self.curr_speed2
			self.AcclN12 = self.current_accl2
			
			#Update current speed given power value
			self.ui.lineEdit.setText(str(self.curr_speed2) + " mph")
			#Send the new calculated current speed to Train Controller
			signals.tnm_curr_speed.emit(self.curr_speed2,2)
			
			#Variable to check speed, then calculate when block changes based on speed
			curr_speed_mps = 0.0
			#calculations of current distance
			curr_speed_mps = MiletoMeter(self.curr_speed2)					#MPH to mps
			self.dist_traveled2 = (self.dist_traveled2 + curr_speed_mps*(1))		#distance in meters m/s *s = m
			#If distance > length, change blocks and emit signal
			if(curr_speed_mps > 0.0):
				if(self.dist_traveled2 >= self.block_length2):
					self.block_finished2 = True
					print(str(self.block_finished2) + " 2 change blocks")
					
					self.dist_traveled2 = 0
					if(self.RouteName2 == "Red Line"):
						signals.tnm_block_finished_red.emit(2)
					elif(self.RouteName2 == "Green Line"):
						signals.tnm_block_finished_green.emit(2)
					signals.tkm_get_blength.connect(self.blockLen)
				
			#Update brake status
			if (self.Brake2 == True or self.eBrake2 == True):
				self.ui.lineEdit_2.setText("On")
			else:
				self.ui.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		elif(self.TrainNum3 == 1):
			#Address Authority Here
			signals.tnm_authority.emit(self.block_authority3,3)
			#Address Commanded Speed
			signals.tnm_comm_speed.emit(self.comm_speed3,3)
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed3, self.current_accl3 = set_curr_speed(self.timeSeconds, self.eBrake3, self.Brake3, self.block_authority3, self.curr_power3, self.Occupancy3, self.SpeedN13, self.AcclN13, self.comm_speed3)

			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN13 = self.curr_speed3
			self.AcclN13 = self.current_accl3
			
			#Update current speed given power value
			self.ui.lineEdit.setText(str(self.curr_speed3) + " mph")
			#Send the new calculated current speed to Train Controller
			signals.tnm_curr_speed.emit(self.curr_speed3,3)
			
			#Variable to check speed, then calculate when block changes based on speed
			curr_speed_mps = 0.0
			#calculations of current distance
			curr_speed_mps = MiletoMeter(self.curr_speed3)					#MPH to mps
			self.dist_traveled3 = (self.dist_traveled3 + curr_speed_mps*(1))		#distance in meters m/s *s = m
			#If distance > length, change blocks and emit signal
			if(curr_speed_mps > 0.0):
				if(self.dist_traveled3 >= self.block_length3):
					self.block_finished3 = True
					print(str(self.block_finished3) + " 3 change blocks")
					
					self.dist_traveled3 = 0
					if(self.RouteName3 == "Red Line"):
						signals.tnm_block_finished_red.emit(3)
					elif(self.RouteName3 == "Green Line"):
						signals.tnm_block_finished_green.emit(3)
					signals.tkm_get_blength.connect(self.blockLen)
				
			#Update brake status
			if (self.Brake3 == True or self.eBrake3 == True):
				self.ui.lineEdit_2.setText("On")
			else:
				self.ui.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		elif(self.TrainNum4 == 1):
			#Address Authority Here
			signals.tnm_authority.emit(self.block_authority4,4)
			#Address Commanded Speed
			signals.tnm_comm_speed.emit(self.comm_speed4,4)
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed4, self.current_accl4 = set_curr_speed(self.timeSeconds, self.eBrake4, self.Brake4, self.block_authority4, self.curr_power4, self.Occupancy4, self.SpeedN14, self.AcclN14, self.comm_speed4)

			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN14 = self.curr_speed4
			self.AcclN14 = self.current_accl4
			
			#Update current speed given power value
			self.ui.lineEdit.setText(str(self.curr_speed4) + " mph")
			#Send the new calculated current speed to Train Controller
			signals.tnm_curr_speed.emit(self.curr_speed4,4)
			
			#Variable to check speed, then calculate when block changes based on speed
			curr_speed_mps = 0.0
			#calculations of current distance
			curr_speed_mps = MiletoMeter(self.curr_speed4)					#MPH to mps
			self.dist_traveled4 = (self.dist_traveled4 + curr_speed_mps*(1))		#distance in meters m/s *s = m
			#If distance > length, change blocks and emit signal
			if(curr_speed_mps > 0.0):
				if(self.dist_traveled4 >= self.block_length4):
					self.block_finished4 = True
					print(str(self.block_finished4) + " 4 change blocks")
					
					self.dist_traveled4 = 0
					if(self.RouteName4 == "Red Line"):
						signals.tnm_block_finished_red.emit(4)
					elif(self.RouteName4 == "Green Line"):
						signals.tnm_block_finished_green.emit(4)
					signals.tkm_get_blength.connect(self.blockLen)
				
			#Update brake status
			if (self.Brake4 == True or self.eBrake4 == True):
				self.ui.lineEdit_2.setText("On")
			else:
				self.ui.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		elif(self.TrainNum5 == 1):
			#Address Authority Here
			signals.tnm_authority.emit(self.block_authority5,5)
			#Address Commanded Speed
			signals.tnm_comm_speed.emit(self.comm_speed5,5)
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed5, self.current_accl5 = set_curr_speed(self.timeSeconds, self.eBrake5, self.Brake5, self.block_authority5, self.curr_power5, self.Occupancy5, self.SpeedN15, self.AcclN15, self.comm_speed5)

			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN15 = self.curr_speed5
			self.AcclN15 = self.current_accl5
			
			#Update current speed given power value
			self.ui.lineEdit.setText(str(self.curr_speed5) + " mph")
			#Send the new calculated current speed to Train Controller
			signals.tnm_curr_speed.emit(self.curr_speed5,5)
			
			#Variable to check speed, then calculate when block changes based on speed
			curr_speed_mps = 0.0
			#calculations of current distance
			curr_speed_mps = MiletoMeter(self.curr_speed5)					#MPH to mps
			self.dist_traveled5 = (self.dist_traveled5 + curr_speed_mps*(1))		#distance in meters m/s *s = m
			#If distance > length, change blocks and emit signal
			if(curr_speed_mps > 0.0):
				if(self.dist_traveled5 >= self.block_length5):
					self.block_finished5 = True
					print(str(self.block_finished5) + " 5 change blocks")
					
					self.dist_traveled5 = 0
					if(self.RouteName5 == "Red Line"):
						signals.tnm_block_finished_red.emit(5)
					elif(self.RouteName5 == "Green Line"):
						signals.tnm_block_finished_green.emit(5)
					signals.tkm_get_blength.connect(self.blockLen)
				
			#Update brake status
			if (self.Brake5 == True or self.eBrake5 == True):
				self.ui.lineEdit_2.setText("On")
			else:
				self.ui.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		elif(self.TrainNum6 == 1):
			#Address Authority Here
			signals.tnm_authority.emit(self.block_authority6,6)
			#Address Commanded Speed
			signals.tnm_comm_speed.emit(self.comm_speed6,6)
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed6, self.current_accl6 = set_curr_speed(self.timeSeconds, self.eBrake6, self.Brake6, self.block_authority6, self.curr_power6, self.Occupancy6, self.SpeedN16, self.AcclN16, self.comm_speed6)

			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN16 = self.curr_speed6
			self.AcclN16 = self.current_accl6
			
			#Update current speed given power value
			self.ui.lineEdit.setText(str(self.curr_speed6) + " mph")
			#Send the new calculated current speed to Train Controller
			signals.tnm_curr_speed.emit(self.curr_speed6,6)
			
			#Variable to check speed, then calculate when block changes based on speed
			curr_speed_mps = 0.0
			#calculations of current distance
			curr_speed_mps = MiletoMeter(self.curr_speed6)					#MPH to mps
			self.dist_traveled6 = (self.dist_traveled6 + curr_speed_mps*(1))		#distance in meters m/s *s = m
			#If distance > length, change blocks and emit signal
			if(curr_speed_mps > 0.0):
				if(self.dist_traveled6 >= self.block_length6):
					self.block_finished6 = True
					print(str(self.block_finished6) + " 6 change blocks")
					
					self.dist_traveled6 = 0
					if(self.RouteName6 == "Red Line"):
						signals.tnm_block_finished_red.emit(6)
					elif(self.RouteName6 == "Green Line"):
						signals.tnm_block_finished_green.emit(6)
					signals.tkm_get_blength.connect(self.blockLen)
				
			#Update brake status
			if (self.Brake6 == True or self.eBrake6 == True):
				self.ui.lineEdit_2.setText("On")
			else:
				self.ui.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		elif(self.TrainNum7 == 1):
			#Address Authority Here
			signals.tnm_authority.emit(self.block_authority7,7)
			#Address Commanded Speed
			signals.tnm_comm_speed.emit(self.comm_speed7,7)
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed7, self.current_accl7 = set_curr_speed(self.timeSeconds, self.eBrake7, self.Brake7, self.block_authority7, self.curr_power7, self.Occupancy7, self.SpeedN17, self.AcclN17, self.comm_speed7)

			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN17 = self.curr_speed7
			self.AcclN17 = self.current_accl17
						
			#Update current speed given power value
			self.ui.lineEdit.setText(str(self.curr_speed7) + " mph")
			#Send the new calculated current speed to Train Controller
			signals.tnm_curr_speed.emit(self.curr_speed7,7)
			
			#Variable to check speed, then calculate when block changes based on speed
			curr_speed_mps = 0.0
			#calculations of current distance
			curr_speed_mps = MiletoMeter(self.curr_speed7)					#MPH to mps
			self.dist_traveled7 = (self.dist_traveled7 + curr_speed_mps*(1))		#distance in meters m/s *s = m
			#If distance > length, change blocks and emit signal
			if(curr_speed_mps > 0.0):
				if(self.dist_traveled7 >= self.block_length7):
					self.block_finished7 = True
					print(str(self.block_finished7) + " 7 change blocks")
					
					self.dist_traveled7 = 0
					if(self.RouteName7 == "Red Line"):
						signals.tnm_block_finished_red.emit(7)
					elif(self.RouteName7 == "Green Line"):
						signals.tnm_block_finished_green.emit(7)
					signals.tkm_get_blength.connect(self.blockLen)
				
			#Update brake status
			if (self.Brake7 == True or self.eBrake7 == True):
				self.ui.lineEdit_2.setText("On")
			else:
				self.ui.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		elif(self.TrainNum8 == 1):
			#Address Authority Here
			signals.tnm_authority.emit(self.block_authority8,8)
			#Address Commanded Speed
			signals.tnm_comm_speed.emit(self.comm_speed8,8)
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed8, self.current_accl8 = set_curr_speed(self.timeSeconds, self.eBrake8, self.Brake8, self.block_authority8, self.curr_power8, self.Occupancy8, self.SpeedN18, self.AcclN18, self.comm_speed8)

			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN18 = self.curr_speed8
			self.AcclN18 = self.current_accl8
			
			#Update current speed given power value
			self.ui.lineEdit.setText(str(self.curr_speed8) + " mph")
			#Send the new calculated current speed to Train Controller
			signals.tnm_curr_speed.emit(self.curr_speed8,8)
			
			#Variable to check speed, then calculate when block changes based on speed
			curr_speed_mps = 0.0
			#calculations of current distance
			curr_speed_mps = MiletoMeter(self.curr_speed8)					#MPH to mps
			self.dist_traveled8 = (self.dist_traveled8 + curr_speed_mps*(1))		#distance in meters m/s *s = m
			#If distance > length, change blocks and emit signal
			if(curr_speed_mps > 0.0):
				if(self.dist_traveled8 >= self.block_length8):
					self.block_finished8 = True
					print(str(self.block_finished8) + " 8 change blocks")
					
					self.dist_traveled8 = 0
					if(self.RouteName8 == "Red Line"):
						signals.tnm_block_finished_red.emit(8)
					elif(self.RouteName8 == "Green Line"):
						signals.tnm_block_finished_green.emit(8)
					signals.tkm_get_blength.connect(self.blockLen)
				
			#Update brake status
			if (self.Brake8 == True or self.eBrake8 == True):
				self.ui.lineEdit_2.setText("On")
			else:
				self.ui.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		
		
		#Don't allow changes to lineEdits
		self.ui.lineEdit.setReadOnly(True)
		self.ui.lineEdit_2.setReadOnly(True)
		self.ui.lineEdit_3.setReadOnly(True)
		self.ui.lineEdit_4.setReadOnly(True)
		self.ui.lineEdit_5.setReadOnly(True)
		
#_______________________________________________________________________	
	#function to update Train Statistics (Mass, Pass & Crew count)
	def update_TrainStat(self):
		#Check which train to update
		if(self.TrainNum1 == 1):
			#Update pass_count
			self.ui.lineEdit_6.setText(str(self.pass_count1))
			#Update crew_count
			self.ui.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy1 = pass_crew_count(self.pass_count1, self.crew_count)
			self.total_mass = ((self.Occupancy1*56.699)/2000) + self.Mass_Empty
			self.ui.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		elif(self.TrainNum2 == 1):
			#Update pass_count
			self.ui.lineEdit_6.setText(str(self.pass_count2))
			#Update crew_count
			self.ui.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy2 = pass_crew_count(self.pass_count2, self.crew_count)
			self.total_mass = ((self.Occupancy2*56.699)/2000) + self.Mass_Empty
			self.ui.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		elif(self.TrainNum3 == 1):
			#Update pass_count
			self.ui.lineEdit_6.setText(str(self.pass_count3))
			#Update crew_count
			self.ui.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy3 = pass_crew_count(self.pass_count3, self.crew_count)
			self.total_mass = ((self.Occupancy3*56.699)/2000) + self.Mass_Empty
			self.ui.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		elif(self.TrainNum4 == 1):
			#Update pass_count
			self.ui.lineEdit_6.setText(str(self.pass_count4))
			#Update crew_count
			self.ui.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy4 = pass_crew_count(self.pass_count4, self.crew_count)
			self.total_mass = ((self.Occupancy4*56.699)/2000) + self.Mass_Empty
			self.ui.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		elif(self.TrainNum5 == 1):
			#Update pass_count
			self.ui.lineEdit_6.setText(str(self.pass_count5))
			#Update crew_count
			self.ui.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy5 = pass_crew_count(self.pass_count5, self.crew_count)
			self.total_mass = ((self.Occupancy5*56.699)/2000) + self.Mass_Empty
			self.ui.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		elif(self.TrainNum6 == 1):
			#Update pass_count
			self.ui.lineEdit_6.setText(str(self.pass_count6))
			#Update crew_count
			self.ui.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy6 = pass_crew_count(self.pass_count6, self.crew_count)
			self.total_mass = ((self.Occupancy6*56.699)/2000) + self.Mass_Empty
			self.ui.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		elif(self.TrainNum7 == 1):
			#Update pass_count
			self.ui.lineEdit_6.setText(str(self.pass_count7))
			#Update crew_count
			self.ui.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy7 = pass_crew_count(self.pass_count7, self.crew_count)
			self.total_mass = ((self.Occupancy7*56.699)/2000) + self.Mass_Empty
			self.ui.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		elif(self.TrainNum8 == 1):
			#Update pass_count
			self.ui.lineEdit_6.setText(str(self.pass_count8))
			#Update crew_count
			self.ui.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy8 = pass_crew_count(self.pass_count8, self.crew_count)
			self.total_mass = ((self.Occupancy8*56.699)/2000) + self.Mass_Empty
			self.ui.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		
		
		#Don't allow changes to lineEdits
		self.ui.lineEdit_6.setReadOnly(True)
		self.ui.lineEdit_7.setReadOnly(True)
		self.ui.lineEdit_8.setReadOnly(True)
		
#_______________________________________________________________________
	#function to update Route Information and Train Internal Controls
	def update_RouteInfo(self):
		#Update Route Information based on Train Number
		if(self.TrainNum1 == 1):
			#Update Train Numbering Header
			self.ui.label_23.setText(self.TrainName1)
			#Update Route Line
			self.ui.lineEdit_9.setText(self.RouteName1)
			#Update Current and Next Station based on Line and direction
			self.ui.lineEdit_19.setText(self.CurrStation1)
			self.ui.lineEdit_10.setText(self.NextStation1)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor1 == True or self.RightDoor1 == True):
				self.DoorStatus1 = True
			if (self.DoorStatus1 == False):
				self.ui.lineEdit_11.setText("Closed")
				self.Brake1 = False
			elif(self.DoorStatus1 == True):
				self.ui.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(1)
				self.Brake1 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui.lineEdit_12.setText("Waiting")
			else:
				self.ui.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin1,1)
			
			#update Cabin Lights status
			if (self.lights_Cab1 == False):
				self.ui.lineEdit_13.setText("Off")
			else:
				self.ui.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High1 == False):
				self.ui.lineEdit_14.setText("Off")
			else:
				self.ui.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun1 == False):
				self.ui.lineEdit_15.setText("Off")
			else:
				self.ui.lineEdit_15.setText("On")
			#____________________________________________________________________
		elif(self.TrainNum2 == 1):
			#Update Train Numbering Header
			self.ui.label_23.setText(self.TrainName2)
			#Update Route Line
			self.ui.lineEdit_9.setText(self.RouteName2)
			#Update Current and Next Station based on Line and direction
			self.ui.lineEdit_19.setText(self.CurrStation2)
			self.ui.lineEdit_10.setText(self.NextStation2)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor2 == True or self.RightDoor2 == True):
				self.DoorStatus2 = True
			if (self.DoorStatus2 == False):
				self.ui.lineEdit_11.setText("Closed")
				self.Brake2 = False
			elif(self.DoorStatus2 == True):
				self.ui.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(2)
				self.Brake2 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui.lineEdit_12.setText("Waiting")
			else:
				self.ui.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin2,2)
			
			#update Cabin Lights status
			if (self.lights_Cab2 == False):
				self.ui.lineEdit_13.setText("Off")
			else:
				self.ui.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High2 == False):
				self.ui.lineEdit_14.setText("Off")
			else:
				self.ui.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun2 == False):
				self.ui.lineEdit_15.setText("Off")
			else:
				self.ui.lineEdit_15.setText("On")
			#____________________________________________________________________
		elif(self.TrainNum3 == 1):
			#Update Train Numbering Header
			self.ui.label_23.setText(self.TrainName3)
			#Update Route Line
			self.ui.lineEdit_9.setText(self.RouteName3)
			#Update Current and Next Station based on Line and direction
			self.ui.lineEdit_19.setText(self.CurrStation3)
			self.ui.lineEdit_10.setText(self.NextStation3)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor3 == True or self.RightDoor3 == True):
				self.DoorStatus3 = True
			if (self.DoorStatus3 == False):
				self.ui.lineEdit_11.setText("Closed")
				self.Brake3 = False
			elif(self.DoorStatus3 == True):
				self.ui.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(3)
				self.Brake3 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui.lineEdit_12.setText("Waiting")
			else:
				self.ui.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin3,3)
			
			#update Cabin Lights status
			if (self.lights_Cab3 == False):
				self.ui.lineEdit_13.setText("Off")
			else:
				self.ui.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High3 == False):
				self.ui.lineEdit_14.setText("Off")
			else:
				self.ui.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun3 == False):
				self.ui.lineEdit_15.setText("Off")
			else:
				self.ui.lineEdit_15.setText("On")
			#____________________________________________________________________
		elif(self.TrainNum4 == 1):
			#Update Train Numbering Header
			self.ui.label_23.setText(self.TrainName4)
			#Update Route Line
			self.ui.lineEdit_9.setText(self.RouteName4)
			#Update Current and Next Station based on Line and direction
			self.ui.lineEdit_19.setText(self.CurrStation4)
			self.ui.lineEdit_10.setText(self.NextStation4)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor4 == True or self.RightDoor4 == True):
				self.DoorStatus4 = True
			if (self.DoorStatus4 == False):
				self.ui.lineEdit_11.setText("Closed")
				self.Brake4 = False
			elif(self.DoorStatus4 == True):
				self.ui.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(4)
				self.Brake4 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui.lineEdit_12.setText("Waiting")
			else:
				self.ui.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin4,4)
			
			#update Cabin Lights status
			if (self.lights_Cab4 == False):
				self.ui.lineEdit_13.setText("Off")
			else:
				self.ui.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High4 == False):
				self.ui.lineEdit_14.setText("Off")
			else:
				self.ui.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun4 == False):
				self.ui.lineEdit_15.setText("Off")
			else:
				self.ui.lineEdit_15.setText("On")
			#____________________________________________________________________
		elif(self.TrainNum5 == 1):
			#Update Train Numbering Header
			self.ui.label_23.setText(self.TrainName5)
			#Update Route Line
			self.ui.lineEdit_9.setText(self.RouteName5)
			#Update Current and Next Station based on Line and direction
			self.ui.lineEdit_19.setText(self.CurrStation5)
			self.ui.lineEdit_10.setText(self.NextStation5)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor5 == True or self.RightDoor5 == True):
				self.DoorStatus5 = True
			if (self.DoorStatus5 == False):
				self.ui.lineEdit_11.setText("Closed")
				self.Brake5 = False
			elif(self.DoorStatus5 == True):
				self.ui.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(5)
				self.Brake5 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui.lineEdit_12.setText("Waiting")
			else:
				self.ui.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin5,5)
			
			#update Cabin Lights status
			if (self.lights_Cab5 == False):
				self.ui.lineEdit_13.setText("Off")
			else:
				self.ui.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High5 == False):
				self.ui.lineEdit_14.setText("Off")
			else:
				self.ui.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun5 == False):
				self.ui.lineEdit_15.setText("Off")
			else:
				self.ui.lineEdit_15.setText("On")
			#____________________________________________________________________
		elif(self.TrainNum6 == 1):
			#Update Train Numbering Header
			self.ui.label_23.setText(self.TrainName6)
			#Update Route Line
			self.ui.lineEdit_9.setText(self.RouteName6)
			#Update Current and Next Station based on Line and direction
			self.ui.lineEdit_19.setText(self.CurrStation6)
			self.ui.lineEdit_10.setText(self.NextStation6)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor6 == True or self.RightDoor6 == True):
				self.DoorStatus6 = True
			if (self.DoorStatus6 == False):
				self.ui.lineEdit_11.setText("Closed")
				self.Brake6 = False
			elif(self.DoorStatus6 == True):
				self.ui.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(6)
				self.Brake6 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui.lineEdit_12.setText("Waiting")
			else:
				self.ui.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin6,6)
			
			#update Cabin Lights status
			if (self.lights_Cab6 == False):
				self.ui.lineEdit_13.setText("Off")
			else:
				self.ui.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High6 == False):
				self.ui.lineEdit_14.setText("Off")
			else:
				self.ui.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun6 == False):
				self.ui.lineEdit_15.setText("Off")
			else:
				self.ui.lineEdit_15.setText("On")
			#____________________________________________________________________
		elif(self.TrainNum7 == 1):
			#Update Train Numbering Header
			self.ui.label_23.setText(self.TrainName7)
			#Update Route Line
			self.ui.lineEdit_9.setText(self.RouteName7)
			#Update Current and Next Station based on Line and direction
			self.ui.lineEdit_19.setText(self.CurrStation7)
			self.ui.lineEdit_10.setText(self.NextStation7)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor7 == True or self.RightDoor7 == True):
				self.DoorStatus7 = True
			if (self.DoorStatus7 == False):
				self.ui.lineEdit_11.setText("Closed")
				self.Brake7 = False
			elif(self.DoorStatus7 == True):
				self.ui.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(7)
				self.Brake7 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui.lineEdit_12.setText("Waiting")
			else:
				self.ui.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin7,7)
			
			#update Cabin Lights status
			if (self.lights_Cab7 == False):
				self.ui.lineEdit_13.setText("Off")
			else:
				self.ui.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High7 == False):
				self.ui.lineEdit_14.setText("Off")
			else:
				self.ui.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun7 == False):
				self.ui.lineEdit_15.setText("Off")
			else:
				self.ui.lineEdit_15.setText("On")
			#____________________________________________________________________
		elif(self.TrainNum8 == 1):
			#Update Train Numbering Header
			self.ui.label_23.setText(self.TrainName8)
			#Update Route Line
			self.ui.lineEdit_9.setText(self.RouteName8)
			#Update Current and Next Station based on Line and direction
			self.ui.lineEdit_19.setText(self.CurrStation8)
			self.ui.lineEdit_10.setText(self.NextStation8)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor8 == True or self.RightDoor8 == True):
				self.DoorStatus8 = True
			if (self.DoorStatus8 == False):
				self.ui.lineEdit_11.setText("Closed")
				self.Brake8 = False
			elif(self.DoorStatus8 == True):
				self.ui.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(8)
				self.Brake8 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui.lineEdit_12.setText("Waiting")
			else:
				self.ui.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin8,8)
			
			#update Cabin Lights status
			if (self.lights_Cab8 == False):
				self.ui.lineEdit_13.setText("Off")
			else:
				self.ui.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High8 == False):
				self.ui.lineEdit_14.setText("Off")
			else:
				self.ui.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun8 == False):
				self.ui.lineEdit_15.setText("Off")
			else:
				self.ui.lineEdit_15.setText("On")
			#____________________________________________________________________
		
		#Don't allow changes to lineEdits
		self.ui.lineEdit_9.setReadOnly(True)
		self.ui.lineEdit_10.setReadOnly(True)
		self.ui.lineEdit_11.setReadOnly(True)
		self.ui.lineEdit_12.setReadOnly(True)
		self.ui.lineEdit_13.setReadOnly(True)
		self.ui.lineEdit_14.setReadOnly(True)
		self.ui.lineEdit_15.setReadOnly(True)
			
#_______________________________________________________________________			
	#function to delegate variables when Emergency Brake triggered
	def EmergencyBraking(self):
		if(self.TrainNum1 == 1):
			if not self.eBrake1:
				self.ui.pushButton.setText("CANCEL")
				self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake1 = True
				signals.tnm_ebrake.emit(self.eBrake1,1)
				print("eBrake is " + str(self.eBrake1))
			else:
				self.ui.pushButton.setText("Emergency Brake")
				self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake1 = False
				signals.tnm_ebrake.emit(self.eBrake1,1)
		#______________________________________
		elif(self.TrainNum2 == 1):
			if not self.eBrake2:
				self.ui.pushButton.setText("CANCEL")
				self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake2 = True
				signals.tnm_ebrake.emit(self.eBrake2,2)
				print("eBrake is " + str(self.eBrake2))
			else:
				self.ui.pushButton.setText("Emergency Brake")
				self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake2 = False
				signals.tnm_ebrake.emit(self.eBrake2,2)
		#______________________________________
		elif(self.TrainNum3 == 1):
			if not self.eBrake3:
				self.ui.pushButton.setText("CANCEL")
				self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake3 = True
				signals.tnm_ebrake.emit(self.eBrake3,3)
				print("eBrake is " + str(self.eBrake3))
			else:
				self.ui.pushButton.setText("Emergency Brake")
				self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake3 = False
				signals.tnm_ebrake.emit(self.eBrake3,3)
		#______________________________________
		elif(self.TrainNum4 == 1):
			if not self.eBrake4:
				self.ui.pushButton.setText("CANCEL")
				self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake4 = True
				signals.tnm_ebrake.emit(self.eBrake4,4)
				print("eBrake is " + str(self.eBrake4))
			else:
				self.ui.pushButton.setText("Emergency Brake")
				self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake4 = False
				signals.tnm_ebrake.emit(self.eBrake4,4)
		#______________________________________
		elif(self.TrainNum5 == 1):
			if not self.eBrake5:
				self.ui.pushButton.setText("CANCEL")
				self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake5 = True
				signals.tnm_ebrake.emit(self.eBrake5,5)
				print("eBrake is " + str(self.eBrake5))
			else:
				self.ui.pushButton.setText("Emergency Brake")
				self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake5 = False
				signals.tnm_ebrake.emit(self.eBrake5,5)
		#______________________________________
		elif(self.TrainNum6 == 1):
			if not self.eBrake6:
				self.ui.pushButton.setText("CANCEL")
				self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake6 = True
				signals.tnm_ebrake.emit(self.eBrake6,6)
				print("eBrake is " + str(self.eBrake6))
			else:
				self.ui.pushButton.setText("Emergency Brake")
				self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake6 = False
				signals.tnm_ebrake.emit(self.eBrake6,6)
		#______________________________________
		elif(self.TrainNum7 == 1):
			if not self.eBrake7:
				self.ui.pushButton.setText("CANCEL")
				self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake7 = True
				signals.tnm_ebrake.emit(self.eBrake7,7)
				print("eBrake is " + str(self.eBrake7))
			else:
				self.ui.pushButton.setText("Emergency Brake")
				self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake7 = False
				signals.tnm_ebrake.emit(self.eBrake7,7)
		#______________________________________
		elif(self.TrainNum8 == 1):
			if not self.eBrake8:
				self.ui.pushButton.setText("CANCEL")
				self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake8 = True
				signals.tnm_ebrake.emit(self.eBrake8,8)
				print("eBrake is " + str(self.eBrake8))
			else:
				self.ui.pushButton.setText("Emergency Brake")
				self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake8 = False
				signals.tnm_ebrake.emit(self.eBrake8,8)
		#_____________________________________
		
#_______________________________________________________________________
	#function to Update Current Temperature of the cabin
	def Temperature(self):
		#Update Temperature based on Train Number
		if(self.TrainNum1 == 1):
			AlphaFlag1 = False
			#Error checking to make sure input is only an INT
			for i in self.ui.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag1 = True
			if(AlphaFlag1 == True):
				self.ui.lineEdit_17.setText(str(self.curr_temp1))
				self.set_temp1 = self.curr_temp1
			elif(self.ui.lineEdit_17.text().isdigit() == True):
				AlphaFlag1 = False
				self.set_temp1 = int(self.ui.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui.lineEdit_16.setText(str(temp_control(self.set_temp1, self.curr_temp1)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp1)
			#_______________________________________________________________
		elif(self.TrainNum2 == 1):
			AlphaFlag2 = False
			#Error checking to make sure input is only an INT
			for i in self.ui.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag2 = True
			if(AlphaFlag2 == True):
				self.ui.lineEdit_17.setText(str(self.curr_temp2))
				self.set_temp2 = self.curr_temp2
			elif(self.ui.lineEdit_17.text().isdigit() == True):
				AlphaFlag2 = False
				self.set_temp2 = int(self.ui.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui.lineEdit_16.setText(str(temp_control(self.set_temp2, self.curr_temp2)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp2)
			#_______________________________________________________________
		elif(self.TrainNum3 == 1):
			AlphaFlag3 = False
			#Error checking to make sure input is only an INT
			for i in self.ui.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag3 = True
			if(AlphaFlag3 == True):
				self.ui.lineEdit_17.setText(str(self.curr_temp3))
				self.set_temp3 = self.curr_temp3
			elif(self.ui.lineEdit_17.text().isdigit() == True):
				AlphaFlag3 = False
				self.set_temp3 = int(self.ui.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui.lineEdit_16.setText(str(temp_control(self.set_temp3, self.curr_temp3)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp3)
			#_______________________________________________________________
		elif(self.TrainNum4 == 1):
			AlphaFlag4 = False
			#Error checking to make sure input is only an INT
			for i in self.ui.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag4 = True
			if(AlphaFlag4 == True):
				self.ui.lineEdit_17.setText(str(self.curr_temp4))
				self.set_temp4 = self.curr_temp4
			elif(self.ui.lineEdit_17.text().isdigit() == True):
				AlphaFlag4 = False
				self.set_temp4 = int(self.ui.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui.lineEdit_16.setText(str(temp_control(self.set_temp4, self.curr_temp4)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp4)
			#_______________________________________________________________
		elif(self.TrainNum5 == 1):
			AlphaFlag5 = False
			#Error checking to make sure input is only an INT
			for i in self.ui.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag5 = True
			if(AlphaFlag5 == True):
				self.ui.lineEdit_17.setText(str(self.curr_temp5))
				self.set_temp5 = self.curr_temp5
			elif(self.ui.lineEdit_17.text().isdigit() == True):
				AlphaFlag5 = False
				self.set_temp5 = int(self.ui.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui.lineEdit_16.setText(str(temp_control(self.set_temp5, self.curr_temp5)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp5)
			#_______________________________________________________________
		elif(self.TrainNum6 == 1):
			AlphaFlag6 = False
			#Error checking to make sure input is only an INT
			for i in self.ui.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag6 = True
			if(AlphaFlag6 == True):
				self.ui.lineEdit_17.setText(str(self.curr_temp6))
				self.set_temp6 = self.curr_temp6
			elif(self.ui.lineEdit_17.text().isdigit() == True):
				AlphaFlag6 = False
				self.set_temp6 = int(self.ui.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui.lineEdit_16.setText(str(temp_control(self.set_temp6, self.curr_temp6)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp6)
			#_______________________________________________________________
		elif(self.TrainNum7 == 1):
			AlphaFlag7 = False
			#Error checking to make sure input is only an INT
			for i in self.ui.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag7 = True
			if(AlphaFlag7 == True):
				self.ui.lineEdit_17.setText(str(self.curr_temp7))
				self.set_temp7 = self.curr_temp7
			elif(self.ui.lineEdit_17.text().isdigit() == True):
				AlphaFlag7 = False
				self.set_temp7 = int(self.ui.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui.lineEdit_16.setText(str(temp_control(self.set_temp7, self.curr_temp7)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp7)
			#_______________________________________________________________
		elif(self.TrainNum8 == 1):
			AlphaFlag8 = False
			#Error checking to make sure input is only an INT
			for i in self.ui.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag8 = True
			if(AlphaFlag8 == True):
				self.ui.lineEdit_17.setText(str(self.curr_temp8))
				self.set_temp8 = self.curr_temp8
			elif(self.ui.lineEdit_17.text().isdigit() == True):
				AlphaFlag8 = False
				self.set_temp8 = int(self.ui.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui.lineEdit_16.setText(str(temp_control(self.set_temp8, self.curr_temp8)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp8)
			#_______________________________________________________________
		
		#Don't allow time module to be edited
		self.ui.lineEdit_16.setReadOnly(True)
	
	#function for updating the current date and time widget
	def GetDatetime(self):
		dateTime = self.ui.dateTimeEdit.dateTime()
		dateTime_string = dateTime.toString(self.ui.dateTimeEdit.displayFormat())
		self.ui.dateTimeEdit.dateTimeFromText(dateTime_string)
		
		#Don't allow time module to be edited
		self.ui.dateTimeEdit.setReadOnly(True)

	#function for updating the internal train announcements
	def DispAnnounce(self):
		if(self.TrainNum1 == 1):
			self.ui.lineEdit_18.setText(self.announce1)
		elif(self.TrainNum2 == 1):
			self.ui.lineEdit_18.setText(self.announce2)
		elif(self.TrainNum3 == 1):
			self.ui.lineEdit_18.setText(self.announce3)
		elif(self.TrainNum4 == 1):
			self.ui.lineEdit_18.setText(self.announce4)
		elif(self.TrainNum5 == 1):
			self.ui.lineEdit_18.setText(self.announce5)
		elif(self.TrainNum6 == 1):
			self.ui.lineEdit_18.setText(self.announce6)
		elif(self.TrainNum7 == 1):
			self.ui.lineEdit_18.setText(self.announce7)
		elif(self.TrainNum8 == 1):
			self.ui.lineEdit_18.setText(self.announce8)
	
		#Don't allow announcements text to be edited
		self.ui.lineEdit_18.setReadOnly(True)
		
#_______________________________________________________________________
	#Function to set power from tnc signal
	def SetPower(self,tnc_power):
		if(self.TrainNum1 == 1):
			self.curr_power1 = tnc_power
		elif(self.TrainNum2 == 1):
			self.curr_power2 = tnc_power
		elif(self.TrainNum3 == 1):
			self.curr_power3 = tnc_power
		elif(self.TrainNum4 == 1):
			self.curr_power4 = tnc_power
		elif(self.TrainNum5 == 1):
			self.curr_power5 = tnc_power
		elif(self.TrainNum6 == 1):
			self.curr_power6 = tnc_power
		elif(self.TrainNum7 == 1):
			self.curr_power7 = tnc_power
		elif(self.TrainNum8 == 1):
			self.curr_power8 = tnc_power
	
	#Function to set Beacon ID from track model signal
	def SetBeaconID(self,tkm_beacon):
		#beacon ID int set, then sent to Train Controller
		self.BeaconId = tkm_beacon
		#Check beacon ID based on Train Number For Green Line
		if(self.TrainNum1 == 1):
			#Call function to append beacon
			self.beacon_bin1 = AppendBeacon(self.BeaconId)
		
			#check if first value is: 1 = green line/0 = red line #Was 2, 3, 4, 5:
			if(self.beacon_bin1[0] == 0):
				self.RouteName1 = "Red Line"
				self.CurrStation1 = "Yard"
				self.NextStation1 = "Shady Side"
			elif(self.beacon_bin1[0] == 1):
				self.RouteName1 = "Green Line"
				self.CurrStation1 = "Yard"
				self.NextStation1 = "Glenbury"
			#check if second value is: 0 = station/1 = underground
			if(self.beacon_bin1[1] == 0):
				self.lights_Tun1 == False
			elif(self.beacon_bin1[1] == 1):
				self.lights_Tun1 == True
			#3rd bit - 0 Left(decrement)/1 Right(increment) directionality
			#0 means left doors open, 1 means right doors open
			if(self.beacon_bin1[2] == 0):
				self.TrainDirection1 = 0
				self.tnm_TrainDir.emit(self.TrainDirection1,1)
			elif(self.beacon_bin1[2] == 1):
				self.TrainDirection1 = 1
				self.tnm_TrainDir.emit(self.TrainDirection1,1)
				
			#Call Beacon function to specify station
			if(self.RouteName1 == "Green Line"):
				self.CurrStation1, self.NextStation1, self.TNMdirectionG1 = GreenBeacon(self.RouteName1, self.TNMdirectionG1, self.TrainDirection1, self.beacon_bin1)
			elif(self.RouteName1 == "Red Line"):
				self.CurrStation1, self.NextStation1, self.TNMdirectionR1 = RedBeacon(self.RouteName1, self.TNMdirectionR1, self.TrainDirection1, self.beacon_bin1)
			signals.tnm_curr_station.emit(self.CurrStation1,1)
			#______________________________________________________________________
		elif(self.TrainNum2 == 1):
			#Call function to append beacon
			self.beacon_bin2 = AppendBeacon(self.BeaconId)
		
			#check if first value is: 1 = green line/0 = red line #Was 2, 3, 4, 5:
			if(self.beacon_bin2[0] == 0):
				self.RouteName2 = "Red Line"
				self.CurrStation2 = "Yard"
				self.NextStation2 = "Shady Side"
			elif(self.beacon_bin2[0] == 1):
				self.RouteName2 = "Green Line"
				self.CurrStation2 = "Yard"
				self.NextStation2 = "Glenbury"
			#check if second value is: 0 = station/1 = underground
			if(self.beacon_bin2[1] == 0):
				self.lights_Tun2 == False
			elif(self.beacon_bin2[1] == 1):
				self.lights_Tun2 == True
			#3rd bit - 0 Left(decrement)/1 Right(increment) directionality
			#0 means left doors open, 1 means right doors open
			if(self.beacon_bin2[2] == 0):
				self.TrainDirection2 = 0
				self.tnm_TrainDir.emit(self.TrainDirection2,2)
			elif(self.beacon_bin2[2] == 1):
				self.TrainDirection2 = 1
				self.tnm_TrainDir.emit(self.TrainDirection2,2)
				
			#Call Beacon function to specify station
			if(self.RouteName2 == "Green Line"):
				self.CurrStation2, self.NextStation2, self.TNMdirectionG2 = GreenBeacon(self.RouteName2, self.TNMdirectionG2, self.TrainDirection2, self.beacon_bin2)
			elif(self.RouteName2 == "Red Line"):
				self.CurrStation2, self.NextStation2, self.TNMdirectionR2 = RedBeacon(self.RouteName2, self.TNMdirectionR2, self.TrainDirection2, self.beacon_bin2)
			signals.tnm_curr_station.emit(self.CurrStation2,2)
			#______________________________________________________________________
		elif(self.TrainNum3 == 1):
			#Call function to append beacon
			self.beacon_bin3 = AppendBeacon(self.BeaconId)
		
			#check if first value is: 1 = green line/0 = red line #Was 2, 3, 4, 5:
			if(self.beacon_bin3[0] == 0):
				self.RouteName3 = "Red Line"
				self.CurrStation3 = "Yard"
				self.NextStation3 = "Shady Side"
			elif(self.beacon_bin3[0] == 1):
				self.RouteName3 = "Green Line"
				self.CurrStation3 = "Yard"
				self.NextStation3 = "Glenbury"
			#check if second value is: 0 = station/1 = underground
			if(self.beacon_bin3[1] == 0):
				self.lights_Tun3 == False
			elif(self.beacon_bin1[1] == 1):
				self.lights_Tun3 == True
			#3rd bit - 0 Left(decrement)/1 Right(increment) directionality
			#0 means left doors open, 1 means right doors open
			if(self.beacon_bin3[2] == 0):
				self.TrainDirection3 = 0
				self.tnm_TrainDir.emit(self.TrainDirection3,3)
			elif(self.beacon_bin3[2] == 1):
				self.TrainDirection3 = 1
				self.tnm_TrainDir.emit(self.TrainDirection3,3)
				
			#Call Beacon function to specify station
			if(self.RouteName3 == "Green Line"):
				self.CurrStation3, self.NextStation3, self.TNMdirectionG3 = GreenBeacon(self.RouteName3, self.TNMdirectionG3, self.TrainDirection3, self.beacon_bin3)
			elif(self.RouteName3 == "Red Line"):
				self.CurrStation3, self.NextStation3, self.TNMdirectionR3 = GreenBeacon(self.RouteName3, self.TNMdirectionR3, self.TrainDirection3, self.beacon_bin3)
			signals.tnm_curr_station.emit(self.CurrStation3,3)
			#______________________________________________________________________
		elif(self.TrainNum4 == 1):
			#Call function to append beacon
			self.beacon_bin4 = AppendBeacon(self.BeaconId)
		
			#check if first value is: 1 = green line/0 = red line #Was 2, 3, 4, 5:
			if(self.beacon_bin4[0] == 0):
				self.RouteName4 = "Red Line"
				self.CurrStation4 = "Yard"
				self.NextStation4 = "Shady Side"
			elif(self.beacon_bin4[0] == 1):
				self.RouteName4 = "Green Line"
				self.CurrStation4 = "Yard"
				self.NextStation4 = "Glenbury"
			#check if second value is: 0 = station/1 = underground
			if(self.beacon_bin4[1] == 0):
				self.lights_Tun4 == False
			elif(self.beacon_bin4[1] == 1):
				self.lights_Tun4 == True
			#3rd bit - 0 Left(decrement)/1 Right(increment) directionality
			#0 means left doors open, 1 means right doors open
			if(self.beacon_bin4[2] == 0):
				self.TrainDirection4 = 0
				self.tnm_TrainDir.emit(self.TrainDirection4,4)
			elif(self.beacon_bin4[2] == 1):
				self.TrainDirection4 = 1
				self.tnm_TrainDir.emit(self.TrainDirection4,4)
				
			#Call Beacon function to specify station
			if(self.RouteName4 == "Green Line"):
				self.CurrStation4, self.NextStation4, self.TNMdirectionG4 = GreenBeacon(self.RouteName4, self.TNMdirectionG4, self.TrainDirection4, self.beacon_bin4)
			elif(self.RouteName4 == "Red Line"):
				self.CurrStation4, self.NextStation4, self.TNMdirectionR4 = GreenBeacon(self.RouteName4, self.TNMdirectionR4, self.TrainDirection4, self.beacon_bin4)
			signals.tnm_curr_station.emit(self.CurrStation4,4)
			#______________________________________________________________________
		elif(self.TrainNum5 == 1):
			#Call function to append beacon
			self.beacon_bin5 = AppendBeacon(self.BeaconId)
		
			#check if first value is: 1 = green line/0 = red line #Was 2, 3, 4, 5:
			if(self.beacon_bin5[0] == 0):
				self.RouteName5 = "Red Line"
				self.CurrStation5 = "Yard"
				self.NextStation5 = "Shady Side"
			elif(self.beacon_bin5[0] == 1):
				self.RouteName5 = "Green Line"
				self.CurrStation5 = "Yard"
				self.NextStation5 = "Glenbury"
			#check if second value is: 0 = station/1 = underground
			if(self.beacon_bin5[1] == 0):
				self.lights_Tun5 == False
			elif(self.beacon_bin5[1] == 1):
				self.lights_Tun5 == True
			#3rd bit - 0 Left(decrement)/1 Right(increment) directionality
			#0 means left doors open, 1 means right doors open
			if(self.beacon_bin5[2] == 0):
				self.TrainDirection5 = 0
				self.tnm_TrainDir.emit(self.TrainDirection5,5)
			elif(self.beacon_bin5[2] == 1):
				self.TrainDirection5 = 1
				self.tnm_TrainDir.emit(self.TrainDirection5,5)
				
			#Call Beacon function to specify station
			if(self.RouteName5 == "Green Line"):
				self.CurrStation5, self.NextStation5, self.TNMdirectionG5 = GreenBeacon(self.RouteName5, self.TNMdirectionG5, self.TrainDirection5, self.beacon_bin5)
			elif(self.RouteName5 == "Red Line"):
				self.CurrStation5, self.NextStation5, self.TNMdirectionR5 = GreenBeacon(self.RouteName5, self.TNMdirectionR5, self.TrainDirection5, self.beacon_bin5)
			signals.tnm_curr_station.emit(self.CurrStation5,5)
			#______________________________________________________________________
		elif(self.TrainNum6 == 1):
			#Call function to append beacon
			self.beacon_bin6 = AppendBeacon(self.BeaconId)
		
			#check if first value is: 1 = green line/0 = red line #Was 2, 3, 4, 5:
			if(self.beacon_bin6[0] == 0):
				self.RouteName6 = "Red Line"
				self.CurrStation6 = "Yard"
				self.NextStation6 = "Shady Side"
			elif(self.beacon_bin6[0] == 1):
				self.RouteName6 = "Green Line"
				self.CurrStation6 = "Yard"
				self.NextStation6 = "Glenbury"
			#check if second value is: 0 = station/1 = underground
			if(self.beacon_bin6[1] == 0):
				self.lights_Tun6 == False
			elif(self.beacon_bin6[1] == 1):
				self.lights_Tun6 == True
			#3rd bit - 0 Left(decrement)/1 Right(increment) directionality
			#0 means left doors open, 1 means right doors open
			if(self.beacon_bin6[2] == 0):
				self.TrainDirection6 = 0
				self.tnm_TrainDir.emit(self.TrainDirection6,6)
			elif(self.beacon_bin6[2] == 1):
				self.TrainDirection6 = 1
				self.tnm_TrainDir.emit(self.TrainDirection6,6)
				
			#Call Beacon function to specify station
			if(self.RouteName6 == "Green Line"):
				self.CurrStation6, self.NextStation6, self.TNMdirectionG6 = GreenBeacon(self.RouteName6, self.TNMdirectionG6, self.TrainDirection6, self.beacon_bin6)
			elif(self.RouteName6 == "Red Line"):
				self.CurrStation6, self.NextStation6, self.TNMdirectionR6 = GreenBeacon(self.RouteName6, self.TNMdirectionR6, self.TrainDirection6, self.beacon_bin6)
			signals.tnm_curr_station.emit(self.CurrStation6,6)
			#______________________________________________________________________
		elif(self.TrainNum7 == 1):
			#Call function to append beacon
			self.beacon_bin7 = AppendBeacon(self.BeaconId)
		
			#check if first value is: 1 = green line/0 = red line #Was 2, 3, 4, 5:
			if(self.beacon_bin7[0] == 0):
				self.RouteName7 = "Red Line"
				self.CurrStation7 = "Yard"
				self.NextStation7 = "Shady Side"
			elif(self.beacon_bin7[0] == 1):
				self.RouteName7 = "Green Line"
				self.CurrStation7 = "Yard"
				self.NextStation7 = "Glenbury"
			#check if second value is: 0 = station/1 = underground
			if(self.beacon_bin7[1] == 0):
				self.lights_Tun7 == False
			elif(self.beacon_bin7[1] == 1):
				self.lights_Tun7 == True
			#3rd bit - 0 Left(decrement)/1 Right(increment) directionality
			#0 means left doors open, 1 means right doors open
			if(self.beacon_bin7[2] == 0):
				self.TrainDirection7 = 0
				self.tnm_TrainDir.emit(self.TrainDirection7,7)
			elif(self.beacon_bin7[2] == 1):
				self.TrainDirection7 = 1
				self.tnm_TrainDir.emit(self.TrainDirection7,7)
				
			#Call Beacon function to specify station
			if(self.RouteName7 == "Green Line"):
				self.CurrStation7, self.NextStation7, self.TNMdirectionG7 = GreenBeacon(self.RouteName7, self.TNMdirectionG7, self.TrainDirection7, self.beacon_bin7)
			elif(self.RouteName7 == "Red Line"):
				self.CurrStation7, self.NextStation7, self.TNMdirectionR7 = GreenBeacon(self.RouteName7, self.TNMdirectionR7, self.TrainDirection7, self.beacon_bin7)
			signals.tnm_curr_station.emit(self.CurrStation7,7)
			#______________________________________________________________________
		elif(self.TrainNum8 == 1):
			#Call function to append beacon
			self.beacon_bin8 = AppendBeacon(self.BeaconId)
		
			#check if first value is: 1 = green line/0 = red line #Was 2, 3, 4, 5:
			if(self.beacon_bin8[0] == 0):
				self.RouteName8 = "Red Line"
				self.CurrStation8 = "Yard"
				self.NextStation8 = "Shady Side"
			elif(self.beacon_bin8[0] == 1):
				self.RouteName8 = "Green Line"
				self.CurrStation8 = "Yard"
				self.NextStation8 = "Glenbury"
			#check if second value is: 0 = station/1 = underground
			if(self.beacon_bin8[1] == 0):
				self.lights_Tun8 == False
			elif(self.beacon_bin8[1] == 1):
				self.lights_Tun8 == True
			#3rd bit - 0 Left(decrement)/1 Right(increment) directionality
			#0 means left doors open, 1 means right doors open
			if(self.beacon_bin8[2] == 0):
				self.TrainDirection8 = 0
				self.tnm_TrainDir.emit(self.TrainDirection8,8)
			elif(self.beacon_bin8[2] == 1):
				self.TrainDirection8 = 1
				self.tnm_TrainDir.emit(self.TrainDirection8,8)
				
			#Call Beacon function to specify station
			if(self.RouteName8 == "Green Line"):
				self.CurrStation8, self.NextStation8, self.TNMdirectionG8 = GreenBeacon(self.RouteName8, self.TNMdirectionG8, self.TrainDirection8, self.beacon_bin8)
			elif(self.RouteName8 == "Red Line"):
				self.CurrStation8, self.NextStation8, self.TNMdirectionR8 = GreenBeacon(self.RouteName8, self.TNMdirectionR8, self.TrainDirection8, self.beacon_bin8)
			signals.tnm_curr_station.emit(self.CurrStation8,8)
			#______________________________________________________________________
			
	
	#Function to specify block number for each line
	def blockNum(self,BlockNum):
		if(self.TrainNum1 == 1):
			self.block_num1 = BlockNum
		elif(self.TrainNum2 == 1):
			self.block_num2 = BlockNum
		elif(self.TrainNum3 == 1):
			self.block_num3 = BlockNum
		elif(self.TrainNum4 == 1):
			self.block_num4 = BlockNum
		elif(self.TrainNum5 == 1):
			self.block_num5 = BlockNum
		elif(self.TrainNum6 == 1):
			self.block_num6 = BlockNum
		elif(self.TrainNum7 == 1):
			self.block_num7 = BlockNum
		elif(self.TrainNum8 == 1):
			self.block_num8 = BlockNum
			
		
	#Function to take in block length and calculate when train reaches next block
	def blockLen(self, BlockLen):
		#set variables based on Train Number
		if(self.TrainNum1 == 1):
			self.block_length1 = BlockLen
		elif(self.TrainNum2 == 1):
			self.block_length2 = BlockLen
		elif(self.TrainNum3 == 1):
			self.block_length3 = BlockLen
		elif(self.TrainNum4 == 1):
			self.block_length4 = BlockLen
		elif(self.TrainNum5 == 1):
			self.block_length5 = BlockLen
		elif(self.TrainNum6 == 1):
			self.block_length6 = BlockLen
		elif(self.TrainNum7 == 1):
			self.block_length7 = BlockLen
		elif(self.TrainNum8 == 1):
			self.block_length8 = BlockLen
			
	
	#Function to set Authority from track model signal
	def SetAuthority(self,tkm_authority):
		if(self.TrainNum1 == 1):
			self.block_authority1 = tkm_authority
		elif(self.TrainNum2 == 1):
			self.block_authority2 = tkm_authority
		elif(self.TrainNum3 == 1):
			self.block_authority3 = tkm_authority
		elif(self.TrainNum4 == 1):
			self.block_authority4 = tkm_authority
		elif(self.TrainNum5 == 1):
			self.block_authority5 = tkm_authority
		elif(self.TrainNum6 == 1):
			self.block_authority6 = tkm_authority
		elif(self.TrainNum7 == 1):
			self.block_authority7 = tkm_authority
		elif(self.TrainNum8 == 1):
			self.block_authority8 = tkm_authority
		
	#Function to set Commanded Speed from track model signal
	def SetCommSpeed(self,commSpeed):
		if(self.TrainNum1 == 1):
			self.comm_speed1 = meterToMile(commSpeed)			#convert mps to MPH
		elif(self.TrainNum2 == 1):
			self.comm_speed2 = meterToMile(commSpeed)
		elif(self.TrainNum3 == 1):
			self.comm_speed3 = meterToMile(commSpeed)
		elif(self.TrainNum4 == 1):
			self.comm_speed4 = meterToMile(commSpeed)
		elif(self.TrainNum5 == 1):
			self.comm_speed5 = meterToMile(commSpeed)
		elif(self.TrainNum6 == 1):
			self.comm_speed6 = meterToMile(commSpeed)
		elif(self.TrainNum7 == 1):
			self.comm_speed7 = meterToMile(commSpeed)
		elif(self.TrainNum8 == 1):
			self.comm_speed8 = meterToMile(commSpeed)
	
	#Function to set Passenger count from track model signal
	def SetOccupancy(self,tkm_pass_count):
		if(self.TrainNum1 == 1):
			self.pass_count1 = tkm_pass_count
		elif(self.TrainNum2 == 1):
			self.pass_count2 = tkm_pass_count
		elif(self.TrainNum3 == 1):
			self.pass_count3 = tkm_pass_count
		elif(self.TrainNum4 == 1):
			self.pass_count4 = tkm_pass_count
		elif(self.TrainNum5 == 1):
			self.pass_count5 = tkm_pass_count
		elif(self.TrainNum6 == 1):
			self.pass_count6 = tkm_pass_count
		elif(self.TrainNum7 == 1):
			self.pass_count7 = tkm_pass_count
		elif(self.TrainNum8 == 1):
			self.pass_count8 = tkm_pass_count
	
	#Function to read the emergency brake state from tnc
	def SetEBrake(self, EmerBrake):
		if(self.TrainNum1 == 1):
			self.eBrake1 = EmerBrake
		elif(self.TrainNum2 == 1):
			self.eBrake2 = EmerBrake
		elif(self.TrainNum3 == 1):
			self.eBrake3 = EmerBrake
		elif(self.TrainNum4 == 1):
			self.eBrake4 = EmerBrake
		elif(self.TrainNum5 == 1):
			self.eBrake5 = EmerBrake
		elif(self.TrainNum6 == 1):
			self.eBrake6 = EmerBrake
		elif(self.TrainNum7 == 1):
			self.eBrake7 = EmerBrake
		elif(self.TrainNum8 == 1):
			self.eBrake8 = EmerBrake
		
	#Function to read the service brake state from tnc
	def SetServiceBrake(self, ServiceBrake):
		if(self.TrainNum1 == 1):
			self.Brake1 = ServiceBrake
		elif(self.TrainNum2 == 1):
			self.Brake2 = ServiceBrake
		elif(self.TrainNum3 == 1):
			self.Brake3 = ServiceBrake
		elif(self.TrainNum4 == 1):
			self.Brake4 = ServiceBrake
		elif(self.TrainNum5 == 1):
			self.Brake5 = ServiceBrake
		elif(self.TrainNum6 == 1):
			self.Brake6 = ServiceBrake
		elif(self.TrainNum7 == 1):
			self.Brake7 = ServiceBrake
		elif(self.TrainNum8 == 1):
			self.Brake8 = ServiceBrake
		
	#Function to read in announcement from tnc
	def SetAnnounce(self, CurrentAnnouncement):
		if(self.TrainNum1 == 1):
			self.announce1 = CurrentAnnouncement
		elif(self.TrainNum2 == 1):
			self.announce2 = CurrentAnnouncement
		elif(self.TrainNum3 == 1):
			self.announce3 = CurrentAnnouncement
		elif(self.TrainNum4 == 1):
			self.announce4 = CurrentAnnouncement
		elif(self.TrainNum5 == 1):
			self.announce5 = CurrentAnnouncement
		elif(self.TrainNum6 == 1):
			self.announce6 = CurrentAnnouncement
		elif(self.TrainNum7 == 1):
			self.announce7 = CurrentAnnouncement
		elif(self.TrainNum8 == 1):
			self.announce8 = CurrentAnnouncement
		
	#Function to update status of Train Left Door
	def setLeftDoor(self, tncLeftDoor):
		if(self.TrainNum1 == 1):
			self.LeftDoor1 = tncLeftDoor
		elif(self.TrainNum2 == 1):
			self.LeftDoor2 = tncLeftDoor
		elif(self.TrainNum3 == 1):
			self.LeftDoor3 = tncLeftDoor
		elif(self.TrainNum4 == 1):
			self.LeftDoor4 = tncLeftDoor
		elif(self.TrainNum5 == 1):
			self.LeftDoor5 = tncLeftDoor
		elif(self.TrainNum6 == 1):
			self.LeftDoor6 = tncLeftDoor
		elif(self.TrainNum7 == 1):
			self.LeftDoor7 = tncLeftDoor
		elif(self.TrainNum8 == 1):
			self.LeftDoor8 = tncLeftDoor
		
	#Function to update status of Train Right Door
	def setRightDoor(self, tncRightDoor):
		if(self.TrainNum1 == 1):
			self.RightDoor1 = tncRightDoor
		elif(self.TrainNum2 == 1):
			self.RightDoor2 = tncRightDoor
		elif(self.TrainNum3 == 1):
			self.RightDoor3 = tncRightDoor
		elif(self.TrainNum4 == 1):
			self.RightDoor4 = tncRightDoor
		elif(self.TrainNum5 == 1):
			self.RightDoor5 = tncRightDoor
		elif(self.TrainNum6 == 1):
			self.RightDoor6 = tncRightDoor
		elif(self.TrainNum7 == 1):
			self.RightDoor7 = tncRightDoor
		elif(self.TrainNum8 == 1):
			self.RightDoor8 = tncRightDoor
		
	#Function to update Cab Light status
	def setCabLight(self, tncCabLight):
		if(self.TrainNum1 == 1):
			self.light_Cab1 = tncCabLight
		elif(self.TrainNum2 == 1):
			self.light_Cab2 = tncCabLight
		elif(self.TrainNum3 == 1):
			self.light_Cab3 = tncCabLight
		elif(self.TrainNum4 == 1):
			self.light_Cab4 = tncCabLight
		elif(self.TrainNum5 == 1):
			self.light_Cab5 = tncCabLight
		elif(self.TrainNum6 == 1):
			self.light_Cab6 = tncCabLight
		elif(self.TrainNum7 == 1):
			self.light_Cab7 = tncCabLight
		elif(self.TrainNum8 == 1):
			self.light_Cab8 = tncCabLight
			
	#Function to update Tun Light status
	def setTunLight(self, tncTunLight):
		if(self.TrainNum1 == 1):
			self.light_Tun1 = tncTunLight
		elif(self.TrainNum2 == 1):
			self.light_Tun2 = tncTunLight
		elif(self.TrainNum3 == 1):
			self.light_Tun3 = tncTunLight
		elif(self.TrainNum4 == 1):
			self.light_Tun4 = tncTunLight
		elif(self.TrainNum5 == 1):
			self.light_Tun5 = tncTunLight
		elif(self.TrainNum6 == 1):
			self.light_Tun6 = tncTunLight
		elif(self.TrainNum7 == 1):
			self.light_Tun7 = tncTunLight
		elif(self.TrainNum8 == 1):
			self.light_Tun8 = tncTunLight
			
	#Function to update High Beam Light status
	def setHighLight(self, tncHighLight):
		if(self.TrainNum1 == 1):
			self.light_High1 = tncHighLight
		elif(self.TrainNum2 == 1):
			self.light_High2 = tncHighLight
		elif(self.TrainNum3 == 1):
			self.light_High3 = tncHighLight
		elif(self.TrainNum4 == 1):
			self.light_High4 = tncHighLight
		elif(self.TrainNum5 == 1):
			self.light_High5 = tncHighLight
		elif(self.TrainNum6 == 1):
			self.light_High6 = tncHighLight
		elif(self.TrainNum7 == 1):
			self.light_High7 = tncHighLight
		elif(self.TrainNum8 == 1):
			self.light_High8 = tncHighLight
		
	#Function to set the train number, and specify the line name
	def setTrainStart(self, tkmTrainNum, tkmTrainLine):			#int, str
		self.TrainNum = tkmTrainNum
		
		if(self.TrainNum == 1):
			self.TrainNum1 = 1
		elif(self.TrainNum == 2):
			self.TrainNum2 = 1
		elif(self.TrainNum == 3):
			self.TrainNum3 = 1
		elif(self.TrainNum == 4):
			self.TrainNum4 = 1
		elif(self.TrainNum == 5):
			self.TrainNum5 = 1
		elif(self.TrainNum == 6):
			self.TrainNum6 = 1
		elif(self.TrainNum == 7):
			self.TrainNum7 = 1
		elif(self.TrainNum == 8):
			self.TrainNum8 = 1
			
		#Determine which Train Number -> Train Name
		if(self.TrainNum1 == 1):
			self.TrainName1 = self.train1
			#Check which line the train is added to, and specify RouteLine variable
			if(tkmTrainLine == "Red"):
				self.RouteName1 = "Red Line"
				self.NextStation1 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName1 = "Green Line"
				self.NextStation1 = "Glenbury"
		elif(self.TrainNum2 == 1):
			self.TrainName2 = self.train2
			#Check which line the train is added to, and specify RouteLine variable
			if(tkmTrainLine == "Red"):
				self.RouteName2 = "Red Line"
				self.NextStation2 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName2 = "Green Line"
				self.NextStation2 = "Glenbury"
		elif(self.TrainNum3 == 1):
			self.TrainName3 = self.train3
			if(tkmTrainLine == "Red"):
				self.RouteName3 = "Red Line"
				self.NextStation3 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName3 = "Green Line"
				self.NextStation3 = "Glenbury"
		elif(self.TrainNum4 == 1):
			self.TrainName4 = self.train4
			if(tkmTrainLine == "Red"):
				self.RouteName4 = "Red Line"
				self.NextStation4 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName4 = "Green Line"
				self.NextStation4 = "Glenbury"
		elif(self.TrainNum5 == 1):
			self.TrainName5 = self.train5
			if(tkmTrainLine == "Red"):
				self.RouteName5 = "Red Line"
				self.NextStation5 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName5 = "Green Line"
				self.NextStation5 = "Glenbury"
		elif(self.TrainNum6 == 1):
			self.TrainName6 = self.train6
			if(tkmTrainLine == "Red"):
				self.RouteName6 = "Red Line"
				self.NextStation6 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName6 = "Green Line"
				self.NextStation6 = "Glenbury"
		elif(self.TrainNum7 == 1):
			self.TrainName7 = self.train7
			if(tkmTrainLine == "Red"):
				self.RouteName7 = "Red Line"
				self.NextStation7 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName7 = "Green Line"
				self.NextStation7 = "Glenbury"
		elif(self.TrainNum8 == 1):
			self.TrainName8 = self.train8
			if(tkmTrainLine == "Red"):
				self.RouteName8 = "Red Line"
				self.NextStation8 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName8 = "Green Line"
				self.NextStation8 = "Glenbury"		
		
	#Function to update train status to 0, if destroyed
	def setDestroyTrain(self, tkmTrainNumDestroyed):
		trainNumber = tkmTrainNumDestroyed
		#Check train number, and stop train from moving on the track anymore
		if(trainNumber == 1):
			self.TrainNum1 = 0
		elif(trainNumber == 2):
			self.TrainNum2 = 0
		elif(trainNumber == 3):
			self.TrainNum3 = 0
		elif(trainNumber == 4):
			self.TrainNum4 = 0
		elif(trainNumber == 5):
			self.TrainNum5 = 0
		elif(trainNumber == 6):
			self.TrainNum6 = 0
		elif(trainNumber == 7):
			self.TrainNum7 = 0
		elif(trainNumber == 8):
			self.TrainNum8 = 0
			
	
	#Function for TIME
	def getTime(self, time_sec, time_min, time_hr, time_tot):
		self.timeSeconds = time_sec
		if(time_min > 0):
			time_sec = time_sec + (time_min*60)
			self.timeSeconds = time_sec
		elif(time_min > 0 and time_hr > 0):
			time_sec = time_sec + (time_min*60)
			time_sec = time_sec + ((time_hr*60)*60)
			self.timeSeconds = time_sec

	
		
#_______________________________________________________________________
if __name__ == "__main__":
	import sys
	
	app = QtWidgets.QApplication(sys.argv)
	#MainWindow = QtWidgets.QMainWindow()
	#TestUi = QtWidgets.QMainWindow()

	#Initialize main program and test program
	prog = tnm_display()
	test = tnm_failureTest()
	
	sys.exit(app.exec_())
	

