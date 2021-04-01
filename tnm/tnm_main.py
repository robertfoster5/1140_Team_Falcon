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


"""
self.tmodel_thread = QThread()
self.tmodel_test = tnm_failureTest()
#self.tmodel_main = tnm_display()
self.tmodel_test.moveToThread(self.tmodel_thread)
self.tmodel_thread.start()
"""

#_______________________________________________________________________
#Failure Test State
class tnm_failureTest(Ui_Test):
	def __init__(self, TestUi):
		super().__init__()
		Ui_Test.__init__(self)
		self.setupUi(TestUi)

		#display test program
		TestUi.show()

		
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
		
		self.lineEdit.editingFinished.connect(self.brake_fail_act)
		self.lineEdit_2.editingFinished.connect(self.brake_fail_act)
		self.lineEdit_3.editingFinished.connect(self.brake_fail_act)
		self.lineEdit_4.editingFinished.connect(self.brake_fail_act)
		self.lineEdit_5.editingFinished.connect(self.brake_fail_act)
		
		self.lineEdit_7.editingFinished.connect(self.engine_fail_act)
		self.lineEdit_12.editingFinished.connect(self.engine_fail_act)
		self.lineEdit_13.editingFinished.connect(self.engine_fail_act)
		self.lineEdit_14.editingFinished.connect(self.engine_fail_act)
		self.lineEdit_15.editingFinished.connect(self.engine_fail_act)
		
		self.lineEdit_21.editingFinished.connect(self.signalP_fail_act)

#_______________________________________________________________________
	#function to update Train Failure interface Info
	def update_Info(self):
		#Update Train Number
		self.label.setText(self.train1_test)
		
		#Don't let Status LineEdits to be edited
		self.lineEdit_6.setReadOnly(True)		#Brake Status's
		self.lineEdit_11.setReadOnly(True)		
		self.lineEdit_8.setReadOnly(True)		
		self.lineEdit_9.setReadOnly(True)			
		self.lineEdit_10.setReadOnly(True)	
		self.lineEdit_16.setReadOnly(True)		#Engine Status's	
		self.lineEdit_17.setReadOnly(True)	
		self.lineEdit_18.setReadOnly(True)	
		self.lineEdit_19.setReadOnly(True)		
		self.lineEdit_20.setReadOnly(True)		
		self.lineEdit_26.setReadOnly(True)		#Signal Pickup Status
		
		
#_______________________________________________________________________
	#function to address Brake Failure Status's
	def brake_fail_act(self):
		#Car 1 Status Change
		#True means brake 1 is functional
		if(self.lineEdit.text() == "Off" or self.lineEdit.text() == "OFF" or self.lineEdit.text() == "off"):	
			self.car1_status = True
			self.lineEdit_6.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)	
		elif(self.lineEdit.text() == "On" or self.lineEdit.text() == "ON" or self.lineEdit.text() == "on"):
			self.car1_status = False	
			self.lineEdit_6.setText("Broken")
			self.sendYard = True
			signals.tnm_sendyard.emit(True)
		else:
			self.car1_status = True
			self.lineEdit.setText("Off")
			self.lineEdit_6.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
			
		#Car 2 Status Change
		#True means brake 2 is functional
		if(self.lineEdit_2.text() == "Off" or self.lineEdit_2.text() == "OFF" or self.lineEdit_2.text() == "off"):
			self.car2_status = True	
			self.lineEdit_11.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.lineEdit_2.text() == "On" or self.lineEdit_2.text() == "ON" or self.lineEdit_2.text() == "on"):
			self.car2_status = False	
			self.lineEdit_11.setText("Broken")
			self.sendYard = True
			signals.tnm_sendyard.emit(True)				
		else:
			self.car2_status = True
			self.lineEdit_2.setText("Off")
			self.lineEdit_11.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		#Car 3 Status Change
		#True means brake 3 is functional
		if(self.lineEdit_3.text() == "Off" or self.lineEdit_3.text() == "OFF" or self.lineEdit_3.text() == "off"):		
			self.car3_status = True
			self.lineEdit_8.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.lineEdit_3.text() == "On" or self.lineEdit_3.text() == "ON" or self.lineEdit_3.text() == "on"):
			self.car3_status = False
			self.lineEdit_8.setText("Broken")
			self.sendYard = True		
			signals.tnm_sendyard.emit(True)			
		else:
			self.car3_status = True
			self.lineEdit_3.setText("Off")
			self.lineEdit_8.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
			
		#Car 4 Status Change
		#True means brake 4 is functional
		if(self.lineEdit_4.text() == "Off" or self.lineEdit_4.text() == "OFF" or self.lineEdit_4.text() == "off"):									
			self.car4_status = True
			self.lineEdit_9.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.lineEdit_4.text() == "On" or self.lineEdit_4.text() == "ON" or self.lineEdit_4.text() == "on"):
			self.car4_status = False
			self.lineEdit_9.setText("Broken")
			self.sendYard = True
			signals.tnm_sendyard.emit(True)							
		else:
			self.car4_status = True
			self.lineEdit_4.setText("Off")
			self.lineEdit_9.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		#Car 5 Status Change
		#True means brake 5 is functional
		if(self.lineEdit_5.text() == "Off" or self.lineEdit_5.text() == "OFF" or self.lineEdit_5.text() == "off"):										
			self.car5_status = True
			self.lineEdit_10.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.lineEdit_5.text() == "On" or self.lineEdit_5.text() == "ON" or self.lineEdit_5.text() == "on"):
			self.car5_status = False
			self.lineEdit_10.setText("Broken")
			self.sendYard = True
			signals.tnm_sendyard.emit(True)					
		else:
			self.car5_status = True
			self.lineEdit_5.setText("Off")
			self.lineEdit_10.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		
