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


"""
self.tmodel_thread = QThread()
self.tmodel_test = tnm_failureTest()
#self.tmodel_main = tnm_display()
self.tmodel_test.moveToThread(self.tmodel_thread)
self.tmodel_thread.start()
"""


#_______________________________________________________________________
#Failure Test State
class tnm_failureTest(QObject):
	def __init__(self):
		super().__init__()
		self.TestUi = QtWidgets.QMainWindow()
		self.ui = Ui_Test()
		
		#display main program
		self.ui.setupUi(self.TestUi)
		self.TestUi.show()
		

		#Signals defined
		tnm_sendyard = pyqtSignal(bool)			#Track Model and Track Controller
		
		#define variables to be used in the Failure Interface
		self.car1_status = True
		self.car2_status = True
		self.car3_status = True
		self.car4_status = True
		self.car5_status = True
		self.train1_status = True
		self.sendYard = False
		self.train1_test = "Train 1 Test Interface"
		
		
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
		#Update Train Number
		self.ui.label.setText(self.train1_test)
		
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
	#function to address Brake Failure Status's
	def brake_fail_act(self):
		#Car 1 Status Change
		#True means brake 1 is functional
		if(self.ui.lineEdit.text() == "Off" or self.ui.lineEdit.text() == "OFF" or self.ui.lineEdit.text() == "off"):	
			self.car1_status = True
			self.ui.lineEdit_6.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)	
		elif(self.ui.lineEdit.text() == "On" or self.ui.lineEdit.text() == "ON" or self.ui.lineEdit.text() == "on"):
			self.car1_status = False	
			self.ui.lineEdit_6.setText("Broken")
			self.sendYard = True
			signals.tnm_sendyard.emit(True)
		else:
			self.car1_status = True
			self.ui.lineEdit.setText("Off")
			self.ui.lineEdit_6.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
			
		#Car 2 Status Change
		#True means brake 2 is functional
		if(self.ui.lineEdit_2.text() == "Off" or self.ui.lineEdit_2.text() == "OFF" or self.ui.lineEdit_2.text() == "off"):
			self.car2_status = True	
			self.ui.lineEdit_11.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_2.text() == "On" or self.ui.lineEdit_2.text() == "ON" or self.ui.lineEdit_2.text() == "on"):
			self.car2_status = False	
			self.ui.lineEdit_11.setText("Broken")
			self.sendYard = True
			signals.tnm_sendyard.emit(True)				
		else:
			self.car2_status = True
			self.ui.lineEdit_2.setText("Off")
			self.ui.lineEdit_11.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		#Car 3 Status Change
		#True means brake 3 is functional
		if(self.ui.lineEdit_3.text() == "Off" or self.ui.lineEdit_3.text() == "OFF" or self.ui.lineEdit_3.text() == "off"):		
			self.car3_status = True
			self.ui.lineEdit_8.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_3.text() == "On" or self.ui.lineEdit_3.text() == "ON" or self.ui.lineEdit_3.text() == "on"):
			self.car3_status = False
			self.ui.lineEdit_8.setText("Broken")
			self.sendYard = True		
			signals.tnm_sendyard.emit(True)			
		else:
			self.car3_status = True
			self.ui.lineEdit_3.setText("Off")
			self.ui.lineEdit_8.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
			
		#Car 4 Status Change
		#True means brake 4 is functional
		if(self.ui.lineEdit_4.text() == "Off" or self.ui.lineEdit_4.text() == "OFF" or self.ui.lineEdit_4.text() == "off"):									
			self.car4_status = True
			self.ui.lineEdit_9.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_4.text() == "On" or self.ui.lineEdit_4.text() == "ON" or self.ui.lineEdit_4.text() == "on"):
			self.car4_status = False
			self.ui.lineEdit_9.setText("Broken")
			self.sendYard = True
			signals.tnm_sendyard.emit(True)							
		else:
			self.car4_status = True
			self.ui.lineEdit_4.setText("Off")
			self.ui.lineEdit_9.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		#Car 5 Status Change
		#True means brake 5 is functional
		if(self.ui.lineEdit_5.text() == "Off" or self.ui.lineEdit_5.text() == "OFF" or self.ui.lineEdit_5.text() == "off"):										
			self.car5_status = True
			self.ui.lineEdit_10.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_5.text() == "On" or self.ui.lineEdit_5.text() == "ON" or self.ui.lineEdit_5.text() == "on"):
			self.car5_status = False
			self.ui.lineEdit_10.setText("Broken")
			self.sendYard = True
			signals.tnm_sendyard.emit(True)					
		else:
			self.car5_status = True
			self.ui.lineEdit_5.setText("Off")
			self.ui.lineEdit_10.setText("Operational")
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
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_7.text() == "On" or self.ui.lineEdit_7.text() == "ON" or self.ui.lineEdit_7.text() == "on"):
			self.car1_status = False	
			self.ui.lineEdit_16.setText("Broken")
			self.sendYard = True
			signals.tnm_sendyard.emit(True)				
		else:
			self.car1_status = True
			self.ui.lineEdit_7.setText("Off")
			self.ui.lineEdit_16.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
			
		#Car 2 Status Change
		#True means engine 2 is functional
		if(self.ui.lineEdit_12.text() == "Off" or self.ui.lineEdit_12.text() == "OFF" or self.ui.lineEdit_12.text() == "off"):
			self.car2_status = True	
			self.ui.lineEdit_17.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_12.text() == "On" or self.ui.lineEdit_12.text() == "ON" or self.ui.lineEdit_12.text() == "on"):
			self.car2_status = False	
			self.ui.lineEdit_17.setText("Broken")
			self.sendYard = True	
			signals.tnm_sendyard.emit(True)				
		else:
			self.car2_status = True
			self.ui.lineEdit_12.setText("Off")
			self.ui.lineEdit_17.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		#Car 3 Status Change
		#True means engine 3 is functional
		if(self.ui.lineEdit_13.text() == "Off" or self.ui.lineEdit_13.text() == "OFF" or self.ui.lineEdit_13.text() == "off"):		
			self.car3_status = True
			self.ui.lineEdit_18.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_13.text() == "On" or self.ui.lineEdit_13.text() == "ON" or self.ui.lineEdit_13.text() == "on"):
			self.car3_status = False
			self.ui.lineEdit_18.setText("Broken")
			self.sendYard = True
			signals.tnm_sendyard.emit(True)					
		else:
			self.car3_status = True
			self.ui.lineEdit_13.setText("Off")
			self.ui.lineEdit_18.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		#Car 4 Status Change
		#True means engine 4 is functional
		if(self.ui.lineEdit_14.text() == "Off" or self.ui.lineEdit_14.text() == "OFF" or self.ui.lineEdit_14.text() == "off"):									
			self.car4_status = True
			self.ui.lineEdit_19.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_14.text() == "On" or self.ui.lineEdit_14.text() == "ON" or self.ui.lineEdit_14.text() == "on"):
			self.car4_status = False
			self.ui.lineEdit_19.setText("Broken")
			self.sendYard = True
			signals.tnm_sendyard.emit(True)					
		else:
			self.car4_status = True
			self.ui.lineEdit_14.setText("Off")
			self.ui.lineEdit_19.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		#Car 5 Status Change
		#True means engine 5 is functional
		if(self.ui.lineEdit_15.text() == "Off" or self.ui.lineEdit_15.text() == "OFF" or self.ui.lineEdit_15.text() == "off"):										
			self.car5_status = True
			self.ui.lineEdit_20.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_15.text() == "On" or self.ui.lineEdit_15.text() == "ON" or self.ui.lineEdit_15.text() == "on"):
			self.car5_status = False
			self.ui.lineEdit_20.setText("Broken")
			self.sendYard = True
			signals.tnm_sendyard.emit(True)					
		else:
			self.car5_status = True
			self.ui.lineEdit_15.setText("Off")
			self.ui.lineEdit_20.setText("Operational")
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
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.ui.lineEdit_21.text() == "On" or self.ui.lineEdit_21.text() == "ON" or self.ui.lineEdit_21.text() == "on"):
			self.train1_status = False	
			self.ui.lineEdit_26.setText("Broken")	
			self.sendYard = True
			signals.tnm_sendyard.emit(True)			
		else:
			self.train1_status = True
			self.ui.lineEdit_21.setText("Off")
			self.ui.lineEdit_26.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
			
		
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

		
	#Define variables to be used in tnm_display
		self.train1 = "Train 1 Information"
	#power connected from tnc
		self.curr_power = 0
		signals.tnc_power.connect(self.SetPower)
		self.curr_speed = 0
		self.comm_speed = 0
		signals.tkm_get_speed.connect(self.SetCommSpeed)
	#authority connected from tkm
		self.block_authority = False
		signals.tkm_get_train_auth.connect(self.SetAuthority)
	#Block length connected from tkm
		self.block_length = 1
		self.block_num = 0
		self.block_finished = False
		self.timeBlock = 0
		signals.tkm_get_blength.connect(self.blockTime)
		signals.tkm_get_block.connect(self.blockNum)
		self.blockTime(self.block_length)
	#brake states
		self.Brake = False
		self.eBrake = False
	#Occupancy 
		self.pass_count = 0
		signals.tkm_get_pass_count.connect(self.SetOccupancy)
		self.crew_count = 3
	#Route Information
		self.Mass_Empty = (5*40.9)
		self.curr_mass = 0
		self.Occupancy = pass_crew_count(self.pass_count, self.crew_count)
		self.RouteName = "Green Line"
		self.NextStation = "Dormont"
		self.DoorStatus = False
	#Beacon ID connected from tkm
		self.beacon_bin = 0b00000000
		self.BeaconID = 00000000					#bit1 (red vs green) bit2 (UG vs Station) bit3 (Left side (62->63) vs Right side(63->64))
		signals.tkm_get_beacon.connect(self.SetBeaconID)
		self.BeaconIDStatus = True
	#Internal control status's
		self.lights_Cab = True
		self.lights_High = False
		self.lights_Tun = False
		self.set_temp = 0		#degrees Fahrenheit
		self.curr_temp = 68		#degrees Fahrenheit
		self.announce = "Watch your step. Have a great day!"


		#Defining Actions for specific UI Interactions
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
		self.ui.pushButton_2.clicked.connect(self.update_TrainStat)
		self.ui.pushButton_2.clicked.connect(self.update_RouteInfo)
		self.ui.pushButton_2.clicked.connect(self.update_MoveStat)
		
	
