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

#HELPER CLASS - for dealing with multiple UI instances
class tnm_threadSupport(QObject):
	def __init__(self):
		super().__init__()
		#Call TNM Display to get Train Model 10 interfaces
		self.MainWindow = QtWidgets.QMainWindow()
		self.uim = Ui_MainWindow()
		self.uim.setupUi(self.MainWindow)
		self.MainWindow.show()

	
#HELPER CLASS2 - for dealing with multiple UI instances
class tnm_threadSupportFail(QObject):
	def __init__(self):
		super().__init__()
		#Call TNM Failure Test to get Train Model 10 failure interfaces
		self.TestUi = QtWidgets.QMainWindow()
		self.ui = Ui_Test()
		self.ui.setupUi(self.TestUi)
		self.TestUi.show() 

#_______________________________________________________________________
#Failure Test State for Train Model Interface
class tnm_failureTest(QObject):
	def __init__(self):
		super().__init__()
		#Main Window Thread 1
		self.ui1 = tnm_threadSupportFail()
		self.threadFail1 = QThread()
		self.ui1.moveToThread(self.threadFail1)
		self.ui1.TestUi.setWindowTitle("Train 1 Fail States")
		self.threadFail1.start()
		#Main Window Thread 2
		self.ui2 = tnm_threadSupportFail()
		self.threadFail2 = QThread()
		self.ui2.moveToThread(self.threadFail2)
		self.ui2.TestUi.setWindowTitle("Train 2 Fail States")
		self.threadFail2.start()
		#Main Window Thread 3
		self.ui3 = tnm_threadSupportFail()
		self.threadFail3 = QThread()
		self.ui3.moveToThread(self.threadFail3)
		self.ui3.TestUi.setWindowTitle("Train 3 Fail States")
		self.threadFail3.start()
		#Main Window Thread 4
		self.ui4 = tnm_threadSupportFail()
		self.threadFail4 = QThread()
		self.ui4.moveToThread(self.threadFail4)
		self.ui4.TestUi.setWindowTitle("Train 4 Fail States")
		self.threadFail4.start()
		#Main Window Thread 5
		self.ui5 = tnm_threadSupportFail()
		self.threadFail5 = QThread()
		self.ui5.moveToThread(self.threadFail5)
		self.ui5.TestUi.setWindowTitle("Train 5 Fail States")
		self.threadFail5.start()
		#Main Window Thread 6
		self.ui6 = tnm_threadSupportFail()
		self.threadFail6 = QThread()
		self.ui6.moveToThread(self.threadFail6)
		self.ui6.TestUi.setWindowTitle("Train 6 Fail States")
		self.threadFail6.start()
		#Main Window Thread 7
		self.ui7 = tnm_threadSupportFail()
		self.threadFail7 = QThread()
		self.ui7.moveToThread(self.threadFail7)
		self.ui7.TestUi.setWindowTitle("Train 7 Fail States")
		self.threadFail7.start()
		#Main Window Thread 8
		self.ui8 = tnm_threadSupportFail()
		self.threadFail8 = QThread()
		self.ui8.moveToThread(self.threadFail8)
		self.ui8.TestUi.setWindowTitle("Train 8 Fail States")
		self.threadFail8.start()
		#Main Window Thread 9
		self.ui9 = tnm_threadSupportFail()
		self.threadFail9 = QThread()
		self.ui9.moveToThread(self.threadFail9)
		self.ui9.TestUi.setWindowTitle("Train 9 Fail States")
		self.threadFail9.start()
		#Main Window Thread 10
		self.ui10 = tnm_threadSupportFail()
		self.threadFail10 = QThread()
		self.ui10.moveToThread(self.threadFail10)
		self.ui10.TestUi.setWindowTitle("Train 10 Fail States")
		self.threadFail10.start()
		

		#Signals defined
		tnm_ebrake = pyqtSignal(bool, int)
		tnm_sendyard = pyqtSignal(bool, int)			#Track Model and Track Controller
		
		#define variables to be used in the Failure Interface
		self.car1_status1, self.car1_status2, self.car1_status3,self.car1_status4, self.car1_status5, self.car1_status6, self.car1_status7, self.car1_status8, self.car1_status9, self.car1_status10 = True,True,True,True,True,True,True,True,True,True
		self.car2_status1, self.car2_status2, self.car2_status3,self.car2_status4, self.car2_status5, self.car2_status6, self.car2_status7, self.car2_status8, self.car2_status9, self.car2_status10 = True,True,True,True,True,True,True,True,True,True
		self.car3_status1, self.car3_status2, self.car3_status3,self.car3_status4, self.car3_status5, self.car3_status6, self.car3_status7, self.car3_status8, self.car3_status9, self.car3_status10 = True,True,True,True,True,True,True,True,True,True
		self.car4_status1, self.car4_status2, self.car4_status3,self.car4_status4, self.car4_status5, self.car4_status6, self.car4_status7, self.car4_status8, self.car4_status9, self.car4_status10 = True,True,True,True,True,True,True,True,True,True
		self.car5_status1, self.car5_status2, self.car5_status3,self.car5_status4, self.car5_status5, self.car5_status6, self.car5_status7, self.car5_status8, self.car5_status9, self.car5_status10 = True,True,True,True,True,True,True,True,True,True
		self.train1_status, self.train2_status, self.train3_status, self.train4_status, self.train5_status, self.train6_status, self.train7_status, self.train8_status, self.train9_status, self.train10_status = True,True,True,True,True,True,True,True,True,True
		self.sendYard1, self.sendYard2, self.sendYard3, self.sendYard4, self.sendYard5, self.sendYard6, self.sendYard7, self.sendYard8, self.sendYard9, self.sendYard10 = False,False,False,False,False,False,False,False,False,False
		self.trainNum = 0
		self.routeLine = 0
		self.train1, self.train2, self.train3, self.train4, self.train5, self.train6, self.train7, self.train8, self.train9, self.train10 = "Train 1 Status", "Train 2 Status", "Train 3 Status", "Train 4 Status", "Train 5 Status", "Train 6 Status", "Train 7 Status","Train 8 Status","Train 9 Status","Train 10 Status"
		self.trainNum1, self.trainNum2, self.trainNum3, self.trainNum4, self.trainNum5, self.trainNum6, self.trainNum7, self.trainNum8, self.trainNum9, self.trainNum10 = 0,0,0,0,0,0,0,0,0,0
		self.eBrakeTest1, self.eBrakeTest2, self.eBrakeTest3, self.eBrakeTest4, self.eBrakeTest5, self.eBrakeTest6, self.eBrakeTest7, self.eBrakeTest8, self.eBrakeTest9, self.eBrakeTest10 = False,False,False,False,False,False,False,False,False,False
		signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
		signals.tkm_get_train_num.connect(self.setTrainInfo)
		
		#Defining Actions for specific UI Interactions
		signals.time.connect(self.update_Info)
		#self.pushButton.clicked.connect(self.update_Info)
		#Check if each module is being edited

		self.ui1.ui.lineEdit.editingFinished.connect(self.brake_fail_act)
		self.ui1.ui.lineEdit_2.editingFinished.connect(self.brake_fail_act)
		self.ui1.ui.lineEdit_3.editingFinished.connect(self.brake_fail_act)
		self.ui1.ui.lineEdit_4.editingFinished.connect(self.brake_fail_act)
		self.ui1.ui.lineEdit_5.editingFinished.connect(self.brake_fail_act)
		self.ui1.ui.lineEdit_7.editingFinished.connect(self.engine_fail_act)
		self.ui1.ui.lineEdit_12.editingFinished.connect(self.engine_fail_act)
		self.ui1.ui.lineEdit_13.editingFinished.connect(self.engine_fail_act)
		self.ui1.ui.lineEdit_14.editingFinished.connect(self.engine_fail_act)
		self.ui1.ui.lineEdit_15.editingFinished.connect(self.engine_fail_act)
		self.ui1.ui.lineEdit_21.editingFinished.connect(self.signalP_fail_act)

		self.ui2.ui.lineEdit.editingFinished.connect(self.brake_fail_act)
		self.ui2.ui.lineEdit_2.editingFinished.connect(self.brake_fail_act)
		self.ui2.ui.lineEdit_3.editingFinished.connect(self.brake_fail_act)
		self.ui2.ui.lineEdit_4.editingFinished.connect(self.brake_fail_act)
		self.ui2.ui.lineEdit_5.editingFinished.connect(self.brake_fail_act)
		self.ui2.ui.lineEdit_7.editingFinished.connect(self.engine_fail_act)
		self.ui2.ui.lineEdit_12.editingFinished.connect(self.engine_fail_act)
		self.ui2.ui.lineEdit_13.editingFinished.connect(self.engine_fail_act)
		self.ui2.ui.lineEdit_14.editingFinished.connect(self.engine_fail_act)
		self.ui2.ui.lineEdit_15.editingFinished.connect(self.engine_fail_act)
		self.ui2.ui.lineEdit_21.editingFinished.connect(self.signalP_fail_act)

		self.ui3.ui.lineEdit.editingFinished.connect(self.brake_fail_act)
		self.ui3.ui.lineEdit_2.editingFinished.connect(self.brake_fail_act)
		self.ui3.ui.lineEdit_3.editingFinished.connect(self.brake_fail_act)
		self.ui3.ui.lineEdit_4.editingFinished.connect(self.brake_fail_act)
		self.ui3.ui.lineEdit_5.editingFinished.connect(self.brake_fail_act)
		self.ui3.ui.lineEdit_7.editingFinished.connect(self.engine_fail_act)
		self.ui3.ui.lineEdit_12.editingFinished.connect(self.engine_fail_act)
		self.ui3.ui.lineEdit_13.editingFinished.connect(self.engine_fail_act)
		self.ui3.ui.lineEdit_14.editingFinished.connect(self.engine_fail_act)
		self.ui3.ui.lineEdit_15.editingFinished.connect(self.engine_fail_act)
		self.ui3.ui.lineEdit_21.editingFinished.connect(self.signalP_fail_act)

		self.ui4.ui.lineEdit.editingFinished.connect(self.brake_fail_act)
		self.ui4.ui.lineEdit_2.editingFinished.connect(self.brake_fail_act)
		self.ui4.ui.lineEdit_3.editingFinished.connect(self.brake_fail_act)
		self.ui4.ui.lineEdit_4.editingFinished.connect(self.brake_fail_act)
		self.ui4.ui.lineEdit_5.editingFinished.connect(self.brake_fail_act)
		self.ui4.ui.lineEdit_7.editingFinished.connect(self.engine_fail_act)
		self.ui4.ui.lineEdit_12.editingFinished.connect(self.engine_fail_act)
		self.ui4.ui.lineEdit_13.editingFinished.connect(self.engine_fail_act)
		self.ui4.ui.lineEdit_14.editingFinished.connect(self.engine_fail_act)
		self.ui4.ui.lineEdit_15.editingFinished.connect(self.engine_fail_act)
		self.ui4.ui.lineEdit_21.editingFinished.connect(self.signalP_fail_act)

		self.ui5.ui.lineEdit.editingFinished.connect(self.brake_fail_act)
		self.ui5.ui.lineEdit_2.editingFinished.connect(self.brake_fail_act)
		self.ui5.ui.lineEdit_3.editingFinished.connect(self.brake_fail_act)
		self.ui5.ui.lineEdit_4.editingFinished.connect(self.brake_fail_act)
		self.ui5.ui.lineEdit_5.editingFinished.connect(self.brake_fail_act)
		self.ui5.ui.lineEdit_7.editingFinished.connect(self.engine_fail_act)
		self.ui5.ui.lineEdit_12.editingFinished.connect(self.engine_fail_act)
		self.ui5.ui.lineEdit_13.editingFinished.connect(self.engine_fail_act)
		self.ui5.ui.lineEdit_14.editingFinished.connect(self.engine_fail_act)
		self.ui5.ui.lineEdit_15.editingFinished.connect(self.engine_fail_act)
		self.ui5.ui.lineEdit_21.editingFinished.connect(self.signalP_fail_act)

		self.ui6.ui.lineEdit.editingFinished.connect(self.brake_fail_act)
		self.ui6.ui.lineEdit_2.editingFinished.connect(self.brake_fail_act)
		self.ui6.ui.lineEdit_3.editingFinished.connect(self.brake_fail_act)
		self.ui6.ui.lineEdit_4.editingFinished.connect(self.brake_fail_act)
		self.ui6.ui.lineEdit_5.editingFinished.connect(self.brake_fail_act)
		self.ui6.ui.lineEdit_7.editingFinished.connect(self.engine_fail_act)
		self.ui6.ui.lineEdit_12.editingFinished.connect(self.engine_fail_act)
		self.ui6.ui.lineEdit_13.editingFinished.connect(self.engine_fail_act)
		self.ui6.ui.lineEdit_14.editingFinished.connect(self.engine_fail_act)
		self.ui6.ui.lineEdit_15.editingFinished.connect(self.engine_fail_act)
		self.ui6.ui.lineEdit_21.editingFinished.connect(self.signalP_fail_act)

		self.ui7.ui.lineEdit.editingFinished.connect(self.brake_fail_act)
		self.ui7.ui.lineEdit_2.editingFinished.connect(self.brake_fail_act)
		self.ui7.ui.lineEdit_3.editingFinished.connect(self.brake_fail_act)
		self.ui7.ui.lineEdit_4.editingFinished.connect(self.brake_fail_act)
		self.ui7.ui.lineEdit_5.editingFinished.connect(self.brake_fail_act)
		self.ui7.ui.lineEdit_7.editingFinished.connect(self.engine_fail_act)
		self.ui7.ui.lineEdit_12.editingFinished.connect(self.engine_fail_act)
		self.ui7.ui.lineEdit_13.editingFinished.connect(self.engine_fail_act)
		self.ui7.ui.lineEdit_14.editingFinished.connect(self.engine_fail_act)
		self.ui7.ui.lineEdit_15.editingFinished.connect(self.engine_fail_act)
		self.ui7.ui.lineEdit_21.editingFinished.connect(self.signalP_fail_act)

		self.ui8.ui.lineEdit.editingFinished.connect(self.brake_fail_act)
		self.ui8.ui.lineEdit_2.editingFinished.connect(self.brake_fail_act)
		self.ui8.ui.lineEdit_3.editingFinished.connect(self.brake_fail_act)
		self.ui8.ui.lineEdit_4.editingFinished.connect(self.brake_fail_act)
		self.ui8.ui.lineEdit_5.editingFinished.connect(self.brake_fail_act)
		self.ui8.ui.lineEdit_7.editingFinished.connect(self.engine_fail_act)
		self.ui8.ui.lineEdit_12.editingFinished.connect(self.engine_fail_act)
		self.ui8.ui.lineEdit_13.editingFinished.connect(self.engine_fail_act)
		self.ui8.ui.lineEdit_14.editingFinished.connect(self.engine_fail_act)
		self.ui8.ui.lineEdit_15.editingFinished.connect(self.engine_fail_act)
		self.ui8.ui.lineEdit_21.editingFinished.connect(self.signalP_fail_act)

		self.ui9.ui.lineEdit.editingFinished.connect(self.brake_fail_act)
		self.ui9.ui.lineEdit_2.editingFinished.connect(self.brake_fail_act)
		self.ui9.ui.lineEdit_3.editingFinished.connect(self.brake_fail_act)
		self.ui9.ui.lineEdit_4.editingFinished.connect(self.brake_fail_act)
		self.ui9.ui.lineEdit_5.editingFinished.connect(self.brake_fail_act)
		self.ui9.ui.lineEdit_7.editingFinished.connect(self.engine_fail_act)
		self.ui9.ui.lineEdit_12.editingFinished.connect(self.engine_fail_act)
		self.ui9.ui.lineEdit_13.editingFinished.connect(self.engine_fail_act)
		self.ui9.ui.lineEdit_14.editingFinished.connect(self.engine_fail_act)
		self.ui9.ui.lineEdit_15.editingFinished.connect(self.engine_fail_act)
		self.ui9.ui.lineEdit_21.editingFinished.connect(self.signalP_fail_act)

		self.ui10.ui.lineEdit.editingFinished.connect(self.brake_fail_act)
		self.ui10.ui.lineEdit_2.editingFinished.connect(self.brake_fail_act)
		self.ui10.ui.lineEdit_3.editingFinished.connect(self.brake_fail_act)
		self.ui10.ui.lineEdit_4.editingFinished.connect(self.brake_fail_act)
		self.ui10.ui.lineEdit_5.editingFinished.connect(self.brake_fail_act)
		self.ui10.ui.lineEdit_7.editingFinished.connect(self.engine_fail_act)
		self.ui10.ui.lineEdit_12.editingFinished.connect(self.engine_fail_act)
		self.ui10.ui.lineEdit_13.editingFinished.connect(self.engine_fail_act)
		self.ui10.ui.lineEdit_14.editingFinished.connect(self.engine_fail_act)
		self.ui10.ui.lineEdit_15.editingFinished.connect(self.engine_fail_act)
		self.ui10.ui.lineEdit_21.editingFinished.connect(self.signalP_fail_act)

#_______________________________________________________________________
	#function to update Train Failure interface Info
	def update_Info(self):
		#Update Train Number based on Route Line
		if(self.trainNum1 == 1):
			self.ui1.ui.label.setText(self.train1)
			self.ui1.ui.lineEdit_6.setReadOnly(True)		#Brake Status's
			self.ui1.ui.lineEdit_11.setReadOnly(True)		
			self.ui1.ui.lineEdit_8.setReadOnly(True)		
			self.ui1.ui.lineEdit_9.setReadOnly(True)			
			self.ui1.ui.lineEdit_10.setReadOnly(True)	
			self.ui1.ui.lineEdit_16.setReadOnly(True)		#Engine Status's	
			self.ui1.ui.lineEdit_17.setReadOnly(True)	
			self.ui1.ui.lineEdit_18.setReadOnly(True)	
			self.ui1.ui.lineEdit_19.setReadOnly(True)		
			self.ui1.ui.lineEdit_20.setReadOnly(True)		
			self.ui1.ui.lineEdit_26.setReadOnly(True)		#Signal Pickup Status
		if(self.trainNum2 == 1):
			self.ui2.ui.label.setText(self.train2)
			self.ui2.ui.lineEdit_6.setReadOnly(True)		#Brake Status's
			self.ui2.ui.lineEdit_11.setReadOnly(True)		
			self.ui2.ui.lineEdit_8.setReadOnly(True)		
			self.ui2.ui.lineEdit_9.setReadOnly(True)			
			self.ui2.ui.lineEdit_10.setReadOnly(True)	
			self.ui2.ui.lineEdit_16.setReadOnly(True)		#Engine Status's	
			self.ui2.ui.lineEdit_17.setReadOnly(True)	
			self.ui2.ui.lineEdit_18.setReadOnly(True)	
			self.ui2.ui.lineEdit_19.setReadOnly(True)		
			self.ui2.ui.lineEdit_20.setReadOnly(True)		
			self.ui2.ui.lineEdit_26.setReadOnly(True)		#Signal Pickup Status
		if(self.trainNum3 == 1):
			self.ui3.ui.label.setText(self.train3)
			self.ui3.ui.lineEdit_6.setReadOnly(True)		#Brake Status's
			self.ui3.ui.lineEdit_11.setReadOnly(True)		
			self.ui3.ui.lineEdit_8.setReadOnly(True)		
			self.ui3.ui.lineEdit_9.setReadOnly(True)			
			self.ui3.ui.lineEdit_10.setReadOnly(True)	
			self.ui3.ui.lineEdit_16.setReadOnly(True)		#Engine Status's	
			self.ui3.ui.lineEdit_17.setReadOnly(True)	
			self.ui3.ui.lineEdit_18.setReadOnly(True)	
			self.ui3.ui.lineEdit_19.setReadOnly(True)		
			self.ui3.ui.lineEdit_20.setReadOnly(True)		
			self.ui3.ui.lineEdit_26.setReadOnly(True)		#Signal Pickup Status
		if(self.trainNum4 == 1):
			self.ui4.ui.label.setText(self.train4)
			self.ui4.ui.lineEdit_6.setReadOnly(True)		#Brake Status's
			self.ui4.ui.lineEdit_11.setReadOnly(True)		
			self.ui4.ui.lineEdit_8.setReadOnly(True)		
			self.ui4.ui.lineEdit_9.setReadOnly(True)			
			self.ui4.ui.lineEdit_10.setReadOnly(True)	
			self.ui4.ui.lineEdit_16.setReadOnly(True)		#Engine Status's	
			self.ui4.ui.lineEdit_17.setReadOnly(True)	
			self.ui4.ui.lineEdit_18.setReadOnly(True)	
			self.ui4.ui.lineEdit_19.setReadOnly(True)		
			self.ui4.ui.lineEdit_20.setReadOnly(True)		
			self.ui4.ui.lineEdit_26.setReadOnly(True)		#Signal Pickup Status
		if(self.trainNum5 == 1):
			self.ui5.ui.label.setText(self.train5)
			self.ui5.ui.lineEdit_6.setReadOnly(True)		#Brake Status's
			self.ui5.ui.lineEdit_11.setReadOnly(True)		
			self.ui5.ui.lineEdit_8.setReadOnly(True)		
			self.ui5.ui.lineEdit_9.setReadOnly(True)			
			self.ui5.ui.lineEdit_10.setReadOnly(True)	
			self.ui5.ui.lineEdit_16.setReadOnly(True)		#Engine Status's	
			self.ui5.ui.lineEdit_17.setReadOnly(True)	
			self.ui5.ui.lineEdit_18.setReadOnly(True)	
			self.ui5.ui.lineEdit_19.setReadOnly(True)		
			self.ui5.ui.lineEdit_20.setReadOnly(True)		
			self.ui5.ui.lineEdit_26.setReadOnly(True)		#Signal Pickup Status
		if(self.trainNum6 == 1):
			self.ui6.ui.label.setText(self.train6)
			self.ui6.ui.lineEdit_6.setReadOnly(True)		#Brake Status's
			self.ui6.ui.lineEdit_11.setReadOnly(True)		
			self.ui6.ui.lineEdit_8.setReadOnly(True)		
			self.ui6.ui.lineEdit_9.setReadOnly(True)			
			self.ui6.ui.lineEdit_10.setReadOnly(True)	
			self.ui6.ui.lineEdit_16.setReadOnly(True)		#Engine Status's	
			self.ui6.ui.lineEdit_17.setReadOnly(True)	
			self.ui6.ui.lineEdit_18.setReadOnly(True)	
			self.ui6.ui.lineEdit_19.setReadOnly(True)		
			self.ui6.ui.lineEdit_20.setReadOnly(True)		
			self.ui6.ui.lineEdit_26.setReadOnly(True)		#Signal Pickup Status
		if(self.trainNum7 == 1):
			self.ui7.ui.label.setText(self.train7)
			self.ui7.ui.lineEdit_6.setReadOnly(True)		#Brake Status's
			self.ui7.ui.lineEdit_11.setReadOnly(True)		
			self.ui7.ui.lineEdit_8.setReadOnly(True)		
			self.ui7.ui.lineEdit_9.setReadOnly(True)			
			self.ui7.ui.lineEdit_10.setReadOnly(True)	
			self.ui7.ui.lineEdit_16.setReadOnly(True)		#Engine Status's	
			self.ui7.ui.lineEdit_17.setReadOnly(True)	
			self.ui7.ui.lineEdit_18.setReadOnly(True)	
			self.ui7.ui.lineEdit_19.setReadOnly(True)		
			self.ui7.ui.lineEdit_20.setReadOnly(True)		
			self.ui7.ui.lineEdit_26.setReadOnly(True)		#Signal Pickup Status
		if(self.trainNum8 == 1):
			self.ui8.ui.label.setText(self.train8)
			self.ui8.ui.lineEdit_6.setReadOnly(True)		#Brake Status's
			self.ui8.ui.lineEdit_11.setReadOnly(True)		
			self.ui8.ui.lineEdit_8.setReadOnly(True)		
			self.ui8.ui.lineEdit_9.setReadOnly(True)			
			self.ui8.ui.lineEdit_10.setReadOnly(True)	
			self.ui8.ui.lineEdit_16.setReadOnly(True)		#Engine Status's	
			self.ui8.ui.lineEdit_17.setReadOnly(True)	
			self.ui8.ui.lineEdit_18.setReadOnly(True)	
			self.ui8.ui.lineEdit_19.setReadOnly(True)		
			self.ui8.ui.lineEdit_20.setReadOnly(True)		
			self.ui8.ui.lineEdit_26.setReadOnly(True)		#Signal Pickup Status
		if(self.trainNum9 == 1):
			self.ui9.ui.label.setText(self.train9)
			self.ui9.ui.lineEdit_6.setReadOnly(True)		#Brake Status's
			self.ui9.ui.lineEdit_11.setReadOnly(True)		
			self.ui9.ui.lineEdit_8.setReadOnly(True)		
			self.ui9.ui.lineEdit_9.setReadOnly(True)			
			self.ui9.ui.lineEdit_10.setReadOnly(True)	
			self.ui9.ui.lineEdit_16.setReadOnly(True)		#Engine Status's	
			self.ui9.ui.lineEdit_17.setReadOnly(True)	
			self.ui9.ui.lineEdit_18.setReadOnly(True)	
			self.ui9.ui.lineEdit_19.setReadOnly(True)		
			self.ui9.ui.lineEdit_20.setReadOnly(True)		
			self.ui9.ui.lineEdit_26.setReadOnly(True)		#Signal Pickup Status
		if(self.trainNum10 == 1):
			self.ui10.ui.label.setText(self.train10)
			self.ui10.ui.lineEdit_6.setReadOnly(True)		#Brake Status's
			self.ui10.ui.lineEdit_11.setReadOnly(True)		
			self.ui10.ui.lineEdit_8.setReadOnly(True)		
			self.ui10.ui.lineEdit_9.setReadOnly(True)			
			self.ui10.ui.lineEdit_10.setReadOnly(True)	
			self.ui10.ui.lineEdit_16.setReadOnly(True)		#Engine Status's	
			self.ui10.ui.lineEdit_17.setReadOnly(True)	
			self.ui10.ui.lineEdit_18.setReadOnly(True)	
			self.ui10.ui.lineEdit_19.setReadOnly(True)		
			self.ui10.ui.lineEdit_20.setReadOnly(True)		
			self.ui10.ui.lineEdit_26.setReadOnly(True)		#Signal Pickup Status
			

#_______________________________________________________________________
	#function to delegate variables when Emergency Brake triggered
	def EmergencyBrakingTest(self):
		if(self.trainNum1 == 1 and self.eBrakeTest1 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest1, 1)
		if(self.trainNum2 == 1 and self.eBrakeTest2 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest2, 2)
		if(self.trainNum3 == 1 and self.eBrakeTest3 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest3, 3)
		if(self.trainNum4 == 1 and self.eBrakeTest4 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest4, 4)
		if(self.trainNum5 == 1 and self.eBrakeTest5 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest5, 5)
		if(self.trainNum6 == 1 and self.eBrakeTest6 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest6, 6)
		if(self.trainNum7 == 1 and self.eBrakeTest7 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest7, 7)
		if(self.trainNum8 == 1 and self.eBrakeTest8 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest8, 8)
		if(self.trainNum9 == 1 and self.eBrakeTest9 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest9, 9)
		if(self.trainNum10 == 1 and self.eBrakeTest10 == True):
			signals.tnm_ebrake.emit(self.eBrakeTest10, 10)				
			
