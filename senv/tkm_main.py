import sys
import sys
#pyuic5 -x tkm_test.ui -o tkm_test.py
#git status
#git pull
 
#git commit -a
#-i (notes) esc
#:WQ enter
#git push
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QObject, QThread, pyqtSignal

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QBrush, QPen
from PyQt5.QtCore import Qt
from tkm_test import Ui_MainWindow

from tkm_class import Block
from tkm_class import Station
from tkm_class import Train
from tkm_class import Track
from tkm_class import Envi_Temp
from tkm_class import Track_Heater

from tkm_functions import m_to_f
from tkm_functions import make_data
from tkm_functions import make_data_s
from tkm_functions import make_data_t
from tkm_functions import load_track
from tkm_functions import make_data_sect
from tkm_functions import make_data_sall

from signals import signals

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data,header):
        super(TableModel, self).__init__()
        self._data = data
        self.header = header

    def data(self, index, role):
        if role == Qt.DisplayRole:
            # See below for the nested-list data structure.
            # .row() indexes into the outer list,
            # .column() indexes into the sub-list
            return self._data[index.row()][index.column()]

    def rowCount(self, index):
        # The length of the outer list.
        return len(self._data)

    def columnCount(self, index):
        # The following takes the first sub-list, and returns
        # the length (only works if all rows are an equal length)
        return len(self._data[0])
        
    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.header[col]
        return None

