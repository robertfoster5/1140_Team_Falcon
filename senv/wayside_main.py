import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QObject, QThread, pyqtSignal
from wayside_qtui_test import Ui_MainWindow
from wayside_ws_control import Wayside
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

class wayside_qtui_test(QObject):
	
	def __init__(self):
		print("running track controller")
		super().__init__()
		self.wayside_qtui_test = QtWidgets.QMainWindow()
		#ui = Ui_MainWindow()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self.wayside_qtui_test)
		self.wayside_qtui_test.show()
	
		#self.MainWindow.show()
		
		#Create wayside objects
		self.g1 = Wayside("g1.txt", "Green")
		self.g2 = Wayside("g2.txt", "Green")
		self.g3 = Wayside("g3.txt", "Green")
		self.g4 = Wayside("g4.txt", "Green")
		self.g5 = Wayside("g5.txt", "Green")
		self.r1 = Wayside("r1.txt", "Red")
		self.r2 = Wayside("r2.txt", "Red")
		self.r3 = Wayside("r3.txt", "Red")

		"""self.g1_thread = QThread()
        self.g1 = Wayside("g1.txt", "Green")
        self.g1.moveToThread(self.g1_thread)
        self.g1_thread.start()"""
        
        #Sets initial table settings for blocks, crossings, and switches
		self.header_blocks = ['Block', 'Status', 'Line']
		
		self.data_blocks = [[0,0,0]]
		
		self.header_cross = ['Crossing', 'Status']
		
		self.data_cross = [[0,0]]
		
		self.header_switch = ['Switch', 'Status']
		
		self.data_switch = [[0,0]]	
		
		self.ui.model = TableModel(self.data_blocks,self.header_blocks)
	
		self.ui.tableView.setModel(self.ui.model)
		
		self.ui.model = TableModel(self.data_cross,self.header_cross)
		
		self.ui.tableView_2.setModel(self.ui.model)
		
		self.ui.model = TableModel(self.data_switch,self.header_switch)
		
		self.ui.tableView_3.setModel(self.ui.model)
		
		#sets initial table shown on UI
		self.update_tables(self.g1)
		
		#Changes visible wayside information based on button presses
		self.ui.pushButton.clicked.connect(lambda: self.update_tables(self.r1))
		self.ui.pushButton_2.clicked.connect(lambda: self.update_tables(self.r2))
		self.ui.pushButton_3.clicked.connect(lambda: self.update_tables(self.r3))
		
		self.ui.pushButton_4.clicked.connect(lambda: self.update_tables(self.g1))
		self.ui.pushButton_7.clicked.connect(lambda: self.update_tables(self.g2))
		self.ui.pushButton_6.clicked.connect(lambda: self.update_tables(self.g3))
		self.ui.pushButton_5.clicked.connect(lambda: self.update_tables(self.g4))
		self.ui.pushButton_8.clicked.connect(lambda: self.update_tables(self.g5))
		
		#connects signals from other modules to functions
		signals.ctc_suggested_speed_red.connect(self.update_speed_red)
		signals.ctc_suggested_speed_green.connect(self.update_speed_green)
		signals.ctc_authority_red.connect(self.new_authority_red)
		signals.ctc_authority_green.connect(self.new_authority_green)
		signals.ctc_maintenance.connect(self.maintenance_order)
		signals.tkm_get_occ.connect(self.update_occupancy)
		
		#update all tables together with current wayside	
	def update_tables(self, ws):
		self.curr_ws = ws
		self.update_block(ws)
		self.update_switch(ws)
		self.update_cross(ws)
		self.show_tables()
	
		#shows tables with updated information
	def show_tables(self):
		self.ui.model = TableModel(self.data_blocks,self.header_blocks)
		
		self.ui.tableView.setModel(self.ui.model)
		
		self.ui.model = TableModel(self.data_switch,self.header_switch)
		
		self.ui.tableView_3.setModel(self.ui.model)
		
		self.ui.model = TableModel(self.data_cross,self.header_cross)
		
		self.ui.tableView_2.setModel(self.ui.model)
		
		#updates block table with health and occupancy	
	def update_block(self, ws):	
		self.data_blocks = []
		for i in range(len(ws.block_occ)):
			if ws.block_health[i] == "1":
				self.data_blocks.append(["Block " + ws.block_name[i], "Broken", ws.line])
			elif ws.block_health[i] == "0" and ws.block_occ[i] == "1":
				self.data_blocks.append(["Block " + ws.block_name[i], "Occupied", ws.line])
			elif ws.block_occ[i] == "0":
				self.data_blocks.append(["Block " + ws.block_name[i], "Empty", ws.line])
		
		#updates switch table with current switch states
	def update_switch(self, ws):
		self.data_switch = []
		if ws.num_switch > 0:
			for i in range(ws.num_switch):
				self.data_switch.append(["Switch " + ws.switch_name[i], ws.switch_state[i]])
		else:
			self.data_switch.append(["N/A", "N/A"])
		
		#updates crossing table if crossing is working
	def update_cross(self, ws):
		self.data_cross = []
		if ws.num_cross > 0:
			for i in range(ws.num_cross):
				self.data_cross.append(["Crossing " + ws.cross_name[i], ws.cross_state[i]])
		else:
			self.data_cross.append(["N/A", "N/A"])

		#maintenance order from CTC
	def maintenance_order(self, order):
		if order[0] != "0":
			#if red line
			if order[0] == "r":
				temp_order = order[1:len(order)]
				#if order on block
				if order[1] == "b":
					temp = []
					or1 = temp_order[1:24]
					or2 = temp_order[24:46]
					or2.append(temp_order[67])
					or2.append(temp_order[68])
					or2.append(temp_order[69])
					or2.append(temp_order[70])
					or2.append(temp_order[71])
					or2.append(temp_order[72])
					or2.append(temp_order[73])
					or2.append(temp_order[74])
					or2.append(temp_order[75])
					or2.append(temp_order[76])
					or3 = temp_order[46:67]
					self.r1.m_order_block(or1)
					self.r2.m_order_block(or2)
					self.r3.m_order_block(or3)
				#if order on switch
				elif order[1] == "s":
					self.r1.m_order_switch(temp_order[1:3])
					self.r2.m_order_switch(temp_order[3:7])
					self.r3.m_order_switch(temp_order[7])
				self.compile_switch_red()
				self.compile_health_red()
				self.compile_block_occ_red()
			#if order on green line
			else:
				temp_order = order[1:len(order)]
				#if order on block
				if order[1] == "b":  
					or1 = temp_order[1:21]
					or2 = temp_order[21:36]
					or2.append(temp_order[147])
					or2.append(temp_order[148])
					or2.append(temp_order[149])
					or2.append(temp_order[150])
					or3 = temp_order[36:74]
					or4 = temp_order[74:110]
					or5 = temp_order[110:147]
					self.g1.m_order_block(or1)
					self.g2.m_order_block(or2)
					self.g3.m_order_block(or3)
					self.g4.m_order_block(or4)
					self.g5.m_order_block(or5)
				#if order on switch
				elif order[1] == "s":
					self.g1.m_order_switch(temp_order[1])
					self.g2.m_order_switch(temp_order[2])
					self.g3.m_order_switch(temp_order[3:5])
					self.g4.m_order_switch(temp_order[5:len(order)])
				self.compile_switch_green()
				self.compile_health_green()
				self.compile_block_occ_green()
		self.update_tables(self.curr_ws)
		
		#sets new authority and sends it through system	
	def new_authority_red(self, authority):
		temp = []
		self.red_authority = authority
		self.r1.authority = authority[1:24]
		temp = authority[24:46]
		temp.append(authority[67])
		temp.append(authority[68])
		temp.append(authority[69])
		temp.append(authority[70])
		temp.append(authority[71])
		temp.append(authority[72])
		temp.append(authority[73])
		temp.append(authority[74])
		temp.append(authority[75])
		temp.append(authority[76])
		self.r2.authority = temp
		self.r3.authority = authority[46:67]
		self.compile_auth_red()
		self.update_tables(self.curr_ws)
		
		#sets new authority and sends it through system
	def new_authority_green(self,authority):
		temp = []
		self.green_authority = authority
		self.g1.authority = authority[1:21]
		temp = authority[21:36]
		temp.append(authority[147])
		temp.append(authority[148])
		temp.append(authority[149])
		temp.append(authority[150])
		self.g2.authority = temp
		self.g3.authority = authority[36:74]
		self.g4.authority = authority[74:110]
		self.g5.authority = authority[110:147]
		self.compile_auth_green()
		self.update_tables(self.curr_ws)
		
		#sets new occupancy and sends it through system		
	def update_occupancy(self, occupancy):
		temp = []
		temp1 = []
		temp2 = []
		if occupancy[0] == "0":
			for i in range(1,24):
				temp1.append(occupancy[i])
			self.r1.occ_change(temp1)
			for i in range(24,46):
				temp.append(occupancy[i])
			temp.append(occupancy[67])
			temp.append(occupancy[68])
			temp.append(occupancy[69])
			temp.append(occupancy[70])
			temp.append(occupancy[71])
			temp.append(occupancy[72])
			temp.append(occupancy[73])
			temp.append(occupancy[74])
			temp.append(occupancy[75])
			temp.append(occupancy[76])
			self.r2.occ_change(temp)
			for i in range(46,67):
				temp2.append(occupancy[i])
			self.r3.occ_change(temp2)
			self.r1.update_ws()
			self.r2.update_ws()
			self.r3.update_ws()
			self.compile_cross_red()
			self.compile_switch_red()
			self.compile_block_occ_red_ctc()
			self.compile_auth_red()
			self.compile_speed_red()
		else:
			self.g1.occ_change(occupancy[1:21])
			temp = occupancy[21:36]
			temp.append(occupancy[147])
			temp.append(occupancy[148])
			temp.append(occupancy[149])
			temp.append(occupancy[150])
			self.g2.occ_change(temp)
			self.g3.occ_change(occupancy[36:74])
			self.g4.occ_change(occupancy[74:110])
			self.g5.occ_change(occupancy[110:147])
			self.g1.update_ws()
			self.g2.update_ws()
			self.g3.update_ws()
			self.g4.update_ws()
			self.g5.update_ws()
			self.compile_cross_green()
			self.compile_switch_green()
			self.compile_block_occ_green_ctc()
			self.compile_auth_green()
			self.compile_speed_green()
		self.update_tables(self.curr_ws)
		
		#sets new speed and sends it through system
		#Creates binary from speed so that waysides can adjust for safety
	def update_speed_red(self, speed):
		temp_s = []
		for i in range(len(speed)):
			if speed[i] == 0:
				temp_s.append(0)
			elif i == 0:
				temp_s.append(speed[0])
			else:
				temp_s.append(1)
		temp = []
		self.red_speed = speed
		self.r1.b_speed = temp_s[1:24]
		temp = temp_s[24:46]
		temp.append(temp_s[67])
		temp.append(temp_s[68])
		temp.append(temp_s[69])
		temp.append(temp_s[70])
		temp.append(temp_s[71])
		temp.append(temp_s[72])
		temp.append(temp_s[73])
		temp.append(temp_s[74])
		temp.append(temp_s[75])
		temp.append(temp_s[76])
		self.r2.b_speed = temp
		self.r3.b_speed = temp_s[46:67]
		self.compile_speed_red()
		self.update_tables(self.curr_ws)
		
		#sets new speed and sends it through system
		#Creates binary from speed so that waysides can adjust for safety	
	def update_speed_green(self, speed):
		temp_s = []
		for i in range(len(speed)):
			if speed[i] == 0:
				temp_s.append(0)
			elif i == 0:
				temp_s.append(speed[0])
			else:
				temp_s.append(1)
		temp = []
		self.green_speed = speed
		self.g1.b_speed = temp_s[1:21]
		temp = temp_s[21:36]
		temp.append(temp_s[147])
		temp.append(temp_s[148])
		temp.append(temp_s[149])
		temp.append(temp_s[150])
		self.g2.b_speed = temp
		self.g3.b_speed = temp_s[36:74]
		self.g4.b_speed = temp_s[74:110]
		self.g5.b_speed = temp_s[110:147]
		self.compile_speed_green()
		self.update_tables(self.curr_ws)
		
		#compiles variable to emit through system	
	def compile_health_red(self):
		temp_h = []
		temp_h.append("0")
		for i in range(23):
			temp_h.append(self.r1.block_health[i])
		for i in range(22):
			temp_h.append(self.r2.block_health[i])
		for i in range(21):
			temp_h.append(self.r3.block_health[i])
		for i in range(22,32):
			temp_h.append(self.r2.block_health[i])
		signals.way_red_health.emit(temp_h)
		
		#compiles variable to emit through system			
	def compile_health_green(self):
		temp = []
		temp.append("1")
		for i in range(20):
			temp.append(self.g1.block_health[i])
		for i in range(15):               
			temp.append(self.g2.block_health[i])
		for i in range(38):               
			temp.append(self.g3.block_health[i])
		for i in range(36):            
			temp.append(self.g4.block_health[i])
		for i in range(37):         
			temp.append(self.g5.block_health[i])
		temp.append(self.g2.block_health[15])
		temp.append(self.g2.block_health[16])
		temp.append(self.g2.block_health[17])
		temp.append(self.g2.block_health[18])
		signals.way_green_health.emit(temp)
		
		#compiles variable to emit through system
	def compile_block_occ_red(self):
		temp = []
		temp.append("0")
		for i in range(23):
			temp.append(self.r1.block_occ[i])
		for i in range(22):
			temp.append(self.r2.block_occ[i])
		for i in range(21):
			temp.append(self.r3.block_occ[i])
		for i in range(22,32):
			temp.append(self.r2.block_occ[i])
		signals.way_red_occupancy.emit(temp)
		
		#compiles variable to emit through system
	def compile_block_occ_red_ctc(self):
		temp = []
		temp.append("0")
		for i in range(23):
			temp.append(self.r1.block_occ[i])
		for i in range(22):
			temp.append(self.r2.block_occ[i])
		for i in range(21):
			temp.append(self.r3.block_occ[i])
		for i in range(22,32):
			temp.append(self.r2.block_occ[i])
		signals.way_red_occupancy_ctc.emit(temp)
		
		#compiles variable to emit through system
	def compile_block_occ_green(self):
		temp_occ = []
		temp_occ.append("1")
		for i in range(20):
			temp_occ.append(self.g1.block_occ[i])
		for i in range(15):
			temp_occ.append(self.g2.block_occ[i])
		for i in range(38):
			temp_occ.append(self.g3.block_occ[i])
		for i in range(36):
			temp_occ.append(self.g4.block_occ[i])
		for i in range(37):
			temp_occ.append(self.g5.block_occ[i])
		temp_occ.append(self.g2.block_occ[15])
		temp_occ.append(self.g2.block_occ[16])
		temp_occ.append(self.g2.block_occ[17])
		temp_occ.append(self.g2.block_occ[18])
		signals.way_green_occupancy.emit(temp_occ)
	
		#compiles variable to emit through system
	def compile_block_occ_green_ctc(self):
		temp_occ = []
		temp_occ.append("1")
		for i in range(20):
			temp_occ.append(self.g1.block_occ[i])
		for i in range(15):
			temp_occ.append(self.g2.block_occ[i])
		for i in range(38):
			temp_occ.append(self.g3.block_occ[i])
		for i in range(36):
			temp_occ.append(self.g4.block_occ[i])
		for i in range(37):
			temp_occ.append(self.g5.block_occ[i])
		temp_occ.append(self.g2.block_occ[15])
		temp_occ.append(self.g2.block_occ[16])
		temp_occ.append(self.g2.block_occ[17])
		temp_occ.append(self.g2.block_occ[18])
		signals.way_green_occupancy_ctc.emit(temp_occ)
		
		#compiles variable to emit through system
	def compile_speed_red(self):
		temp = []
		temp.append("0")
		j = 0
		for i in range(23):
			if(self.r1.b_speed[i] == 0):
				temp.append(self.r1.b_speed[i])
			else:
				temp.append(self.red_speed[j+1])
			j=j+1
		for i in range(22):
			if(self.r2.b_speed[i] == 0):
				temp.append(self.r2.b_speed[i])
			else:
				temp.append(self.red_speed[j+1])
			j=j+1
		for i in range(21):
			if(self.r3.b_speed[i] == 0):
				temp.append(self.r3.b_speed[i])
			else:
				temp.append(self.red_speed[j+1])
			j=j+1
		for i in range(22,32):
			if(self.r2.b_speed[i] == 0):
				temp.append(self.r2.b_speed[i])
			else:
				temp.append(self.red_speed[j+1])
			j=j+1
		signals.way_red_speed.emit(temp)
		
		#compiles variable to emit through system
	def compile_speed_green(self):
		temp = []
		temp.append("g")
		j=0
		for i in range(20):
			if(self.g1.b_speed[i] == 0):
				temp.append(self.g1.b_speed[i])
			else:
				temp.append(self.green_speed[j+1])
			j=j+1
		for i in range(15):
			if(self.g2.b_speed[i] == 0):
				temp.append(self.g2.b_speed[i])
			else:
				temp.append(self.green_speed[j+1])
			j=j+1
		for i in range(38):
			if(self.g3.b_speed[i] == 0):
				temp.append(self.g3.b_speed[i])
			else:
				temp.append(self.green_speed[j+1])
			j=j+1
		for i in range(36):
			if(self.g4.b_speed[i] == 0):
				temp.append(self.g4.b_speed[i])
			else:
				temp.append(self.green_speed[j+1])
			j=j+1
		for i in range(37):
			if(self.g5.b_speed[i] == 0):
				temp.append(self.g5.b_speed[i])
			else:
				temp.append(self.green_speed[j+1])
			j=j+1
		for i in range(15,19):
			if(self.g2.b_speed[i] == 0):
				temp.append(self.g2.b_speed[i])
			else:
				temp.append(self.green_speed[j+1])
			j=j+1
		signals.way_green_speed.emit(temp)
		
		#compiles variable to emit through system
	def compile_switch_red(self):
		temp_sw = []
		temp_sw.append("0")
		if self.r1.mode == 1 or self.r2.mode == 1 or self.r3.mode == 1:
			temp_sw.append(self.r1.m_switch_state[0])
			temp_sw.append(self.r1.m_switch_state[1])
			temp_sw.append(self.r2.m_switch_state[0])
			temp_sw.append(self.r2.m_switch_state[1])
			temp_sw.append(self.r2.m_switch_state[2])
			temp_sw.append(self.r2.m_switch_state[3])
			temp_sw.append(self.r3.m_switch_state[0])
		else:
			temp_sw.append(self.r1.switch_state[0])
			temp_sw.append(self.r1.switch_state[1])
			temp_sw.append(self.r2.switch_state[0])
			temp_sw.append(self.r2.switch_state[1])
			temp_sw.append(self.r2.switch_state[2])
			temp_sw.append(self.r2.switch_state[3])
			temp_sw.append(self.r3.switch_state[0])
		
		signals.way_red_switch_state.emit(temp_sw)
	
		#compiles variable to emit through system
	def compile_switch_green(self):
		temp_sw = []
		temp_sw.append("1")
		if self.g1.mode == 1 or self.g2.mode == 1 or self.g3.mode == 1 or self.g4.mode == 1:
			temp_sw.append(self.g1.m_switch_state[0])
			temp_sw.append(self.g2.m_switch_state[0])
			temp_sw.append(self.g3.m_switch_state[0])
			temp_sw.append(self.g3.m_switch_state[1])
			temp_sw.append(self.g4.m_switch_state[0])
			temp_sw.append(self.g4.m_switch_state[1])			
		else:
			temp_sw.append(self.g1.switch_state[0])
			temp_sw.append(self.g2.switch_state[0])
			temp_sw.append(self.g3.switch_state[0])
			temp_sw.append(self.g3.switch_state[1])
			temp_sw.append(self.g4.switch_state[0])
			temp_sw.append(self.g4.switch_state[1])
		signals.way_green_switch_state.emit(temp_sw)
		
		#compiles variable to emit through system
	def compile_cross_red(self):
		temp_cr = []
		temp_cr.append("0")
		temp_cr.append(self.r3.cross_state[0])
		signals.way_red_cross_state.emit(temp_cr)
		
		#compiles variable to emit through system
	def compile_cross_green(self):
		temp_cr = []
		temp_cr.append("1")
		temp_cr.append(self.g1.cross_state[0])
		signals.way_green_cross_state.emit(temp_cr)
		
		#compiles variable to emit through system
	def compile_auth_red(self):
		temp = []
		temp.append("0")
		j = 0
		for i in range(23):
			if(self.r1.authority[i] == 0):
				temp.append(self.r1.authority[i])
			else:
				temp.append(self.red_authority[j+1])
			j=j+1
		for i in range(22):
			if(self.r2.authority[i] == 0):
				temp.append(self.r2.authority[i])
			else:
				temp.append(self.red_authority[j+1])
			j=j+1
		for i in range(21):
			if(self.r3.authority[i] == 0):
				temp.append(self.r3.authority[i])
			else:
				temp.append(self.red_authority[j+1])
			j=j+1
		for i in range(22,32):
			if(self.r2.authority[i] == 0):
				temp.append(self.r2.authority[i])
			else:
				temp.append(self.red_authority[j+1])
			j=j+1
		signals.way_red_authority.emit(temp)
		
		#compiles variable to emit through system
	def compile_auth_green(self):
		temp = []
		temp.append("1")
		j=0
		for i in range(20):
			if(self.g1.authority[i] == 0):
				temp.append(self.g1.authority[i])
			else:
				temp.append(self.green_authority[j+1])
			j=j+1
		for i in range(15):
			if(self.g2.authority[i] == 0):
				temp.append(self.g2.authority[i])
			else:
				temp.append(self.green_authority[j+1])
			j=j+1
		for i in range(38):
			if(self.g3.authority[i] == 0):
				temp.append(self.g3.authority[i])
			else:
				temp.append(self.green_authority[j+1])
			j=j+1
		for i in range(36):
			if(self.g4.authority[i] == 0):
				temp.append(self.g4.authority[i])
			else:
				temp.append(self.green_authority[j+1])
			j=j+1
		for i in range(37):
			if(self.g5.authority[i] == 0):
				temp.append(self.g5.authority[i])
				
			else:
				temp.append(self.green_authority[j+1])
			j=j+1
		for i in range(15,19):
			if(self.g2.authority[i] == 0):
				temp.append(self.g2.authority[i])
			else:
				temp.append(self.green_authority[j+1])
			j=j+1
		signals.way_green_authority.emit(temp)
		
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    
    prog = wayside_qtui_test()
    
    sys.exit(app.exec_())
