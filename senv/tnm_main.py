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
		tnm_ebrake = pyqtSignal(bool)
		tnm_sendyard = pyqtSignal(bool)			#Track Model and Track Controller
		
		#define variables to be used in the Failure Interface
		self.car1_status = True
		self.car2_status = True
		self.car3_status = True
		self.car4_status = True
		self.car5_status = True
		self.train1_status = True
		self.sendYard = False
		self.trainNum = 0
		self.routeLine = 0
		self.train1_red, self.train2_red, self.train3_red, self.train4_red, self.train5_red = "Train 1 Status - Red", "Train 2 Status - Red", "Train 3 Status - Red", "Train 4 Status - Red", "Train 5 Status - Red"
		self.train1_green, self.train2_green, self.train3_green, self.train4_green, self.train5_green = "Train 1 Status - Green", "Train 2 Status - Green", "Train 3 Status - Green", "Train 4 Status - Green", "Train 5 Status - Green"
		self.eBrakeTest = False
		signals.tnc_emergency_brake.connect(self.SetEBrakeTest)
		
		
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
		if(self.routeLine == 0):		#red line
			if(self.trainNum == 1):
				self.ui.label.setText(self.train1_red)
			elif(self.trainNum == 2):
				self.ui.label.setText(self.train2_red)
			elif(self.trainNum == 3):
				self.ui.label.setText(self.train3_red)
			elif(self.trainNum == 4):
				self.ui.label.setText(self.train4_red)
			elif(self.trainNum == 5):
				self.ui.label.setText(self.train5_red)
		elif(self.routeLine == 1):		#green line
			if(self.trainNum == 1):
				self.ui.label.setText(self.train1_green)
			elif(self.trainNum == 2):
				self.ui.label.setText(self.train2_green)
			elif(self.trainNum == 3):
				self.ui.label.setText(self.train3_green)
			elif(self.trainNum == 4):
				self.ui.label.setText(self.train4_green)
			elif(self.trainNum == 5):
				self.ui.label.setText(self.train5_green)
		
		
		
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
		if(self.eBrakeTest == True):
			signals.tnm_ebrake.emit(self.eBrakeTest)
			print("eBrake is " + str(self.eBrakeTest))
			
#_______________________________________________________________________
	#function to set Emergency Brake from tnc
	def SetEBrakeTest(self, eBrakeTNC):
		self.eBrakeTest = eBrakeTNC
		
#_______________________________________________________________________
	#function to address Brake Failure Status's
	def brake_fail_act(self):
		#Car 1 Status Change
		#True means brake 1 is functional
		if(self.ui.lineEdit.text() == "Off" or self.ui.lineEdit.text() == "OFF" or self.ui.lineEdit.text() == "off"):	
			self.car1_status = True
			self.ui.lineEdit_6.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)	
		elif(self.ui.lineEdit.text() == "On" or self.ui.lineEdit.text() == "ON" or self.ui.lineEdit.text() == "on"):
			self.car1_status = False	
			self.ui.lineEdit_6.setText("Broken")
			self.eBrakeTest = True
			self.EmergencyBrakingTest()
			self.sendYard = True
			signals.tnm_sendyard.emit(True)
		else:
			self.car1_status = True
			self.ui.lineEdit.setText("Off")
			self.ui.lineEdit_6.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
			
		#Car 2 Status Change
		#True means brake 2 is functional
		if(self.ui.lineEdit_2.text() == "Off" or self.ui.lineEdit_2.text() == "OFF" or self.ui.lineEdit_2.text() == "off"):
			self.car2_status = True	
			self.ui.lineEdit_11.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_2.text() == "On" or self.ui.lineEdit_2.text() == "ON" or self.ui.lineEdit_2.text() == "on"):
			self.car2_status = False	
			self.ui.lineEdit_11.setText("Broken")
			self.eBrakeTest = True
			self.EmergencyBrakingTest()
			self.sendYard = True
			signals.tnm_sendyard.emit(True)				
		else:
			self.car2_status = True
			self.ui.lineEdit_2.setText("Off")
			self.ui.lineEdit_11.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		#Car 3 Status Change
		#True means brake 3 is functional
		if(self.ui.lineEdit_3.text() == "Off" or self.ui.lineEdit_3.text() == "OFF" or self.ui.lineEdit_3.text() == "off"):		
			self.car3_status = True
			self.ui.lineEdit_8.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_3.text() == "On" or self.ui.lineEdit_3.text() == "ON" or self.ui.lineEdit_3.text() == "on"):
			self.car3_status = False
			self.ui.lineEdit_8.setText("Broken")
			self.eBrakeTest = True
			self.EmergencyBrakingTest()
			self.sendYard = True		
			signals.tnm_sendyard.emit(True)			
		else:
			self.car3_status = True
			self.ui.lineEdit_3.setText("Off")
			self.ui.lineEdit_8.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
			
		#Car 4 Status Change
		#True means brake 4 is functional
		if(self.ui.lineEdit_4.text() == "Off" or self.ui.lineEdit_4.text() == "OFF" or self.ui.lineEdit_4.text() == "off"):									
			self.car4_status = True
			self.ui.lineEdit_9.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_4.text() == "On" or self.ui.lineEdit_4.text() == "ON" or self.ui.lineEdit_4.text() == "on"):
			self.car4_status = False
			self.ui.lineEdit_9.setText("Broken")
			self.eBrakeTest = True
			self.EmergencyBrakingTest()
			self.sendYard = True
			signals.tnm_sendyard.emit(True)							
		else:
			self.car4_status = True
			self.ui.lineEdit_4.setText("Off")
			self.ui.lineEdit_9.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		#Car 5 Status Change
		#True means brake 5 is functional
		if(self.ui.lineEdit_5.text() == "Off" or self.ui.lineEdit_5.text() == "OFF" or self.ui.lineEdit_5.text() == "off"):										
			self.car5_status = True
			self.ui.lineEdit_10.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_5.text() == "On" or self.ui.lineEdit_5.text() == "ON" or self.ui.lineEdit_5.text() == "on"):
			self.car5_status = False
			self.ui.lineEdit_10.setText("Broken")
			self.eBrakeTest = True
			self.EmergencyBrakingTest()
			self.sendYard = True
			signals.tnm_sendyard.emit(True)					
		else:
			self.car5_status = True
			self.ui.lineEdit_5.setText("Off")
			self.ui.lineEdit_10.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		