class tkm_test(QObject):
	def __init__(self):		
		super().__init__()
		print("running track model")
		self.MainWindow = QtWidgets.QMainWindow()
		
		self.ui = Ui_MainWindow()  
		self.ui.setupUi(self.MainWindow)     
		self.MainWindow.show()
		
		#loading red and green lines
		track = load_track("tkm_load_g.xls")
		t = Track(track)
		
		track = load_track("tkm_load_r.xls")
		q = Track(track)
		
		#setting up temp and track heater obj
		self.ui.heat_stat.setText("Off")
		self.ui.spinBox.setValue(40)
		self.temp = Envi_Temp(self.ui.spinBox.value())
		signals.tkm_get_envi_temp.emit(self.temp.temp)
		
		#create tracks
		self.info = []
		self.info.append(t)
		self.info.append(q)
		self.version = 0
		
		self.mins = 0
		
		self.ui.curLin.setText(self.info[self.version].line)
		
		#create trains
		self.trains = []
		#self.info[0].add_train(1,1,1)
		
		#set headers for grids
		self.header_b = ['Block', 'Info']
		self.header_s = ['Station', 'Info']
		self.header_t = ['Train', 'Info']
		self.header_sect = ["Num","Length","Grade","Speed Limit","Station","Switch","Switch State","Crossing","Elevation","Cumulative","Underground","Beacon ID","Occupancy","Block Error"] 
		self.header_sall = ["Station Name","Station Side","Sales","# of People","Station Block"]
		
		#set default block data
		self.data_b = make_data(self.info[self.version].blocks,0)
		
		#find first station to show as default
		i = 0
		while(i<len(self.info[self.version].blocks)):
			if(self.info[self.version].blocks[i].station.name != 0):
				break;
			i = i+1
			 
		#set station info
		self.data_s = make_data_s(self.info[self.version].blocks[i])
		self.data_t = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
		
		#default section info
		self.data_sect = make_data_sect(self.info[self.version].blocks,"A")
		
		#all station info
		self.data_sall = make_data_sall(self.info[self.version].blocks)
		
        #final set up of data tables
		self.ui.model_b = TableModel(self.data_b, self.header_b)
		self.ui.model_s = TableModel(self.data_s, self.header_s)
		self.ui.model_t = TableModel(self.data_t, self.header_t)
		self.ui.model_sect = TableModel(self.data_sect, self.header_sect)
		self.ui.model_Sall = TableModel(self.data_sall, self.header_sall)
		
		self.ui.tableView.setModel(self.ui.model_b)
		self.ui.tableView_S.setModel(self.ui.model_s)
		self.ui.tableView_T.setModel(self.ui.model_t)
		self.ui.tableView_Sect.setModel(self.ui.model_sect)
		self.ui.tableView_Sall.setModel(self.ui.model_Sall)
		
		#check if block change is entered
		self.ui.enterB.clicked.connect(lambda: self.display_b())
		self.ui.enterS.clicked.connect(lambda: self.display_s())
		self.ui.enterT.clicked.connect(lambda: self.display_t())
		self.ui.enterF.clicked.connect(lambda: self.load_f())
		self.ui.enterV.clicked.connect(lambda: self.display_v())
		self.ui.enterTemp.clicked.connect(lambda: self.display_temp())
		self.ui.enterH.clicked.connect(lambda: self.track_heat())
		self.ui.enterE.clicked.connect(lambda: self.error_select())
		self.ui.refresh.clicked.connect(lambda: self.ref())
		self.ui.enterSect.clicked.connect(lambda: self.display_sect())
		
		#signals from other modules
		signals.way_green_speed.connect(self.info[0].set_speed)
		signals.way_red_speed.connect(self.info[1].set_speed)
		
		signals.way_green_occupancy.connect(self.info[0].set_occ)
		signals.way_red_occupancy.connect(self.info[1].set_occ)
		
		signals.way_green_switch_state.connect(self.info[0].set_swit)
		signals.way_red_switch_state.connect(self.info[1].set_swit)
		
		signals.way_green_authority.connect(self.info[0].set_auth)
		signals.way_red_authority.connect(self.info[1].set_auth)
        
		signals.way_green_health.connect(self.info[0].set_health)
		signals.way_red_health.connect(self.info[1].set_health)
        
		signals.tnm_block_finished_green.connect(self.info[0].set_train_block)
		signals.tnm_block_finished_red.connect(self.info[1].set_train_block)
		
		signals.ctc_make_train_green.connect(self.info[0].add_train)
		signals.ctc_make_train_red.connect(self.info[1].add_train)
		
		signals.ctc_destroy_train_green.connect(self.t_dest)
		signals.ctc_destroy_train_red.connect(self.t_dest)
		
		signals.tnm_train_stop_num.connect(self.t_find)
		
		signals.time.connect(self.sales)
		signals.time.connect(self.ref)
        
        		
	#for changing block info
	def display_b(self):
		if self.ui.lineEdit.text() != "":
			b_num = int(self.ui.lineEdit.text())-1
			if b_num < len(self.info[self.version].blocks) and b_num >= 0: 
				self.data_b = make_data(self.info[self.version].blocks,b_num)
				self.ui.model_b = TableModel(self.data_b, self.header_b)
				self.ui.tableView.setModel(self.ui.model_b)
				
	#for changing train info
	def display_t(self):
		if self.ui.lineEdit_t.text() != "" and len(self.info[self.version].train) >0 :
			t_num = int(self.ui.lineEdit_t.text())-1
			if t_num < len(self.info[self.version].train):
				self.data_t = make_data_t(self.info[self.version].train[t_num],self.info[self.version].blocks)
				self.ui.model_t = TableModel(self.data_t, self.header_t)
				self.ui.tableView_T.setModel(self.ui.model_t)
	
	#for changing station info			
	def display_s(self):
		if self.ui.lineEdit_s.text() != "":
			s_name = self.ui.lineEdit_s.text()
			if(s_name.islower()):
				s_name = s_name.upper()
				
			i = 0
			while i < len(self.info[self.version].blocks):
				if s_name == self.info[self.version].blocks[i].station.name:
					break
				
				i = i+1
				
			if i == len(self.info[self.version].blocks):
				return 0
			else:
				self.data_s = make_data_s(self.info[self.version].blocks[i])
				self.ui.model_s = TableModel(self.data_s, self.header_s)
				self.ui.tableView_S.setModel(self.ui.model_s)
	#displaying sections of a line
	def display_sect(self):
		if self.ui.select_sect.text() != "":
			sect = self.ui.select_sect.text()
			sect = sect.upper()
			self.data_sect = make_data_sect(self.info[self.version].blocks,sect)
			self.ui.model_sect = TableModel(self.data_sect, self.header_sect)
			self.ui.tableView_Sect.setModel(self.ui.model_sect)
	#loading a new track file	
	def load_f(self):
		if self.ui.lineEdit_f.text() != "":
			new = load_track(str(self.ui.lineEdit_f.text())+".xls")
			new = Track(new)
			self.info.append(new)
	#switching which track line info is being shown 
	def display_v(self):
		if self.ui.lineEdit_v.text() != "":
			i = 0
			while i < len(self.info):
				if self.ui.lineEdit_v.text() == self.info[i].line or self.ui.lineEdit_v.text() == self.info[i].line.upper() or self.ui.lineEdit_v.text() == self.info[i].line.lower():
					break
				i = i+1
			
			#self.display_b()
			#self.display_s()
			self.version = i
			self.ui.curLin.setText(self.info[self.version].line)
			self.ref()
	#changing environmental temperature
	def display_temp(self):
		self.temp.set_temp(self.ui.spinBox.value())
		if self.temp.th.state == 1 and self.ui.heat_stat.text() != "On":
			self.ui.heat_stat.setText("On")
		signals.tkm_get_envi_temp.emit(self.temp.temp)
	#track heat toggle	
	def track_heat(self):
		if self.ui.heat_stat.text() == "Off":
			self.temp.th.toggle(1)
			self.ui.heat_stat.setText("On")
		elif self.temp.temp > 4.44:
			self.temp.th.toggle(0)
			self.ui.heat_stat.setText("Off")
	#generate ticket sales every minute
	def sales(self,sec,mini,hr,tot):
		if self.mins < mini or (self.mins == 59 and mini == 0):
			self.mins = mini
			q = 0
			tots = 0
			while q < len(self.info):
				p = 0
				while p < len(self.info[q].blocks):
					if self.info[q].blocks[p].station.name != 0:
							if self.info[q].blocks[p].station.occ < 300:	
								tots = tots + self.info[q].blocks[p].station.get_sales()
					p = p+1
				q = q+1
				
			signals.tkm_get_sales.emit(tots)
	#selecting block errors			
	def error_select(self):
		if self.ui.checkBox.isChecked() == 1 or self.ui.checkBox_2.isChecked() == 1 or self.ui.checkBox_3.isChecked() == 1:
			#self.info[self.version].blocks[int(self.ui.selectE.text())-1].health = 1
			self.info[self.version].blocks[int(self.ui.selectE.text())-1].occ = 1
			self.ui.checkBox.setChecked(False)
			self.ui.checkBox_2.setChecked(False)
			self.ui.checkBox_3.setChecked(False)
			self.ui.selectE.clear()
			signals.tkm_get_occ.emit(self.info[self.version].get_occ())
	#refresh data	
	def ref(self):
		if self.ui.lineEdit.text() != "":
			self.display_b()
		elif self.ui.lineEdit_s.text() != "":
			self.display_s()
		if len(self.info[self.version].train) > 0:
			if self.ui.lineEdit_t.text() != "":
				self.display_t()
		if self.ui.select_sect.text() != "":
			self.display_sect()
			
		self.data_sall = make_data_sall(self.info[self.version].blocks)
		self.ui.model_Sall = TableModel(self.data_sall, self.header_sall)
		self.ui.tableView_Sall.setModel(self.ui.model_Sall)
	#destroy train when told by CTC		
	def t_dest(self,num):
		j = 0
		while j < len(self.info):
			i = 0
			while i < len(self.info[j].train):
				if num == self.info[j].train[i].num:
					val = self.info[j].train[i].destroy()-1
					self.info[j].blocks[int(val)].occ = 0
					self.info[j].set_occ(self.info[j].get_occ())
					i = len(self.info[j].train)
					j = len(self.info)-1
				i = i+1
			j = j+1				
	#find which train to update disembark and boarding
	def t_find(self,num):
		j = 0
		while j < len(self.info):
			i = 0
			while i <len(self.info[j].train):
				if num == self.info[j].train[i].num:
					print("Stop at station "+str(self.info[j].train[i].num))
					self.info[j].update_dis(i)
					break
					#i = len(self.info[j].train)
					
				i = i+1
			
			j = j+1
			
				
#end of main

if __name__ == '__main__':
	import sys
	
	app = QtWidgets.QApplication(sys.argv)
	
	#MainWindow = QtWidgets.QMainWindow()
	
	prog = tkm_test()
		
	
	sys.exit(app.exec_())   