#_______________________________________________________________________
	#function to address Engine Failure Status's
	def engine_fail_act(self):
		#Car 1 Status Change
		#True means engine 1 is functional
		if(self.lineEdit_7.text() == "Off" or self.lineEdit_7.text() == "OFF" or self.lineEdit_7.text() == "off"):	
			self.car1_status = True
			self.lineEdit_16.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.lineEdit_7.text() == "On" or self.lineEdit_7.text() == "ON" or self.lineEdit_7.text() == "on"):
			self.car1_status = False	
			self.lineEdit_16.setText("Broken")
			self.sendYard = True
			signals.tnm_sendyard.emit(True)				
		else:
			self.car1_status = True
			self.lineEdit_7.setText("Off")
			self.lineEdit_16.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
			
		#Car 2 Status Change
		#True means engine 2 is functional
		if(self.lineEdit_12.text() == "Off" or self.lineEdit_12.text() == "OFF" or self.lineEdit_12.text() == "off"):
			self.car2_status = True	
			self.lineEdit_17.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.lineEdit_12.text() == "On" or self.lineEdit_12.text() == "ON" or self.lineEdit_12.text() == "on"):
			self.car2_status = False	
			self.lineEdit_17.setText("Broken")
			self.sendYard = True	
			signals.tnm_sendyard.emit(True)				
		else:
			self.car2_status = True
			self.lineEdit_12.setText("Off")
			self.lineEdit_17.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		#Car 3 Status Change
		#True means engine 3 is functional
		if(self.lineEdit_13.text() == "Off" or self.lineEdit_13.text() == "OFF" or self.lineEdit_13.text() == "off"):		
			self.car3_status = True
			self.lineEdit_18.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.lineEdit_13.text() == "On" or self.lineEdit_13.text() == "ON" or self.lineEdit_13.text() == "on"):
			self.car3_status = False
			self.lineEdit_18.setText("Broken")
			self.sendYard = True
			signals.tnm_sendyard.emit(True)					
		else:
			self.car3_status = True
			self.lineEdit_13.setText("Off")
			self.lineEdit_18.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		#Car 4 Status Change
		#True means engine 4 is functional
		if(self.lineEdit_14.text() == "Off" or self.lineEdit_14.text() == "OFF" or self.lineEdit_14.text() == "off"):									
			self.car4_status = True
			self.lineEdit_19.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.lineEdit_14.text() == "On" or self.lineEdit_14.text() == "ON" or self.lineEdit_14.text() == "on"):
			self.car4_status = False
			self.lineEdit_19.setText("Broken")
			self.sendYard = True
			signals.tnm_sendyard.emit(True)					
		else:
			self.car4_status = True
			self.lineEdit_14.setText("Off")
			self.lineEdit_19.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		#Car 5 Status Change
		#True means engine 5 is functional
		if(self.lineEdit_15.text() == "Off" or self.lineEdit_15.text() == "OFF" or self.lineEdit_15.text() == "off"):										
			self.car5_status = True
			self.lineEdit_20.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.lineEdit_15.text() == "On" or self.lineEdit_15.text() == "ON" or self.lineEdit_15.text() == "on"):
			self.car5_status = False
			self.lineEdit_20.setText("Broken")
			self.sendYard = True
			signals.tnm_sendyard.emit(True)					
		else:
			self.car5_status = True
			self.lineEdit_15.setText("Off")
			self.lineEdit_20.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
			
	
