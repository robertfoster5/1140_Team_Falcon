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

from tkm_functions import m_to_f
from tkm_functions import make_data
from tkm_functions import make_data_s
from tkm_functions import make_data_t
from tkm_functions import load_track
from tkm_functions import up_x

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
		
		track = load_track("tkm_load_g.xls")
		t = Track(track)
		
		track = load_track("tkm_load_g.xls")
		q = Track(track)
		
		#create tracks
		self.info = []
		self.info.append(t)
		self.info.append(q)
		self.version = 0
		
		#create trains
		self.trains = []
		#self.info[0].add_train(1,1,1)
		
		#set headers for grids
		self.header_b = ['Block', 'Info']
		self.header_s = ['Station', 'Info']
		self.header_t = ['Train', 'Info']
		
		#set default block data
		self.data_b = make_data(self.info[self.version].blocks,0)
		
		#find first station to show as default
		i = 0
		while(i<len(self.info[self.version].blocks)):
			if(self.info[self.version].blocks[i].station.name != 0):
				break;
			i = i+1
			 
		#set station info
		self.data_s = make_data_s(self.info[self.version].blocks[i].station)
		#self.data_t = make_data_t(self.info[0].train[0],self.info[0].blocks)
		self.data_t = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
		
        #final set up of data tables
		self.ui.model_b = TableModel(self.data_b, self.header_b)
		self.ui.model_s = TableModel(self.data_s, self.header_s)
		self.ui.model_t = TableModel(self.data_t, self.header_t)
		
		self.ui.tableView.setModel(self.ui.model_b)
		self.ui.tableView_S.setModel(self.ui.model_s)
		self.ui.tableView_T.setModel(self.ui.model_t)
		
		#check if block change is entered
		self.ui.enterB.clicked.connect(lambda: self.display_b())
		self.ui.enterS.clicked.connect(lambda: self.display_s())
		self.ui.enterT.clicked.connect(lambda: self.display_t())
		self.ui.enterF.clicked.connect(lambda: self.load_f())
		self.ui.enterV.clicked.connect(lambda: self.display_v())
		
		signals.way_green_speed.connect(self.info[0].set_speed)
		signals.way_red_speed.connect(self.info[1].set_speed)
		
		signals.way_green_occupancy.connect(self.info[0].set_occ)
		signals.way_red_occupancy.connect(self.info[1].set_occ)
		
		signals.way_green_switch_state.connect(self.info[0].set_swit)
		signals.way_red_switch_state.connect(self.info[1].set_swit)
		
		signals.way_green_authority.connect(self.info[0].set_auth)
		signals.way_red_authority.connect(self.info[1].set_auth)
        
		signals.tnm_block_finished.connect(self.info[0].set_train_block)
        		
	#for changing block info
	def display_b(self):
		if self.ui.lineEdit.text() != "":
			b_num = int(self.ui.lineEdit.text())-1
			print(self.version)
			if b_num <= self.info[self.version].end+1 and b_num > 0: 
				self.data_b = make_data(self.info[self.version].blocks,b_num)
				self.ui.model_b = TableModel(self.data_b, self.header_b)
				self.ui.tableView.setModel(self.ui.model_b)
				
	#for changing train info
	def display_t(self):
		if self.ui.lineEdit_t.text() != "":
			t_num = int(self.ui.lineEdit_t.text())-1
			if t_num <= len(self.info[self.version].train):
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
				self.data_s = make_data_s(self.info[self.version].blocks[i].station)
				self.ui.model_s = TableModel(self.data_s, self.header_s)
				self.ui.tableView_S.setModel(self.ui.model_s)
				
	def load_f(self):
		if self.ui.lineEdit_f.text() != "":
			new = load_track(str(self.ui.lineEdit_f.text())+".xls")
			new = Track(new)
			self.info.append(new)
			print(self.info[1].blocks[0].num)
			print(self.info[1].blocks[31].num)
			
	def display_v(self):
		i = 0
		while i < len(self.info):
			if self.ui.lineEdit_v.text() == self.info[i].line:
				break
			i = i+1
			
			self.display_b()
			self.display_s()
			'''
			if len(self.info[i].train) == 0:
				return i
			else:
				self.display_t(i)
				return i
			'''
			self.version = i
			
				
#end of main

if __name__ == '__main__':
	import sys
	
	app = QtWidgets.QApplication(sys.argv)
	
	#MainWindow = QtWidgets.QMainWindow()
	
	prog = tkm_test()
		
	
	sys.exit(app.exec_())   