#_______________________________________________________________________
	#function to set Emergency Brake from tnc
	def SetEBrakeTest(self, eBrakeTNC, tncTrainNum):
		if(self.trainNum1 == 1 and tncTrainNum == 1):
			self.eBrakeTest1 = eBrakeTNC
		elif(self.trainNum2 == 1 and tncTrainNum == 2):
			self.eBrakeTest2 = eBrakeTNC
		elif(self.trainNum3 == 1 and tncTrainNum == 3):
			self.eBrakeTest3 = eBrakeTNC
		elif(self.trainNum4 == 1 and tncTrainNum == 4):
			self.eBrakeTest4 = eBrakeTNC
		elif(self.trainNum5 == 1 and tncTrainNum == 5):
			self.eBrakeTest5 = eBrakeTNC
		elif(self.trainNum6 == 1 and tncTrainNum == 6):
			self.eBrakeTest6 = eBrakeTNC
		elif(self.trainNum7 == 1 and tncTrainNum == 7):
			self.eBrakeTest7 = eBrakeTNC
		elif(self.trainNum8 == 1 and tncTrainNum == 8):
			self.eBrakeTest8 = eBrakeTNC
		elif(self.trainNum9 == 1 and tncTrainNum == 9):
			self.eBrakeTest9 = eBrakeTNC
		elif(self.trainNum10 == 1 and tncTrainNum == 10):
			self.eBrakeTest10 = eBrakeTNC
		
#_______________________________________________________________________
	#function to address Brake Failure Status's
	def brake_fail_act(self):
		if(self.trainNum1 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui1.ui.lineEdit.text() == "Off" or self.ui1.ui.lineEdit.text() == "OFF" or self.ui1.ui.lineEdit.text() == "off"):	
				self.car1_status1 = True
				self.ui1.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False ,1)	
			elif(self.ui1.ui.lineEdit.text() == "On" or self.ui1.ui.lineEdit.text() == "ON" or self.ui1.ui.lineEdit.text() == "on"):
				self.car1_status1 = False	
				self.ui1.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True, 1)
			else:
				self.car1_status1 = True
				self.ui1.ui.lineEdit.setText("Off")
				self.ui1.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui1.ui.lineEdit_2.text() == "Off" or self.ui1.ui.lineEdit_2.text() == "OFF" or self.ui1.ui.lineEdit_2.text() == "off"):
				self.car2_status1 = True	
				self.ui1.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui1.ui.lineEdit_2.text() == "On" or self.ui1.ui.lineEdit_2.text() == "ON" or self.ui1.ui.lineEdit_2.text() == "on"):
				self.car2_status1 = False	
				self.ui1.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True,1)				
			else:
				self.car2_status1 = True
				self.ui1.ui.lineEdit_2.setText("Off")
				self.ui1.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui1.ui.lineEdit_3.text() == "Off" or self.ui1.ui.lineEdit_3.text() == "OFF" or self.ui1.ui.lineEdit_3.text() == "off"):		
				self.car3_status1 = True
				self.ui1.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui1.ui.lineEdit_3.text() == "On" or self.ui1.ui.lineEdit_3.text() == "ON" or self.ui1.ui.lineEdit_3.text() == "on"):
				self.car3_status1 = False
				self.ui1.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True		
				signals.tnm_sendyard.emit(True,1)			
			else:
				self.car3_status1 = True
				self.ui1.ui.lineEdit_3.setText("Off")
				self.ui1.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui1.ui.lineEdit_4.text() == "Off" or self.ui1.ui.lineEdit_4.text() == "OFF" or self.ui1.ui.lineEdit_4.text() == "off"):									
				self.car4_status1 = True
				self.ui1.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui1.ui.lineEdit_4.text() == "On" or self.ui1.ui.lineEdit_4.text() == "ON" or self.ui1.ui.lineEdit_4.text() == "on"):
				self.car4_status1 = False
				self.ui1.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True,1)							
			else:
				self.car4_status1 = True
				self.ui1.ui.lineEdit_4.setText("Off")
				self.ui1.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui1.ui.lineEdit_5.text() == "Off" or self.ui1.ui.lineEdit_5.text() == "OFF" or self.ui1.ui.lineEdit_5.text() == "off"):										
				self.car5_status1 = True
				self.ui1.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui1.ui.lineEdit_5.text() == "On" or self.ui1.ui.lineEdit_5.text() == "ON" or self.ui1.ui.lineEdit_5.text() == "on"):
				self.car5_status1 = False
				self.ui1.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True,1)					
			else:
				self.car5_status1 = True
				self.ui1.ui.lineEdit_5.setText("Off")
				self.ui1.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#_______________________________________________________________________
		if(self.trainNum2 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui2.ui.lineEdit.text() == "Off" or self.ui2.ui.lineEdit.text() == "OFF" or self.ui2.ui.lineEdit.text() == "off"):	
				self.car1_status2 = True
				self.ui2.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False ,2)	
			elif(self.ui2.ui.lineEdit.text() == "On" or self.ui2.ui.lineEdit.text() == "ON" or self.ui2.ui.lineEdit.text() == "on"):
				self.car1_status2 = False	
				self.ui2.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True, 2)
			else:
				self.car1_status2 = True
				self.ui2.ui.lineEdit.setText("Off")
				self.ui2.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui2.ui.lineEdit_2.text() == "Off" or self.ui2.ui.lineEdit_2.text() == "OFF" or self.ui2.ui.lineEdit_2.text() == "off"):
				self.car2_status2 = True	
				self.ui2.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui2.ui.lineEdit_2.text() == "On" or self.ui2.ui.lineEdit_2.text() == "ON" or self.ui2.ui.lineEdit_2.text() == "on"):
				self.car2_status2 = False	
				self.ui2.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True,2)				
			else:
				self.car2_status2 = True
				self.ui2.ui.lineEdit_2.setText("Off")
				self.ui2.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui2.ui.lineEdit_3.text() == "Off" or self.ui2.ui.lineEdit_3.text() == "OFF" or self.ui2.ui.lineEdit_3.text() == "off"):		
				self.car3_status2 = True
				self.ui2.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui2.ui.lineEdit_3.text() == "On" or self.ui2.ui.lineEdit_3.text() == "ON" or self.ui2.ui.lineEdit_3.text() == "on"):
				self.car3_status2 = False
				self.ui2.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True		
				signals.tnm_sendyard.emit(True,2)			
			else:
				self.car3_status2 = True
				self.ui2.ui.lineEdit_3.setText("Off")
				self.ui2.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui2.ui.lineEdit_4.text() == "Off" or self.ui2.ui.lineEdit_4.text() == "OFF" or self.ui2.ui.lineEdit_4.text() == "off"):									
				self.car4_status2 = True
				self.ui2.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui2.ui.lineEdit_4.text() == "On" or self.ui2.ui.lineEdit_4.text() == "ON" or self.ui2.ui.lineEdit_4.text() == "on"):
				self.car4_status2 = False
				self.ui2.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True,2)							
			else:
				self.car4_status2 = True
				self.ui2.ui.lineEdit_4.setText("Off")
				self.ui2.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui2.ui.lineEdit_5.text() == "Off" or self.ui2.ui.lineEdit_5.text() == "OFF" or self.ui2.ui.lineEdit_5.text() == "off"):										
				self.car5_status2 = True
				self.ui2.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui2.ui.lineEdit_5.text() == "On" or self.ui2.ui.lineEdit_5.text() == "ON" or self.ui2.ui.lineEdit_5.text() == "on"):
				self.car5_status2 = False
				self.ui2.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True,2)					
			else:
				self.car5_status2 = True
				self.ui2.ui.lineEdit_5.setText("Off")
				self.ui2.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#__________________________________________________________________
		if(self.trainNum3 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui3.ui.lineEdit.text() == "Off" or self.ui3.ui.lineEdit.text() == "OFF" or self.ui3.ui.lineEdit.text() == "off"):	
				self.car1_status3 = True
				self.ui3.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False ,3)	
			elif(self.ui3.ui.lineEdit.text() == "On" or self.ui3.ui.lineEdit.text() == "ON" or self.ui3.ui.lineEdit.text() == "on"):
				self.car1_status3 = False	
				self.ui3.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True, 3)
			else:
				self.car1_status3 = True
				self.ui3.ui.lineEdit.setText("Off")
				self.ui3.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui3.ui.lineEdit_2.text() == "Off" or self.ui3.ui.lineEdit_2.text() == "OFF" or self.ui3.ui.lineEdit_2.text() == "off"):
				self.car2_status3 = True	
				self.ui3.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui3.ui.lineEdit_2.text() == "On" or self.ui3.ui.lineEdit_2.text() == "ON" or self.ui3.ui.lineEdit_2.text() == "on"):
				self.car2_status3 = False	
				self.ui3.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True,3)				
			else:
				self.car2_status3 = True
				self.ui3.lineEdit_2.setText("Off")
				self.ui3.lineEdit_11.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui3.ui.lineEdit_3.text() == "Off" or self.ui3.ui.lineEdit_3.text() == "OFF" or self.ui3.ui.lineEdit_3.text() == "off"):		
				self.car3_status3 = True
				self.ui3.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui3.ui.lineEdit_3.text() == "On" or self.ui3.ui.lineEdit_3.text() == "ON" or self.ui3.ui.lineEdit_3.text() == "on"):
				self.car3_status3 = False
				self.ui3.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True		
				signals.tnm_sendyard.emit(True,3)			
			else:
				self.car3_status3 = True
				self.ui3.ui.lineEdit_3.setText("Off")
				self.ui3.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui3.ui.lineEdit_4.text() == "Off" or self.ui3.ui.lineEdit_4.text() == "OFF" or self.ui3.ui.lineEdit_4.text() == "off"):									
				self.car4_status3 = True
				self.ui3.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui3.ui.lineEdit_4.text() == "On" or self.ui3.ui.lineEdit_4.text() == "ON" or self.ui3.ui.lineEdit_4.text() == "on"):
				self.car4_status3 = False
				self.ui3.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True,3)							
			else:
				self.car4_status3 = True
				self.ui3.ui.lineEdit_4.setText("Off")
				self.ui3.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui3.ui.lineEdit_5.text() == "Off" or self.ui3.ui.lineEdit_5.text() == "OFF" or self.ui3.ui.lineEdit_5.text() == "off"):										
				self.car5_status3 = True
				self.ui3.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui3.ui.lineEdit_5.text() == "On" or self.ui3.ui.lineEdit_5.text() == "ON" or self.ui3.ui.lineEdit_5.text() == "on"):
				self.car5_status3 = False
				self.ui3.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True,3)					
			else:
				self.car5_status3 = True
				self.ui3.ui.lineEdit_5.setText("Off")
				self.ui3.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#_________________________________________________________________
		if(self.trainNum4 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui4.ui.lineEdit.text() == "Off" or self.ui4.ui.lineEdit.text() == "OFF" or self.ui4.ui.lineEdit.text() == "off"):	
				self.car1_status4 = True
				self.ui4.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False ,4)	
			elif(self.ui4.ui.lineEdit.text() == "On" or self.ui4.ui.lineEdit.text() == "ON" or self.ui4.ui.lineEdit.text() == "on"):
				self.car1_status4 = False	
				self.ui4.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True, 4)
			else:
				self.car1_status4 = True
				self.ui4.ui.lineEdit.setText("Off")
				self.ui4.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui4.ui.lineEdit_2.text() == "Off" or self.ui4.ui.lineEdit_2.text() == "OFF" or self.ui4.ui.lineEdit_2.text() == "off"):
				self.car2_status4 = True	
				self.ui4.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui4.ui.lineEdit_2.text() == "On" or self.ui4.ui.lineEdit_2.text() == "ON" or self.ui4.ui.lineEdit_2.text() == "on"):
				self.car2_status4 = False	
				self.ui4.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True,4)				
			else:
				self.car2_status4 = True
				self.ui4.ui.lineEdit_2.setText("Off")
				self.ui4.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui4.ui.lineEdit_3.text() == "Off" or self.ui4.ui.lineEdit_3.text() == "OFF" or self.ui4.ui.lineEdit_3.text() == "off"):		
				self.car3_status4 = True
				self.ui4.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui4.ui.lineEdit_3.text() == "On" or self.ui4.ui.lineEdit_3.text() == "ON" or self.ui4.ui.lineEdit_3.text() == "on"):
				self.car3_status4 = False
				self.ui4.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True		
				signals.tnm_sendyard.emit(True,4)			
			else:
				self.car3_status4 = True
				self.ui4.ui.lineEdit_3.setText("Off")
				self.ui4.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui4.ui.lineEdit_4.text() == "Off" or self.ui4.ui.lineEdit_4.text() == "OFF" or self.ui4.ui.lineEdit_4.text() == "off"):									
				self.car4_status4 = True
				self.ui4.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui4.ui.lineEdit_4.text() == "On" or self.ui4.ui.lineEdit_4.text() == "ON" or self.ui4.ui.lineEdit_4.text() == "on"):
				self.car4_status4 = False
				self.ui4.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True,4)							
			else:
				self.car4_status4 = True
				self.ui4.ui.lineEdit_4.setText("Off")
				self.ui4.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui4.ui.lineEdit_5.text() == "Off" or self.ui4.ui.lineEdit_5.text() == "OFF" or self.ui4.ui.lineEdit_5.text() == "off"):										
				self.car5_status4 = True
				self.ui4.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui4.ui.lineEdit_5.text() == "On" or self.ui4.ui.lineEdit_5.text() == "ON" or self.ui4.ui.lineEdit_5.text() == "on"):
				self.car5_status4 = False
				self.ui4.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True,4)					
			else:
				self.car5_status4 = True
				self.ui4.ui.lineEdit_5.setText("Off")
				self.ui4.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#__________________________________________________________________
		if(self.trainNum5 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui5.ui.lineEdit.text() == "Off" or self.ui5.ui.lineEdit.text() == "OFF" or self.ui5.ui.lineEdit.text() == "off"):	
				self.car1_status5 = True
				self.ui5.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False ,5)	
			elif(self.ui5.ui.lineEdit.text() == "On" or self.ui5.ui.lineEdit.text() == "ON" or self.ui5.ui.lineEdit.text() == "on"):
				self.car1_status5 = False	
				self.ui5.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True, 5)
			else:
				self.car1_status5 = True
				self.ui5.ui.lineEdit.setText("Off")
				self.ui5.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui5.ui.lineEdit_2.text() == "Off" or self.ui5.ui.lineEdit_2.text() == "OFF" or self.ui5.ui.lineEdit_2.text() == "off"):
				self.car2_status5 = True	
				self.ui5.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui5.ui.lineEdit_2.text() == "On" or self.ui5.ui.lineEdit_2.text() == "ON" or self.ui5.ui.lineEdit_2.text() == "on"):
				self.car2_status5 = False	
				self.ui5.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True,5)				
			else:
				self.car2_status5 = True
				self.ui5.ui.lineEdit_2.setText("Off")
				self.ui5.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui5.ui.lineEdit_3.text() == "Off" or self.ui5.ui.lineEdit_3.text() == "OFF" or self.ui5.ui.lineEdit_3.text() == "off"):		
				self.car3_status5 = True
				self.ui5.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui5.ui.lineEdit_3.text() == "On" or self.ui5.ui.lineEdit_3.text() == "ON" or self.ui.lineEdit_3.text() == "on"):
				self.car3_status5 = False
				self.ui5.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True		
				signals.tnm_sendyard.emit(True,5)			
			else:
				self.car3_status5 = True
				self.ui5.ui.lineEdit_3.setText("Off")
				self.ui5.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui5.ui.lineEdit_4.text() == "Off" or self.ui5.ui.lineEdit_4.text() == "OFF" or self.ui5.ui.lineEdit_4.text() == "off"):									
				self.car4_status5 = True
				self.ui5.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui5.ui.lineEdit_4.text() == "On" or self.ui5.ui.lineEdit_4.text() == "ON" or self.ui5.ui.lineEdit_4.text() == "on"):
				self.car4_status5 = False
				self.ui5.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True,5)							
			else:
				self.car4_status5 = True
				self.ui5.ui.lineEdit_4.setText("Off")
				self.ui5.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui5.ui.lineEdit_5.text() == "Off" or self.ui5.ui.lineEdit_5.text() == "OFF" or self.ui5.ui.lineEdit_5.text() == "off"):										
				self.car5_status5 = True
				self.ui5.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui5.ui.lineEdit_5.text() == "On" or self.ui5.ui.lineEdit_5.text() == "ON" or self.ui5.ui.lineEdit_5.text() == "on"):
				self.car5_status5 = False
				self.ui5.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True,5)					
			else:
				self.car5_status5 = True
				self.ui5.ui.lineEdit_5.setText("Off")
				self.ui5.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#___________________________________________________________________
		if(self.trainNum6 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui6.ui.lineEdit.text() == "Off" or self.ui6.ui.lineEdit.text() == "OFF" or self.ui6.ui.lineEdit.text() == "off"):	
				self.car1_status6 = True
				self.ui6.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False ,6)	
			elif(self.ui6.ui.lineEdit.text() == "On" or self.ui6.ui.lineEdit.text() == "ON" or self.ui6.ui.lineEdit.text() == "on"):
				self.car1_status6 = False	
				self.ui6.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True, 6)
			else:
				self.car1_status6 = True
				self.ui6.ui.lineEdit.setText("Off")
				self.ui6.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui6.ui.lineEdit_2.text() == "Off" or self.ui6.ui.lineEdit_2.text() == "OFF" or self.ui6.ui.lineEdit_2.text() == "off"):
				self.car2_status6 = True	
				self.ui6.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui6.ui.lineEdit_2.text() == "On" or self.ui6.ui.lineEdit_2.text() == "ON" or self.ui6.ui.lineEdit_2.text() == "on"):
				self.car2_status6 = False	
				self.ui6.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True,6)				
			else:
				self.car2_status6 = True
				self.ui6.ui.lineEdit_2.setText("Off")
				self.ui6.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui6.ui.lineEdit_3.text() == "Off" or self.ui6.ui.lineEdit_3.text() == "OFF" or self.ui6.ui.lineEdit_3.text() == "off"):		
				self.car3_status6 = True
				self.ui6.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui6.ui.lineEdit_3.text() == "On" or self.ui6.ui.lineEdit_3.text() == "ON" or self.ui6.ui.lineEdit_3.text() == "on"):
				self.car3_status6 = False
				self.ui6.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True		
				signals.tnm_sendyard.emit(True,6)			
			else:
				self.car3_status6 = True
				self.ui6.ui.lineEdit_3.setText("Off")
				self.ui6.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui6.ui.lineEdit_4.text() == "Off" or self.ui6.ui.lineEdit_4.text() == "OFF" or self.ui6.ui.lineEdit_4.text() == "off"):									
				self.car4_status6 = True
				self.ui6.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui6.ui.lineEdit_4.text() == "On" or self.ui6.ui.lineEdit_4.text() == "ON" or self.ui6.ui.lineEdit_4.text() == "on"):
				self.car4_status6 = False
				self.ui6.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True,6)							
			else:
				self.car4_status6 = True
				self.ui6.ui.lineEdit_4.setText("Off")
				self.ui6.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui6.ui.lineEdit_5.text() == "Off" or self.ui6.ui.lineEdit_5.text() == "OFF" or self.ui6.ui.lineEdit_5.text() == "off"):										
				self.car5_status6 = True
				self.ui6.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui6.ui.lineEdit_5.text() == "On" or self.ui6.ui.lineEdit_5.text() == "ON" or self.ui6.ui.lineEdit_5.text() == "on"):
				self.car5_status6 = False
				self.ui6.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True,6)					
			else:
				self.car5_status6 = True
				self.ui6.ui.lineEdit_5.setText("Off")
				self.ui6.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#______________________________________________________________________
		if(self.trainNum7 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui7.ui.lineEdit.text() == "Off" or self.ui7.ui.lineEdit.text() == "OFF" or self.ui7.ui.lineEdit.text() == "off"):	
				self.car1_status7 = True
				self.ui7.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False ,7)	
			elif(self.ui7.ui.lineEdit.text() == "On" or self.ui7.ui.lineEdit.text() == "ON" or self.ui7.ui.lineEdit.text() == "on"):
				self.car1_status7 = False	
				self.ui7.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)
			else:
				self.car1_status7 = True
				self.ui7.ui.lineEdit.setText("Off")
				self.ui7.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui7.ui.lineEdit_2.text() == "Off" or self.ui7.ui.lineEdit_2.text() == "OFF" or self.ui7.ui.lineEdit_2.text() == "off"):
				self.car2_status7 = True	
				self.ui7.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui7.ui.lineEdit_2.text() == "On" or self.ui7.ui.lineEdit_2.text() == "ON" or self.ui7.ui.lineEdit_2.text() == "on"):
				self.car2_status7 = False	
				self.ui7.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)				
			else:
				self.car2_status7 = True
				self.ui7.ui.lineEdit_2.setText("Off")
				self.ui7.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui7.ui.lineEdit_3.text() == "Off" or self.ui7.ui.lineEdit_3.text() == "OFF" or self.ui7.ui.lineEdit_3.text() == "off"):		
				self.car3_status7 = True
				self.ui7.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui7.ui.lineEdit_3.text() == "On" or self.ui7.ui.lineEdit_3.text() == "ON" or self.ui7.ui.lineEdit_3.text() == "on"):
				self.car3_status7 = False
				self.ui7.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True		
				signals.tnm_sendyard.emit(True,7)			
			else:
				self.car3_status7 = True
				self.ui7.ui.lineEdit_3.setText("Off")
				self.ui7.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui7.ui.lineEdit_4.text() == "Off" or self.ui7.ui.lineEdit_4.text() == "OFF" or self.ui7.ui.lineEdit_4.text() == "off"):									
				self.car4_status7 = True
				self.ui7.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui7.ui.lineEdit_4.text() == "On" or self.ui7.ui.lineEdit_4.text() == "ON" or self.ui7.ui.lineEdit_4.text() == "on"):
				self.car4_status7 = False
				self.ui7.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)							
			else:
				self.car4_status7 = True
				self.ui7.ui.lineEdit_4.setText("Off")
				self.ui7.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui7.ui.lineEdit_5.text() == "Off" or self.ui7.ui.lineEdit_5.text() == "OFF" or self.ui7.ui.lineEdit_5.text() == "off"):										
				self.car5_status7 = True
				self.ui7.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui7.ui.lineEdit_5.text() == "On" or self.ui7.ui.lineEdit_5.text() == "ON" or self.ui7.ui.lineEdit_5.text() == "on"):
				self.car5_status7 = False
				self.ui7.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)					
			else:
				self.car5_status7 = True
				self.ui7.ui.lineEdit_5.setText("Off")
				self.ui7.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#____________________________________________________________________
		if(self.trainNum8 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui8.ui.lineEdit.text() == "Off" or self.ui8.ui.lineEdit.text() == "OFF" or self.ui8.ui.lineEdit.text() == "off"):	
				self.car1_status8 = True
				self.ui8.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False ,8)	
			elif(self.ui8.ui.lineEdit.text() == "On" or self.ui8.ui.lineEdit.text() == "ON" or self.ui8.ui.lineEdit.text() == "on"):
				self.car1_status8 = False	
				self.ui8.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)
			else:
				self.car1_status8 = True
				self.ui8.ui.lineEdit.setText("Off")
				self.ui8.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui8.ui.lineEdit_2.text() == "Off" or self.ui8.ui.lineEdit_2.text() == "OFF" or self.ui8.ui.lineEdit_2.text() == "off"):
				self.car2_status8 = True	
				self.ui8.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui8.ui.lineEdit_2.text() == "On" or self.ui8.ui.lineEdit_2.text() == "ON" or self.ui8.ui.lineEdit_2.text() == "on"):
				self.car2_status8 = False	
				self.ui8.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)				
			else:
				self.car2_status8 = True
				self.ui8.ui.lineEdit_2.setText("Off")
				self.ui8.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui8.ui.lineEdit_3.text() == "Off" or self.ui8.ui.lineEdit_3.text() == "OFF" or self.ui8.ui.lineEdit_3.text() == "off"):		
				self.car3_status8 = True
				self.ui8.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui8.ui.lineEdit_3.text() == "On" or self.ui8.ui.lineEdit_3.text() == "ON" or self.ui8.ui.lineEdit_3.text() == "on"):
				self.car3_status8 = False
				self.ui8.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True		
				signals.tnm_sendyard.emit(True,8)			
			else:
				self.car3_status8 = True
				self.ui8.ui.lineEdit_3.setText("Off")
				self.ui8.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui8.ui.lineEdit_4.text() == "Off" or self.ui8.ui.lineEdit_4.text() == "OFF" or self.ui8.ui.lineEdit_4.text() == "off"):									
				self.car4_status8 = True
				self.ui8.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui8.ui.lineEdit_4.text() == "On" or self.ui8.ui.lineEdit_4.text() == "ON" or self.ui8.ui.lineEdit_4.text() == "on"):
				self.car4_status8 = False
				self.ui8.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)							
			else:
				self.car4_status8 = True
				self.ui8.ui.lineEdit_4.setText("Off")
				self.ui8.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui8.ui.lineEdit_5.text() == "Off" or self.ui8.ui.lineEdit_5.text() == "OFF" or self.ui8.ui.lineEdit_5.text() == "off"):										
				self.car5_status8 = True
				self.ui8.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui8.ui.lineEdit_5.text() == "On" or self.ui8.ui.lineEdit_5.text() == "ON" or self.ui8.ui.lineEdit_5.text() == "on"):
				self.car5_status8 = False
				self.ui8.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)					
			else:
				self.car5_status8 = True
				self.ui8.ui.lineEdit_5.setText("Off")
				self.ui8.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#__________________________________________________________________
		if(self.trainNum9 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui9.ui.lineEdit.text() == "Off" or self.ui9.ui.lineEdit.text() == "OFF" or self.ui9.ui.lineEdit.text() == "off"):	
				self.car1_status9 = True
				self.ui9.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False ,9)	
			elif(self.ui9.ui.lineEdit.text() == "On" or self.ui9.ui.lineEdit.text() == "ON" or self.ui9.ui.lineEdit.text() == "on"):
				self.car1_status9 = False	
				self.ui9.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest9 = True
				self.EmergencyBrakingTest()
				self.sendYard9 = True
				signals.tnm_sendyard.emit(True,9)
			else:
				self.car1_status9 = True
				self.ui9.ui.lineEdit.setText("Off")
				self.ui9.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui9.ui.lineEdit_2.text() == "Off" or self.ui9.ui.lineEdit_2.text() == "OFF" or self.ui9.ui.lineEdit_2.text() == "off"):
				self.car2_status9 = True	
				self.ui9.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			elif(self.ui9.ui.lineEdit_2.text() == "On" or self.ui9.ui.lineEdit_2.text() == "ON" or self.ui9.ui.lineEdit_2.text() == "on"):
				self.car2_status9 = False	
				self.ui9.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest9 = True
				self.EmergencyBrakingTest()
				self.sendYard9 = True
				signals.tnm_sendyard.emit(True,9)				
			else:
				self.car2_status9 = True
				self.ui9.ui.lineEdit_2.setText("Off")
				self.ui9.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui9.ui.lineEdit_3.text() == "Off" or self.ui9.ui.lineEdit_3.text() == "OFF" or self.ui9.ui.lineEdit_3.text() == "off"):		
				self.car3_status9 = True
				self.ui9.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			elif(self.ui9.ui.lineEdit_3.text() == "On" or self.ui9.ui.lineEdit_3.text() == "ON" or self.ui9.ui.lineEdit_3.text() == "on"):
				self.car3_status9 = False
				self.ui9.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest9 = True
				self.EmergencyBrakingTest()
				self.sendYard9 = True		
				signals.tnm_sendyard.emit(True,9)			
			else:
				self.car3_status9 = True
				self.ui9.ui.lineEdit_3.setText("Off")
				self.ui9.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui9.ui.lineEdit_4.text() == "Off" or self.ui9.ui.lineEdit_4.text() == "OFF" or self.ui9.ui.lineEdit_4.text() == "off"):									
				self.car4_status9 = True
				self.ui9.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			elif(self.ui9.ui.lineEdit_4.text() == "On" or self.ui9.ui.lineEdit_4.text() == "ON" or self.ui9.ui.lineEdit_4.text() == "on"):
				self.car4_status9 = False
				self.ui9.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest9 = True
				self.EmergencyBrakingTest()
				self.sendYard9 = True
				signals.tnm_sendyard.emit(True,9)							
			else:
				self.car4_status9 = True
				self.ui9.ui.lineEdit_4.setText("Off")
				self.ui9.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui9.ui.lineEdit_5.text() == "Off" or self.ui9.ui.lineEdit_5.text() == "OFF" or self.ui9.ui.lineEdit_5.text() == "off"):										
				self.car5_status9 = True
				self.ui9.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			elif(self.ui9.ui.lineEdit_5.text() == "On" or self.ui9.ui.lineEdit_5.text() == "ON" or self.ui9.ui.lineEdit_5.text() == "on"):
				self.car5_status9 = False
				self.ui9.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest9 = True
				self.EmergencyBrakingTest()
				self.sendYard9 = True
				signals.tnm_sendyard.emit(True,9)					
			else:
				self.car5_status9 = True
				self.ui9.ui.lineEdit_5.setText("Off")
				self.ui9.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#____________________________________________________________________
		if(self.trainNum10 == 1):
			#Car 1 Status Change
			#True means brake 1 is functional
			if(self.ui10.ui.lineEdit.text() == "Off" or self.ui10.ui.lineEdit.text() == "OFF" or self.ui10.ui.lineEdit.text() == "off"):	
				self.car1_status10 = True
				self.ui10.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False ,10)	
			elif(self.ui10.ui.lineEdit.text() == "On" or self.ui10.ui.lineEdit.text() == "ON" or self.ui10.ui.lineEdit.text() == "on"):
				self.car1_status10 = False	
				self.ui10.ui.lineEdit_6.setText("Broken")
				self.eBrakeTest10 = True
				self.EmergencyBrakingTest()
				self.sendYard10 = True
				signals.tnm_sendyard.emit(True,10)
			else:
				self.car1_status10 = True
				self.ui10.ui.lineEdit.setText("Off")
				self.ui10.ui.lineEdit_6.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
				
			#Car 2 Status Change
			#True means brake 2 is functional
			if(self.ui10.ui.lineEdit_2.text() == "Off" or self.ui10.ui.lineEdit_2.text() == "OFF" or self.ui10.ui.lineEdit_2.text() == "off"):
				self.car2_status10 = True	
				self.ui10.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			elif(self.ui10.ui.lineEdit_2.text() == "On" or self.ui10.ui.lineEdit_2.text() == "ON" or self.ui10.ui.lineEdit_2.text() == "on"):
				self.car2_status10 = False	
				self.ui10.ui.lineEdit_11.setText("Broken")
				self.eBrakeTest10 = True
				self.EmergencyBrakingTest()
				self.sendYard10 = True
				signals.tnm_sendyard.emit(True,10)				
			else:
				self.car2_status10 = True
				self.ui10.ui.lineEdit_2.setText("Off")
				self.ui10.ui.lineEdit_11.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			
			#Car 3 Status Change
			#True means brake 3 is functional
			if(self.ui10.ui.lineEdit_3.text() == "Off" or self.ui10.ui.lineEdit_3.text() == "OFF" or self.ui10.ui.lineEdit_3.text() == "off"):		
				self.car3_status10 = True
				self.ui10.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			elif(self.ui10.ui.lineEdit_3.text() == "On" or self.ui10.ui.lineEdit_3.text() == "ON" or self.ui10.ui.lineEdit_3.text() == "on"):
				self.car3_status10 = False
				self.ui10.ui.lineEdit_8.setText("Broken")
				self.eBrakeTest10 = True
				self.EmergencyBrakingTest()
				self.sendYard10 = True		
				signals.tnm_sendyard.emit(True,10)			
			else:
				self.car3_status10 = True
				self.ui10.ui.lineEdit_3.setText("Off")
				self.ui10.ui.lineEdit_8.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
				
			#Car 4 Status Change
			#True means brake 4 is functional
			if(self.ui10.ui.lineEdit_4.text() == "Off" or self.ui10.ui.lineEdit_4.text() == "OFF" or self.ui10.ui.lineEdit_4.text() == "off"):									
				self.car4_status10 = True
				self.ui10.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			elif(self.ui10.ui.lineEdit_4.text() == "On" or self.ui10.ui.lineEdit_4.text() == "ON" or self.ui10.ui.lineEdit_4.text() == "on"):
				self.car4_status10 = False
				self.ui10.ui.lineEdit_9.setText("Broken")
				self.eBrakeTest10 = True
				self.EmergencyBrakingTest()
				self.sendYard10 = True
				signals.tnm_sendyard.emit(True,10)							
			else:
				self.car4_status10 = True
				self.ui10.ui.lineEdit_4.setText("Off")
				self.ui10.ui.lineEdit_9.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			
			#Car 5 Status Change
			#True means brake 5 is functional
			if(self.ui10.ui.lineEdit_5.text() == "Off" or self.ui10.ui.lineEdit_5.text() == "OFF" or self.ui10.ui.lineEdit_5.text() == "off"):										
				self.car5_status10 = True
				self.ui10.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			elif(self.ui10.ui.lineEdit_5.text() == "On" or self.ui10.ui.lineEdit_5.text() == "ON" or self.ui10.ui.lineEdit_5.text() == "on"):
				self.car5_status10 = False
				self.ui10.ui.lineEdit_10.setText("Broken")
				self.eBrakeTest10 = True
				self.EmergencyBrakingTest()
				self.sendYard10 = True
				signals.tnm_sendyard.emit(True,10)					
			else:
				self.car5_status10 = True
				self.ui10.ui.lineEdit_5.setText("Off")
				self.ui10.ui.lineEdit_10.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#____________________________________________________________________