#_______________________________________________________________________
	#function to address Engine Failure Status's
	def engine_fail_act(self):
		#Car 1 Status Change
		#True means engine 1 is functional
		if(self.ui.lineEdit_7.text() == "Off" or self.ui.lineEdit_7.text() == "OFF" or self.ui.lineEdit_7.text() == "off"):	
			self.car1_status = True
			self.ui.lineEdit_16.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_7.text() == "On" or self.ui.lineEdit_7.text() == "ON" or self.ui.lineEdit_7.text() == "on"):
			self.car1_status = False	
			self.ui.lineEdit_16.setText("Broken")
			self.eBrakeTest = True
			self.EmergencyBrakingTest()
			self.sendYard = True
			signals.tnm_sendyard.emit(True)				
		else:
			self.car1_status = True
			self.ui.lineEdit_7.setText("Off")
			self.ui.lineEdit_16.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
			
		#Car 2 Status Change
		#True means engine 2 is functional
		if(self.ui.lineEdit_12.text() == "Off" or self.ui.lineEdit_12.text() == "OFF" or self.ui.lineEdit_12.text() == "off"):
			self.car2_status = True	
			self.ui.lineEdit_17.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_12.text() == "On" or self.ui.lineEdit_12.text() == "ON" or self.ui.lineEdit_12.text() == "on"):
			self.car2_status = False	
			self.ui.lineEdit_17.setText("Broken")
			self.eBrakeTest = True
			self.EmergencyBrakingTest()
			self.sendYard = True	
			signals.tnm_sendyard.emit(True)				
		else:
			self.car2_status = True
			self.ui.lineEdit_12.setText("Off")
			self.ui.lineEdit_17.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		#Car 3 Status Change
		#True means engine 3 is functional
		if(self.ui.lineEdit_13.text() == "Off" or self.ui.lineEdit_13.text() == "OFF" or self.ui.lineEdit_13.text() == "off"):		
			self.car3_status = True
			self.ui.lineEdit_18.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_13.text() == "On" or self.ui.lineEdit_13.text() == "ON" or self.ui.lineEdit_13.text() == "on"):
			self.car3_status = False
			self.ui.lineEdit_18.setText("Broken")
			self.eBrakeTest = True
			self.EmergencyBrakingTest()
			self.sendYard = True
			signals.tnm_sendyard.emit(True)					
		else:
			self.car3_status = True
			self.ui.lineEdit_13.setText("Off")
			self.ui.lineEdit_18.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		#Car 4 Status Change
		#True means engine 4 is functional
		if(self.ui.lineEdit_14.text() == "Off" or self.ui.lineEdit_14.text() == "OFF" or self.ui.lineEdit_14.text() == "off"):									
			self.car4_status = True
			self.ui.lineEdit_19.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_14.text() == "On" or self.ui.lineEdit_14.text() == "ON" or self.ui.lineEdit_14.text() == "on"):
			self.car4_status = False
			self.ui.lineEdit_19.setText("Broken")
			self.eBrakeTest = True
			self.EmergencyBrakingTest()
			self.sendYard = True
			signals.tnm_sendyard.emit(True)					
		else:
			self.car4_status = True
			self.ui.lineEdit_14.setText("Off")
			self.ui.lineEdit_19.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		#Car 5 Status Change
		#True means engine 5 is functional
		if(self.ui.lineEdit_15.text() == "Off" or self.ui.lineEdit_15.text() == "OFF" or self.ui.lineEdit_15.text() == "off"):										
			self.car5_status = True
			self.ui.lineEdit_20.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_15.text() == "On" or self.ui.lineEdit_15.text() == "ON" or self.ui.lineEdit_15.text() == "on"):
			self.car5_status = False
			self.ui.lineEdit_20.setText("Broken")
			self.eBrakeTest = True
			self.EmergencyBrakingTest()
			self.sendYard = True
			signals.tnm_sendyard.emit(True)					
		else:
			self.car5_status = True
			self.ui.lineEdit_15.setText("Off")
			self.ui.lineEdit_20.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
			
	
