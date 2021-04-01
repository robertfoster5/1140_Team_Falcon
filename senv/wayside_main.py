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
		super().__init__()
		self.wayside_qtui_test = QtWidgets.QMainWindow()
		#ui = Ui_MainWindow()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self.wayside_qtui_test)
		self.wayside_qtui_test.show()
	
		#self.MainWindow.show()
		
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
        
		self.header_blocks = ['Block', 'Status', 'Line']
		
		self.data_blocks = [[0,0,0]]
		
		self.header_cross = ['Crossing', 'Status']
		
		self.data_cross = [[0,0]]
		
		self.header_switch = ['Switch', 'Status']
		
		self.data_switch = [[0,0]]	
		
		self.ui.model = TableModel(self.data_blocks,self.header_blocks)
		
		
		print("Load Blocks Table")
		self.ui.tableView.setModel(self.ui.model)
		
		self.ui.model = TableModel(self.data_cross,self.header_cross)
		print("Load Crossings Table")
		self.ui.tableView_2.setModel(self.ui.model)
		
		self.ui.model = TableModel(self.data_switch,self.header_switch)
		print("Load Switch Table")
		self.ui.tableView_3.setModel(self.ui.model)
		
		self.ui.pushButton.clicked.connect(lambda: self.update_tables(self.r1))
		self.ui.pushButton_2.clicked.connect(lambda: self.update_tables(self.r2))
		self.ui.pushButton_3.clicked.connect(lambda: self.update_tables(self.r3))
		
		self.ui.pushButton_4.clicked.connect(lambda: self.update_tables(self.g1))
		self.ui.pushButton_7.clicked.connect(lambda: self.update_tables(self.g2))
		self.ui.pushButton_6.clicked.connect(lambda: self.update_tables(self.g3))
		self.ui.pushButton_5.clicked.connect(lambda: self.update_tables(self.g4))
		self.ui.pushButton_8.clicked.connect(lambda: self.update_tables(self.g5))
		
		signals.ctc_authority.connect(self.new_authority)
		signals.ctc_suggested_speed.connect(self.update_speed)
		signals.ctc_maintenance.connect(self.maintenance_order)
		signals.tkm_get_occ.connect(self.update_occupancy)
		
			
	def update_tables(self, ws):
		print("update_table")
		self.update_block(ws)
		self.update_switch(ws)
		self.update_cross(ws)
		self.show_tables()
	
	def show_tables(self):
		self.ui.model = TableModel(self.data_blocks,self.header_blocks)
		print("Load Blocks Table")
		self.ui.tableView.setModel(self.ui.model)
		
		self.ui.model = TableModel(self.data_switch,self.header_switch)
		print("Load Switch Table")
		self.ui.tableView_3.setModel(self.ui.model)
		
		self.ui.model = TableModel(self.data_cross,self.header_cross)
		print("Load Cross Table")
		self.ui.tableView_2.setModel(self.ui.model)
			
	def update_block(self, ws):	
		self.data_blocks = []
		for i in range(len(ws.block_occ)):
			if ws.block_health[i] == "1":
				self.data_blocks.append([ws.block_name[i], "Broken", ws.line])
			elif ws.block_health[i] == "0" and ws.block_occ[i] == "1":
				self.data_blocks.append([ws.block_name[i], "Occupied", ws.line])
			elif ws.block_occ[i] == "0":
				self.data_blocks.append([ws.block_name[i], "Empty", ws.line])
		
	def update_switch(self, ws):
		self.data_switch = []
		if ws.num_switch > 0:
			for i in range(ws.num_switch):
				self.data_switch.append([ws.switch_name[i], ws.switch_state[i]])
		else:
			self.data_switch.append(["N/A", "N/A"])

	def update_cross(self, ws):
		self.data_cross = []
		if ws.num_cross > 0:
			for i in range(ws.num_cross):
				self.data_cross.append([ws.cross_name[i], ws.cross_state[i]])
		else:
			self.data_cross.append(["N/A", "N/A"])

	def maintenance_order(self, order):
		if order[0] != "0":
			if order[0] == "r":
				temp_order = order[1:-1]
				if order[1] == "b":
					or1 = temp_order[1:23]
					or2 = temp_order[24:45] + temp_order[67:76]
					or3 = temp_order[46:66]
					self.r1.m_order_block(or1)
					self.r2.m_order_block(or2)
					self.r3.m_order_block(or3)
				elif order[1] == "s":
					self.r1.m_order_switch(temp_order[1:2])
					self.r2.m_order_switch(temp_order[3:6])
					self.r3.m_order_switch(temp_order[7])
			else:
				temp_order = order[1:-1]
				if order[1] == "b":
					or1 = temp_order[0] + temp_order[1:20]
					or2 = temp_order[0] + temp_order[22:35] + temp_order[147:150]
					or3 = temp_order[0] + temp_order[36:73]
					or4 = temp_order[0] + temp_order[74:109]
					or5 = temp_order[0] + temp_order[110:146]
					self.g1.m_order(or1)
					self.g2.m_order(or2)
					self.g3.m_order(or3)
					self.g4.m_order(or4)
					self.g5.m_order(or5)
				elif order[1] == "s":
					self.g1.m_order_switch(temp_order[1])
					self.g2.m_order_switch(temp_order[2])
					self.g3.m_order_switch(temp_order[3:4])
					self.g4.m_order_switch(temp_order[5:6])
			self.update_tables(self.r1)
			self.update_tables(self.r2)
			self.update_tables(self.r3)
			self.update_tables(self.g1)
			self.update_tables(self.g2)
			self.update_tables(self.g3)
			self.update_tables(self.g4)
			self.update_tables(self.g5)
			self.compile_block_occ_green()
			self.compile_switch_green()
			self.compile_cross_green()
			self.compile_auth_green()
			
	def new_authority(self, authority):
		if authority[0] == "r":
			self.r1.authority = authority[1:23]
			self.r2.authority = authority[24:45] + authority[67:76]
			self.r3.authority = authority[46:66]
			self.r1.switch_state_change()
			self.r2.switch_state_change()
			self.r3.switch_state_change()
		else:
			self.g1.authority = authority[1:20]
			self.g2.authority = authority[21:35] + authority[147:150]
			self.g3.authority = authority[36:73]
			self.g4.authority = authority[74:109]
			self.g5.authority = authority[110:146]
			self.g1.switch_state_change()
			self.g2.switch_state_change()
			self.g3.switch_state_change()
			self.g4.switch_state_change()
			self.g5.switch_state_change()
		self.update_tables(self.r1)
		self.update_tables(self.r2)
		self.update_tables(self.r3)
		self.update_tables(self.g1)
		self.update_tables(self.g2)
		self.update_tables(self.g3)
		self.update_tables(self.g4)
		self.update_tables(self.g5)
		self.compile_block_occ_green()
		self.compile_switch_green()
		self.compile_cross_green()
		self.compile_auth_green()
				
	def update_occupancy(self, occupancy):
		if self.line == "r":
			self.r1.block_occ = occupancy[1:23]
			self.r2.block_occ = occupancy[24:45] + occupancy[67:76]
			self.r3.block_occ = occupancy[46:66]
			self.r1.cross_change()
			self.r2.cross_change()
			self.r3.cross_change()
		else:
			self.g1.block_occ = occupancy[1:20]
			self.g2.block_occ = occupancy[21:35] + occupancy[147:150]
			self.g3.block_occ = occupancy[36:73]
			self.g4.block_occ = occupancy[74:109]
			self.g5.block_occ = occupancy[110:146]
			self.g1.cross_change()
			self.g2.cross_change()
			self.g3.cross_change()
			self.g4.cross_change()
			self.g5.cross_change()
		self.update_tables(self.r1)
		self.update_tables(self.r2)
		self.update_tables(self.r3)
		self.update_tables(self.g1)
		self.update_tables(self.g2)
		self.update_tables(self.g3)
		self.update_tables(self.g4)
		self.update_tables(self.g5)
		self.compile_block_occ_green()
		self.compile_switch_green()
		self.compile_cross_green()
		self.compile_auth_green()
		
	def update_speed(self, speed):
		self.speed = speed
		signals.way_speed.emit(self.speed)
					
	"""def compile_block_occ_red(self):
		temp_occ = []"""
	
	def compile_block_occ_green(self):
		temp_occ = []
		temp_occ.append("1")
		temp_occ.append(self.g1.block_occ)
		temp_occ.append(self.g2.block_occ[0:13])
		temp_occ.append(self.g3.block_occ)
		temp_occ.append(self.g4.block_occ)
		temp_occ.append(self.g5.block_occ)
		temp_occ.append(self.g2.block_occ[14:17])
		signals.way_occupancy.emit(temp_occ)
	
	"""def compile_switch_red(self):
		temp_sw = []"""
	
	def compile_switch_green(self):
		temp_sw = []
		temp_sw.append("1")
		temp_sw.append(g1.switch_state)
		temp_sw.append(g2.switch_state)
		temp_sw.append(g3.switch_state)
		temp_sw.append(g4.switch_state)
		signals.way_switch_state.emit(temp_sw)
		
	"""def compile_cross_red(self):
		temp_cr = []"""
		
	def compile_cross_green(self):
		temp_cr = []
		temp_cr.append("1")
		temp_cr.append(g1.cross_state)
		signals.way_cross_state.emit(temp_cr)
		
	"""def compile_auth_red(self):
		temp_auth = []"""
		
	def compile_auth_green(self):
		temp_auth = []
		temp_auth.append("1")
		temp_auth.append(self.g1.authority)
		temp_auth.append(self.g2.authority[0:13])
		temp_auth.append(self.g3.authority)
		temp_auth.append(self.g4.authority)
		temp_auth.append(self.g5.authority)
		temp_auth.append(self.g2.authority[14:17])
		signals.way_authority.emit(temp_auth)
		
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    #MainWindow = QtWidgets.QMainWindow()
    
    prog = wayside_qtui_test()
    
    sys.exit(app.exec_())