#_______________________________________________________________________
	#function to address Signal Pickup Failure Status's
	def signalP_fail_act(self):
		#train 1 Status Change
		#True means train 1 is functional
		if(self.lineEdit_21.text() == "Off" or self.lineEdit_21.text() == "OFF" or self.lineEdit_21.text() == "off"):	
			self.train1_status = True
			self.lineEdit_26.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		elif(self.lineEdit_21.text() == "On" or self.lineEdit_21.text() == "ON" or self.lineEdit_21.text() == "on"):
			self.train1_status = False	
			self.lineEdit_26.setText("Broken")	
			self.sendYard = True
			signals.tnm_sendyard.emit(True)			
		else:
			self.train1_status = True
			self.lineEdit_21.setText("Off")
			self.lineEdit_26.setText("Operational")
			self.sendYard = False
			signals.tnm_sendyard.emit(False)
		
		
#_____________________________________________________________________________________________________________		
#_____________________________________________________________________________________________________________
#Main Window for Train Model Interface
class tnm_display(Ui_MainWindow):
	
	ui = ""
	
	def __init__(self, MainWindow):
		Ui_MainWindow.__init__(self)
		self.setupUi(MainWindow)
		super().__init__()
		
		#display main program
		MainWindow.show()
		
		#Signals defined here
		tnm_comm_speed = pyqtSignal(float)		#All signals for Track Controller
		tnm_curr_speed = pyqtSignal(float)
		tnm_authority = pyqtSignal(bool)
		tnm_beacondID = pyqtSignal(list)
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
		signals.tkm_get_auth.connect(self.SetAuthority)
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
		self.RouteName = "Blue Line"
		self.NextStation = "Dormont"
		self.DoorStatus = False
			#Beacon ID connected from tkm
		self.BeaconID = 00000000					#bit1 (red vs green) bit2 (UG vs Station) bit3 (Left side vs Right side)
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
		
		signals.time.connect(self.GetDatetime)							#Display running time
		self.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
		self.dateTimeEdit.setDisplayFormat("MM/dd/yyyy hh:mm:ss")
		
		self.pushButton.clicked.connect(self.EmergencyBraking)			#Verify eBrake is pressed
		
		self.lineEdit_17.editingFinished.connect(self.Temperature)		#Update Temperature interface
		#self.pushButton_2.clicked.connect(self.update_TrainStat)
	
#_______________________________________________________________________
	#function to update Movement Statistics
	def update_MoveStat(self):
		self.curr_speed = set_curr_speed(self.curr_power, self.Occupancy)
		#Update current speed given power value
		self.lineEdit.setText(str(self.curr_speed) + " mph")
		#Send the new calculated current speed to Train Controller
		signals.tnm_curr_speed.emit(self.curr_speed)
		#Update brake status
		if (self.Brake == False):
			self.lineEdit_2.setText("Off")
		else:
			self.lineEdit_2.setText("On")
		
		#Don't allow changes to lineEdits
		self.lineEdit.setReadOnly(True)
		self.lineEdit_2.setReadOnly(True)
		self.lineEdit_3.setReadOnly(True)
		self.lineEdit_4.setReadOnly(True)
		self.lineEdit_5.setReadOnly(True)
		
		#Address Authority Here
		signals.tnm_authority.emit(self.block_authority)
		
		#Address Commanded Speed
		signals.tnm_comm_speed.emit(self.comm_speed)
		
		#Display stopping distance based on current speed
		stopping_dist(set_curr_speed(self.curr_power, self.Occupancy))

#_______________________________________________________________________	
	#function to update Train Statistics (Mass, Pass & Crew count)
	def update_TrainStat(self):
		
		#Update pass_count
		self.lineEdit_6.setText(str(self.pass_count))
		#Update crew_count
		self.lineEdit_7.setText(str(self.crew_count))
		#Update current Mass of Train
		self.Occupancy = pass_crew_count(self.pass_count, self.crew_count)
		self.total_mass = ((self.Occupancy*56.699)/2000) + self.Mass_Empty
		self.lineEdit_8.setText(str(round(self.total_mass)) + " tons")
		
		#Don't allow changes to lineEdits
		self.lineEdit_6.setReadOnly(True)
		self.lineEdit_7.setReadOnly(True)
		self.lineEdit_8.setReadOnly(True)
		