#_______________________________________________________________________
	#function to address Engine Failure Status's
	def engine_fail_act(self):
		if(self.trainNum1 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui1.ui.lineEdit_7.text() == "Off" or self.ui1.ui.lineEdit_7.text() == "OFF" or self.ui1.ui.lineEdit_7.text() == "off"):	
				self.car1_status1 = True
				self.ui1.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui1.ui.lineEdit_7.text() == "On" or self.ui1.ui.lineEdit_7.text() == "ON" or self.ui1.ui.lineEdit_7.text() == "on"):
				self.car1_status1 = False	
				self.ui1.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True,1)				
			else:
				self.car1_status1 = True
				self.ui1.ui.lineEdit_7.setText("Off")
				self.ui1.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui1.ui.lineEdit_12.text() == "Off" or self.ui1.ui.lineEdit_12.text() == "OFF" or self.ui1.ui.lineEdit_12.text() == "off"):
				self.car2_status1 = True	
				self.ui1.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui1.ui.lineEdit_12.text() == "On" or self.ui1.ui.lineEdit_12.text() == "ON" or self.ui1.ui.lineEdit_12.text() == "on"):
				self.car2_status1 = False	
				self.ui1.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True	
				signals.tnm_sendyard.emit(True,1)				
			else:
				self.car2_status1 = True
				self.ui1.ui.lineEdit_12.setText("Off")
				self.ui1.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui1.ui.lineEdit_13.text() == "Off" or self.ui1.ui.lineEdit_13.text() == "OFF" or self.ui1.ui.lineEdit_13.text() == "off"):		
				self.car3_status1 = True
				self.ui1.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui1.ui.lineEdit_13.text() == "On" or self.ui1.ui.lineEdit_13.text() == "ON" or self.ui1.ui.lineEdit_13.text() == "on"):
				self.car3_status1 = False
				self.ui1.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True,1)					
			else:
				self.car3_status1 = True
				self.ui1.ui.lineEdit_13.setText("Off")
				self.ui1.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui1.ui.lineEdit_14.text() == "Off" or self.ui1.ui.lineEdit_14.text() == "OFF" or self.ui1.ui.lineEdit_14.text() == "off"):									
				self.car4_status1 = True
				self.ui1.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui1.ui.lineEdit_14.text() == "On" or self.ui1.ui.lineEdit_14.text() == "ON" or self.ui1.ui.lineEdit_14.text() == "on"):
				self.car4_status1 = False
				self.ui1.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True,1)					
			else:
				self.car4_status1 = True
				self.ui1.ui.lineEdit_14.setText("Off")
				self.ui1.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui1.ui.lineEdit_15.text() == "Off" or self.ui1.ui.lineEdit_15.text() == "OFF" or self.ui1.ui.lineEdit_15.text() == "off"):										
				self.car5_status1 = True
				self.ui1.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui1.ui.lineEdit_15.text() == "On" or self.ui1.ui.lineEdit_15.text() == "ON" or self.ui1.ui.lineEdit_15.text() == "on"):
				self.car5_status1 = False
				self.ui1.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True,1)					
			else:
				self.car5_status1 = True
				self.ui1.ui.lineEdit_15.setText("Off")
				self.ui1.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#__________________________________________________________________
		if(self.trainNum2 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui2.ui.lineEdit_7.text() == "Off" or self.ui2.ui.lineEdit_7.text() == "OFF" or self.ui2.ui.lineEdit_7.text() == "off"):	
				self.car1_status2 = True
				self.ui2.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui2.ui.lineEdit_7.text() == "On" or self.ui2.ui.lineEdit_7.text() == "ON" or self.ui2.ui.lineEdit_7.text() == "on"):
				self.car1_status2 = False	
				self.ui2.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True,2)				
			else:
				self.car1_status2 = True
				self.ui2.ui.lineEdit_7.setText("Off")
				self.ui2.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui2.ui.lineEdit_12.text() == "Off" or self.ui2.ui.lineEdit_12.text() == "OFF" or self.ui2.ui.lineEdit_12.text() == "off"):
				self.car2_status2 = True	
				self.ui2.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui2.ui.lineEdit_12.text() == "On" or self.ui2.ui.lineEdit_12.text() == "ON" or self.ui2.ui.lineEdit_12.text() == "on"):
				self.car2_status2 = False	
				self.ui2.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True	
				signals.tnm_sendyard.emit(True,2)				
			else:
				self.car2_status2 = True
				self.ui2.ui.lineEdit_12.setText("Off")
				self.ui2.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui2.ui.lineEdit_13.text() == "Off" or self.ui2.ui.lineEdit_13.text() == "OFF" or self.ui2.ui.lineEdit_13.text() == "off"):		
				self.car3_status2 = True
				self.ui2.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui2.ui.lineEdit_13.text() == "On" or self.ui2.ui.lineEdit_13.text() == "ON" or self.ui2.ui.lineEdit_13.text() == "on"):
				self.car3_status2 = False
				self.ui2.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True,2)					
			else:
				self.car3_status2 = True
				self.ui2.ui.lineEdit_13.setText("Off")
				self.ui2.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui2.ui.lineEdit_14.text() == "Off" or self.ui2.ui.lineEdit_14.text() == "OFF" or self.ui2.ui.lineEdit_14.text() == "off"):									
				self.car4_status2 = True
				self.ui2.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui2.ui.lineEdit_14.text() == "On" or self.ui2.ui.lineEdit_14.text() == "ON" or self.ui2.ui.lineEdit_14.text() == "on"):
				self.car4_status2 = False
				self.ui2.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True,2)					
			else:
				self.car4_status2 = True
				self.ui2.ui.lineEdit_14.setText("Off")
				self.ui2.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui2.ui.lineEdit_15.text() == "Off" or self.ui2.ui.lineEdit_15.text() == "OFF" or self.ui2.ui.lineEdit_15.text() == "off"):										
				self.car5_status2 = True
				self.ui2.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui2.ui.lineEdit_15.text() == "On" or self.ui2.ui.lineEdit_15.text() == "ON" or self.ui2.ui.lineEdit_15.text() == "on"):
				self.car5_status2 = False
				self.ui2.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True,2)					
			else:
				self.car5_status2 = True
				self.ui2.ui.lineEdit_15.setText("Off")
				self.ui2.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#____________________________________________________________________
		if(self.trainNum3 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui3.ui.lineEdit_7.text() == "Off" or self.ui3.ui.lineEdit_7.text() == "OFF" or self.ui3.ui.lineEdit_7.text() == "off"):	
				self.car1_status3 = True
				self.ui3.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui3.ui.lineEdit_7.text() == "On" or self.ui3.ui.lineEdit_7.text() == "ON" or self.ui3.ui.lineEdit_7.text() == "on"):
				self.car1_status3 = False	
				self.ui3.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True,3)				
			else:
				self.car1_status3 = True
				self.ui3.ui.lineEdit_7.setText("Off")
				self.ui3.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui3.ui.lineEdit_12.text() == "Off" or self.ui3.ui.lineEdit_12.text() == "OFF" or self.ui3.ui.lineEdit_12.text() == "off"):
				self.car2_status3 = True	
				self.ui3.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui3.ui.lineEdit_12.text() == "On" or self.ui3.ui.lineEdit_12.text() == "ON" or self.ui3.ui.lineEdit_12.text() == "on"):
				self.car2_status3 = False	
				self.ui3.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True	
				signals.tnm_sendyard.emit(True,3)				
			else:
				self.car2_status3 = True
				self.ui3.ui.lineEdit_12.setText("Off")
				self.ui3.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui3.ui.lineEdit_13.text() == "Off" or self.ui3.ui.lineEdit_13.text() == "OFF" or self.ui3.ui.lineEdit_13.text() == "off"):		
				self.car3_status3 = True
				self.ui3.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui3.ui.lineEdit_13.text() == "On" or self.ui3.ui.lineEdit_13.text() == "ON" or self.ui3.ui.lineEdit_13.text() == "on"):
				self.car3_status3 = False
				self.ui3.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True,3)					
			else:
				self.car3_status3 = True
				self.ui3.ui.lineEdit_13.setText("Off")
				self.ui3.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui3.ui.lineEdit_14.text() == "Off" or self.ui3.ui.lineEdit_14.text() == "OFF" or self.ui3.ui.lineEdit_14.text() == "off"):									
				self.car4_status3 = True
				self.ui3.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui3.ui.lineEdit_14.text() == "On" or self.ui3.ui.lineEdit_14.text() == "ON" or self.ui3.ui.lineEdit_14.text() == "on"):
				self.car4_status3 = False
				self.ui3.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True,3)					
			else:
				self.car4_status3 = True
				self.ui3.ui.lineEdit_14.setText("Off")
				self.ui3.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui3.ui.lineEdit_15.text() == "Off" or self.ui3.ui.lineEdit_15.text() == "OFF" or self.ui3.ui.lineEdit_15.text() == "off"):										
				self.car5_status3 = True
				self.ui3.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui3.ui.lineEdit_15.text() == "On" or self.ui3.ui.lineEdit_15.text() == "ON" or self.ui3.ui.lineEdit_15.text() == "on"):
				self.car5_status3 = False
				self.ui3.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True,3)					
			else:
				self.car5_status3 = True
				self.ui3.ui.lineEdit_15.setText("Off")
				self.ui3.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#__________________________________________________________________
		if(self.trainNum4 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui4.ui.lineEdit_7.text() == "Off" or self.ui4.ui.lineEdit_7.text() == "OFF" or self.ui4.ui.lineEdit_7.text() == "off"):	
				self.car1_status4 = True
				self.ui4.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui4.ui.lineEdit_7.text() == "On" or self.ui4.ui.lineEdit_7.text() == "ON" or self.ui4.ui.lineEdit_7.text() == "on"):
				self.car1_status4 = False	
				self.ui4.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True,4)				
			else:
				self.car1_status4 = True
				self.ui4.ui.lineEdit_7.setText("Off")
				self.ui4.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui4.ui.lineEdit_12.text() == "Off" or self.ui4.ui.lineEdit_12.text() == "OFF" or self.ui4.ui.lineEdit_12.text() == "off"):
				self.car2_status4 = True	
				self.ui4.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui4.ui.lineEdit_12.text() == "On" or self.ui4.ui.lineEdit_12.text() == "ON" or self.ui4.ui.lineEdit_12.text() == "on"):
				self.car2_status4 = False	
				self.ui4.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True	
				signals.tnm_sendyard.emit(True,4)				
			else:
				self.car2_status4 = True
				self.ui4.ui.lineEdit_12.setText("Off")
				self.ui4.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui4.ui.lineEdit_13.text() == "Off" or self.ui4.ui.lineEdit_13.text() == "OFF" or self.ui4.ui.lineEdit_13.text() == "off"):		
				self.car3_status4 = True
				self.ui4.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui4.ui.lineEdit_13.text() == "On" or self.ui4.ui.lineEdit_13.text() == "ON" or self.ui4.ui.lineEdit_13.text() == "on"):
				self.car3_status4 = False
				self.ui4.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True,4)					
			else:
				self.car3_status4 = True
				self.ui4.ui.lineEdit_13.setText("Off")
				self.ui4.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui4.ui.lineEdit_14.text() == "Off" or self.ui4.ui.lineEdit_14.text() == "OFF" or self.ui4.ui.lineEdit_14.text() == "off"):									
				self.car4_status4 = True
				self.ui4.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui4.ui.lineEdit_14.text() == "On" or self.ui4.ui.lineEdit_14.text() == "ON" or self.ui4.ui.lineEdit_14.text() == "on"):
				self.car4_status4 = False
				self.ui4.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True,4)					
			else:
				self.car4_status4 = True
				self.ui4.ui.lineEdit_14.setText("Off")
				self.ui4.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui4.ui.lineEdit_15.text() == "Off" or self.ui4.ui.lineEdit_15.text() == "OFF" or self.ui4.ui.lineEdit_15.text() == "off"):										
				self.car5_status4 = True
				self.ui4.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui4.ui.lineEdit_15.text() == "On" or self.ui4.ui.lineEdit_15.text() == "ON" or self.ui4.ui.lineEdit_15.text() == "on"):
				self.car5_status4 = False
				self.ui4.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True,4)					
			else:
				self.car5_status4 = True
				self.ui4.ui.lineEdit_15.setText("Off")
				self.ui4.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#____________________________________________________________________
		if(self.trainNum5 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui5.ui.lineEdit_7.text() == "Off" or self.ui5.ui.lineEdit_7.text() == "OFF" or self.ui5.ui.lineEdit_7.text() == "off"):	
				self.car1_status5 = True
				self.ui5.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui5.ui.lineEdit_7.text() == "On" or self.ui5.ui.lineEdit_7.text() == "ON" or self.ui5.ui.lineEdit_7.text() == "on"):
				self.car1_status5 = False	
				self.ui5.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True,5)				
			else:
				self.car1_status5 = True
				self.ui5.ui.lineEdit_7.setText("Off")
				self.ui5.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui5.ui.lineEdit_12.text() == "Off" or self.ui5.ui.lineEdit_12.text() == "OFF" or self.ui5.ui.lineEdit_12.text() == "off"):
				self.car2_status5 = True	
				self.ui5.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui5.ui.lineEdit_12.text() == "On" or self.ui5.ui.lineEdit_12.text() == "ON" or self.ui5.ui.lineEdit_12.text() == "on"):
				self.car2_status5 = False	
				self.ui5.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True	
				signals.tnm_sendyard.emit(True,5)				
			else:
				self.car2_status5 = True
				self.ui5.ui.lineEdit_12.setText("Off")
				self.ui5.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui5.ui.lineEdit_13.text() == "Off" or self.ui5.ui.lineEdit_13.text() == "OFF" or self.ui5.ui.lineEdit_13.text() == "off"):		
				self.car3_status5 = True
				self.ui5.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui5.ui.lineEdit_13.text() == "On" or self.ui5.ui.lineEdit_13.text() == "ON" or self.ui5.ui.lineEdit_13.text() == "on"):
				self.car3_status5 = False
				self.ui5.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True,5)					
			else:
				self.car3_status5 = True
				self.ui5.ui.lineEdit_13.setText("Off")
				self.ui5.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui5.ui.lineEdit_14.text() == "Off" or self.ui5.ui.lineEdit_14.text() == "OFF" or self.ui5.ui.lineEdit_14.text() == "off"):									
				self.car4_status5 = True
				self.ui5.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui5.ui.lineEdit_14.text() == "On" or self.ui5.ui.lineEdit_14.text() == "ON" or self.ui5.ui.lineEdit_14.text() == "on"):
				self.car4_status5 = False
				self.ui5.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True,5)					
			else:
				self.car4_status5 = True
				self.ui5.ui.lineEdit_14.setText("Off")
				self.ui5.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui5.ui.lineEdit_15.text() == "Off" or self.ui5.ui.lineEdit_15.text() == "OFF" or self.ui5.ui.lineEdit_15.text() == "off"):										
				self.car5_status5 = True
				self.ui5.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui5.ui.lineEdit_15.text() == "On" or self.ui5.ui.lineEdit_15.text() == "ON" or self.ui5.ui.lineEdit_15.text() == "on"):
				self.car5_status5 = False
				self.ui5.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True,5)					
			else:
				self.car5_status5 = True
				self.ui5.ui.lineEdit_15.setText("Off")
				self.ui5.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#____________________________________________________________________
		if(self.trainNum6 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui6.ui.lineEdit_7.text() == "Off" or self.ui6.ui.lineEdit_7.text() == "OFF" or self.ui6.ui.lineEdit_7.text() == "off"):	
				self.car1_status6 = True
				self.ui6.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui6.ui.lineEdit_7.text() == "On" or self.ui6.ui.lineEdit_7.text() == "ON" or self.ui6.ui.lineEdit_7.text() == "on"):
				self.car1_status6 = False	
				self.ui6.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True,6)				
			else:
				self.car1_status6 = True
				self.ui6.ui.lineEdit_7.setText("Off")
				self.ui6.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui6.ui.lineEdit_12.text() == "Off" or self.ui6.ui.lineEdit_12.text() == "OFF" or self.ui6.ui.lineEdit_12.text() == "off"):
				self.car2_status6 = True	
				self.ui6.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui6.ui.lineEdit_12.text() == "On" or self.ui6.ui.lineEdit_12.text() == "ON" or self.ui6.ui.lineEdit_12.text() == "on"):
				self.car2_status6 = False	
				self.ui6.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True	
				signals.tnm_sendyard.emit(True,6)				
			else:
				self.car2_status6 = True
				self.ui6.ui.lineEdit_12.setText("Off")
				self.ui6.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui6.ui.lineEdit_13.text() == "Off" or self.ui6.ui.lineEdit_13.text() == "OFF" or self.ui6.ui.lineEdit_13.text() == "off"):		
				self.car3_status6 = True
				self.ui6.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui6.ui.lineEdit_13.text() == "On" or self.ui6.ui.lineEdit_13.text() == "ON" or self.ui6.ui.lineEdit_13.text() == "on"):
				self.car3_status6 = False
				self.ui6.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True,6)					
			else:
				self.car3_status6 = True
				self.ui6.ui.lineEdit_13.setText("Off")
				self.ui6.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui6.ui.lineEdit_14.text() == "Off" or self.ui6.ui.lineEdit_14.text() == "OFF" or self.ui6.ui.lineEdit_14.text() == "off"):									
				self.car4_status6 = True
				self.ui6.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui6.ui.lineEdit_14.text() == "On" or self.ui6.ui.lineEdit_14.text() == "ON" or self.ui6.ui.lineEdit_14.text() == "on"):
				self.car4_status6 = False
				self.ui6.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True,6)					
			else:
				self.car4_status6 = True
				self.ui6.ui.lineEdit_14.setText("Off")
				self.ui6.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui6.ui.lineEdit_15.text() == "Off" or self.ui6.ui.lineEdit_15.text() == "OFF" or self.ui6.ui.lineEdit_15.text() == "off"):										
				self.car5_status6 = True
				self.ui6.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui6.ui.lineEdit_15.text() == "On" or self.ui6.ui.lineEdit_15.text() == "ON" or self.ui6.ui.lineEdit_15.text() == "on"):
				self.car5_status6 = False
				self.ui6.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True,6)					
			else:
				self.car5_status6 = True
				self.ui6.ui.lineEdit_15.setText("Off")
				self.ui6.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#_____________________________________________________________________
		if(self.trainNum7 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui7.ui.lineEdit_7.text() == "Off" or self.ui7.ui.lineEdit_7.text() == "OFF" or self.ui7.ui.lineEdit_7.text() == "off"):	
				self.car1_status7 = True
				self.ui7.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui7.ui.lineEdit_7.text() == "On" or self.ui7.ui.lineEdit_7.text() == "ON" or self.ui7.ui.lineEdit_7.text() == "on"):
				self.car1_status7 = False	
				self.ui7.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)				
			else:
				self.car1_status7 = True
				self.ui7.ui.lineEdit_7.setText("Off")
				self.ui7.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui7.ui.lineEdit_12.text() == "Off" or self.ui7.ui.lineEdit_12.text() == "OFF" or self.ui7.ui.lineEdit_12.text() == "off"):
				self.car2_status7 = True	
				self.ui7.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui7.ui.lineEdit_12.text() == "On" or self.ui7.ui.lineEdit_12.text() == "ON" or self.ui7.ui.lineEdit_12.text() == "on"):
				self.car2_status7 = False	
				self.ui7.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True	
				signals.tnm_sendyard.emit(True,7)				
			else:
				self.car2_status7 = True
				self.ui7.ui.lineEdit_12.setText("Off")
				self.ui7.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui7.ui.lineEdit_13.text() == "Off" or self.ui7.ui.lineEdit_13.text() == "OFF" or self.ui7.ui.lineEdit_13.text() == "off"):		
				self.car3_status7 = True
				self.ui7.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui7.ui.lineEdit_13.text() == "On" or self.ui7.ui.lineEdit_13.text() == "ON" or self.ui7.ui.lineEdit_13.text() == "on"):
				self.car3_status7 = False
				self.ui7.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)					
			else:
				self.car3_status7 = True
				self.ui7.ui.lineEdit_13.setText("Off")
				self.ui7.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui7.ui.lineEdit_14.text() == "Off" or self.ui7.ui.lineEdit_14.text() == "OFF" or self.ui7.ui.lineEdit_14.text() == "off"):									
				self.car4_status7 = True
				self.ui7.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui7.ui.lineEdit_14.text() == "On" or self.ui7.ui.lineEdit_14.text() == "ON" or self.ui7.ui.lineEdit_14.text() == "on"):
				self.car4_status7 = False
				self.ui7.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)					
			else:
				self.car4_status7 = True
				self.ui7.ui.lineEdit_14.setText("Off")
				self.ui7.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui7.ui.lineEdit_15.text() == "Off" or self.ui7.ui.lineEdit_15.text() == "OFF" or self.ui7.ui.lineEdit_15.text() == "off"):										
				self.car5_status7 = True
				self.ui7.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui7.ui.lineEdit_15.text() == "On" or self.ui7.ui.lineEdit_15.text() == "ON" or self.ui7.ui.lineEdit_15.text() == "on"):
				self.car5_status7 = False
				self.ui7.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)					
			else:
				self.car5_status7 = True
				self.ui7.ui.lineEdit_15.setText("Off")
				self.ui7.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#__________________________________________________________________
		if(self.trainNum8 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui8.ui.lineEdit_7.text() == "Off" or self.ui8.ui.lineEdit_7.text() == "OFF" or self.ui8.ui.lineEdit_7.text() == "off"):	
				self.car1_status8 = True
				self.ui8.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui8.ui.lineEdit_7.text() == "On" or self.ui8.ui.lineEdit_7.text() == "ON" or self.ui8.ui.lineEdit_7.text() == "on"):
				self.car1_status8 = False	
				self.ui8.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)				
			else:
				self.car1_status8 = True
				self.ui8.ui.lineEdit_7.setText("Off")
				self.ui8.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui8.ui.lineEdit_12.text() == "Off" or self.ui8.ui.lineEdit_12.text() == "OFF" or self.ui8.ui.lineEdit_12.text() == "off"):
				self.car2_status8 = True	
				self.ui8.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui8.ui.lineEdit_12.text() == "On" or self.ui8.ui.lineEdit_12.text() == "ON" or self.ui8.ui.lineEdit_12.text() == "on"):
				self.car2_status8 = False	
				self.ui8.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True	
				signals.tnm_sendyard.emit(True,8)				
			else:
				self.car2_status8 = True
				self.ui8.ui.lineEdit_12.setText("Off")
				self.ui8.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui8.ui.lineEdit_13.text() == "Off" or self.ui8.ui.lineEdit_13.text() == "OFF" or self.ui8.ui.lineEdit_13.text() == "off"):		
				self.car3_status8 = True
				self.ui8.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui8.ui.lineEdit_13.text() == "On" or self.ui8.ui.lineEdit_13.text() == "ON" or self.ui8.ui.lineEdit_13.text() == "on"):
				self.car3_status8 = False
				self.ui8.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)					
			else:
				self.car3_status8 = True
				self.ui8.ui.lineEdit_13.setText("Off")
				self.ui8.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui8.ui.lineEdit_14.text() == "Off" or self.ui8.ui.lineEdit_14.text() == "OFF" or self.ui8.ui.lineEdit_14.text() == "off"):									
				self.ui8.car4_status8 = True
				self.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui8.ui.lineEdit_14.text() == "On" or self.ui8.ui.lineEdit_14.text() == "ON" or self.ui8.ui.lineEdit_14.text() == "on"):
				self.car4_status8 = False
				self.ui8.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)					
			else:
				self.car4_status8 = True
				self.ui8.ui.lineEdit_14.setText("Off")
				self.ui8.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui8.ui.lineEdit_15.text() == "Off" or self.ui8.ui.lineEdit_15.text() == "OFF" or self.ui8.ui.lineEdit_15.text() == "off"):										
				self.car5_status8 = True
				self.ui8.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui8.ui.lineEdit_15.text() == "On" or self.ui8.ui.lineEdit_15.text() == "ON" or self.ui8.ui.lineEdit_15.text() == "on"):
				self.car5_status8 = False
				self.ui8.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)					
			else:
				self.car5_status8 = True
				self.ui8.ui.lineEdit_15.setText("Off")
				self.ui8.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#____________________________________________________________________
		if(self.trainNum9 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui9.ui.lineEdit_7.text() == "Off" or self.ui9.ui.lineEdit_7.text() == "OFF" or self.ui9.ui.lineEdit_7.text() == "off"):	
				self.car1_status9 = True
				self.ui9.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			elif(self.ui9.ui.lineEdit_7.text() == "On" or self.ui9.ui.lineEdit_7.text() == "ON" or self.ui9.ui.lineEdit_7.text() == "on"):
				self.car1_status9 = False	
				self.ui9.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest9 = True
				self.EmergencyBrakingTest()
				self.sendYard9 = True
				signals.tnm_sendyard.emit(True,9)				
			else:
				self.car1_status9 = True
				self.ui9.ui.lineEdit_7.setText("Off")
				self.ui9.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui9.ui.lineEdit_12.text() == "Off" or self.ui9.ui.lineEdit_12.text() == "OFF" or self.ui9.ui.lineEdit_12.text() == "off"):
				self.car2_status9 = True	
				self.ui9.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			elif(self.ui9.ui.lineEdit_12.text() == "On" or self.ui9.ui.lineEdit_12.text() == "ON" or self.ui9.ui.lineEdit_12.text() == "on"):
				self.car2_status9 = False	
				self.ui9.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest9 = True
				self.EmergencyBrakingTest()
				self.sendYard9 = True	
				signals.tnm_sendyard.emit(True,9)				
			else:
				self.car2_status9 = True
				self.ui9.ui.lineEdit_12.setText("Off")
				self.ui9.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui9.ui.lineEdit_13.text() == "Off" or self.ui9.ui.lineEdit_13.text() == "OFF" or self.ui9.ui.lineEdit_13.text() == "off"):		
				self.car3_status9 = True
				self.ui9.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			elif(self.ui9.ui.lineEdit_13.text() == "On" or self.ui9.ui.lineEdit_13.text() == "ON" or self.ui9.ui.lineEdit_13.text() == "on"):
				self.car3_status9 = False
				self.ui9.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest9 = True
				self.EmergencyBrakingTest()
				self.sendYard9 = True
				signals.tnm_sendyard.emit(True,9)					
			else:
				self.car3_status9 = True
				self.ui9.ui.lineEdit_13.setText("Off")
				self.ui9.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui9.ui.lineEdit_14.text() == "Off" or self.ui9.ui.lineEdit_14.text() == "OFF" or self.ui9.ui.lineEdit_14.text() == "off"):									
				self.car4_status9 = True
				self.ui9.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			elif(self.ui9.ui.lineEdit_14.text() == "On" or self.ui9.ui.lineEdit_14.text() == "ON" or self.ui9.ui.lineEdit_14.text() == "on"):
				self.car4_status9 = False
				self.ui9.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest9 = True
				self.EmergencyBrakingTest()
				self.sendYard9 = True
				signals.tnm_sendyard.emit(True,9)					
			else:
				self.car4_status9 = True
				self.ui9.ui.lineEdit_14.setText("Off")
				self.ui9.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui9.ui.lineEdit_15.text() == "Off" or self.ui9.ui.lineEdit_15.text() == "OFF" or self.ui9.ui.lineEdit_15.text() == "off"):										
				self.car5_status9 = True
				self.ui9.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			elif(self.ui9.ui.lineEdit_15.text() == "On" or self.ui9.ui.lineEdit_15.text() == "ON" or self.ui9.ui.lineEdit_15.text() == "on"):
				self.car5_status9 = False
				self.ui9.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest9 = True
				self.EmergencyBrakingTest()
				self.sendYard9 = True
				signals.tnm_sendyard.emit(True,9)					
			else:
				self.car5_status9 = True
				self.ui9.ui.lineEdit_15.setText("Off")
				self.ui9.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#__________________________________________________________________
		if(self.trainNum10 == 1):
			#Car 1 Status Change
			#True means engine 1 is functional
			if(self.ui10.ui.lineEdit_7.text() == "Off" or self.ui10.ui.lineEdit_7.text() == "OFF" or self.ui10.ui.lineEdit_7.text() == "off"):	
				self.car1_status10 = True
				self.ui10.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			elif(self.ui10.ui.lineEdit_7.text() == "On" or self.ui10.ui.lineEdit_7.text() == "ON" or self.ui10.ui.lineEdit_7.text() == "on"):
				self.car1_status10 = False	
				self.ui10.ui.lineEdit_16.setText("Broken")
				self.eBrakeTest10 = True
				self.EmergencyBrakingTest()
				self.sendYard10 = True
				signals.tnm_sendyard.emit(True,10)				
			else:
				self.car1_status10 = True
				self.ui10.ui.lineEdit_7.setText("Off")
				self.ui10.ui.lineEdit_16.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
				
			#Car 2 Status Change
			#True means engine 2 is functional
			if(self.ui10.ui.lineEdit_12.text() == "Off" or self.ui10.ui.lineEdit_12.text() == "OFF" or self.ui10.ui.lineEdit_12.text() == "off"):
				self.car2_status10 = True	
				self.ui10.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			elif(self.ui10.ui.lineEdit_12.text() == "On" or self.ui10.ui.lineEdit_12.text() == "ON" or self.ui10.ui.lineEdit_12.text() == "on"):
				self.car2_status10 = False	
				self.ui10.ui.lineEdit_17.setText("Broken")
				self.eBrakeTest10 = True
				self.EmergencyBrakingTest()
				self.sendYard10 = True	
				signals.tnm_sendyard.emit(True,10)				
			else:
				self.car2_status10 = True
				self.ui10.ui.lineEdit_12.setText("Off")
				self.ui10.ui.lineEdit_17.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			
			#Car 3 Status Change
			#True means engine 3 is functional
			if(self.ui10.ui.lineEdit_13.text() == "Off" or self.ui10.ui.lineEdit_13.text() == "OFF" or self.ui10.ui.lineEdit_13.text() == "off"):		
				self.car3_status10 = True
				self.ui10.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			elif(self.ui10.ui.lineEdit_13.text() == "On" or self.ui10.ui.lineEdit_13.text() == "ON" or self.ui10.ui.lineEdit_13.text() == "on"):
				self.car3_status10 = False
				self.ui10.ui.lineEdit_18.setText("Broken")
				self.eBrakeTest10 = True
				self.EmergencyBrakingTest()
				self.sendYard10 = True
				signals.tnm_sendyard.emit(True,10)					
			else:
				self.car3_status10 = True
				self.ui10.ui.lineEdit_13.setText("Off")
				self.ui10.ui.lineEdit_18.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			
			#Car 4 Status Change
			#True means engine 4 is functional
			if(self.ui10.ui.lineEdit_14.text() == "Off" or self.ui10.ui.lineEdit_14.text() == "OFF" or self.ui10.ui.lineEdit_14.text() == "off"):									
				self.car4_status10 = True
				self.ui10.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			elif(self.ui10.ui.lineEdit_14.text() == "On" or self.ui10.ui.lineEdit_14.text() == "ON" or self.ui10.ui.lineEdit_14.text() == "on"):
				self.car4_status10 = False
				self.ui10.ui.lineEdit_19.setText("Broken")
				self.eBrakeTest10 = True
				self.EmergencyBrakingTest()
				self.sendYard10 = True
				signals.tnm_sendyard.emit(True,10)					
			else:
				self.car4_status10 = True
				self.ui10.ui.lineEdit_14.setText("Off")
				self.ui10.ui.lineEdit_19.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			
			#Car 5 Status Change
			#True means engine 5 is functional
			if(self.ui10.ui.lineEdit_15.text() == "Off" or self.ui10.ui.lineEdit_15.text() == "OFF" or self.ui10.ui.lineEdit_15.text() == "off"):										
				self.car5_status10 = True
				self.ui10.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			elif(self.ui10.ui.lineEdit_15.text() == "On" or self.ui10.ui.lineEdit_15.text() == "ON" or self.ui10.ui.lineEdit_15.text() == "on"):
				self.car5_status10 = False
				self.ui10.ui.lineEdit_20.setText("Broken")
				self.eBrakeTest10 = True
				self.EmergencyBrakingTest()
				self.sendYard10 = True
				signals.tnm_sendyard.emit(True,10)					
			else:
				self.car5_status10 = True
				self.ui10.ui.lineEdit_15.setText("Off")
				self.ui10.ui.lineEdit_20.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#__________________________________________________________________
	