#_______________________________________________________________________
	#function to address Signal Pickup Failure Status's
	def signalP_fail_act(self):
		#train 1 Status Change
		#True means train 1 is functional
		if(self.ui.lineEdit_21.text() == "Off" or self.ui.lineEdit_21.text() == "OFF" or self.ui.lineEdit_21.text() == "off"):	
			self.train1_status = True
			self.ui.lineEdit_26.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_21.text() == "On" or self.ui.lineEdit_21.text() == "ON" or self.ui.lineEdit_21.text() == "on"):
			self.train1_status = False	
			self.ui.lineEdit_26.setText("Broken")	
			self.eBrakeTest = True
			self.EmergencyBrakingTest()
			self.sendYard = True
			signals.tnm_sendyard.emit(True)			
		else:
			self.train1_status = True
			self.ui.lineEdit_21.setText("Off")
			self.ui.lineEdit_26.setText("Operational")
			self.eBrakeTest = False
			self.EmergencyBrakingTest()
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
			

	#Function to check which line the train is on
	def setTrainInfo(self, tkmTrainNum, tkmTrainLine):
		#Set train Number
		self.trainNum = tkmTrainNum
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
		tnm_comm_speed = pyqtSignal(float)		#All signals for Track Controller
		tnm_curr_speed = pyqtSignal(float)
		tnm_authority = pyqtSignal(bool)
		tnm_beacondID = pyqtSignal(int)
		tnm_ebrake = pyqtSignal(bool)
		tnm_cab_temp = pyqtSignal(int)
		tnm_sendYard = pyqtSignal(int)
		tnm_block_finished_green = pyqtSignal(int)
		tnm_block_finished_red = pyqtSignal(int)
		tnm_curr_station = pyqtSignal(str)
		tnm_TrainDir = pyqtSignal(bool)
		tnm_train_stop_num = pyqtSignal(int)