#_______________________________________________________________________
	#function to update Movement Statistics
	def update_MoveStat(self):
		self.curr_speed = set_curr_speed(self.curr_power, self.Occupancy)
		#Update current speed given power value
		self.ui.lineEdit.setText(str(self.curr_speed) + " mph")
		#Send the new calculated current speed to Train Controller
		signals.tnm_curr_speed.emit(self.curr_speed)
		#Update brake status
		if (self.Brake == False):
			self.ui.lineEdit_2.setText("Off")
		else:
			self.ui.lineEdit_2.setText("On")
		
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
		
		#Display stopping distance based on current speed
		#stopping_dist(set_curr_speed(self.curr_power, self.Occupancy))

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
		self.ui.label_23.setText(self.train1)
		
		#Update Route Line
		self.ui.lineEdit_9.setText(self.RouteName)
		#Update Next Station
		self.ui.lineEdit_10.setText(self.NextStation)
		#Update Doors Status
		if (self.DoorStatus == False):
			self.ui.lineEdit_11.setText("Closed")
		else:
			self.ui.lineEdit_11.setText("Open")
			
		#Update Beacon ID Status
		if (self.BeaconIDStatus == False):
			self.ui.lineEdit_12.setText("Error")
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
		if(self.eBrake != True):
			self.eBrake = True
			signals.tnm_ebrake.emit(self.eBrake)
			print(self.eBrake)

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
		signals.tnm_cab_temp.emit(self.curr_temp)
		
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
		
		self.beacon_bin = bin(tkm_beacon)
		#remove first two char: 0b
		beacon_bin = beacon_bin[2:]
		#check if first value is: 1 = green line/0 = red line
		if(self.beacon_bin[2] == 0):
			self.RouteName = "Red Line"
		elif(self.beacon_bin[2] == 1):
			self.RouteName = "Green Line"
		#check if second value is: 0 = station/1 = underground
		if(self.beacon_bin[3] == 0):
			self.lights_Tun == False
		elif(self.beacon_bin[3] == 1):
			self.lights_Tun == True
		#4th bit 	0 Left/1 Right directionality
		
		#Add beacon specification here (for last 5 bits)	Dormont 01010 - station 10
		if(self.beacon_bin[5:] == 0b01010):
			self.NextStation = "Dormont"
	
	#Function to specify block number for each line
	def blockNum(self,BlockNum):
		self.block_num = BlockNum
	
	#Function to take in block length and calculate when train reaches next block
	def blockTime(self,BlockLen):
		#set variables
		self.block_length = BlockLen
		
		#print(self.block_length)
		#calculations
		curr_speed_mps = (self.curr_speed/2.237)						#MPH to mps
		if (self.block_length == 0):
			time_block = 10
		else:
			time_block = (curr_speed_mps/self.block_length)
			self.timeBlock = time_block
		
		#self.block_finished = True
		#signals.tnm_block_finished.emit(self.block_finished)
			
	
	#Function to set Authority from track model signal
	def SetAuthority(self,tkm_authority):
		self.block_authority = tkm_authority
		
	#Function to set Commanded Speed from track model signal
	def SetCommSpeed(self,commSpeed):
		self.comm_speed = commSpeed
		print(str(commSpeed) + " comm speed")
	
	#Function to set Passenger count from track model signal
	def SetOccupancy(self,tkm_pass_count):
		self.pass_count = tkm_pass_count
		
		
	#Function for TIME
	def getTime(self, time_sec, time_min, time_hr, time_tot):
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
	"""
	#display main program and test program, then exit program
	MainWindow.show()
	TestUi.show()
	"""
	sys.exit(app.exec_())
	