#_______________________________________________________________________
	#function to address Signal Pickup Failure Status's
	def signalP_fail_act(self):
		if(self.trainNum1 == 1):
			#train 1 Status Change
			#True means train 1 is functional
			if(self.ui1.ui.lineEdit_21.text() == "Off" or self.ui1.ui.lineEdit_21.text() == "OFF" or self.ui1.ui.lineEdit_21.text() == "off"):	
				self.train1_status = True
				self.ui1.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			elif(self.ui1.ui.lineEdit_21.text() == "On" or self.ui1.ui.lineEdit_21.text() == "ON" or self.ui1.ui.lineEdit_21.text() == "on"):
				self.train1_status = False	
				self.ui1.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest1 = True
				self.EmergencyBrakingTest()
				self.sendYard1 = True
				signals.tnm_sendyard.emit(True,1)			
			else:
				self.train1_status = True
				self.ui1.ui.lineEdit_21.setText("Off")
				self.ui1.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest1 = False
				self.EmergencyBrakingTest()
				self.sendYard1 = False
				signals.tnm_sendyard.emit(False,1)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#________________________________________________________________
		if(self.trainNum2 == 1):
			#train 2 Status Change
			#True means train 2 is functional
			if(self.ui2.ui.lineEdit_21.text() == "Off" or self.ui2.ui.lineEdit_21.text() == "OFF" or self.ui2.ui.lineEdit_21.text() == "off"):	
				self.train2_status = True
				self.ui2.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			elif(self.ui2.ui.lineEdit_21.text() == "On" or self.ui2.ui.lineEdit_21.text() == "ON" or self.ui2.ui.lineEdit_21.text() == "on"):
				self.train2_status = False	
				self.ui2.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest2 = True
				self.EmergencyBrakingTest()
				self.sendYard2 = True
				signals.tnm_sendyard.emit(True,2)			
			else:
				self.train2_status = True
				self.ui2.ui.lineEdit_21.setText("Off")
				self.ui2.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest2 = False
				self.EmergencyBrakingTest()
				self.sendYard2 = False
				signals.tnm_sendyard.emit(False,2)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#______________________________________________________________________
		if(self.trainNum3 == 1):
			#train 3 Status Change
			#True means train 3 is functional
			if(self.ui3.ui.lineEdit_21.text() == "Off" or self.ui3.ui.lineEdit_21.text() == "OFF" or self.ui3.ui.lineEdit_21.text() == "off"):	
				self.train3_status = True
				self.ui3.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			elif(self.ui3.ui.lineEdit_21.text() == "On" or self.ui3.ui.lineEdit_21.text() == "ON" or self.ui3.ui.lineEdit_21.text() == "on"):
				self.train3_status = False	
				self.ui3.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest3 = True
				self.EmergencyBrakingTest()
				self.sendYard3 = True
				signals.tnm_sendyard.emit(True,3)			
			else:
				self.train3_status = True
				self.ui3.ui.lineEdit_21.setText("Off")
				self.ui3.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest3 = False
				self.EmergencyBrakingTest()
				self.sendYard3 = False
				signals.tnm_sendyard.emit(False,3)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#_________________________________________________________________
		if(self.trainNum4 == 1):
			#train 4 Status Change
			#True means train 4 is functional
			if(self.ui4.ui.lineEdit_21.text() == "Off" or self.ui4.ui.lineEdit_21.text() == "OFF" or self.ui4.ui.lineEdit_21.text() == "off"):	
				self.train4_status = True
				self.ui4.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			elif(self.ui4.ui.lineEdit_21.text() == "On" or self.ui4.ui.lineEdit_21.text() == "ON" or self.ui4.ui.lineEdit_21.text() == "on"):
				self.train4_status = False	
				self.ui4.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest4 = True
				self.EmergencyBrakingTest()
				self.sendYard4 = True
				signals.tnm_sendyard.emit(True,4)			
			else:
				self.train4_status = True
				self.ui4.ui.lineEdit_21.setText("Off")
				self.ui4.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest4 = False
				self.EmergencyBrakingTest()
				self.sendYard4 = False
				signals.tnm_sendyard.emit(False,4)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#_____________________________________________________________________
		if(self.trainNum5 == 1):
			#train 5 Status Change
			#True means train 5 is functional
			if(self.ui5.ui.lineEdit_21.text() == "Off" or self.ui5.ui.lineEdit_21.text() == "OFF" or self.ui5.ui.lineEdit_21.text() == "off"):	
				self.train5_status = True
				self.ui5.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			elif(self.ui5.ui.lineEdit_21.text() == "On" or self.ui5.ui.lineEdit_21.text() == "ON" or self.ui5.ui.lineEdit_21.text() == "on"):
				self.train5_status = False	
				self.ui5.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest5 = True
				self.EmergencyBrakingTest()
				self.sendYard5 = True
				signals.tnm_sendyard.emit(True,5)			
			else:
				self.train5_status = True
				self.ui5.ui.lineEdit_21.setText("Off")
				self.ui5.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest5 = False
				self.EmergencyBrakingTest()
				self.sendYard5 = False
				signals.tnm_sendyard.emit(False,5)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#_____________________________________________________________________
		if(self.trainNum6 == 1):
			#train 6 Status Change
			#True means train 6 is functional
			if(self.ui6.ui.lineEdit_21.text() == "Off" or self.ui6.ui.lineEdit_21.text() == "OFF" or self.ui6.ui.lineEdit_21.text() == "off"):	
				self.train6_status = True
				self.ui6.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			elif(self.ui6.ui.lineEdit_21.text() == "On" or self.ui6.ui.lineEdit_21.text() == "ON" or self.ui6.ui.lineEdit_21.text() == "on"):
				self.train6_status = False	
				self.ui6.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest6 = True
				self.EmergencyBrakingTest()
				self.sendYard6 = True
				signals.tnm_sendyard.emit(True,6)			
			else:
				self.train6_status = True
				self.ui6.ui.lineEdit_21.setText("Off")
				self.ui6.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest6 = False
				self.EmergencyBrakingTest()
				self.sendYard6 = False
				signals.tnm_sendyard.emit(False,6)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#___________________________________________________________________
		if(self.trainNum7 == 1):
			#train 7 Status Change
			#True means train 7 is functional
			if(self.ui7.ui.lineEdit_21.text() == "Off" or self.ui7.ui.lineEdit_21.text() == "OFF" or self.ui7.ui.lineEdit_21.text() == "off"):	
				self.train7_status = True
				self.ui7.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			elif(self.ui7.ui.lineEdit_21.text() == "On" or self.ui7.ui.lineEdit_21.text() == "ON" or self.ui7.ui.lineEdit_21.text() == "on"):
				self.train7_status = False	
				self.ui7.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest7 = True
				self.EmergencyBrakingTest()
				self.sendYard7 = True
				signals.tnm_sendyard.emit(True,7)			
			else:
				self.train7_status = True
				self.ui7.ui.lineEdit_21.setText("Off")
				self.ui7.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest7 = False
				self.EmergencyBrakingTest()
				self.sendYard7 = False
				signals.tnm_sendyard.emit(False,7)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#____________________________________________________________________
		if(self.trainNum8 == 1):
			#train 8 Status Change
			#True means train 8 is functional
			if(self.ui8.ui.lineEdit_21.text() == "Off" or self.ui8.ui.lineEdit_21.text() == "OFF" or self.ui8.ui.lineEdit_21.text() == "off"):	
				self.train8_status = True
				self.ui8.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			elif(self.ui8.ui.lineEdit_21.text() == "On" or self.ui8.ui.lineEdit_21.text() == "ON" or self.ui8.ui.lineEdit_21.text() == "on"):
				self.train8_status = False	
				self.ui8.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest8 = True
				self.EmergencyBrakingTest()
				self.sendYard8 = True
				signals.tnm_sendyard.emit(True,8)			
			else:
				self.train8_status = True
				self.ui8.ui.lineEdit_21.setText("Off")
				self.ui8.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest8 = False
				self.EmergencyBrakingTest()
				self.sendYard8 = False
				signals.tnm_sendyard.emit(False,8)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#_________________________________________________________________
		if(self.trainNum9 == 1):
			#train 9 Status Change
			#True means train 9 is functional
			if(self.ui9.ui.lineEdit_21.text() == "Off" or self.ui9.ui.lineEdit_21.text() == "OFF" or self.ui9.ui.lineEdit_21.text() == "off"):	
				self.train9_status = True
				self.ui9.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			elif(self.ui9.ui.lineEdit_21.text() == "On" or self.ui9.ui.lineEdit_21.text() == "ON" or self.ui9.ui.lineEdit_21.text() == "on"):
				self.train9_status = False	
				self.ui9.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest9 = True
				self.EmergencyBrakingTest()
				self.sendYard9 = True
				signals.tnm_sendyard.emit(True,9)			
			else:
				self.train9_status = True
				self.ui9.ui.lineEdit_21.setText("Off")
				self.ui9.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest9 = False
				self.EmergencyBrakingTest()
				self.sendYard9 = False
				signals.tnm_sendyard.emit(False,9)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#_________________________________________________________________
		if(self.trainNum10 == 1):
			#train 10 Status Change
			#True means train 10 is functional
			if(self.ui10.ui.lineEdit_21.text() == "Off" or self.ui10.ui.lineEdit_21.text() == "OFF" or self.ui10.ui.lineEdit_21.text() == "off"):	
				self.train10_status = True
				self.ui10.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			elif(self.ui10.ui.lineEdit_21.text() == "On" or self.ui10.ui.lineEdit_21.text() == "ON" or self.ui10.ui.lineEdit_21.text() == "on"):
				self.train10_status = False	
				self.ui10.ui.lineEdit_26.setText("Broken")	
				self.eBrakeTest10 = True
				self.EmergencyBrakingTest()
				self.sendYard10 = True
				signals.tnm_sendyard.emit(True,10)			
			else:
				self.train10_status = True
				self.ui10.ui.lineEdit_21.setText("Off")
				self.ui10.ui.lineEdit_26.setText("Operational")
				self.eBrakeTest10 = False
				self.EmergencyBrakingTest()
				self.sendYard10 = False
				signals.tnm_sendyard.emit(False,10)
			signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
			#_________________________________________________________________
			

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
		elif(self.trainNum == 9):
			self.trainNum9 = 1
		elif(self.trainNum == 10):
			self.trainNum10 = 1
		
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
		#Main Window Thread 1
		self.ui1 = tnm_threadSupport()
		self.threadMain1 = QThread()
		self.ui1.moveToThread(self.threadMain1)
		self.ui1.MainWindow.setWindowTitle("Train Model 1")
		self.threadMain1.start()
		#Main Window Thread 2
		self.ui2 = tnm_threadSupport()
		self.threadMain2 = QThread()
		self.ui2.moveToThread(self.threadMain2)
		self.ui2.MainWindow.setWindowTitle("Train Model 2")
		self.threadMain2.start()
		#Main Window Thread 3
		self.ui3 = tnm_threadSupport()
		self.threadMain3 = QThread()
		self.ui3.moveToThread(self.threadMain3)
		self.ui3.MainWindow.setWindowTitle("Train Model 3")
		self.threadMain3.start()
		#Main Window Thread 4
		self.ui4 = tnm_threadSupport()
		self.threadMain4 = QThread()
		self.ui4.moveToThread(self.threadMain4)
		self.ui4.MainWindow.setWindowTitle("Train Model 4")
		self.threadMain4.start()
		#Main Window Thread 5
		self.ui5 = tnm_threadSupport()
		self.threadMain5 = QThread()
		self.ui5.moveToThread(self.threadMain5)
		self.ui5.MainWindow.setWindowTitle("Train Model 5")
		self.threadMain5.start()
		#Main Window Thread 6
		self.ui6 = tnm_threadSupport()
		self.threadMain6 = QThread()
		self.ui6.moveToThread(self.threadMain6)
		self.ui6.MainWindow.setWindowTitle("Train Model 6")
		self.threadMain6.start()
		#Main Window Thread 7
		self.ui7 = tnm_threadSupport()
		self.threadMain7 = QThread()
		self.ui7.moveToThread(self.threadMain7)
		self.ui7.MainWindow.setWindowTitle("Train Model 7")
		self.threadMain7.start()
		#Main Window Thread 8
		self.ui8 = tnm_threadSupport()
		self.threadMain8 = QThread()
		self.ui8.moveToThread(self.threadMain8)
		self.ui8.MainWindow.setWindowTitle("Train Model 8")
		self.threadMain8.start()
		#Main Window Thread 9
		self.ui9 = tnm_threadSupport()
		self.threadMain9 = QThread()
		self.ui9.moveToThread(self.threadMain9)
		self.ui9.MainWindow.setWindowTitle("Train Model 9")
		self.threadMain9.start()
		#Main Window Thread 10
		self.ui10 = tnm_threadSupport()
		self.threadMain10 = QThread()
		self.ui10.moveToThread(self.threadMain10)
		self.ui10.MainWindow.setWindowTitle("Train Model 10")
		self.threadMain10.start()
		
		
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
		self.TotTrainNum = 0
		self.TrainName1, self.TrainName2, self.TrainName3, self.TrainName4, self.TrainName5, self.TrainName6, self.TrainName7, self.TrainName8, self.TrainName9, self.TrainName10 = " -- Information"," -- Information"," -- Information"," -- Information"," -- Information"," -- Information"," -- Information"," -- Information", " -- Information", " -- Information"
		self.train1, self.train2, self.train3, self.train4, self.train5, self.train6, self.train7, self.train8, self.train9, self.train10 = "Train 1 Information", "Train 2 Information", "Train 3 Information", "Train 4 Information", "Train 5 Information", "Train 6 Information", "Train 7 Information", "Train 8 Information", "Train 9 Information", "Train 10 Information"
		#Train Number x - 0 if not added (or destroyed), 1 if on the track
		self.TrainNum1, self.TrainNum2, self.TrainNum3, self.TrainNum4, self.TrainNum5, self.TrainNum6, self.TrainNum7, self.TrainNum8, self.TrainNum9, self.TrainNum10 = 0,0,0,0,0,0,0,0,0,0	
		self.timeSeconds = 0
		signals.tkm_get_train_num.connect(self.setTrainStart)
	#authority connected from tkm
		self.block_authority1, self.block_authority2, self.block_authority3, self.block_authority4, self.block_authority5, self.block_authority6, self.block_authority7, self.block_authority8, self.block_authority9, self.block_authority10 = False,False,False,False,False,False,False,False,False,False
		signals.tkm_get_train_auth.connect(self.SetAuthority)
	#power connected from tnc
		self.curr_power1, self.curr_power2, self.curr_power3, self.curr_power4, self.curr_power5, self.curr_power6, self.curr_power7, self.curr_power8, self.curr_power9, self.curr_power10 = 0,0,0,0,0,0,0,0,0,0
		signals.tnc_power.connect(self.SetPower)
		self.curr_speed1, self.curr_speed2, self.curr_speed3, self.curr_speed4, self.curr_speed5, self.curr_speed6, self.curr_speed7, self.curr_speed8, self.curr_speed9, self.curr_speed10 = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
		self.curr_accl1, self.curr_accl2, self.curr_accl3, self.curr_accl4, self.curr_accl5, self.curr_accl6, self.curr_accl7, self.curr_accl8, self.curr_accl9, self.curr_accl10 = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
		self.comm_speed1, self.comm_speed2, self.comm_speed3, self.comm_speed4, self.comm_speed5, self.comm_speed6, self.comm_speed7, self.comm_speed8, self.comm_speed9, self.comm_speed10 = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
		signals.tkm_get_speed.connect(self.SetCommSpeed)
		#train starts at rest v		-> #Used as value for inital speed for curr_speed calculation. Then is set to curr_speed for next calculation
		self.SpeedN11, self.SpeedN12, self.SpeedN13, self.SpeedN14, self.SpeedN15, self.SpeedN16, self.SpeedN17, self.SpeedN18, self.SpeedN19, self.SpeedN110 = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0			
		self.AcclN11, self.AcclN12, self.AcclN13, self.AcclN14, self.AcclN15, self.AcclN16, self.AcclN17, self.AcclN18, self.AcclN19, self.AcclN110 = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
	#Block length connected from tkm
		self.block_length1, self.block_length2, self.block_length3, self.block_length4, self.block_length5, self.block_length6, self.block_length7, self.block_length8, self.block_length9, self.block_length10 = 1,1,1,1,1,1,1,1,1,1
		self.block_num1, self.block_num2, self.block_num3, self.block_num4, self.block_num5, self.block_num6, self.block_num7, self.block_num8, self.block_num9, self.block_num10 = 0,0,0,0,0,0,0,0,0,0
		self.block_finished1, self.block_finished2, self.block_finished3, self.block_finished4, self.block_finished5, self.block_finished6, self.block_finished7, self.block_finished8, self.block_finished9, self.block_finished10 = False,False,False,False,False,False,False,False,False,False
		self.timeBlock = 0
		self.dist_traveled1, self.dist_traveled2, self.dist_traveled3, self.dist_traveled4, self.dist_traveled5, self.dist_traveled6, self.dist_traveled7, self.dist_traveled8, self.dist_traveled9, self.dist_traveled10  = 0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0
		signals.tkm_get_blength.connect(self.blockLen)
		signals.tkm_get_block.connect(self.blockNum)
	#brake states
		self.Brake1, self.Brake2, self.Brake3, self.Brake4, self.Brake5, self.Brake6, self.Brake7, self.Brake8, self.Brake9, self.Brake10  = False,False,False,False,False,False,False,False,False,False
		self.eBrake1, self.eBrake2, self.eBrake3, self.eBrake4, self.eBrake5, self.eBrake6, self.eBrake7, self.eBrake8, self.eBrake9, self.eBrake10 = False,False,False,False,False,False,False,False,False,False
		signals.tnc_emergency_brake.connect(self.SetEBrake)
		signals.tnc_service_brake.connect(self.SetServiceBrake)
	#Occupancy 
		self.pass_count1, self.pass_count2, self.pass_count3, self.pass_count4, self.pass_count5, self.pass_count6, self.pass_count7, self.pass_count8, self.pass_count9, self.pass_count10 = 0,0,0,0,0,0,0,0,0,0
		signals.tkm_get_pass_count.connect(self.SetOccupancy)
		self.crew_count = 3
	#Route Information
		self.Mass_Empty = (5*40.9)								#Tons with no passengers/crew
		self.Occupancy1, self.Occupancy2, self.Occupancy3, self.Occupancy4, self.Occupancy5, self.Occupancy6, self.Occupancy7, self.Occupancy8, self.Occupancy9, self.Occupancy10 = 3,3,3,3,3,3,3,3,3,3
		self.RouteName1, self.RouteName2, self.RouteName3, self.RouteName4, self.RouteName5, self.RouteName6, self.RouteName7, self.RouteName8, self.RouteName9, self.RouteName10 = " --- "," --- "," --- "," --- "," --- "," --- "," --- "," --- "," --- "," --- "
		self.TrainDirection1, self.TrainDirection2, self.TrainDirection3, self.TrainDirection4, self.TrainDirection5, self.TrainDirection6, self.TrainDirection7, self.TrainDirection8, self.TrainDirection9, self.TrainDirection10 = 1,1,1,1,1,1,1,1,1,1
		#internal direction for train on the red line
		self.TNMdirectionR1, self.TNMdirectionR2, self.TNMdirectionR3, self.TNMdirectionR4, self.TNMdirectionR5, self.TNMdirectionR6, self.TNMdirectionR7, self.TNMdirectionR8, self.TNMdirectionR9, self.TNMdirectionR10 = 1,1,1,1,1,1,1,1,1,1
		#internal direction for train on the green line
		self.TNMdirectionG1, self.TNMdirectionG2, self.TNMdirectionG3, self.TNMdirectionG4, self.TNMdirectionG5, self.TNMdirectionG6, self.TNMdirectionG7, self.TNMdirectionG8, self.TNMdirectionG9, self.TNMdiretionG10 = 1,1,1,1,1,1,1,1,1,1
		self.CurrStation1, self.CurrStation2, self.CurrStation3, self.CurrStation4, self.CurrStation5, self.CurrStation6, self.CurrStation7, self.CurrStation8, self.CurrStation9, self.CurrStation10 = "Yard","Yard","Yard","Yard","Yard","Yard","Yard","Yard","Yard","Yard"
		self.NextStation1, self.NextStation2, self.NextStation3, self.NextStation4, self.NextStation5, self.NextStation6, self.NextStation7, self.NextStation8, self.NextStation9, self.NextStation10 = " --- "," --- "," --- "," --- "," --- "," --- "," --- "," --- "," --- "," --- "
		self.DoorStatus1, self.DoorStatus2, self.DoorStatus3, self.DoorStatus4, self.DoorStatus5, self.DoorStatus6, self.DoorStatus7, self.DoorStatus8, self.DoorStatus9, self.DoorStatus10 = False,False,False,False,False,False,False,False,False,False
		self.LeftDoor1, self.LeftDoor2, self.LeftDoor3, self.LeftDoor4, self.LeftDoor5, self.LeftDoor6, self.LeftDoor7, self.LeftDoor8, self.LeftDoor9, self.LeftDoor10 = False,False,False,False,False,False,False,False,False,False
		self.RightDoor1, self.RightDoor2, self.RightDoor3, self.RightDoor4, self.RightDoor5, self.RightDoor6, self.RightDoor7, self.RightDoor8, self.RightDoor9, self.RightDoor10 = False,False,False,False,False,False,False,False,False,False
		signals.tnc_left_door.connect(self.setRightDoor)
		signals.tnc_right_door.connect(self.setLeftDoor)
	#Beacon ID connected from tkm
		self.beacon_bin1, self.beacon_bin2, self.beacon_bin3, self.beacon_bin4, self.beacon_bin5, self.beacon_bin6, self.beacon_bin7, self.beacon_bin8, self.beacon_bin9, self.beacon_bin10 = 0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000,0b00000000
		#self.BeaconID = 00000000								#bit1 (red vs green) bit2 (UG vs Station) bit3 (Left side (62->63) vs Right side(63->64))
		signals.tkm_get_beacon.connect(self.SetBeaconID)
		self.BeaconIDStatus = True
	#Internal control status's
		self.lights_Cab1, self.lights_Cab2, self.lights_Cab3, self.lights_Cab4, self.lights_Cab5, self.lights_Cab6, self.lights_Cab7, self.lights_Cab8, self.lights_Cab9, self.lights_Cab10 = True,True,True,True,True,True,True,True,True,True
		self.lights_High1, self.lights_High2, self.lights_High3, self.lights_High4, self.lights_High5, self.lights_High6, self.lights_High7, self.lights_High8, self.lights_High9, self.lights_High10 = False,False,False,False,False,False,False,False,False,False
		self.lights_Tun1, self.lights_Tun2, self.lights_Tun3, self.lights_Tun4, self.lights_Tun5, self.lights_Tun6, self.lights_Tun7, self.lights_Tun8, self.lights_Tun9, self.lights_Tun10 = False,False,False,False,False,False,False,False,False,False
		signals.tnc_cab_light.connect(self.setCabLight)
		signals.tnc_tunnel_light.connect(self.setTunLight)
		signals.tnc_high_beam_light.connect(self.setHighLight)
		#degrees Fahrenheit
		self.set_temp1, self.set_temp2, self.set_temp3, self.set_temp4, self.set_temp5, self.set_temp6, self.set_temp7, self.set_temp8, self.set_temp9, self.set_temp10 = 68,68,68,68,68,68,68,68,68,68
		self.curr_temp1, self.curr_temp2, self.curr_temp3, self.curr_temp4, self.curr_temp5, self.curr_temp6, self.curr_temp7, self.curr_temp8, self.curr_temp9, self.curr_temp10 = 68,68,68,68,68,68,68,68,68,68
		self.announce1, self.announce2, self.announce3, self.announce4, self.announce5, self.announce6, self.announce7, self.announce8, self.announce9, self.announce10 = "Watch your step. Have a great day!","Watch your step. Have a great day!","Watch your step. Have a great day!","Watch your step. Have a great day!","Watch your step. Have a great day!","Watch your step. Have a great day!","Watch your step. Have a great day!","Watch your step. Have a great day!","Watch your step. Have a great day!","Watch your step. Have a great day!"
		signals.tnc_announcement.connect(self.SetAnnounce)


		#Defining Actions for specific UI Interactions
		
		signals.time.connect(self.update_MoveStat)						#Update Movement Statistics
		
		signals.time.connect(self.update_TrainStat)						#Update Train Statistics
		
		signals.time.connect(self.update_RouteInfo)						#Update Route Information
		
		signals.time.connect(self.DispAnnounce)							#Display current Announcements
		
		signals.time.connect(self.getTime)
		
		#Display running time
		signals.time.connect(self.GetDatetime)
		self.ui1.uim.pushButton.clicked.connect(self.EmergencyBraking)			#Verify eBrake is pressed
		self.ui1.uim.lineEdit_17.editingFinished.connect(self.Temperature)		#Update Temperature interface

		signals.time.connect(self.GetDatetime)
		self.ui2.uim.pushButton.clicked.connect(self.EmergencyBraking)			#Verify eBrake is pressed
		self.ui2.uim.lineEdit_17.editingFinished.connect(self.Temperature)		#Update Temperature interface

		signals.time.connect(self.GetDatetime)
		self.ui3.uim.pushButton.clicked.connect(self.EmergencyBraking)			#Verify eBrake is pressed
		self.ui3.uim.lineEdit_17.editingFinished.connect(self.Temperature)		#Update Temperature interface

		signals.time.connect(self.GetDatetime)
		self.ui4.uim.pushButton.clicked.connect(self.EmergencyBraking)			#Verify eBrake is pressed
		self.ui4.uim.lineEdit_17.editingFinished.connect(self.Temperature)		#Update Temperature interface

		signals.time.connect(self.GetDatetime)
		self.ui5.uim.pushButton.clicked.connect(self.EmergencyBraking)			#Verify eBrake is pressed
		self.ui5.uim.lineEdit_17.editingFinished.connect(self.Temperature)		#Update Temperature interface

		signals.time.connect(self.GetDatetime)
		self.ui6.uim.pushButton.clicked.connect(self.EmergencyBraking)			#Verify eBrake is pressed
		self.ui6.uim.lineEdit_17.editingFinished.connect(self.Temperature)		#Update Temperature interface

		signals.time.connect(self.GetDatetime)
		self.ui7.uim.pushButton.clicked.connect(self.EmergencyBraking)			#Verify eBrake is pressed
		self.ui7.uim.lineEdit_17.editingFinished.connect(self.Temperature)		#Update Temperature interface

		signals.time.connect(self.GetDatetime)
		self.ui8.uim.pushButton.clicked.connect(self.EmergencyBraking)			#Verify eBrake is pressed
		self.ui8.uim.lineEdit_17.editingFinished.connect(self.Temperature)		#Update Temperature interface

		signals.time.connect(self.GetDatetime)
		self.ui9.uim.pushButton.clicked.connect(self.EmergencyBraking)			#Verify eBrake is pressed
		self.ui9.uim.lineEdit_17.editingFinished.connect(self.Temperature)		#Update Temperature interface

		signals.time.connect(self.GetDatetime)
		self.ui10.uim.pushButton.clicked.connect(self.EmergencyBraking)			#Verify eBrake is pressed
		self.ui10.uim.lineEdit_17.editingFinished.connect(self.Temperature)		#Update Temperature interface
		
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
			signals.tkm_get_speed.connect(self.SetCommSpeed)
			signals.tnm_comm_speed.emit(self.comm_speed1,1)
			signals.tnc_power.connect(self.SetPower)
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed1, self.current_accl1 = set_curr_speed(self.timeSeconds, self.eBrake1, self.Brake1, self.block_authority1, self.curr_power1, self.Occupancy1, self.SpeedN11, self.AcclN11, self.comm_speed1,1)
			#print(str(self.curr_speed1) + " mph train 1")
			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN11 = self.curr_speed1
			self.AcclN11 = self.current_accl1
			
			#Update current speed given power value
			self.ui1.uim.lineEdit.setText(str(self.curr_speed1) + " mph")
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
					signals.tkm_get_speed.connect(self.SetCommSpeed)
					signals.tkm_get_block.connect(self.blockNum)
					signals.tkm_get_train_auth.connect(self.SetAuthority)
				
			#Update brake status
			if (self.Brake1 == True or self.eBrake1 == True):
				self.ui1.uim.lineEdit_2.setText("On")
			else:
				self.ui1.uim.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		if(self.TrainNum2 == 1):
			#Address Authority Here
			signals.tnm_authority.emit(self.block_authority2,2)
			#Address Commanded Speed
			signals.tkm_get_speed.connect(self.SetCommSpeed)
			signals.tnm_comm_speed.emit(self.comm_speed2,2)
			signals.tnc_power.connect(self.SetPower)
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed2, self.current_accl2 = set_curr_speed(self.timeSeconds, self.eBrake2, self.Brake2, self.block_authority2, self.curr_power2, self.Occupancy2, self.SpeedN12, self.AcclN12, self.comm_speed2,2)
			#print(str(self.curr_speed2) + " mph train 2")
			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN12 = self.curr_speed2
			self.AcclN12 = self.current_accl2
			
			#Update current speed given power value
			self.ui2.uim.lineEdit.setText(str(self.curr_speed2) + " mph")
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
					signals.tkm_get_speed.connect(self.SetCommSpeed)
					signals.tkm_get_block.connect(self.blockNum)
					signals.tkm_get_train_auth.connect(self.SetAuthority)
					
			#Update brake status
			if (self.Brake2 == True or self.eBrake2 == True):
				self.ui2.uim.lineEdit_2.setText("On")
			else:
				self.ui2.uim.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		if(self.TrainNum3 == 1):
			#Address Authority Here
			signals.tnm_authority.emit(self.block_authority3,3)
			#Address Commanded Speed
			signals.tkm_get_speed.connect(self.SetCommSpeed)
			signals.tnm_comm_speed.emit(self.comm_speed3,3)
			signals.tnc_power.connect(self.SetPower)
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed3, self.current_accl3 = set_curr_speed(self.timeSeconds, self.eBrake3, self.Brake3, self.block_authority3, self.curr_power3, self.Occupancy3, self.SpeedN13, self.AcclN13, self.comm_speed3,3)

			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN13 = self.curr_speed3
			self.AcclN13 = self.current_accl3
			
			#Update current speed given power value
			self.ui3.uim.lineEdit.setText(str(self.curr_speed3) + " mph")
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
					signals.tkm_get_speed.connect(self.SetCommSpeed)
					signals.tkm_get_block.connect(self.blockNum)
					signals.tkm_get_train_auth.connect(self.SetAuthority)
				
			#Update brake status
			if (self.Brake3 == True or self.eBrake3 == True):
				self.ui3.uim.lineEdit_2.setText("On")
			else:
				self.ui3.uim.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		if(self.TrainNum4 == 1):
			#Address Authority Here
			signals.tnm_authority.emit(self.block_authority4,4)
			#Address Commanded Speed
			signals.tkm_get_speed.connect(self.SetCommSpeed)
			signals.tnm_comm_speed.emit(self.comm_speed4,4)
			signals.tnc_power.connect(self.SetPower)
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed4, self.current_accl4 = set_curr_speed(self.timeSeconds, self.eBrake4, self.Brake4, self.block_authority4, self.curr_power4, self.Occupancy4, self.SpeedN14, self.AcclN14, self.comm_speed4,4)

			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN14 = self.curr_speed4
			self.AcclN14 = self.current_accl4
			
			#Update current speed given power value
			self.ui4.uim.lineEdit.setText(str(self.curr_speed4) + " mph")
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
					signals.tkm_get_speed.connect(self.SetCommSpeed)
					signals.tkm_get_block.connect(self.blockNum)
					signals.tkm_get_train_auth.connect(self.SetAuthority)
				
			#Update brake status
			if (self.Brake4 == True or self.eBrake4 == True):
				self.ui4.uim.lineEdit_2.setText("On")
			else:
				self.ui4.uim.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		if(self.TrainNum5 == 1):
			#Address Authority Here
			signals.tnm_authority.emit(self.block_authority5,5)
			#Address Commanded Speed
			signals.tkm_get_speed.connect(self.SetCommSpeed)
			signals.tnm_comm_speed.emit(self.comm_speed5,5)
			signals.tnc_power.connect(self.SetPower)
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed5, self.current_accl5 = set_curr_speed(self.timeSeconds, self.eBrake5, self.Brake5, self.block_authority5, self.curr_power5, self.Occupancy5, self.SpeedN15, self.AcclN15, self.comm_speed5,5)

			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN15 = self.curr_speed5
			self.AcclN15 = self.current_accl5
			
			#Update current speed given power value
			self.ui5.uim.lineEdit.setText(str(self.curr_speed5) + " mph")
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
					signals.tkm_get_speed.connect(self.SetCommSpeed)
					signals.tkm_get_block.connect(self.blockNum)
					signals.tkm_get_train_auth.connect(self.SetAuthority)
				
			#Update brake status
			if (self.Brake5 == True or self.eBrake5 == True):
				self.ui5.uim.lineEdit_2.setText("On")
			else:
				self.ui5.uim.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		if(self.TrainNum6 == 1):
			#Address Authority Here
			signals.tnm_authority.emit(self.block_authority6,6)
			#Address Commanded Speed
			signals.tkm_get_speed.connect(self.SetCommSpeed)
			signals.tnm_comm_speed.emit(self.comm_speed6,6)
			signals.tnc_power.connect(self.SetPower)
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed6, self.current_accl6 = set_curr_speed(self.timeSeconds, self.eBrake6, self.Brake6, self.block_authority6, self.curr_power6, self.Occupancy6, self.SpeedN16, self.AcclN16, self.comm_speed6,6)

			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN16 = self.curr_speed6
			self.AcclN16 = self.current_accl6
			
			#Update current speed given power value
			self.ui6.uim.lineEdit.setText(str(self.curr_speed6) + " mph")
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
					signals.tkm_get_speed.connect(self.SetCommSpeed)
					signals.tkm_get_block.connect(self.blockNum)
					signals.tkm_get_train_auth.connect(self.SetAuthority)
				
			#Update brake status
			if (self.Brake6 == True or self.eBrake6 == True):
				self.ui6.uim.lineEdit_2.setText("On")
			else:
				self.ui6.uim.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		if(self.TrainNum7 == 1):
			#Address Authority Here
			signals.tnm_authority.emit(self.block_authority7,7)
			#Address Commanded Speed
			signals.tkm_get_speed.connect(self.SetCommSpeed)
			signals.tnm_comm_speed.emit(self.comm_speed7,7)
			signals.tnc_power.connect(self.SetPower)
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed7, self.current_accl7 = set_curr_speed(self.timeSeconds, self.eBrake7, self.Brake7, self.block_authority7, self.curr_power7, self.Occupancy7, self.SpeedN17, self.AcclN17, self.comm_speed7,7)

			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN17 = self.curr_speed7
			self.AcclN17 = self.current_accl17
						
			#Update current speed given power value
			self.ui7.uim.lineEdit.setText(str(self.curr_speed7) + " mph")
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
					signals.tkm_get_speed.connect(self.SetCommSpeed)
					signals.tkm_get_block.connect(self.blockNum)
					signals.tkm_get_train_auth.connect(self.SetAuthority)
				
			#Update brake status
			if (self.Brake7 == True or self.eBrake7 == True):
				self.ui7.uim.lineEdit_2.setText("On")
			else:
				self.ui7.uim.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		if(self.TrainNum8 == 1):
			#Address Authority Here
			signals.tnm_authority.emit(self.block_authority8,8)
			#Address Commanded 
			signals.tkm_get_speed.connect(self.SetCommSpeed)
			signals.tnm_comm_speed.emit(self.comm_speed8,8)
			signals.tnc_power.connect(self.SetPower)
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed8, self.current_accl8 = set_curr_speed(self.timeSeconds, self.eBrake8, self.Brake8, self.block_authority8, self.curr_power8, self.Occupancy8, self.SpeedN18, self.AcclN18, self.comm_speed8,8)

			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN18 = self.curr_speed8
			self.AcclN18 = self.current_accl8
			
			#Update current speed given power value
			self.ui8.uim.lineEdit.setText(str(self.curr_speed8) + " mph")
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
					signals.tkm_get_speed.connect(self.SetCommSpeed)
					signals.tkm_get_block.connect(self.blockNum)
					signals.tkm_get_train_auth.connect(self.SetAuthority)
				
			#Update brake status
			if (self.Brake8 == True or self.eBrake8 == True):
				self.ui8.uim.lineEdit_2.setText("On")
			else:
				self.ui8.uim.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		if(self.TrainNum9 == 1):
			#Address Authority Here
			signals.tnm_authority.emit(self.block_authority9,9)
			#Address Commanded Speed
			signals.tkm_get_speed.connect(self.SetCommSpeed)
			signals.tnm_comm_speed.emit(self.comm_speed9,9)
			signals.tnc_power.connect(self.SetPower)
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed9, self.current_accl9 = set_curr_speed(self.timeSeconds, self.eBrake9, self.Brake9, self.block_authority9, self.curr_power9, self.Occupancy9, self.SpeedN19, self.AcclN19, self.comm_speed9,9)

			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN19 = self.curr_speed9
			self.AcclN19 = self.current_accl9
			
			#Update current speed given power value
			self.ui9.uim.lineEdit.setText(str(self.curr_speed9) + " mph")
			#Send the new calculated current speed to Train Controller
			signals.tnm_curr_speed.emit(self.curr_speed9,9)
			
			#Variable to check speed, then calculate when block changes based on speed
			curr_speed_mps = 0.0
			#calculations of current distance
			curr_speed_mps = MiletoMeter(self.curr_speed9)					#MPH to mps
			self.dist_traveled9 = (self.dist_traveled9 + curr_speed_mps*(1))		#distance in meters m/s *s = m
			#If distance > length, change blocks and emit signal
			if(curr_speed_mps > 0.0):
				if(self.dist_traveled9 >= self.block_length9):
					self.block_finished9 = True
					print(str(self.block_finished9) + " 9 change blocks")
					
					self.dist_traveled9 = 0
					if(self.RouteName9 == "Red Line"):
						signals.tnm_block_finished_red.emit(9)
					elif(self.RouteName9 == "Green Line"):
						signals.tnm_block_finished_green.emit(9)
					signals.tkm_get_blength.connect(self.blockLen)
					signals.tkm_get_speed.connect(self.SetCommSpeed)
					signals.tkm_get_block.connect(self.blockNum)
					signals.tkm_get_train_auth.connect(self.SetAuthority)
				
			#Update brake status
			if (self.Brake9 == True or self.eBrake9 == True):
				self.ui9.uim.lineEdit_2.setText("On")
			else:
				self.ui9.uim.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		if(self.TrainNum10 == 1):
			#Address Authority Here
			signals.tnm_authority.emit(self.block_authority10,10)
			#Address Commanded Speed
			signals.tkm_get_speed.connect(self.SetCommSpeed)
			signals.tnm_comm_speed.emit(self.comm_speed10,10)
			signals.tnc_power.connect(self.SetPower)
			signals.tnc_service_brake.connect(self.SetServiceBrake)
			#Calculate current speed
			self.curr_speed10, self.current_accl10 = set_curr_speed(self.timeSeconds, self.eBrake10, self.Brake10, self.block_authority10, self.curr_power10, self.Occupancy10, self.SpeedN110, self.AcclN110, self.comm_speed10,10)

			#Set At - 1 variables for use in next sec. speed calculation
			self.SpeedN110 = self.curr_speed10
			self.AcclN110 = self.current_accl10
			
			#Update current speed given power value
			self.ui10.uim.lineEdit.setText(str(self.curr_speed10) + " mph")
			#Send the new calculated current speed to Train Controller
			signals.tnm_curr_speed.emit(self.curr_speed10,10)
			
			#Variable to check speed, then calculate when block changes based on speed
			curr_speed_mps = 0.0
			#calculations of current distance
			curr_speed_mps = MiletoMeter(self.curr_speed10)					#MPH to mps
			self.dist_traveled10 = (self.dist_traveled10 + curr_speed_mps*(1))		#distance in meters m/s *s = m
			#If distance > length, change blocks and emit signal
			if(curr_speed_mps > 0.0):
				if(self.dist_traveled10 >= self.block_length10):
					self.block_finished10 = True
					print(str(self.block_finished10) + " 10 change blocks")
					
					self.dist_traveled10 = 0
					if(self.RouteName10 == "Red Line"):
						signals.tnm_block_finished_red.emit(10)
					elif(self.RouteName10 == "Green Line"):
						signals.tnm_block_finished_green.emit(10)
					signals.tkm_get_blength.connect(self.blockLen)
					signals.tkm_get_speed.connect(self.SetCommSpeed)
					signals.tkm_get_block.connect(self.blockNum)
					signals.tkm_get_train_auth.connect(self.SetAuthority)
				
			#Update brake status
			if (self.Brake10 == True or self.eBrake10 == True):
				self.ui10.uim.lineEdit_2.setText("On")
			else:
				self.ui10.uim.lineEdit_2.setText("Off")
		#___________________________________________________________________________
		
		
		#Don't allow changes to lineEdits
		self.ui1.uim.lineEdit.setReadOnly(True)
		self.ui1.uim.lineEdit_2.setReadOnly(True)
		self.ui1.uim.lineEdit_3.setReadOnly(True)
		self.ui1.uim.lineEdit_4.setReadOnly(True)
		self.ui1.uim.lineEdit_5.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui2.uim.lineEdit.setReadOnly(True)
		self.ui2.uim.lineEdit_2.setReadOnly(True)
		self.ui2.uim.lineEdit_3.setReadOnly(True)
		self.ui2.uim.lineEdit_4.setReadOnly(True)
		self.ui2.uim.lineEdit_5.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui3.uim.lineEdit.setReadOnly(True)
		self.ui3.uim.lineEdit_2.setReadOnly(True)
		self.ui3.uim.lineEdit_3.setReadOnly(True)
		self.ui3.uim.lineEdit_4.setReadOnly(True)
		self.ui3.uim.lineEdit_5.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui4.uim.lineEdit.setReadOnly(True)
		self.ui4.uim.lineEdit_2.setReadOnly(True)
		self.ui4.uim.lineEdit_3.setReadOnly(True)
		self.ui4.uim.lineEdit_4.setReadOnly(True)
		self.ui4.uim.lineEdit_5.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui5.uim.lineEdit.setReadOnly(True)
		self.ui5.uim.lineEdit_2.setReadOnly(True)
		self.ui5.uim.lineEdit_3.setReadOnly(True)
		self.ui5.uim.lineEdit_4.setReadOnly(True)
		self.ui5.uim.lineEdit_5.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui6.uim.lineEdit.setReadOnly(True)
		self.ui6.uim.lineEdit_2.setReadOnly(True)
		self.ui6.uim.lineEdit_3.setReadOnly(True)
		self.ui6.uim.lineEdit_4.setReadOnly(True)
		self.ui6.uim.lineEdit_5.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui7.uim.lineEdit.setReadOnly(True)
		self.ui7.uim.lineEdit_2.setReadOnly(True)
		self.ui7.uim.lineEdit_3.setReadOnly(True)
		self.ui7.uim.lineEdit_4.setReadOnly(True)
		self.ui7.uim.lineEdit_5.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui8.uim.lineEdit.setReadOnly(True)
		self.ui8.uim.lineEdit_2.setReadOnly(True)
		self.ui8.uim.lineEdit_3.setReadOnly(True)
		self.ui8.uim.lineEdit_4.setReadOnly(True)
		self.ui8.uim.lineEdit_5.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui9.uim.lineEdit.setReadOnly(True)
		self.ui9.uim.lineEdit_2.setReadOnly(True)
		self.ui9.uim.lineEdit_3.setReadOnly(True)
		self.ui9.uim.lineEdit_4.setReadOnly(True)
		self.ui9.uim.lineEdit_5.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui10.uim.lineEdit.setReadOnly(True)
		self.ui10.uim.lineEdit_2.setReadOnly(True)
		self.ui10.uim.lineEdit_3.setReadOnly(True)
		self.ui10.uim.lineEdit_4.setReadOnly(True)
		self.ui10.uim.lineEdit_5.setReadOnly(True)
		