#Define variables to be used in tnm_display
		self.TrainNum = 0
		self.TrainName = " -- Information"
		self.train1, self.train2, self.train3, self.train4, self.train5 = "Train 1 Information", "Train 2 Information", "Train 3 Information", "Train 4 Information", "Train 5 Information"
		self.timeSeconds = 0
	#authority connected from tkm
		self.block_authority = False
		signals.tkm_get_train_auth.connect(self.SetAuthority)
	#power connected from tnc
		self.curr_power = 0
		signals.tnc_power.connect(self.SetPower)
		self.curr_speed = 0.0
		self.curr_accl = 0.0
		self.comm_speed = 0.0
		signals.tkm_get_speed.connect(self.SetCommSpeed)
		#train starts at rest v
		self.SpeedN1 = 0.0					#Used as value for inital speed for curr_speed calculation. Then is set to curr_speed for next calculation
		self.AcclN1 = 0.0
	#Block length connected from tkm
		self.block_length = 1
		self.block_num = 0
		self.block_finished = False
		self.timeBlock = 0
		self.dist_traveled = 0.0
		signals.tkm_get_blength.connect(self.blockLen)
		signals.tkm_get_block.connect(self.blockNum)
		signals.tkm_get_train_num.connect(self.setTrainStart)
	#brake states
		self.Brake = False
		self.eBrake = False
		signals.tnc_emergency_brake.connect(self.SetEBrake)
		signals.tnc_service_brake.connect(self.SetServiceBrake)
	#Occupancy 
		self.pass_count = 10
		signals.tkm_get_pass_count.connect(self.SetOccupancy)
		self.crew_count = 3
	#Route Information
		self.Mass_Empty = (5*40.9)								#Tons with no passengers/crew
		self.Occupancy = pass_crew_count(self.pass_count, self.crew_count)
		self.RouteLine = 0		#0 for Red line, 1 for Green line
		self.RouteName = " --- "
		self.TrainDirection = 1
		self.TNMdirectionR = 1				#internal direction for train on the red line
		self.TNMdirectionG = 1				#internal direction for train on the green line
		self.CurrStation = "Yard"
		self.NextStation = " --- "
		self.DoorStatus = False
		self.LeftDoor = False
		self.RightDoor = False
		signals.tnc_left_door.connect(self.setRightDoor)
		signals.tnc_right_door.connect(self.setLeftDoor)
	#Beacon ID connected from tkm
		self.beacon_bin = 0b00000000
		self.BeaconID = 00000000								#bit1 (red vs green) bit2 (UG vs Station) bit3 (Left side (62->63) vs Right side(63->64))
		signals.tkm_get_beacon.connect(self.SetBeaconID)
		self.BeaconIDStatus = True
	#Internal control status's
		self.lights_Cab = True
		self.lights_High = False
		self.lights_Tun = False
		signals.tnc_cab_light.connect(self.setCabLight)
		signals.tnc_tunnel_light.connect(self.setTunLight)
		signals.tnc_high_beam_light.connect(self.setHighLight)
		self.set_temp = 0		#degrees Fahrenheit
		self.curr_temp = 68		#degrees Fahrenheit
		self.announce = "Watch your step. Have a great day!"
		signals.tnc_announcement.connect(self.SetAnnounce)

		#Defining Actions for specific UI Interactions
		signals.time.connect(self.update_MoveStat)						#Update Movement Statistics
		signals.time.connect(self.SetCommSpeed)
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
		
		signals.tnc_service_brake.connect(self.SetServiceBrake)
		#Calculate current speed
		self.curr_speed, self.current_accl = set_curr_speed(self.timeSeconds, self.eBrake, self.Brake, self.block_authority, self.curr_power, self.Occupancy, self.SpeedN1, self.AcclN1, self.comm_speed)

		#Set At - 1 variables for use in next sec. speed calculation
		self.SpeedN1 = self.curr_speed
		self.AcclN1 = self.current_accl
		
		#Update current speed given power value
		self.ui.lineEdit.setText(str(self.curr_speed) + " mph")
		#Send the new calculated current speed to Train Controller
		signals.tnm_curr_speed.emit(self.curr_speed)
		
		#Variable to check speed, then calculate when block changes based on speed
		curr_speed_mps = 0.0
		#calculations of current distance
		curr_speed_mps = MiletoMeter(self.curr_speed)					#MPH to mps
		self.dist_traveled = (self.dist_traveled + curr_speed_mps*(1))		#distance in meters m/s *s = m
		#print(str(round(self.dist_traveled,2)) + " meters at " + str(self.timeSeconds))
		#If distance > length, change blocks and emit signal
		if(curr_speed_mps > 0.0):
			if(self.dist_traveled >= self.block_length):
				self.block_finished = True
				print(str(self.block_finished) + " change blocks")
				
				self.dist_traveled = 0
				if(self.RouteLine == 0):
					signals.tnm_block_finished_red.emit(self.TrainNum)
				elif(self.RouteLine == 1):
					signals.tnm_block_finished_green.emit(self.TrainNum)
				signals.tkm_get_blength.connect(self.blockLen)
		
		
		#Update brake status
		if (self.Brake == True or self.eBrake == True):
			self.ui.lineEdit_2.setText("On")
		else:
			self.ui.lineEdit_2.setText("Off")
		
		#Update the curr_accl rate
		#self.ui.lineEdit_3.setText(str(self.current_accl) + " mph2")
		
		#Don't allow changes to lineEdits
		self.ui.lineEdit.setReadOnly(True)
		self.ui.lineEdit_2.setReadOnly(True)
		self.ui.lineEdit_3.setReadOnly(True)
		self.ui.lineEdit_4.setReadOnly(True)
		self.ui.lineEdit_5.setReadOnly(True)
		
		#Address Authority Here
		signals.tnm_authority.emit(self.block_authority)
		#self.blockTime(self.block_length)
		#Address Commanded Speed
		signals.tnm_comm_speed.emit(self.comm_speed)
		
