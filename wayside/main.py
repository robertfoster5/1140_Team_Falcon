import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from wayside_qtui_test import Ui_MainWindow
from wayside_ws_control import Wayside

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


class wayside_qtui_test(Ui_MainWindow):
	
	def __init__(self, dialog):
		
		ui = Ui_MainWindow()
		
		g1 = Wayside("g1.txt", "Green")
		g2 = Wayside("g2.txt", "Green")
		g3 = Wayside("g3.txt", "Green")
		g4 = Wayside("g4.txt", "Green")
		g5 = Wayside("g5.txt", "Green")
		r1 = Wayside("r1.txt", "Red")
		r2 = Wayside("r2.txt", "Red")
		r3 = Wayside("r3.txt", "Red")
		
		self.header_blocks = ['Block', 'Status', 'Line']
		
		self.data_blocks = [[0,0,0]]
		
		self.header_cross = ['Crossing', 'Status']
		
		self.data_cross = [[0,0]]
		
		self.header_switch = ['Switch', 'Status']
		
		self.data_switch = [[0,0]]	
		
		ui.model = TableModel(self.data_blocks,self.header_blocks)
		
		ui.setupUi(MainWindow)
		print("Load Blocks Table")
		ui.tableView.setModel(ui.model)
		
		ui.model = TableModel(self.data_cross,self.header_cross)
		print("Load Crossings Table")
		ui.tableView_2.setModel(ui.model)
		
		ui.model = TableModel(self.data_switch,self.header_switch)
		print("Load Switch Table")
		ui.tableView_3.setModel(ui.model)
		
		ui.pushButton.clicked.connect(lambda: self.update_tables(ui, r1))
		ui.pushButton_2.clicked.connect(lambda: self.update_tables(ui,r2))
		ui.pushButton_3.clicked.connect(lambda: self.update_tables(ui,r3))
		
		ui.pushButton_4.clicked.connect(lambda: self.update_tables(ui,g1))
		ui.pushButton_7.clicked.connect(lambda: self.update_tables(ui,g2))
		ui.pushButton_6.clicked.connect(lambda: self.update_tables(ui,g3))
		ui.pushButton_5.clicked.connect(lambda: self.update_tables(ui,g4))
		ui.pushButton_8.clicked.connect(lambda: self.update_tables(ui,g5))
		
	def update_tables(self, ui, ws):
		self.update_block(ui, ws)
		self.update_switch(ui, ws)
		self.update_cross(ui, ws)
		
	def update_block(self, ui, ws):	
		self.data_blocks = []
		for i in range(len(ws.block_occ)):
			if ws.block_health[i] == "1":
				self.data_blocks.append([ws.block_name[i], "Broken", ws.line])
			elif ws.block_health[i] == "0" and ws.block_occ[i] == "1":
				self.data_blocks.append([ws.block_name[i], "Occupied", ws.line])
			elif ws.block_occ[i] == "0":
				self.data_blocks.append([ws.block_name[i], "Empty", ws.line])
		ui.model = TableModel(self.data_blocks,self.header_blocks)
		print("Load Blocks Table")
		ui.tableView.setModel(ui.model)
				
	def update_switch(self, ui, ws):
		self.data_switch = []
		if ws.num_switch > 0:
			for i in range(ws.num_switch):
				self.data_switch.append([ws.switch_name[i], ws.switch_state[i]])
		else:
			self.data_switch.append(["N/A", "N/A"])
		ui.model = TableModel(self.data_switch,self.header_switch)
		print("Load Switch Table")
		ui.tableView_3.setModel(ui.model)
		
	def update_cross(self, ui, ws):
		self.data_cross = []
		if ws.num_cross > 0:
			for i in range(ws.num_cross):
				self.data_cross.append([ws.cross_name[i], ws.cross_state[i]])
		else:
			self.data_cross.append(["N/A", "N/A"])
		ui.model = TableModel(self.data_cross,self.header_cross)
		print(self.data_cross)
		ui.tableView_2.setModel(ui.model)

	def maintenance_order(self, order, r1, r2, r3, g1, g2, g3, g4, g5):
		if order[0] == "r":
			temp_order = order[1:-1]
			or1 = temp_order[0] + temp_order[1:23]
			or2 = temp_order[0] + temp_order[24:45] + temp_order[67:76]
			or3 = temp_order[0] + temp_order[46:66]
			r1.m_order(or1)
			r2.m_order(or2)
			r3.m_order(or3)
		else:
			temp_order = order[1:-1]
			or1 = temp_order[0] + temp_order[1:20]
			or2 = temp_order[0] + temp_order[22:35] + temp_order[147:150]
			or3 = temp_order[0] + temp_order[36:73]
			or4 = temp_order[0] + temp_order[74:109]
			or5 = temp_order[0] + temp_order[110:146]
			g1.m_order(or1)
			g2.m_order(or2)
			g3.m_order(or3)
			g4.m_order(or4)
			g5.m_order(or5)
	
	def new_authority(self, authority, r1, r2, r3, g1, g2, g3, g4, g5):
		if authority[0] == "r":
			r1.authority = authority[1:23]
			r2.authority = authority[24:45] + authority[67:76]
			r3.authority = authority[46:66]
		else:
			g1.authority = authority[1:20]
			g2.authority = authority[21:35] + authority[147:150]
			g3.authority = authority[36:73]
			g4.authority = authority[74:109]
			g5.authority = authority[110:146]
				
	def update_occupancy(self, occupancy, r1, r2, r3, g1, g2, g3, g4, g5):
		if self.line == "r":
			r1.block_occ = occupancy[1:23]
			r2.block_occ = occupancy[24:45] + occupancy[67:76]
			r3.block_occ = occupancy[46:66]
		else:
			g1.block_occ = occupancy[1:20]
			g2.block_occ = occupancy[21:35] + occupancy[147:150]
			g3.block_occ = occupancy[36:73]
			g4.block_occ = occupancy[74:109]
			g5.block_occ = occupancy[110:146]
				
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    prog = wayside_qtui_test(MainWindow)
    
    
    
    MainWindow.show()
    sys.exit(app.exec_())