#_______________________________________________________________________	
	#function to update Train Statistics (Mass, Pass & Crew count)
	def update_TrainStat(self):
		#Check which train to update
		if(self.TrainNum1 == 1):
			#Update pass_count
			self.ui1.uim.lineEdit_6.setText(str(self.pass_count1))
			#Update crew_count
			self.ui1.uim.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy1 = pass_crew_count(self.pass_count1, self.crew_count)
			self.total_mass = ((self.Occupancy1*56.699)/2000) + self.Mass_Empty
			self.ui1.uim.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		if(self.TrainNum2 == 1):
			#Update pass_count
			self.ui2.uim.lineEdit_6.setText(str(self.pass_count2))
			#Update crew_count
			self.ui2.uim.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy2 = pass_crew_count(self.pass_count2, self.crew_count)
			self.total_mass = ((self.Occupancy2*56.699)/2000) + self.Mass_Empty
			self.ui2.uim.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		if(self.TrainNum3 == 1):
			#Update pass_count
			self.ui3.uim.lineEdit_6.setText(str(self.pass_count3))
			#Update crew_count
			self.ui3.uim.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy3 = pass_crew_count(self.pass_count3, self.crew_count)
			self.total_mass = ((self.Occupancy3*56.699)/2000) + self.Mass_Empty
			self.ui3.uim.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		if(self.TrainNum4 == 1):
			#Update pass_count
			self.ui4.uim.lineEdit_6.setText(str(self.pass_count4))
			#Update crew_count
			self.ui4.uim.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy4 = pass_crew_count(self.pass_count4, self.crew_count)
			self.total_mass = ((self.Occupancy4*56.699)/2000) + self.Mass_Empty
			self.ui4.uim.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		if(self.TrainNum5 == 1):
			#Update pass_count
			self.ui5.uim.lineEdit_6.setText(str(self.pass_count5))
			#Update crew_count
			self.ui5.uim.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy5 = pass_crew_count(self.pass_count5, self.crew_count)
			self.total_mass = ((self.Occupancy5*56.699)/2000) + self.Mass_Empty
			self.ui5.uim.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		if(self.TrainNum6 == 1):
			#Update pass_count
			self.ui6.uim.lineEdit_6.setText(str(self.pass_count6))
			#Update crew_count
			self.ui6.uim.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy6 = pass_crew_count(self.pass_count6, self.crew_count)
			self.total_mass = ((self.Occupancy6*56.699)/2000) + self.Mass_Empty
			self.ui6.uim.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		if(self.TrainNum7 == 1):
			#Update pass_count
			self.ui7.uim.lineEdit_6.setText(str(self.pass_count7))
			#Update crew_count
			self.ui7.uim.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy7 = pass_crew_count(self.pass_count7, self.crew_count)
			self.total_mass = ((self.Occupancy7*56.699)/2000) + self.Mass_Empty
			self.ui7.uim.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		if(self.TrainNum8 == 1):
			#Update pass_count
			self.ui8.uim.lineEdit_6.setText(str(self.pass_count8))
			#Update crew_count
			self.ui8.uim.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy8 = pass_crew_count(self.pass_count8, self.crew_count)
			self.total_mass = ((self.Occupancy8*56.699)/2000) + self.Mass_Empty
			self.ui8.uim.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		if(self.TrainNum9 == 1):
			#Update pass_count
			self.ui9.uim.lineEdit_6.setText(str(self.pass_count9))
			#Update crew_count
			self.ui9.uim.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy9 = pass_crew_count(self.pass_count9, self.crew_count)
			self.total_mass = ((self.Occupancy9*56.699)/2000) + self.Mass_Empty
			self.ui9.uim.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		if(self.TrainNum10 == 1):
			#Update pass_count
			self.ui10.uim.lineEdit_6.setText(str(self.pass_count10))
			#Update crew_count
			self.ui10.uim.lineEdit_7.setText(str(self.crew_count))
			#Update current Mass of Train
			self.Occupancy10 = pass_crew_count(self.pass_count10, self.crew_count)
			self.total_mass = ((self.Occupancy10*56.699)/2000) + self.Mass_Empty
			self.ui10.uim.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		#____________________________________
		
		#Don't allow changes to lineEdits
		self.ui1.uim.lineEdit_6.setReadOnly(True)
		self.ui1.uim.lineEdit_7.setReadOnly(True)
		self.ui1.uim.lineEdit_8.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui2.uim.lineEdit_6.setReadOnly(True)
		self.ui2.uim.lineEdit_7.setReadOnly(True)
		self.ui2.uim.lineEdit_8.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui3.uim.lineEdit_6.setReadOnly(True)
		self.ui3.uim.lineEdit_7.setReadOnly(True)
		self.ui3.uim.lineEdit_8.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui4.uim.lineEdit_6.setReadOnly(True)
		self.ui4.uim.lineEdit_7.setReadOnly(True)
		self.ui4.uim.lineEdit_8.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui5.uim.lineEdit_6.setReadOnly(True)
		self.ui5.uim.lineEdit_7.setReadOnly(True)
		self.ui5.uim.lineEdit_8.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui6.uim.lineEdit_6.setReadOnly(True)
		self.ui6.uim.lineEdit_7.setReadOnly(True)
		self.ui6.uim.lineEdit_8.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui7.uim.lineEdit_6.setReadOnly(True)
		self.ui7.uim.lineEdit_7.setReadOnly(True)
		self.ui7.uim.lineEdit_8.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui8.uim.lineEdit_6.setReadOnly(True)
		self.ui8.uim.lineEdit_7.setReadOnly(True)
		self.ui8.uim.lineEdit_8.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui9.uim.lineEdit_6.setReadOnly(True)
		self.ui9.uim.lineEdit_7.setReadOnly(True)
		self.ui9.uim.lineEdit_8.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui10.uim.lineEdit_6.setReadOnly(True)
		self.ui10.uim.lineEdit_7.setReadOnly(True)
		self.ui10.uim.lineEdit_8.setReadOnly(True)
		