#_______________________________________________________________________
	#function to update Route Information and Train Internal Controls
	def update_RouteInfo(self):
		
		#Update Train Numbering Header
		self.label_23.setText(self.train1)
		
		#Update Route Line
		self.lineEdit_9.setText(self.RouteName)
		#Update Next Station
		self.lineEdit_10.setText(self.NextStation)
		#Update Doors Status
		if (self.DoorStatus == False):
			self.lineEdit_11.setText("Closed")
		else:
			self.lineEdit_11.setText("Open")
		#Update Beacon ID Status
		if (self.BeaconIDStatus == False):
			self.lineEdit_12.setText("Error")
		else:
			self.lineEdit_12.setText("Recieved")
			signals.tnm_beaconID.emit(self.BeaconID)

		
		#update Cabin Lights status
		if (self.lights_Cab == False):
			self.lineEdit_13.setText("Off")
		else:
			self.lineEdit_13.setText("On")
		#update High Beam Lights status
		if (self.lights_High == False):
			self.lineEdit_14.setText("Off")
		else:
			self.lineEdit_14.setText("On")
		#update Tunnel Lights status
		if (self.lights_Tun == False):
			self.lineEdit_15.setText("Off")
		else:
			self.lineEdit_15.setText("On")
			
		#Don't allow changes to lineEdits
		self.lineEdit_9.setReadOnly(True)
		self.lineEdit_10.setReadOnly(True)
		self.lineEdit_11.setReadOnly(True)
		self.lineEdit_12.setReadOnly(True)
		self.lineEdit_13.setReadOnly(True)
		self.lineEdit_14.setReadOnly(True)
		self.lineEdit_15.setReadOnly(True)
			
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
		for i in self.lineEdit_17.text():
				if(i.isalpha() == True):
					AlphaFlag = True
		if(AlphaFlag == True):
			self.lineEdit_17.setText(str(self.curr_temp))
			self.set_temp = self.curr_temp
		elif(self.lineEdit_17.text().isdigit() == True):
			AlphaFlag = False
			self.set_temp = int(self.lineEdit_17.text())
		
		#Use temp_control function to set the current temperature
		self.lineEdit_16.setText(str(temp_control(self.set_temp, self.curr_temp)) + " F")
		signals.tnm_cab_temp.emit(self.curr_temp)
		
		#Don't allow time module to be edited
		self.lineEdit_16.setReadOnly(True)
	
	
	#function for updating the current date and time widget
	def GetDatetime(self):
		dateTime = self.dateTimeEdit.dateTime()
		dateTime_string = dateTime.toString(self.dateTimeEdit.displayFormat())
		self.dateTimeEdit.dateTimeFromText(dateTime_string)
		
		#Don't allow time module to be edited
		self.dateTimeEdit.setReadOnly(True)

	#function for updating the internal train announcements
	def DispAnnounce(self):
		self.lineEdit_18.setText(self.announce)
		
		#Don't allow announcements text to be edited
		self.lineEdit_18.setReadOnly(True)
		
#_______________________________________________________________________
	#Function to set power from tnc signal
	def SetPower(tnc_power):
		self.curr_power = tnc_power
	
	#Function to set Beacon ID from track model signal
	def SetBeaconID(tkm_beacon):
		self.BeaconId = tkm_beacon
	
	#Function to set Authority from track model signal
	def SetAuthority(tkm_authority):
		self.block_authority = tkm_authority
		
	#Function to set Commanded Speed from track model signal
	def SetCommSpeed(tkm_comm_speed):
		self.comm_speed = tkm_comm_speed
	
	#Function to set Passenger count from track model signal
	def SetOccupancy(tkm_pass_count):
		self.pass_count = tkm_pass_count
		
#_______________________________________________________________________
if __name__ == "__main__":
	import sys
	
	app = QtWidgets.QApplication(sys.argv)
	MainWindow = QtWidgets.QMainWindow()
	TestUi = QtWidgets.QMainWindow()

	#Initialize main program and test program
	prog = tnm_display(MainWindow)
	test = tnm_failureTest(TestUi)
	"""
	#display main program and test program, then exit program
	MainWindow.show()
	TestUi.show()
	"""
	sys.exit(app.exec_())
	