#_______________________________________________________________________	
	#function to update Train Statistics (Mass, Pass & Crew count)
	def update_TrainStat(self):
		
		#Update pass_count
		self.ui.lineEdit_6.setText(str(self.pass_count))
		#Update crew_count
		self.ui.lineEdit_7.setText(str(self.crew_count))
		#Update current Mass of Train
		self.Occupancy = pass_crew_count(self.pass_count, self.crew_count)
		self.total_mass = ((self.Occupancy*56.699)/2000) + self.Mass_Empty
		self.ui.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		
		#Don't allow changes to lineEdits
		self.ui.lineEdit_6.setReadOnly(True)
		self.ui.lineEdit_7.setReadOnly(True)
		self.ui.lineEdit_8.setReadOnly(True)
		
#_______________________________________________________________________
	#function to update Route Information and Train Internal Controls
	def update_RouteInfo(self):
		
		#Update Train Numbering Header
		self.ui.label_23.setText(self.TrainName)
		
		#Update Route Line
		self.ui.lineEdit_9.setText(self.RouteName)
		
		#Update Current and Next Station based on Line and direction
		self.ui.lineEdit_19.setText(self.CurrStation)
		self.ui.lineEdit_10.setText(self.NextStation)
		
		#Update Doors Status		#Doors will be held open for one minute
		if(self.LeftDoor == True or self.RightDoor == True):
			self.DoorStatus = True
			
		if (self.DoorStatus == False):
			self.ui.lineEdit_11.setText("Closed")
			self.Brake = False
		elif(self.DoorStatus == True):
			self.ui.lineEdit_11.setText("Open")
			signals.tnm_train_stop_num.emit(self.TrainNum)
			self.Brake = True
			
		#Update Beacon ID Status
		if (self.BeaconIDStatus == False):
			self.ui.lineEdit_12.setText("Waiting")
		else:
			self.ui.lineEdit_12.setText("Recieved")
			signals.tnm_beaconID.emit(self.BeaconID)					#emit int BeaconID

		
		#update Cabin Lights status
		if (self.lights_Cab == False):
			self.ui.lineEdit_13.setText("Off")
		else:
			self.ui.lineEdit_13.setText("On")
		#update High Beam Lights status
		if (self.lights_High == False):
			self.ui.lineEdit_14.setText("Off")
		else:
			self.ui.lineEdit_14.setText("On")
		#update Tunnel Lights status
		if (self.lights_Tun == False):
			self.ui.lineEdit_15.setText("Off")
		else:
			self.ui.lineEdit_15.setText("On")
			
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
		if not self.eBrake:
			self.ui.pushButton.setText("CANCEL")
			self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: white;")
			self.eBrake = True
			signals.tnm_ebrake.emit(self.eBrake)
			print("eBrake is " + str(self.eBrake))
		else:
			self.ui.pushButton.setText("Emergency Brake")
			self.ui.pushButton.setStyleSheet("background-color: rgb(170, 0, 0); color: black;")
			self.eBrake = False
			signals.tnm_ebrake.emit(False)
			
		"""   
		if(self.eBrake == False):
		self.eBrake = True
		signals.tnm_ebrake.emit(self.eBrake)
		print("eBrake is " + str(self.eBrake))
		"""

#_______________________________________________________________________
	#function to Update Current Temperature of the cabin
	def Temperature(self):
		AlphaFlag = False
		#Error checking to make sure input is only an INT
		for i in self.ui.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag = True
		if(AlphaFlag == True):
			self.ui.lineEdit_17.setText(str(self.curr_temp))
			self.set_temp = self.curr_temp
		elif(self.ui.lineEdit_17.text().isdigit() == True):
			AlphaFlag = False
			self.set_temp = int(self.ui.lineEdit_17.text())
		
		#Use temp_control function to set the current temperature
		self.ui.lineEdit_16.setText(str(temp_control(self.set_temp, self.curr_temp)) + " F")
		#signals.tnm_cab_temp.emit(self.curr_temp)
		
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
		self.ui.lineEdit_18.setText(self.announce)
		
		#Don't allow announcements text to be edited
		self.ui.lineEdit_18.setReadOnly(True)
		