#_______________________________________________________________________
	#function to update Route Information and Train Internal Controls
	def update_RouteInfo(self):
		#Update Route Information based on Train Number
		if(self.TrainNum1 == 1):
			#Check Beacon ID each time
			signals.tkm_get_beacon.connect(self.SetBeaconID)
			signals.tkm_get_pass_count.connect(self.SetOccupancy)
			#Update Train Numbering Header
			self.ui1.uim.label_23.setText(self.train1)
			#Update Route Line
			self.ui1.uim.lineEdit_9.setText(self.RouteName1)
			#Update Current and Next Station based on Line and direction
			self.ui1.uim.lineEdit_19.setText(self.CurrStation1)
			self.ui1.uim.lineEdit_10.setText(self.NextStation1)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor1 == True or self.RightDoor1 == True):
				self.DoorStatus1 = True
			if(self.DoorStatus1 == False):
				self.ui1.uim.lineEdit_11.setText("Closed")
				self.Brake1 = False
			elif(self.DoorStatus1 == True):
				self.ui1.uim.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(1)
				self.Brake1 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui1.uim.lineEdit_12.setText("Waiting")
			else:
				self.ui1.uim.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin1,1)
			
			#update Cabin Lights status
			if (self.lights_Cab1 == False):
				self.ui1.uim.lineEdit_13.setText("Off")
			else:
				self.ui1.uim.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High1 == False):
				self.ui1.uim.lineEdit_14.setText("Off")
			else:
				self.ui1.uim.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun1 == False):
				self.ui1.uim.lineEdit_15.setText("Off")
			else:
				self.ui1.uim.lineEdit_15.setText("On")
			#____________________________________________________________________
		if(self.TrainNum2 == 1):
			#Check Beacon ID each time
			signals.tkm_get_beacon.connect(self.SetBeaconID)
			#Update Train Numbering Header
			self.ui2.uim.label_23.setText(self.train2)
			#Update Route Line
			self.ui2.uim.lineEdit_9.setText(self.RouteName2)
			#Update Current and Next Station based on Line and direction
			self.ui2.uim.lineEdit_19.setText(self.CurrStation2)
			self.ui2.uim.lineEdit_10.setText(self.NextStation2)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor2 == True or self.RightDoor2 == True):
				self.DoorStatus2 = True
				signals.tkm_get_pass_count.connect(self.SetOccupancy)
			if (self.DoorStatus2 == False):
				self.ui2.uim.lineEdit_11.setText("Closed")
				self.Brake2 = False
			elif(self.DoorStatus2 == True):
				self.ui2.uim.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(2)
				self.Brake2 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui2.uim.lineEdit_12.setText("Waiting")
			else:
				self.ui2.uim.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin2,2)
			
			#update Cabin Lights status
			if (self.lights_Cab2 == False):
				self.ui2.uim.lineEdit_13.setText("Off")
			else:
				self.ui2.uim.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High2 == False):
				self.ui2.uim.lineEdit_14.setText("Off")
			else:
				self.ui2.uim.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun2 == False):
				self.ui2.uim.lineEdit_15.setText("Off")
			else:
				self.ui2.uim.lineEdit_15.setText("On")
			#____________________________________________________________________
		if(self.TrainNum3 == 1):
			#Check Beacon ID each time
			signals.tkm_get_beacon.connect(self.SetBeaconID)
			#Update Train Numbering Header
			self.ui3.uim.label_23.setText(self.train3)
			#Update Route Line
			self.ui3.uim.lineEdit_9.setText(self.RouteName3)
			#Update Current and Next Station based on Line and direction
			self.ui3.uim.lineEdit_19.setText(self.CurrStation3)
			self.ui3.uim.lineEdit_10.setText(self.NextStation3)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor3 == True or self.RightDoor3 == True):
				self.DoorStatus3 = True
				signals.tkm_get_pass_count.connect(self.SetOccupancy)
			if (self.DoorStatus3 == False):
				self.ui3.uim.lineEdit_11.setText("Closed")
				self.Brake3 = False
			elif(self.DoorStatus3 == True):
				self.ui3.uim.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(3)
				self.Brake3 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui3.uim.lineEdit_12.setText("Waiting")
			else:
				self.ui3.uim.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin3,3)
			
			#update Cabin Lights status
			if (self.lights_Cab3 == False):
				self.ui3.uim.lineEdit_13.setText("Off")
			else:
				self.ui3.uim.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High3 == False):
				self.ui3.uim.lineEdit_14.setText("Off")
			else:
				self.ui3.uim.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun3 == False):
				self.ui3.uim.lineEdit_15.setText("Off")
			else:
				self.ui3.uim.lineEdit_15.setText("On")
			#____________________________________________________________________
		if(self.TrainNum4 == 1):
			#Check Beacon ID each time
			signals.tkm_get_beacon.connect(self.SetBeaconID)
			#Update Train Numbering Header
			self.ui4.uim.label_23.setText(self.train4)
			#Update Route Line
			self.ui4.uim.lineEdit_9.setText(self.RouteName4)
			#Update Current and Next Station based on Line and direction
			self.ui4.uim.lineEdit_19.setText(self.CurrStation4)
			self.ui4.uim.lineEdit_10.setText(self.NextStation4)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor4 == True or self.RightDoor4 == True):
				self.DoorStatus4 = True
				signals.tkm_get_pass_count.connect(self.SetOccupancy)
			if (self.DoorStatus4 == False):
				self.ui4.uim.lineEdit_11.setText("Closed")
				self.Brake4 = False
			elif(self.DoorStatus4 == True):
				self.ui4.uim.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(4)
				self.Brake4 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui4.uim.lineEdit_12.setText("Waiting")
			else:
				self.ui4.uim.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin4,4)
			
			#update Cabin Lights status
			if (self.lights_Cab4 == False):
				self.ui4.uim.lineEdit_13.setText("Off")
			else:
				self.ui4.uim.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High4 == False):
				self.ui4.uim.lineEdit_14.setText("Off")
			else:
				self.ui4.uim.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun4 == False):
				self.ui4.uim.lineEdit_15.setText("Off")
			else:
				self.ui4.uim.lineEdit_15.setText("On")
			#____________________________________________________________________
		if(self.TrainNum5 == 1):
			#Check Beacon ID each time
			signals.tkm_get_beacon.connect(self.SetBeaconID)
			#Update Train Numbering Header
			self.ui5.uim.label_23.setText(self.train5)
			#Update Route Line
			self.ui5.uim.lineEdit_9.setText(self.RouteName5)
			#Update Current and Next Station based on Line and direction
			self.ui5.uim.lineEdit_19.setText(self.CurrStation5)
			self.ui5.uim.lineEdit_10.setText(self.NextStation5)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor5 == True or self.RightDoor5 == True):
				self.DoorStatus5 = True
				signals.tkm_get_pass_count.connect(self.SetOccupancy)
			if (self.DoorStatus5 == False):
				self.ui5.uim.lineEdit_11.setText("Closed")
				self.Brake5 = False
			elif(self.DoorStatus5 == True):
				self.ui5.uim.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(5)
				self.Brake5 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui5.uim.lineEdit_12.setText("Waiting")
			else:
				self.ui5.uim.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin5,5)
			
			#update Cabin Lights status
			if (self.lights_Cab5 == False):
				self.ui5.uim.lineEdit_13.setText("Off")
			else:
				self.ui5.uim.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High5 == False):
				self.ui5.uim.lineEdit_14.setText("Off")
			else:
				self.ui5.uim.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun5 == False):
				self.ui5.uim.lineEdit_15.setText("Off")
			else:
				self.ui5.uim.lineEdit_15.setText("On")
			#____________________________________________________________________
		if(self.TrainNum6 == 1):
			#Check Beacon ID each time
			signals.tkm_get_beacon.connect(self.SetBeaconID)
			#Update Train Numbering Header
			self.ui6.uim.label_23.setText(self.train6)
			#Update Route Line
			self.ui6.uim.lineEdit_9.setText(self.RouteName6)
			#Update Current and Next Station based on Line and direction
			self.ui6.uim.lineEdit_19.setText(self.CurrStation6)
			self.ui6.uim.lineEdit_10.setText(self.NextStation6)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor6 == True or self.RightDoor6 == True):
				self.DoorStatus6 = True
				signals.tkm_get_pass_count.connect(self.SetOccupancy)
			if (self.DoorStatus6 == False):
				self.ui6.uim.lineEdit_11.setText("Closed")
				self.Brake6 = False
			elif(self.DoorStatus6 == True):
				self.ui6.uim.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(6)
				self.Brake6 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui6.uim.lineEdit_12.setText("Waiting")
			else:
				self.ui6.uim.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin6,6)
			
			#update Cabin Lights status
			if (self.lights_Cab6 == False):
				self.ui6.uim.lineEdit_13.setText("Off")
			else:
				self.ui6.uim.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High6 == False):
				self.ui6.uim.lineEdit_14.setText("Off")
			else:
				self.ui6.uim.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun6 == False):
				self.ui6.uim.lineEdit_15.setText("Off")
			else:
				self.ui6.uim.lineEdit_15.setText("On")
			#____________________________________________________________________
		if(self.TrainNum7 == 1):
			#Check Beacon ID each time
			signals.tkm_get_beacon.connect(self.SetBeaconID)
			#Update Train Numbering Header
			self.ui7.uim.label_23.setText(self.train7)
			#Update Route Line
			self.ui7.uim.lineEdit_9.setText(self.RouteName7)
			#Update Current and Next Station based on Line and direction
			self.ui7.uim.lineEdit_19.setText(self.CurrStation7)
			self.ui7.uim.lineEdit_10.setText(self.NextStation7)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor7 == True or self.RightDoor7 == True):
				self.DoorStatus7 = True
				signals.tkm_get_pass_count.connect(self.SetOccupancy)
			if (self.DoorStatus7 == False):
				self.ui7.uim.lineEdit_11.setText("Closed")
				self.Brake7 = False
			elif(self.DoorStatus7 == True):
				self.ui7.uim.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(7)
				self.Brake7 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui7.uim.lineEdit_12.setText("Waiting")
			else:
				self.ui7.uim.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin7,7)
			
			#update Cabin Lights status
			if (self.lights_Cab7 == False):
				self.ui7.uim.lineEdit_13.setText("Off")
			else:
				self.ui7.uim.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High7 == False):
				self.ui7.uim.lineEdit_14.setText("Off")
			else:
				self.ui7.uim.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun7 == False):
				self.ui7.uim.lineEdit_15.setText("Off")
			else:
				self.ui7.uim.lineEdit_15.setText("On")
			#____________________________________________________________________
		if(self.TrainNum8 == 1):
			#Check Beacon ID each time
			signals.tkm_get_beacon.connect(self.SetBeaconID)
			#Update Train Numbering Header
			self.ui8.uim.label_23.setText(self.train8)
			#Update Route Line
			self.ui8.uim.lineEdit_9.setText(self.RouteName8)
			#Update Current and Next Station based on Line and direction
			self.ui8.uim.lineEdit_19.setText(self.CurrStation8)
			self.ui8.uim.lineEdit_10.setText(self.NextStation8)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor8 == True or self.RightDoor8 == True):
				self.DoorStatus8 = True
				signals.tkm_get_pass_count.connect(self.SetOccupancy)
			if (self.DoorStatus8 == False):
				self.ui8.uim.lineEdit_11.setText("Closed")
				self.Brake8 = False
			elif(self.DoorStatus8 == True):
				self.ui8.uim.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(8)
				self.Brake8 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui8.uim.lineEdit_12.setText("Waiting")
			else:
				self.ui8.uim.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin8,8)
			
			#update Cabin Lights status
			if (self.lights_Cab8 == False):
				self.ui8.uim.lineEdit_13.setText("Off")
			else:
				self.ui8.uim.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High8 == False):
				self.ui8.uim.lineEdit_14.setText("Off")
			else:
				self.ui8.uim.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun8 == False):
				self.ui8.uim.lineEdit_15.setText("Off")
			else:
				self.ui8.uim.lineEdit_15.setText("On")
			#____________________________________________________________________
		if(self.TrainNum9 == 1):
			#Check Beacon ID each time
			signals.tkm_get_beacon.connect(self.SetBeaconID)
			#Update Train Numbering Header
			self.ui9.uim.label_23.setText(self.train9)
			#Update Route Line
			self.ui9.uim.lineEdit_9.setText(self.RouteName9)
			#Update Current and Next Station based on Line and direction
			self.ui9.uim.lineEdit_19.setText(self.CurrStation9)
			self.ui9.uim.lineEdit_10.setText(self.NextStation9)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor9 == True or self.RightDoor9 == True):
				self.DoorStatus9 = True
				signals.tkm_get_pass_count.connect(self.SetOccupancy)
			if (self.DoorStatus9 == False):
				self.ui9.uim.lineEdit_11.setText("Closed")
				self.Brake9 = False
			elif(self.DoorStatus9 == True):
				self.ui9.uim.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(9)
				self.Brake9 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui9.uim.lineEdit_12.setText("Waiting")
			else:
				self.ui9.uim.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin9,9)
			
			#update Cabin Lights status
			if (self.lights_Cab9 == False):
				self.ui9.uim.lineEdit_13.setText("Off")
			else:
				self.ui9.uim.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High9 == False):
				self.ui9.uim.lineEdit_14.setText("Off")
			else:
				self.ui9.uim.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun9 == False):
				self.ui9.uim.lineEdit_15.setText("Off")
			else:
				self.ui9.uim.lineEdit_15.setText("On")
			#____________________________________________________________________
		if(self.TrainNum10 == 1):
			#Check Beacon ID each time
			signals.tkm_get_beacon.connect(self.SetBeaconID)
			#Update Train Numbering Header
			self.ui10.uim.label_23.setText(self.train10)
			#Update Route Line
			self.ui10.uim.lineEdit_9.setText(self.RouteName10)
			#Update Current and Next Station based on Line and direction
			self.ui10.uim.lineEdit_19.setText(self.CurrStation10)
			self.ui10.uim.lineEdit_10.setText(self.NextStation10)
			
			#Update Doors Status		#Doors will be held open for one minute
			if(self.LeftDoor10 == True or self.RightDoor10 == True):
				self.DoorStatus10 = True
				signals.tkm_get_pass_count.connect(self.SetOccupancy)
			if (self.DoorStatus10 == False):
				self.ui10.uim.lineEdit_11.setText("Closed")
				self.Brake10 = False
			elif(self.DoorStatus10 == True):
				self.ui10.uim.lineEdit_11.setText("Open")
				signals.tnm_train_stop_num.emit(10)
				self.Brake10 = True
				
			#Update Beacon ID Status
			if (self.BeaconIDStatus == False):
				self.ui10.uim.lineEdit_12.setText("Waiting")
			else:
				self.ui10.uim.lineEdit_12.setText("Recieved")
				signals.tnm_beaconID.emit(self.beacon_bin10,10)
			
			#update Cabin Lights status
			if (self.lights_Cab10 == False):
				self.ui10.uim.lineEdit_13.setText("Off")
			else:
				self.ui10.uim.lineEdit_13.setText("On")
			#update High Beam Lights status
			if (self.lights_High10 == False):
				self.ui10.uim.lineEdit_14.setText("Off")
			else:
				self.ui10.uim.lineEdit_14.setText("On")
			#update Tunnel Lights status
			if (self.lights_Tun10 == False):
				self.ui10.uim.lineEdit_15.setText("Off")
			else:
				self.ui10.uim.lineEdit_15.setText("On")
			#____________________________________________________________________
		
		#Don't allow changes to lineEdits
		self.ui1.uim.lineEdit_9.setReadOnly(True)
		self.ui1.uim.lineEdit_10.setReadOnly(True)
		self.ui1.uim.lineEdit_11.setReadOnly(True)
		self.ui1.uim.lineEdit_12.setReadOnly(True)
		self.ui1.uim.lineEdit_13.setReadOnly(True)
		self.ui1.uim.lineEdit_14.setReadOnly(True)
		self.ui1.uim.lineEdit_15.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui2.uim.lineEdit_9.setReadOnly(True)
		self.ui2.uim.lineEdit_10.setReadOnly(True)
		self.ui2.uim.lineEdit_11.setReadOnly(True)
		self.ui2.uim.lineEdit_12.setReadOnly(True)
		self.ui2.uim.lineEdit_13.setReadOnly(True)
		self.ui2.uim.lineEdit_14.setReadOnly(True)
		self.ui2.uim.lineEdit_15.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui3.uim.lineEdit_9.setReadOnly(True)
		self.ui3.uim.lineEdit_10.setReadOnly(True)
		self.ui3.uim.lineEdit_11.setReadOnly(True)
		self.ui3.uim.lineEdit_12.setReadOnly(True)
		self.ui3.uim.lineEdit_13.setReadOnly(True)
		self.ui3.uim.lineEdit_14.setReadOnly(True)
		self.ui3.uim.lineEdit_15.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui4.uim.lineEdit_9.setReadOnly(True)
		self.ui4.uim.lineEdit_10.setReadOnly(True)
		self.ui4.uim.lineEdit_11.setReadOnly(True)
		self.ui4.uim.lineEdit_12.setReadOnly(True)
		self.ui4.uim.lineEdit_13.setReadOnly(True)
		self.ui4.uim.lineEdit_14.setReadOnly(True)
		self.ui4.uim.lineEdit_15.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui5.uim.lineEdit_9.setReadOnly(True)
		self.ui5.uim.lineEdit_10.setReadOnly(True)
		self.ui5.uim.lineEdit_11.setReadOnly(True)
		self.ui5.uim.lineEdit_12.setReadOnly(True)
		self.ui5.uim.lineEdit_13.setReadOnly(True)
		self.ui5.uim.lineEdit_14.setReadOnly(True)
		self.ui5.uim.lineEdit_15.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui6.uim.lineEdit_9.setReadOnly(True)
		self.ui6.uim.lineEdit_10.setReadOnly(True)
		self.ui6.uim.lineEdit_11.setReadOnly(True)
		self.ui6.uim.lineEdit_12.setReadOnly(True)
		self.ui6.uim.lineEdit_13.setReadOnly(True)
		self.ui6.uim.lineEdit_14.setReadOnly(True)
		self.ui6.uim.lineEdit_15.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui7.uim.lineEdit_9.setReadOnly(True)
		self.ui7.uim.lineEdit_10.setReadOnly(True)
		self.ui7.uim.lineEdit_11.setReadOnly(True)
		self.ui7.uim.lineEdit_12.setReadOnly(True)
		self.ui7.uim.lineEdit_13.setReadOnly(True)
		self.ui7.uim.lineEdit_14.setReadOnly(True)
		self.ui7.uim.lineEdit_15.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui8.uim.lineEdit_9.setReadOnly(True)
		self.ui8.uim.lineEdit_10.setReadOnly(True)
		self.ui8.uim.lineEdit_11.setReadOnly(True)
		self.ui8.uim.lineEdit_12.setReadOnly(True)
		self.ui8.uim.lineEdit_13.setReadOnly(True)
		self.ui8.uim.lineEdit_14.setReadOnly(True)
		self.ui8.uim.lineEdit_15.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui9.uim.lineEdit_9.setReadOnly(True)
		self.ui9.uim.lineEdit_10.setReadOnly(True)
		self.ui9.uim.lineEdit_11.setReadOnly(True)
		self.ui9.uim.lineEdit_12.setReadOnly(True)
		self.ui9.uim.lineEdit_13.setReadOnly(True)
		self.ui9.uim.lineEdit_14.setReadOnly(True)
		self.ui9.uim.lineEdit_15.setReadOnly(True)
		#Don't allow changes to lineEdits
		self.ui10.uim.lineEdit_9.setReadOnly(True)
		self.ui10.uim.lineEdit_10.setReadOnly(True)
		self.ui10.uim.lineEdit_11.setReadOnly(True)
		self.ui10.uim.lineEdit_12.setReadOnly(True)
		self.ui10.uim.lineEdit_13.setReadOnly(True)
		self.ui10.uim.lineEdit_14.setReadOnly(True)
		self.ui10.uim.lineEdit_15.setReadOnly(True)
			
#_______________________________________________________________________			
	#function to delegate variables when Emergency Brake triggered
	def EmergencyBraking(self):
		if(self.TrainNum1 == 1):
			if not self.eBrake1:
				self.ui1.uim.pushButton.setText("CANCEL")
				self.ui1.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake1 = True
				signals.tnm_ebrake.emit(self.eBrake1,1)
				print("eBrake is " + str(self.eBrake1))
			else:
				self.ui1.uim.pushButton.setText("Emergency Brake")
				self.ui1.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake1 = False
				signals.tnm_ebrake.emit(self.eBrake1,1)
		#______________________________________
		if(self.TrainNum2 == 1):
			if not self.eBrake2:
				self.ui2.uim.pushButton.setText("CANCEL")
				self.ui2.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake2 = True
				signals.tnm_ebrake.emit(self.eBrake2,2)
				print("eBrake is " + str(self.eBrake2))
			else:
				self.ui2.uim.pushButton.setText("Emergency Brake")
				self.ui2.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake2 = False
				signals.tnm_ebrake.emit(self.eBrake2,2)
		#______________________________________
		if(self.TrainNum3 == 1):
			if not self.eBrake3:
				self.ui3.uim.pushButton.setText("CANCEL")
				self.ui3.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake3 = True
				signals.tnm_ebrake.emit(self.eBrake3,3)
				print("eBrake is " + str(self.eBrake3))
			else:
				self.ui3.uim.pushButton.setText("Emergency Brake")
				self.ui3.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake3 = False
				signals.tnm_ebrake.emit(self.eBrake3,3)
		#______________________________________
		if(self.TrainNum4 == 1):
			if not self.eBrake4:
				self.ui4.uim.pushButton.setText("CANCEL")
				self.ui4.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake4 = True
				signals.tnm_ebrake.emit(self.eBrake4,4)
				print("eBrake is " + str(self.eBrake4))
			else:
				self.ui4.uim.pushButton.setText("Emergency Brake")
				self.ui4.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake4 = False
				signals.tnm_ebrake.emit(self.eBrake4,4)
		#______________________________________
		if(self.TrainNum5 == 1):
			if not self.eBrake5:
				self.ui5.uim.pushButton.setText("CANCEL")
				self.ui5.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake5 = True
				signals.tnm_ebrake.emit(self.eBrake5,5)
				print("eBrake is " + str(self.eBrake5))
			else:
				self.ui5.uim.pushButton.setText("Emergency Brake")
				self.ui5.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake5 = False
				signals.tnm_ebrake.emit(self.eBrake5,5)
		#______________________________________
		if(self.TrainNum6 == 1):
			if not self.eBrake6:
				self.ui6.uim.pushButton.setText("CANCEL")
				self.ui6.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake6 = True
				signals.tnm_ebrake.emit(self.eBrake6,6)
				print("eBrake is " + str(self.eBrake6))
			else:
				self.ui6.uim.pushButton.setText("Emergency Brake")
				self.ui6.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake6 = False
				signals.tnm_ebrake.emit(self.eBrake6,6)
		#______________________________________
		if(self.TrainNum7 == 1):
			if not self.eBrake7:
				self.ui7.uim.pushButton.setText("CANCEL")
				self.ui7.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake7 = True
				signals.tnm_ebrake.emit(self.eBrake7,7)
				print("eBrake is " + str(self.eBrake7))
			else:
				self.ui7.uim.pushButton.setText("Emergency Brake")
				self.ui7.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake7 = False
				signals.tnm_ebrake.emit(self.eBrake7,7)
		#______________________________________
		if(self.TrainNum8 == 1):
			if not self.eBrake8:
				self.ui8.uim.pushButton.setText("CANCEL")
				self.ui8.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake8 = True
				signals.tnm_ebrake.emit(self.eBrake8,8)
				print("eBrake is " + str(self.eBrake8))
			else:
				self.ui8.uim.pushButton.setText("Emergency Brake")
				self.ui8.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake8 = False
				signals.tnm_ebrake.emit(self.eBrake8,8)
		#_____________________________________
		if(self.TrainNum9 == 1):
			if not self.eBrake9:
				self.ui9.uim.pushButton.setText("CANCEL")
				self.ui9.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake9 = True
				signals.tnm_ebrake.emit(self.eBrake9,9)
				print("eBrake is " + str(self.eBrake9))
			else:
				self.ui9.uim.pushButton.setText("Emergency Brake")
				self.ui9.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake9 = False
				signals.tnm_ebrake.emit(self.eBrake9,9)
		#_____________________________________
		if(self.TrainNum10 == 1):
			if not self.eBrake10:
				self.ui10.uim.pushButton.setText("CANCEL")
				self.ui10.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
				self.eBrake10 = True
				signals.tnm_ebrake.emit(self.eBrake10,10)
				print("eBrake is " + str(self.eBrake10))
			else:
				self.ui10.uim.pushButton.setText("Emergency Brake")
				self.ui10.uim.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
				self.eBrake10 = False
				signals.tnm_ebrake.emit(self.eBrake10,10)
		#_____________________________________
		