#_______________________________________________________________________
	#Function to set power from tnc signal
	def SetPower(self,tnc_power):
		self.curr_power = tnc_power
	
	#Function to set Beacon ID from track model signal
	def SetBeaconID(self,tkm_beacon):
		#beacon ID int set, then sent to Train Controller
		self.BeaconId = tkm_beacon
		
		self.beacon_bin = bin(self.BeaconId)
		
		#Ensure Beacon ID is correct by appending necessary 0's after conversion
		if(len(self.beacon_bin) == 10):
			#remove first two char: 0b
			self.beacon_bin = self.beacon_bin[2:]
		elif(len(self.beacon_bin) == 9):
			self.beacon_bin = self.beacon_bin[2:]
			self.beacon_bin = ("0" + self.beacon_bin)
		elif(len(self.beacon_bin) == 8):
			self.beacon_bin = self.beacon_bin[2:]
			self.beacon_bin = ("00" + self.beacon_bin)
		elif(len(self.beacon_bin) == 7):
			self.beacon_bin = self.beacon_bin[2:]
			self.beacon_bin = ("000" + self.beacon_bin)
		elif(len(self.beacon_bin) == 6):
			self.beacon_bin = self.beacon_bin[2:]
			self.beacon_bin = ("0000" + self.beacon_bin)
		elif(len(self.beacon_bin) == 5):
			self.beacon_bin = self.beacon_bin[2:]
			self.beacon_bin = ("00000" + self.beacon_bin)
		elif(len(self.beacon_bin) == 4):
			self.beacon_bin = self.beacon_bin[2:]
			self.beacon_bin = ("000000" + self.beacon_bin)
		elif(len(self.beacon_bin) == 3):
			self.beacon_bin = self.beacon_bin[2:]
			self.beacon_bin = ("0000000" + self.beacon_bin)
		elif(len(self.beacon_bin) == 2):
			self.beacon_bin = self.beacon_bin[2:]
			self.beacon_bin = ("00000000" + self.beacon_bin)
	
		#check if first value is: 1 = green line/0 = red line #Was 2, 3, 4, 5:
		if(self.beacon_bin[0] == 0):
			self.RouteName = "Red Line"
			self.CurrStation = "Yard"
			self.NextStation = "Shady Side"
		elif(self.beacon_bin[0] == 1):
			self.RouteName = "Green Line"
			self.CurrStation = "Yard"
			self.NextStation = "Glenbury"
		#check if second value is: 0 = station/1 = underground
		if(self.beacon_bin[1] == 0):
			self.lights_Tun == False
		elif(self.beacon_bin[1] == 1):
			self.lights_Tun == True
		#3rd bit - 0 Left(decrement)/1 Right(increment) directionality
		#0 means left doors open, 1 means right doors open
		if(self.beacon_bin[2] == 0):
			self.TrainDirection = 0
			self.tnm_TrainDir.emit(self.TrainDirection)
		elif(self.beacon_bin[2] == 1):
			self.TrainDirection = 1
			self.tnm_TrainDir.emit(self.TrainDirection)
		
		#Add beacon specification here (for last 5 bits)
		#Green Line stations defined here, with the train incrementally (13 Stations)	
		if(self.RouteName == "Green Line" and self.TNMdirectionG == 1 and self.TrainDirection == 1):
			if(self.beacon_bin[3:] == "00000"):
				self.CurrStation = "Yard"
				self.NextStation = "Glenbury"
			elif(self.beacon_bin[3:] == "01001"):
				self.CurrStation = "Glenbury"
				self.NextStation = "Dormont"
			elif(self.beacon_bin[3:] == "01010"):
				self.CurrStation = "Dormont"
				self.NextStation = "Mt Lebanon"
			elif(self.beacon_bin[3:] == "01011"):
				self.CurrStation = "Mt Lebanon"
				self.NextStation = "Poplar"
			elif(self.beacon_bin[3:] == "01100"):
				self.CurrStation = "Poplar"
				self.NextStation = "Castle Shannon"
			elif(self.beacon_bin[3:] == "01101"):
				self.CurrStation = "Castle Shannon"
				self.TNMdirectionG == 0		#changed direction going back up the left track
				self.NextStation = "Mt Lebanon"
				
			elif(self.beacon_bin[3:] == "00011"):
				self.CurrStation = "Falcon"
				self.NextStation = "Whited"
			elif(self.beacon_bin[3:] == "00100"):
				self.CurrStation = "Whited"
				self.NextStation = "South Bank"
			elif(self.beacon_bin[3:] == "00101"):
				self.CurrStation = "South Bank"
				self.NextStation = "Central"
			elif(self.beacon_bin[3:] == "00110"):
				self.CurrStation = "Central"
				self.NextStation = "Inglewood"
			elif(self.beacon_bin[3:] == "00111"):
				self.CurrStation = "Inglewood"
				self.NextStation = "Glenbury"
			else:
				self.CurrStation = " ---- "
				self.NextStation = " ---- "
			signals.tnm_curr_station.emit(self.CurrStation)
		#Train Going reverse direction on the green line		(13 Stations)
		if(self.RouteName == "Green Line" and self.TNMdirectionG == 0 and self.TrainDirection == 1):
			if(self.beacon_bin[3:] == "00000"):			#Likely won't reach this unless sent to Yard
				self.CurrStation = "Yard"
				self.NextStation = " ---- "
			elif(self.beacon_bin[3:] == "01011"):
				self.CurrStation = "Mt Lebanon"
				self.NextStation = "Dormont"
			elif(self.beacon_bin[3:] == "01010"):
				self.CurrStation = "Dormont"
				self.NextStation = "Glenbury"
			elif(self.beacon_bin[3:] == "01001"):
				self.CurrStation = "Glenbury"
				self.NextStation = "Overbrook"
			elif(self.beacon_bin[3:] == "01000"):
				self.CurrStation = "Overbrook"
				self.NextStation = "Inglewood"
			elif(self.beacon_bin[3:] == "00111"):
				self.CurrStation = "Inglewood"
				self.NextStation = "Central"
			elif(self.beacon_bin[3:] == "00110"):
				self.CurrStation = "Central"
				self.NextStation = "Whited"
			elif(self.beacon_bin[3:] == "00100"):
				self.CurrStation = "Whited"
				self.NextStation = "Falcon"
			elif(self.beacon_bin[3:] == "00011"):
				self.CurrStation = "Falcon"
				self.NextStation = "Edgebrook"
			elif(self.beacon_bin[3:] == "00010"):
				self.CurrStation = "Edgebrook"
				self.NextStation = "Pioneer"
			elif(self.beacon_bin[3:] == "00001"):
				self.CurrStation = "Pioneer"
				self.TNMdirectionG = 1			#change direction going back down on the right line
				self.NextStation = "Falcon"
			else:
				self.CurrStation = " ---- "
				self.NextStation = " ---- "
			signals.tnm_curr_station.emit(self.CurrStation)
		#Route names for the Red Line going to stations incrementally (7 Stations)
		elif(self.RouteName == "Red Line" and self.TNMdirectionR == 1 and self.TrainDirection == 1):
			if(self.beacon_bin[3:] == "00000"):
				self.CurrStation = "Yard"
				#self.TNMdirectionR = 1 		#counting up
				self.NextStation = "Shadyside"
			elif(self.beacon_bin[3:] == "00001"):
				self.CurrStation = "Shadyside"
				self.NextStation = "Herron Ave"
			elif(self.beacon_bin[3:] == "00010"):
				self.CurrStation = "Herron Ave"
				self.NextStation = "Swissvale"
			elif(self.beacon_bin[3:] == "00011"):
				self.CurrStation = "Swissvale"
				self.NextStation = "Penn Station"
			elif(self.beacon_bin[3:] == "00100"):
				self.CurrStation = "Penn Station"
				self.NextStation = "Steel Plaza"
			elif(self.beacon_bin[3:] == "00101"):
				self.CurrStation = "Steel Plaza"
				self.NextStation = "First Ave"
			elif(self.beacon_bin[3:] == "00110"):
				self.CurrStation = "First Ave"
				self.NextStation = "Station Square"
			elif(self.beacon_bin[3:] == "00111"):
				self.CurrStation = "Station Square"
				self.NextStation = "South Hills J."
			elif(self.beacon_bin[3:] == "01000"):
				self.CurrStation = "South Hills J."
				self.TNMdirectionR = 0	#"counting down"
				self.NextStation = "Station Square"
			else:
				self.CurrStation = " ---- "
				self.NextStation = " ---- "
			signals.tnm_curr_station.emit(self.CurrStation)
		#Route names for the Red Line going to stations decrementally	(7 Stations)
		elif(self.RouteName == "Red Line" and self.TNMdirectionR == 0 and self.TrainDirection == 1):
			if(self.beacon_bin[3:] == "00000"):					#Likely won't reach this unless sent to yard
				self.CurrStation = "Yard"
				self.NextStation = " ---- "
			elif(self.beacon_bin[3:] == "00001"):
				self.CurrStation = "Shadyside"
				self.TNMdirectionR = 1	#"counting up"
				self.NextStation = "Herron Ave"
			elif(self.beacon_bin[3:] == "00010"):
				self.CurrStation = "Herron Ave"
				self.NextStation = "Shadyside"
			elif(self.beacon_bin[3:] == "00011"):
				self.CurrStation = "Swissvale"
				self.NextStation = "Herron Ave"
			elif(self.beacon_bin[3:] == "00100"):
				self.CurrStation = "Penn Station"
				self.NextStation = "Swissvale"
			elif(self.beacon_bin[3:] == "00101"):
				self.CurrStation = "Steel Plaza"
				self.NextStation = "Penn Station"
			elif(self.beacon_bin[3:] == "00110"):
				self.CurrStation = "First Ave"
				self.NextStation = "Steel Plaza"
			elif(self.beacon_bin[3:] == "00111"):
				self.CurrStation = "Station Square"
				self.NextStation = "First Ave"
			else:
				self.CurrStation = " ---- "
				self.NextStation = " ---- "
			signals.tnm_curr_station.emit(self.CurrStation)
	
	#Function to specify block number for each line
	def blockNum(self,BlockNum):
		self.block_num = BlockNum
		
	#Function to take in block length and calculate when train reaches next block
	def blockLen(self, BlockLen):
		#set variables
		self.block_length = BlockLen
	
	#Function to set Authority from track model signal
	def SetAuthority(self,tkm_authority):
		self.block_authority = tkm_authority
		
	#Function to set Commanded Speed from track model signal
	def SetCommSpeed(self,commSpeed):
		self.comm_speed = meterToMile(commSpeed)			#convert mps to MPH
		#print(str(self.comm_speed) + " comm speed from tnm")
	
	#Function to set Passenger count from track model signal
	def SetOccupancy(self,tkm_pass_count):
		self.pass_count = tkm_pass_count
	
	#Function to read the emergency brake state from tnc
	def SetEBrake(self, EmerBrake):
		self.eBrake = EmerBrake
		
	#Function to read the service brake state from tnc
	def SetServiceBrake(self, ServiceBrake):
		self.Brake = ServiceBrake
		
	#Function to read in announcement from tnc
	def SetAnnounce(self, CurrentAnnouncement):
		self.announce = CurrentAnnouncement
		
	#Function to update status of Train Left Door
	def setLeftDoor(self, tncLeftDoor):
		self.LeftDoor = tncLeftDoor
		#print("Left door = " + str(self.LeftDoor))
		
	#Function to update status of Train Right Door
	def setRightDoor(self, tncRightDoor):
		self.RightDoor = tncRightDoor
		#print("Right door = " + str(self.RightDoor))
		
	#Function to update Cab Light status
	def setCabLight(self, tncCabLight):
		self.light_Cab = tncCabLight
	#Function to update Tun Light status
	def setTunLight(self, tncTunLight):
		self.light_Tun = tncTunLight
	#Function to update High Beam Light status
	def setHighLight(self, tncHighLight):
		self.light_High = tncHighLight
		
	#Function to set the train number, and specify the line name
	def setTrainStart(self, tkmTrainNum, tkmTrainLine):			#int, str
		self.TrainNum = tkmTrainNum
		#Check which line the train is added to, and specify RouteLine variable
		if(tkmTrainLine == "Red"):
			self.RouteLine = 0
		elif(tkmTrainLine == "Green"):
			self.RouteLine = 1
		
		#Determine which Train Number -> Train Name
		if(self.TrainNum == 1):
			self.TrainName = self.train1
		elif(self.TrainNum == 2):
			self.TrainName = self.train2
		elif(self.TrainNum == 3):
			self.TrainName = self.train3
		elif(self.TrainNum == 4):
			self.TrainName = self.train4
		elif(self.TrainNum == 5):
			self.TrainName = self.train5
		else:
			self.TrainName = " ----- "
		
		#Specify which track the train is on, red or green
		if(self.RouteLine == 0):
			self.RouteName = "Red Line"
			self.NextStation = "Shady Side"
		elif(self.RouteLine == 1):
			self.RouteName = "Green Line"
			self.NextStation = "Glenbury"
		
			
	
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
		
		finished = self.timeBlock - 1
		if(finished == 0):
			self.block_finished = True
			signals.tnm_block_finished.emit(self.block_finished)

	
		
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
	