#_______________________________________________________________________
	#function to Update Current Temperature of the cabin
	def Temperature(self):
		#Update Temperature based on Train Number
		if(self.TrainNum1 == 1):
			AlphaFlag1 = False
			#Error checking to make sure input is only an INT
			for i in self.ui1.uim.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag1 = True
			if(AlphaFlag1 == True):
				self.ui1.uim.lineEdit_17.setText(str(self.curr_temp1))
				self.set_temp1 = self.curr_temp1
			elif(self.ui1.uim.lineEdit_17.text().isdigit() == True):
				AlphaFlag1 = False
				self.set_temp1 = int(self.ui1.uim.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui1.uim.lineEdit_16.setText(str(temp_control(self.set_temp1, self.curr_temp1)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp1)
			#_______________________________________________________________
		if(self.TrainNum2 == 1):
			AlphaFlag2 = False
			#Error checking to make sure input is only an INT
			for i in self.ui2.uim.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag2 = True
			if(AlphaFlag2 == True):
				self.ui2.uim.lineEdit_17.setText(str(self.curr_temp2))
				self.set_temp2 = self.curr_temp2
			elif(self.ui2.uim.lineEdit_17.text().isdigit() == True):
				AlphaFlag2 = False
				self.set_temp2 = int(self.ui2.uim.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui2.uim.lineEdit_16.setText(str(temp_control(self.set_temp2, self.curr_temp2)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp2)
			#_______________________________________________________________
		if(self.TrainNum3 == 1):
			AlphaFlag3 = False
			#Error checking to make sure input is only an INT
			for i in self.ui3.uim.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag3 = True
			if(AlphaFlag3 == True):
				self.ui3.uim.lineEdit_17.setText(str(self.curr_temp3))
				self.set_temp3 = self.curr_temp3
			elif(self.ui3.uim.lineEdit_17.text().isdigit() == True):
				AlphaFlag3 = False
				self.set_temp3 = int(self.ui3.uim.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui3.uim.lineEdit_16.setText(str(temp_control(self.set_temp3, self.curr_temp3)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp3)
			#_______________________________________________________________
		if(self.TrainNum4 == 1):
			AlphaFlag4 = False
			#Error checking to make sure input is only an INT
			for i in self.ui4.uim.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag4 = True
			if(AlphaFlag4 == True):
				self.ui4.uim.lineEdit_17.setText(str(self.curr_temp4))
				self.set_temp4 = self.curr_temp4
			elif(self.ui4.uim.lineEdit_17.text().isdigit() == True):
				AlphaFlag4 = False
				self.set_temp4 = int(self.ui4.uim.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui4.uim.lineEdit_16.setText(str(temp_control(self.set_temp4, self.curr_temp4)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp4)
			#_______________________________________________________________
		if(self.TrainNum5 == 1):
			AlphaFlag5 = False
			#Error checking to make sure input is only an INT
			for i in self.ui5.uim.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag5 = True
			if(AlphaFlag5 == True):
				self.ui5.uim.lineEdit_17.setText(str(self.curr_temp5))
				self.set_temp5 = self.curr_temp5
			elif(self.ui5.uim.lineEdit_17.text().isdigit() == True):
				AlphaFlag5 = False
				self.set_temp5 = int(self.ui5.uim.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui5.uim.lineEdit_16.setText(str(temp_control(self.set_temp5, self.curr_temp5)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp5)
			#_______________________________________________________________
		if(self.TrainNum6 == 1):
			AlphaFlag6 = False
			#Error checking to make sure input is only an INT
			for i in self.ui6.uim.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag6 = True
			if(AlphaFlag6 == True):
				self.ui6.uim.lineEdit_17.setText(str(self.curr_temp6))
				self.set_temp6 = self.curr_temp6
			elif(self.ui6.uim.lineEdit_17.text().isdigit() == True):
				AlphaFlag6 = False
				self.set_temp6 = int(self.ui6.uim.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui6.uim.lineEdit_16.setText(str(temp_control(self.set_temp6, self.curr_temp6)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp6)
			#_______________________________________________________________
		if(self.TrainNum7 == 1):
			AlphaFlag7 = False
			#Error checking to make sure input is only an INT
			for i in self.ui7.uim.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag7 = True
			if(AlphaFlag7 == True):
				self.ui7.uim.lineEdit_17.setText(str(self.curr_temp7))
				self.set_temp7 = self.curr_temp7
			elif(self.ui7.uim.lineEdit_17.text().isdigit() == True):
				AlphaFlag7 = False
				self.set_temp7 = int(self.ui7.uim.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui7.uim.lineEdit_16.setText(str(temp_control(self.set_temp7, self.curr_temp7)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp7)
			#_______________________________________________________________
		if(self.TrainNum8 == 1):
			AlphaFlag8 = False
			#Error checking to make sure input is only an INT
			for i in self.ui8.uim.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag8 = True
			if(AlphaFlag8 == True):
				self.ui8.uim.lineEdit_17.setText(str(self.curr_temp8))
				self.set_temp8 = self.curr_temp8
			elif(self.ui8.uim.lineEdit_17.text().isdigit() == True):
				AlphaFlag8 = False
				self.set_temp8 = int(self.ui8.uim.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui8.uim.lineEdit_16.setText(str(temp_control(self.set_temp8, self.curr_temp8)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp8)
			#_______________________________________________________________
		if(self.TrainNum9 == 1):
			AlphaFlag9 = False
			#Error checking to make sure input is only an INT
			for i in self.ui9.uim.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag9 = True
			if(AlphaFlag9 == True):
				self.ui9.uim.lineEdit_17.setText(str(self.curr_temp9))
				self.set_temp9 = self.curr_temp9
			elif(self.ui9.uim.lineEdit_17.text().isdigit() == True):
				AlphaFlag9 = False
				self.set_temp9 = int(self.ui9.uim.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui9.uim.lineEdit_16.setText(str(temp_control(self.set_temp9, self.curr_temp9)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp9)
			#_______________________________________________________________
		if(self.TrainNum10 == 1):
			AlphaFlag10 = False
			#Error checking to make sure input is only an INT
			for i in self.ui10.uim.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag10 = True
			if(AlphaFlag10 == True):
				self.ui10.uim.lineEdit_17.setText(str(self.curr_temp10))
				self.set_temp10 = self.curr_temp10
			elif(self.ui10.uim.lineEdit_17.text().isdigit() == True):
				AlphaFlag10 = False
				self.set_temp10 = int(self.ui10.uim.lineEdit_17.text())
			
			#Use temp_control function to set the current temperature
			self.ui10.uim.lineEdit_16.setText(str(temp_control(self.set_temp10, self.curr_temp10)) + " F")
			#signals.tnm_cab_temp.emit(self.curr_temp10)
			#_______________________________________________________________
		
		#Don't allow time module to be edited
		self.ui1.uim.lineEdit_16.setReadOnly(True)
		#Don't allow time module to be edited
		self.ui2.uim.lineEdit_16.setReadOnly(True)
		#Don't allow time module to be edited
		self.ui3.uim.lineEdit_16.setReadOnly(True)
		#Don't allow time module to be edited
		self.ui4.uim.lineEdit_16.setReadOnly(True)
		#Don't allow time module to be edited
		self.ui5.uim.lineEdit_16.setReadOnly(True)
		#Don't allow time module to be edited
		self.ui6.uim.lineEdit_16.setReadOnly(True)
		#Don't allow time module to be edited
		self.ui7.uim.lineEdit_16.setReadOnly(True)
		#Don't allow time module to be edited
		self.ui8.uim.lineEdit_16.setReadOnly(True)
		#Don't allow time module to be edited
		self.ui9.uim.lineEdit_16.setReadOnly(True)
		#Don't allow time module to be edited
		self.ui10.uim.lineEdit_16.setReadOnly(True)
	
	#function for updating the current date and time widget
	def GetDatetime(self):
		if(self.TrainNum1 == 1):
			self.ui1.uim.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
			self.ui1.uim.dateTimeEdit.setDisplayFormat("MM/dd/yyyy hh:mm:ss")
			self.ui1.uim.dateTimeEdit.setReadOnly(True)
		if(self.TrainNum2 == 1):
			self.ui2.uim.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
			self.ui2.uim.dateTimeEdit.setDisplayFormat("MM/dd/yyyy hh:mm:ss")
			#Don't allow time module to be edited
			self.ui2.uim.dateTimeEdit.setReadOnly(True)
		if(self.TrainNum3 == 1):
			self.ui3.uim.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
			self.ui3.uim.dateTimeEdit.setDisplayFormat("MM/dd/yyyy hh:mm:ss")
			#Don't allow time module to be edited
			self.ui3.uim.dateTimeEdit.setReadOnly(True)
		if(self.TrainNum4 == 1):
			self.ui4.uim.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
			self.ui4.uim.dateTimeEdit.setDisplayFormat("MM/dd/yyyy hh:mm:ss")
			#Don't allow time module to be edited
			self.ui4.uim.dateTimeEdit.setReadOnly(True)
		if(self.TrainNum5 == 1):
			self.ui5.uim.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
			self.ui5.uim.dateTimeEdit.setDisplayFormat("MM/dd/yyyy hh:mm:ss")
			#Don't allow time module to be edited
			self.ui5.uim.dateTimeEdit.setReadOnly(True)
		if(self.TrainNum6 == 1):
			self.ui6.uim.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
			self.ui6.uim.dateTimeEdit.setDisplayFormat("MM/dd/yyyy hh:mm:ss")
			#Don't allow time module to be edited
			self.ui6.uim.dateTimeEdit.setReadOnly(True)
		if(self.TrainNum7 == 1):
			self.ui7.uim.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
			self.ui7.uim.dateTimeEdit.setDisplayFormat("MM/dd/yyyy hh:mm:ss")
			#Don't allow time module to be edited
			self.ui7.uim.dateTimeEdit.setReadOnly(True)
		if(self.TrainNum8 == 1):
			self.ui8.uim.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
			self.ui8.uim.dateTimeEdit.setDisplayFormat("MM/dd/yyyy hh:mm:ss")
			#Don't allow time module to be edited
			self.ui8.uim.dateTimeEdit.setReadOnly(True)
		if(self.TrainNum9 == 1):
			self.ui9.uim.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
			self.ui9.uim.dateTimeEdit.setDisplayFormat("MM/dd/yyyy hh:mm:ss")
			#Don't allow time module to be edited
			self.ui9.uim.dateTimeEdit.setReadOnly(True)
		if(self.TrainNum10 == 1):
			self.ui10.uim.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
			self.ui10.uim.dateTimeEdit.setDisplayFormat("MM/dd/yyyy hh:mm:ss")
			#Don't allow time module to be edited
			self.ui10.uim.dateTimeEdit.setReadOnly(True)

	#function for updating the internal train announcements
	def DispAnnounce(self):
		if(self.TrainNum1 == 1):
			self.ui1.uim.lineEdit_18.setText(self.announce1)
		if(self.TrainNum2 == 1):
			self.ui2.uim.lineEdit_18.setText(self.announce2)
		if(self.TrainNum3 == 1):
			self.ui3.uim.lineEdit_18.setText(self.announce3)
		if(self.TrainNum4 == 1):
			self.ui4.uim.lineEdit_18.setText(self.announce4)
		if(self.TrainNum5 == 1):
			self.ui5.uim.lineEdit_18.setText(self.announce5)
		if(self.TrainNum6 == 1):
			self.ui6.uim.lineEdit_18.setText(self.announce6)
		if(self.TrainNum7 == 1):
			self.ui7.uim.lineEdit_18.setText(self.announce7)
		if(self.TrainNum8 == 1):
			self.ui8.uim.lineEdit_18.setText(self.announce8)
		if(self.TrainNum9 == 1):
			self.ui9.uim.lineEdit_18.setText(self.announce9)
		if(self.TrainNum10 == 1):
			self.ui10.uim.lineEdit_18.setText(self.announce10)
	
		#Don't allow announcements text to be edited
		self.ui1.uim.lineEdit_18.setReadOnly(True)
		#Don't allow announcements text to be edited
		self.ui2.uim.lineEdit_18.setReadOnly(True)
		#Don't allow announcements text to be edited
		self.ui3.uim.lineEdit_18.setReadOnly(True)
		#Don't allow announcements text to be edited
		self.ui4.uim.lineEdit_18.setReadOnly(True)
		#Don't allow announcements text to be edited
		self.ui5.uim.lineEdit_18.setReadOnly(True)
		#Don't allow announcements text to be edited
		self.ui6.uim.lineEdit_18.setReadOnly(True)
		#Don't allow announcements text to be edited
		self.ui7.uim.lineEdit_18.setReadOnly(True)
		#Don't allow announcements text to be edited
		self.ui8.uim.lineEdit_18.setReadOnly(True)
		#Don't allow announcements text to be edited
		self.ui9.uim.lineEdit_18.setReadOnly(True)
		#Don't allow announcements text to be edited
		self.ui10.uim.lineEdit_18.setReadOnly(True)
		
#_______________________________________________________________________
	#Function to set power from tnc signal
	def SetPower(self,tnc_power, tncTrainNum):
		if(self.TrainNum1 == 1 and tncTrainNum == 1):
			self.curr_power1 = tnc_power
		elif(self.TrainNum2 == 1 and tncTrainNum == 2):
			self.curr_power2 = tnc_power
		elif(self.TrainNum3 == 1 and tncTrainNum == 3):
			self.curr_power3 = tnc_power
		elif(self.TrainNum4 == 1 and tncTrainNum == 4):
			self.curr_power4 = tnc_power
		elif(self.TrainNum5 == 1 and tncTrainNum == 5):
			self.curr_power5 = tnc_power
		elif(self.TrainNum6 == 1 and tncTrainNum == 6):
			self.curr_power6 = tnc_power
		elif(self.TrainNum7 == 1 and tncTrainNum == 7):
			self.curr_power7 = tnc_power
		elif(self.TrainNum8 == 1 and tncTrainNum == 8):
			self.curr_power8 = tnc_power
		elif(self.TrainNum9 == 1 and tncTrainNum == 9):
			self.curr_power9 = tnc_power
		elif(self.TrainNum10 == 1 and tncTrainNum == 10):
			self.curr_power10 = tnc_power
	
	#Function to set Beacon ID from track model signal
	def SetBeaconID(self,tkm_beacon, tncTrainNum):
		#beacon ID int set, then sent to Train Controller
		self.BeaconId = tkm_beacon
		#Check beacon ID based on Train Number For Green Line
		if(self.TrainNum1 == 1 and tncTrainNum == 1):
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
				signals.tnm_TrainDir.emit(self.TrainDirection1,1)
			elif(self.beacon_bin1[2] == 1):
				self.TrainDirection1 = 1
				signals.tnm_TrainDir.emit(self.TrainDirection1,1)
				
			#Call Beacon function to specify station
			if(self.RouteName1 == "Green Line"):
				self.CurrStation1, self.NextStation1, self.TNMdirectionG1 = GreenBeacon(self.RouteName1, self.TNMdirectionG1, self.TrainDirection1, self.beacon_bin1)
			elif(self.RouteName1 == "Red Line"):
				self.CurrStation1, self.NextStation1, self.TNMdirectionR1 = RedBeacon(self.RouteName1, self.TNMdirectionR1, self.TrainDirection1, self.beacon_bin1)
			signals.tnm_curr_station.emit(self.CurrStation1,1)
			#______________________________________________________________________
		elif(self.TrainNum2 == 1 and tncTrainNum == 2):
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
				signals.tnm_TrainDir.emit(self.TrainDirection2,2)
			elif(self.beacon_bin2[2] == 1):
				self.TrainDirection2 = 1
				signals.tnm_TrainDir.emit(self.TrainDirection2,2)
				
			#Call Beacon function to specify station
			if(self.RouteName2 == "Green Line"):
				self.CurrStation2, self.NextStation2, self.TNMdirectionG2 = GreenBeacon(self.RouteName2, self.TNMdirectionG2, self.TrainDirection2, self.beacon_bin2)
			elif(self.RouteName2 == "Red Line"):
				self.CurrStation2, self.NextStation2, self.TNMdirectionR2 = RedBeacon(self.RouteName2, self.TNMdirectionR2, self.TrainDirection2, self.beacon_bin2)		
			signals.tnm_curr_station.emit(self.CurrStation2,2)
			#______________________________________________________________________
		elif(self.TrainNum3 == 1 and tncTrainNum == 3):
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
				signals.tnm_TrainDir.emit(self.TrainDirection3,3)
			elif(self.beacon_bin3[2] == 1):
				self.TrainDirection3 = 1
				signals.tnm_TrainDir.emit(self.TrainDirection3,3)
				
			#Call Beacon function to specify station
			if(self.RouteName3 == "Green Line"):
				self.CurrStation3, self.NextStation3, self.TNMdirectionG3 = GreenBeacon(self.RouteName3, self.TNMdirectionG3, self.TrainDirection3, self.beacon_bin3)
			elif(self.RouteName3 == "Red Line"):
				self.CurrStation3, self.NextStation3, self.TNMdirectionR3 = GreenBeacon(self.RouteName3, self.TNMdirectionR3, self.TrainDirection3, self.beacon_bin3)
			signals.tnm_curr_station.emit(self.CurrStation3,3)
			#______________________________________________________________________
		elif(self.TrainNum4 == 1 and tncTrainNum == 4):
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
				signals.tnm_TrainDir.emit(self.TrainDirection4,4)
			elif(self.beacon_bin4[2] == 1):
				self.TrainDirection4 = 1
				signals.tnm_TrainDir.emit(self.TrainDirection4,4)
				
			#Call Beacon function to specify station
			if(self.RouteName4 == "Green Line"):
				self.CurrStation4, self.NextStation4, self.TNMdirectionG4 = GreenBeacon(self.RouteName4, self.TNMdirectionG4, self.TrainDirection4, self.beacon_bin4)
			elif(self.RouteName4 == "Red Line"):
				self.CurrStation4, self.NextStation4, self.TNMdirectionR4 = GreenBeacon(self.RouteName4, self.TNMdirectionR4, self.TrainDirection4, self.beacon_bin4)
			signals.tnm_curr_station.emit(self.CurrStation4,4)
			#______________________________________________________________________
		elif(self.TrainNum5 == 1 and tncTrainNum == 5):
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
				signals.tnm_TrainDir.emit(self.TrainDirection5,5)
			elif(self.beacon_bin5[2] == 1):
				self.TrainDirection5 = 1
				signals.tnm_TrainDir.emit(self.TrainDirection5,5)
				
			#Call Beacon function to specify station
			if(self.RouteName5 == "Green Line"):
				self.CurrStation5, self.NextStation5, self.TNMdirectionG5 = GreenBeacon(self.RouteName5, self.TNMdirectionG5, self.TrainDirection5, self.beacon_bin5)
			elif(self.RouteName5 == "Red Line"):
				self.CurrStation5, self.NextStation5, self.TNMdirectionR5 = GreenBeacon(self.RouteName5, self.TNMdirectionR5, self.TrainDirection5, self.beacon_bin5)
			signals.tnm_curr_station.emit(self.CurrStation5,5)
			#______________________________________________________________________
		elif(self.TrainNum6 == 1 and tncTrainNum == 6):
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
				signals.tnm_TrainDir.emit(self.TrainDirection6,6)
			elif(self.beacon_bin6[2] == 1):
				self.TrainDirection6 = 1
				signals.tnm_TrainDir.emit(self.TrainDirection6,6)
				
			#Call Beacon function to specify station
			if(self.RouteName6 == "Green Line"):
				self.CurrStation6, self.NextStation6, self.TNMdirectionG6 = GreenBeacon(self.RouteName6, self.TNMdirectionG6, self.TrainDirection6, self.beacon_bin6)
			elif(self.RouteName6 == "Red Line"):
				self.CurrStation6, self.NextStation6, self.TNMdirectionR6 = GreenBeacon(self.RouteName6, self.TNMdirectionR6, self.TrainDirection6, self.beacon_bin6)
			signals.tnm_curr_station.emit(self.CurrStation6,6)
			#______________________________________________________________________
		elif(self.TrainNum7 == 1 and tncTrainNum == 7):
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
				signals.tnm_TrainDir.emit(self.TrainDirection7,7)
			elif(self.beacon_bin7[2] == 1):
				self.TrainDirection7 = 1
				signals.tnm_TrainDir.emit(self.TrainDirection7,7)
				
			#Call Beacon function to specify station
			if(self.RouteName7 == "Green Line"):
				self.CurrStation7, self.NextStation7, self.TNMdirectionG7 = GreenBeacon(self.RouteName7, self.TNMdirectionG7, self.TrainDirection7, self.beacon_bin7)
			elif(self.RouteName7 == "Red Line"):
				self.CurrStation7, self.NextStation7, self.TNMdirectionR7 = GreenBeacon(self.RouteName7, self.TNMdirectionR7, self.TrainDirection7, self.beacon_bin7)
			signals.tnm_curr_station.emit(self.CurrStation7,7)
			#______________________________________________________________________
		elif(self.TrainNum8 == 1 and tncTrainNum == 8):
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
				signals.tnm_TrainDir.emit(self.TrainDirection8,8)
			elif(self.beacon_bin8[2] == 1):
				self.TrainDirection8 = 1
				signals.tnm_TrainDir.emit(self.TrainDirection8,8)
				
			#Call Beacon function to specify station
			if(self.RouteName8 == "Green Line"):
				self.CurrStation8, self.NextStation8, self.TNMdirectionG8 = GreenBeacon(self.RouteName8, self.TNMdirectionG8, self.TrainDirection8, self.beacon_bin8)
			elif(self.RouteName8 == "Red Line"):
				self.CurrStation8, self.NextStation8, self.TNMdirectionR8 = GreenBeacon(self.RouteName8, self.TNMdirectionR8, self.TrainDirection8, self.beacon_bin8)
			signals.tnm_curr_station.emit(self.CurrStation8,8)
			#______________________________________________________________________
		elif(self.TrainNum9 == 1 and tncTrainNum == 9):
			#Call function to append beacon
			self.beacon_bin9 = AppendBeacon(self.BeaconId)
		
			#check if first value is: 1 = green line/0 = red line #Was 2, 3, 4, 5:
			if(self.beacon_bin9[0] == 0):
				self.RouteName9 = "Red Line"
				self.CurrStation9 = "Yard"
				self.NextStation9 = "Shady Side"
			elif(self.beacon_bin9[0] == 1):
				self.RouteName9 = "Green Line"
				self.CurrStation9 = "Yard"
				self.NextStation9 = "Glenbury"
			#check if second value is: 0 = station/1 = underground
			if(self.beacon_bin9[1] == 0):
				self.lights_Tun9 == False
			elif(self.beacon_bin9[1] == 1):
				self.lights_Tun9 == True
			#3rd bit - 0 Left(decrement)/1 Right(increment) directionality
			#0 means left doors open, 1 means right doors open
			if(self.beacon_bin9[2] == 0):
				self.TrainDirection9 = 0
				signals.tnm_TrainDir.emit(self.TrainDirection9,9)
			elif(self.beacon_bin9[2] == 1):
				self.TrainDirection9 = 1
				signals.tnm_TrainDir.emit(self.TrainDirection9,9)
				
			#Call Beacon function to specify station
			if(self.RouteName9 == "Green Line"):
				self.CurrStation9, self.NextStation9, self.TNMdirectionG9 = GreenBeacon(self.RouteName9, self.TNMdirectionG9, self.TrainDirection9, self.beacon_bin9)
			elif(self.RouteName9 == "Red Line"):
				self.CurrStation9, self.NextStation9, self.TNMdirectionR9 = GreenBeacon(self.RouteName9, self.TNMdirectionR9, self.TrainDirection9, self.beacon_bin9)
			signals.tnm_curr_station.emit(self.CurrStation9,9)
			#______________________________________________________________________
		elif(self.TrainNum10 == 1 and tncTrainNum == 10):
			#Call function to append beacon
			self.beacon_bin10 = AppendBeacon(self.BeaconId)
		
			#check if first value is: 1 = green line/0 = red line #Was 2, 3, 4, 5:
			if(self.beacon_bin10[0] == 0):
				self.RouteName10 = "Red Line"
				self.CurrStation10 = "Yard"
				self.NextStation10 = "Shady Side"
			elif(self.beacon_bin10[0] == 1):
				self.RouteName10 = "Green Line"
				self.CurrStation10 = "Yard"
				self.NextStation10 = "Glenbury"
			#check if second value is: 0 = station/1 = underground
			if(self.beacon_bin10[1] == 0):
				self.lights_Tun10 == False
			elif(self.beacon_bin10[1] == 1):
				self.lights_Tun10 == True
			#3rd bit - 0 Left(decrement)/1 Right(increment) directionality
			#0 means left doors open, 1 means right doors open
			if(self.beacon_bin10[2] == 0):
				self.TrainDirection10 = 0
				signals.tnm_TrainDir.emit(self.TrainDirection10,10)
			elif(self.beacon_bin10[2] == 1):
				self.TrainDirection10 = 1
				signals.tnm_TrainDir.emit(self.TrainDirection10,10)
				
			#Call Beacon function to specify station
			if(self.RouteName10 == "Green Line"):
				self.CurrStation10, self.NextStation10, self.TNMdirectionG10 = GreenBeacon(self.RouteName10, self.TNMdirectionG10, self.TrainDirection10, self.beacon_bin10)
			elif(self.RouteName10 == "Red Line"):
				self.CurrStation10, self.NextStation10, self.TNMdirectionR10 = GreenBeacon(self.RouteName10, self.TNMdirectionR10, self.TrainDirection10, self.beacon_bin10)
			signals.tnm_curr_station.emit(self.CurrStation10,10)
			#______________________________________________________________________
	
	#Function to specify block number for each line
	def blockNum(self,BlockNum,tkmTrainNum):
		if(self.TrainNum1 == 1  and tkmTrainNum == 1):
			self.block_num1 = BlockNum
		elif(self.TrainNum2 == 1 and tkmTrainNum == 2):
			self.block_num2 = BlockNum
		elif(self.TrainNum3 == 1 and tkmTrainNum == 3):
			self.block_num3 = BlockNum
		elif(self.TrainNum4 == 1 and tkmTrainNum == 4):
			self.block_num4 = BlockNum
		elif(self.TrainNum5 == 1 and tkmTrainNum == 5):
			self.block_num5 = BlockNum
		elif(self.TrainNum6 == 1 and tkmTrainNum == 6):
			self.block_num6 = BlockNum
		elif(self.TrainNum7 == 1 and tkmTrainNum == 7):
			self.block_num7 = BlockNum
		elif(self.TrainNum8 == 1 and tkmTrainNum == 8):
			self.block_num8 = BlockNum
		elif(self.TrainNum9 == 1 and tkmTrainNum == 9):
			self.block_num9 = BlockNum
		elif(self.TrainNum10 == 1 and tkmTrainNum == 10):
			self.block_num10 = BlockNum
			
		
	#Function to take in block length and calculate when train reaches next block
	def blockLen(self, BlockLen,tkmTrainNum):
		#set variables based on Train Number
		if(self.TrainNum1 == 1 and tkmTrainNum == 1):
			self.block_length1 = BlockLen
		elif(self.TrainNum2 == 1 and tkmTrainNum == 2):
			self.block_length2 = BlockLen
		elif(self.TrainNum3 == 1 and tkmTrainNum == 3):
			self.block_length3 = BlockLen
		elif(self.TrainNum4 == 1 and tkmTrainNum == 4):
			self.block_length4 = BlockLen
		elif(self.TrainNum5 == 1 and tkmTrainNum == 5):
			self.block_length5 = BlockLen
		elif(self.TrainNum6 == 1 and tkmTrainNum == 6):
			self.block_length6 = BlockLen
		elif(self.TrainNum7 == 1 and tkmTrainNum == 7):
			self.block_length7 = BlockLen
		elif(self.TrainNum8 == 1 and tkmTrainNum == 8):
			self.block_length8 = BlockLen
		elif(self.TrainNum9 == 1 and tkmTrainNum == 9):
			self.block_length9 = BlockLen
		elif(self.TrainNum10 == 1 and tkmTrainNum == 10):
			self.block_length10 = BlockLen
			
	
	#Function to set Authority from track model signal
	def SetAuthority(self,tkm_authority,tkmTrainNum):
		if(self.TrainNum1 == 1 and tkmTrainNum == 1):
			self.block_authority1 = tkm_authority
		elif(self.TrainNum2 == 1 and tkmTrainNum == 2):
			self.block_authority2 = tkm_authority
		elif(self.TrainNum3 == 1 and tkmTrainNum == 3):
			self.block_authority3 = tkm_authority
		elif(self.TrainNum4 == 1 and tkmTrainNum == 4):
			self.block_authority4 = tkm_authority
		elif(self.TrainNum5 == 1 and tkmTrainNum == 5):
			self.block_authority5 = tkm_authority
		elif(self.TrainNum6 == 1 and tkmTrainNum == 6):
			self.block_authority6 = tkm_authority
		elif(self.TrainNum7 == 1 and tkmTrainNum == 7):
			self.block_authority7 = tkm_authority
		elif(self.TrainNum8 == 1 and tkmTrainNum == 8):
			self.block_authority8 = tkm_authority
		elif(self.TrainNum9 == 1 and tkmTrainNum == 9):
			self.block_authority9 = tkm_authority
		elif(self.TrainNum10 == 1 and tkmTrainNum == 10):
			self.block_authority10 = tkm_authority
		
	#Function to set Commanded Speed from track model signal
	def SetCommSpeed(self,commSpeed, tkmTrainNum):
		if(self.TrainNum1 == 1 and tkmTrainNum == 1):
			self.comm_speed1 = meterToMile(commSpeed)
			#print(str(self.comm_speed1) + " comm speed 1")
		elif(self.TrainNum2 == 1 and tkmTrainNum == 2):
			self.comm_speed2 = meterToMile(commSpeed)
			#print(str(self.comm_speed2) + "TNM comm speed 2..")
		elif(self.TrainNum3 == 1 and tkmTrainNum == 3):
			self.comm_speed3 = meterToMile(commSpeed)
		elif(self.TrainNum4 == 1 and tkmTrainNum == 4):
			self.comm_speed4 = meterToMile(commSpeed)
		elif(self.TrainNum5 == 1 and tkmTrainNum == 5):
			self.comm_speed5 = meterToMile(commSpeed)
		elif(self.TrainNum6 == 1 and tkmTrainNum == 6):
			self.comm_speed6 = meterToMile(commSpeed)
		elif(self.TrainNum7 == 1 and tkmTrainNum == 7):
			self.comm_speed7 = meterToMile(commSpeed)
		elif(self.TrainNum8 == 1 and tkmTrainNum == 8):
			self.comm_speed8 = meterToMile(commSpeed)
		elif(self.TrainNum9 == 1 and tkmTrainNum == 9):
			self.comm_speed9 = meterToMile(commSpeed)
		elif(self.TrainNum10 == 1 and tkmTrainNum == 10):
			self.comm_speed10 = meterToMile(commSpeed)
	
	#Function to set Passenger count from track model signal
	def SetOccupancy(self,tkm_pass_count, tkmTrainNum):
		if(self.TrainNum1 == 1 and tkmTrainNum == 1):
			#print(str(tkmTrainNum) + " pass from tkm")
			self.pass_count1 = tkm_pass_count
		elif(self.TrainNum2 == 1 and tkmTrainNum == 2):
			self.pass_count2 = tkm_pass_count
		elif(self.TrainNum3 == 1 and tkmTrainNum == 3):
			self.pass_count3 = tkm_pass_count
		elif(self.TrainNum4 == 1 and tkmTrainNum == 4):
			self.pass_count4 = tkm_pass_count
		elif(self.TrainNum5 == 1 and tkmTrainNum == 5):
			self.pass_count5 = tkm_pass_count
		elif(self.TrainNum6 == 1 and tkmTrainNum == 6):
			self.pass_count6 = tkm_pass_count
		elif(self.TrainNum7 == 1 and tkmTrainNum == 7):
			self.pass_count7 = tkm_pass_count
		elif(self.TrainNum8 == 1 and tkmTrainNum == 8):
			self.pass_count8 = tkm_pass_count
		elif(self.TrainNum9 == 1 and tkmTrainNum == 9):
			self.pass_count9 = tkm_pass_count
		elif(self.TrainNum10 == 1 and tkmTrainNum == 10):
			self.pass_count10 = tkm_pass_count
	
	#Function to read the emergency brake state from tnc
	def SetEBrake(self, EmerBrake, tncTrainNum):
		if(self.TrainNum1 == 1 and tncTrainNum == 1):
			self.eBrake1 = EmerBrake
		elif(self.TrainNum2 == 1 and tncTrainNum == 2):
			self.eBrake2 = EmerBrake
		elif(self.TrainNum3 == 1 and tncTrainNum == 3):
			self.eBrake3 = EmerBrake
		elif(self.TrainNum4 == 1 and tncTrainNum == 4):
			self.eBrake4 = EmerBrake
		elif(self.TrainNum5 == 1 and tncTrainNum == 5):
			self.eBrake5 = EmerBrake
		elif(self.TrainNum6 == 1 and tncTrainNum == 6):
			self.eBrake6 = EmerBrake
		elif(self.TrainNum7 == 1 and tncTrainNum == 7):
			self.eBrake7 = EmerBrake
		elif(self.TrainNum8 == 1 and tncTrainNum == 8):
			self.eBrake8 = EmerBrake
		elif(self.TrainNum9 == 1 and tncTrainNum == 9):
			self.eBrake9 = EmerBrake
		elif(self.TrainNum10 == 1 and tncTrainNum == 10):
			self.eBrake10 = EmerBrake
		
	#Function to read the service brake state from tnc
	def SetServiceBrake(self, ServiceBrake, tncTrainNum):
		if(self.TrainNum1 == 1 and tncTrainNum == 1):
			self.Brake1 = ServiceBrake
		elif(self.TrainNum2 == 1 and tncTrainNum == 2):
			self.Brake2 = ServiceBrake
		elif(self.TrainNum3 == 1 and tncTrainNum == 3):
			self.Brake3 = ServiceBrake
		elif(self.TrainNum4 == 1 and tncTrainNum == 4):
			self.Brake4 = ServiceBrake
		elif(self.TrainNum5 == 1 and tncTrainNum == 5):
			self.Brake5 = ServiceBrake
		elif(self.TrainNum6 == 1 and tncTrainNum == 6):
			self.Brake6 = ServiceBrake
		elif(self.TrainNum7 == 1 and tncTrainNum == 7):
			self.Brake7 = ServiceBrake
		elif(self.TrainNum8 == 1 and tncTrainNum == 8):
			self.Brake8 = ServiceBrake
		elif(self.TrainNum9 == 1 and tncTrainNum == 9):
			self.Brake9 = ServiceBrake
		elif(self.TrainNum10 == 1 and tncTrainNum == 10):
			self.Brake10 = ServiceBrake
		
	#Function to read in announcement from tnc
	def SetAnnounce(self, CurrentAnnouncement, tncTrainNum):
		if(self.TrainNum1 == 1 and tncTrainNum == 1):
			self.announce1 = CurrentAnnouncement
		elif(self.TrainNum2 == 1 and tncTrainNum == 2):
			self.announce2 = CurrentAnnouncement
		elif(self.TrainNum3 == 1 and tncTrainNum == 3):
			self.announce3 = CurrentAnnouncement
		elif(self.TrainNum4 == 1 and tncTrainNum == 4):
			self.announce4 = CurrentAnnouncement
		elif(self.TrainNum5 == 1 and tncTrainNum == 5):
			self.announce5 = CurrentAnnouncement
		elif(self.TrainNum6 == 1 and tncTrainNum == 6):
			self.announce6 = CurrentAnnouncement
		elif(self.TrainNum7 == 1 and tncTrainNum == 7):
			self.announce7 = CurrentAnnouncement
		elif(self.TrainNum8 == 1 and tncTrainNum == 8):
			self.announce8 = CurrentAnnouncement
		elif(self.TrainNum9 == 1 and tncTrainNum == 9):
			self.announce9 = CurrentAnnouncement
		elif(self.TrainNum10 == 1 and tncTrainNum == 10):
			self.announce10 = CurrentAnnouncement
		
	#Function to update status of Train Left Door
	def setLeftDoor(self, tncLeftDoor, tncTrainNum):
		if(self.TrainNum1 == 1 and tncTrainNum == 1):
			self.LeftDoor1 = tncLeftDoor
		elif(self.TrainNum2 == 1 and tncTrainNum == 2):
			self.LeftDoor2 = tncLeftDoor
		elif(self.TrainNum3 == 1 and tncTrainNum == 3):
			self.LeftDoor3 = tncLeftDoor
		elif(self.TrainNum4 == 1 and tncTrainNum == 4):
			self.LeftDoor4 = tncLeftDoor
		elif(self.TrainNum5 == 1 and tncTrainNum == 5):
			self.LeftDoor5 = tncLeftDoor
		elif(self.TrainNum6 == 1 and tncTrainNum == 6):
			self.LeftDoor6 = tncLeftDoor
		elif(self.TrainNum7 == 1 and tncTrainNum == 7):
			self.LeftDoor7 = tncLeftDoor
		elif(self.TrainNum8 == 1 and tncTrainNum == 8):
			self.LeftDoor8 = tncLeftDoor
		elif(self.TrainNum9 == 1 and tncTrainNum == 9):
			self.LeftDoor9 = tncLeftDoor
		elif(self.TrainNum10 == 1 and tncTrainNum == 10):
			self.LeftDoor10 = tncLeftDoor
		
	#Function to update status of Train Right Door
	def setRightDoor(self, tncRightDoor, tncTrainNum):
		if(self.TrainNum1 == 1 and tncTrainNum == 1):
			self.RightDoor1 = tncRightDoor
		elif(self.TrainNum2 == 1 and tncTrainNum == 2):
			self.RightDoor2 = tncRightDoor
		elif(self.TrainNum3 == 1 and tncTrainNum == 3):
			self.RightDoor3 = tncRightDoor
		elif(self.TrainNum4 == 1 and tncTrainNum == 4):
			self.RightDoor4 = tncRightDoor
		elif(self.TrainNum5 == 1 and tncTrainNum == 5):
			self.RightDoor5 = tncRightDoor
		elif(self.TrainNum6 == 1 and tncTrainNum == 6):
			self.RightDoor6 = tncRightDoor
		elif(self.TrainNum7 == 1 and tncTrainNum == 7):
			self.RightDoor7 = tncRightDoor
		elif(self.TrainNum8 == 1 and tncTrainNum == 8):
			self.RightDoor8 = tncRightDoor
		elif(self.TrainNum9 == 1 and tncTrainNum == 9):
			self.RightDoor9 = tncRightDoor
		elif(self.TrainNum10 == 1 and tncTrainNum == 10):
			self.RightDoor10 = tncRightDoor
		
	#Function to update Cab Light status
	def setCabLight(self, tncCabLight, tncTrainNum):
		if(self.TrainNum1 == 1 and tncTrainNum == 1):
			self.light_Cab1 = tncCabLight
		elif(self.TrainNum2 == 1 and tncTrainNum == 2):
			self.light_Cab2 = tncCabLight
		elif(self.TrainNum3 == 1 and tncTrainNum == 3):
			self.light_Cab3 = tncCabLight
		elif(self.TrainNum4 == 1 and tncTrainNum == 4):
			self.light_Cab4 = tncCabLight
		elif(self.TrainNum5 == 1 and tncTrainNum == 5):
			self.light_Cab5 = tncCabLight
		elif(self.TrainNum6 == 1 and tncTrainNum == 6):
			self.light_Cab6 = tncCabLight
		elif(self.TrainNum7 == 1 and tncTrainNum == 7):
			self.light_Cab7 = tncCabLight
		elif(self.TrainNum8 == 1 and tncTrainNum == 8):
			self.light_Cab8 = tncCabLight
		elif(self.TrainNum9 == 1 and tncTrainNum == 9):
			self.light_Cab9 = tncCabLight
		elif(self.TrainNum10 == 1 and tncTrainNum == 10):
			self.light_Cab10 = tncCabLight
			
	#Function to update Tun Light status
	def setTunLight(self, tncTunLight, tncTrainNum):
		if(self.TrainNum1 == 1 and tncTrainNum == 1):
			self.light_Tun1 = tncTunLight
		elif(self.TrainNum2 == 1 and tncTrainNum == 2):
			self.light_Tun2 = tncTunLight
		elif(self.TrainNum3 == 1 and tncTrainNum == 3):
			self.light_Tun3 = tncTunLight
		elif(self.TrainNum4 == 1 and tncTrainNum == 4):
			self.light_Tun4 = tncTunLight
		elif(self.TrainNum5 == 1 and tncTrainNum == 5):
			self.light_Tun5 = tncTunLight
		elif(self.TrainNum6 == 1 and tncTrainNum == 6):
			self.light_Tun6 = tncTunLight
		elif(self.TrainNum7 == 1 and tncTrainNum == 7):
			self.light_Tun7 = tncTunLight
		elif(self.TrainNum8 == 1 and tncTrainNum == 8):
			self.light_Tun8 = tncTunLight
		elif(self.TrainNum9 == 1 and tncTrainNum == 9):
			self.light_Tun9 = tncTunLight
		elif(self.TrainNum10 == 1 and tncTrainNum == 10):
			self.light_Tun10 = tncTunLight
			
	#Function to update High Beam Light status
	def setHighLight(self, tncHighLight, tncTrainNum):
		if(self.TrainNum1 == 1 and tncTrainNum == 1):
			self.light_High1 = tncHighLight
		elif(self.TrainNum2 == 1 and tncTrainNum == 2):
			self.light_High2 = tncHighLight
		elif(self.TrainNum3 == 1 and tncTrainNum == 3):
			self.light_High3 = tncHighLight
		elif(self.TrainNum4 == 1 and tncTrainNum == 4):
			self.light_High4 = tncHighLight
		elif(self.TrainNum5 == 1 and tncTrainNum == 5):
			self.light_High5 = tncHighLight
		elif(self.TrainNum6 == 1 and tncTrainNum == 6):
			self.light_High6 = tncHighLight
		elif(self.TrainNum7 == 1 and tncTrainNum == 7):
			self.light_High7 = tncHighLight
		elif(self.TrainNum8 == 1 and tncTrainNum == 8):
			self.light_High8 = tncHighLight
		elif(self.TrainNum9 == 1 and tncTrainNum == 9):
			self.light_High9 = tncHighLight
		elif(self.TrainNum10 == 1 and tncTrainNum == 10):
			self.light_High10 = tncHighLight
		
	#Function to set the train number, and specify the line name
	def setTrainStart(self, tkmTrainNum, tkmTrainLine):			#int, str
		self.TotTrainNum = tkmTrainNum
		
		if(self.TotTrainNum == 1):
			self.TrainNum1 = 1
			#Check which line the train is added to, and specify RouteLine variable
			if(tkmTrainLine == "Red"):
				self.RouteName1 = "Red Line"
				self.NextStation1 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName1 = "Green Line"
				self.NextStation1 = "Glenbury"
		elif(self.TotTrainNum == 2):
			self.TrainNum2 = 1
			#Check which line the train is added to, and specify RouteLine variable
			if(tkmTrainLine == "Red"):
				self.RouteName2 = "Red Line"
				self.NextStation2 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName2 = "Green Line"
				self.NextStation2 = "Glenbury"
		elif(self.TotTrainNum == 3):
			self.TrainNum3 = 1
			#Check which line the train is added to, and specify RouteLine variable
			if(tkmTrainLine == "Red"):
				self.RouteName3 = "Red Line"
				self.NextStation3 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName3 = "Green Line"
				self.NextStation3 = "Glenbury"
		elif(self.TotTrainNum == 4):
			self.TrainNum4 = 1
			#Check which line the train is added to, and specify RouteLine variable
			if(tkmTrainLine == "Red"):
				self.RouteName4 = "Red Line"
				self.NextStation4 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName4 = "Green Line"
				self.NextStation4 = "Glenbury"
		elif(self.TotTrainNum == 5):
			self.TrainNum5 = 1
			#Check which line the train is added to, and specify RouteLine variable
			if(tkmTrainLine == "Red"):
				self.RouteName5 = "Red Line"
				self.NextStation5 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName5 = "Green Line"
				self.NextStation5 = "Glenbury"
		elif(self.TotTrainNum == 6):
			self.TrainNum6 = 1
			#Check which line the train is added to, and specify RouteLine variable
			if(tkmTrainLine == "Red"):
				self.RouteName6 = "Red Line"
				self.NextStation6 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName6 = "Green Line"
				self.NextStation6 = "Glenbury"
		elif(self.TotTrainNum == 7):
			self.TrainNum7 = 1
			#Check which line the train is added to, and specify RouteLine variable
			if(tkmTrainLine == "Red"):
				self.RouteName7 = "Red Line"
				self.NextStation7 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName7 = "Green Line"
				self.NextStation7 = "Glenbury"
		elif(self.TotTrainNum == 8):
			self.TrainNum8 = 1
			#Check which line the train is added to, and specify RouteLine variable
			if(tkmTrainLine == "Red"):
				self.RouteName8 = "Red Line"
				self.NextStation8 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName8 = "Green Line"
				self.NextStation8 = "Glenbury"
		elif(self.TotTrainNum == 9):
			self.TrainNum9 = 1
			#Check which line the train is added to, and specify RouteLine variable
			if(tkmTrainLine == "Red"):
				self.RouteName9 = "Red Line"
				self.NextStation9 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName9 = "Green Line"
				self.NextStation9 = "Glenbury"
		elif(self.TotTrainNum == 10):
			self.TrainNum10 = 1
			#Check which line the train is added to, and specify RouteLine variable
			if(tkmTrainLine == "Red"):
				self.RouteName10 = "Red Line"
				self.NextStation10 = "Shady Side"
			elif(tkmTrainLine == "Green"):
				self.RouteName10 = "Green Line"
				self.NextStation10 = "Glenbury"
			
		
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
		elif(trainNumber == 9):
			self.TrainNum9 = 0
		elif(trainNumber == 10):
			self.TrainNum10 = 0
			
	
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
	

