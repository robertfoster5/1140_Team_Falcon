import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from wayside_qtui_test import Ui_MainWindow

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
	global track_occupancy 
	global line
	def __init__(self, dialog):
		
		ui = Ui_MainWindow()
		
		global track_occupancy
		track_occupancy = "000000000000000000000"
		 
		line = 'Green'
		
		header_blocks = ['Block', 'Status', 'Line']
		
		data_blocks = [[0,0,0],
						[0,0,0],
						[0,0,0],
						[0,0,0],
						[0,0,0],
						[0,0,0],
						[0,0,0],
						[0,0,0],
						[0,0,0],
						[0,0,0],
						[0,0,0],
						[0,0,0],
						[0,0,0],
						[0,0,0],
						[0,0,0],
						[0,0,0],
						[0,0,0],
						[0,0,0],
						[0,0,0],
						[0,0,0]]
		for x in range(20):
			data_blocks[x][0] = 'Block ' + str(x+1)
			if track_occupancy[x] == "0":
				data_blocks[x][1] = 'Empty'
			else:
				data_blocks[x][1] = 'Occupied'
			data_blocks[x][2] = line
		
		header_cross = ['Crossing', 'Status']
		
		data_cross = [['Crossing_1','Open']]
		
		header_switch = ['Switch', 'Status']
		
		data_switch = [['Switch_1', track_occupancy[15]]]	
		
		ui.model = TableModel(data_blocks,header_blocks)
		
		ui.setupUi(MainWindow)
		print("Load Blocks Table")
		ui.tableView.setModel(ui.model)
		
		ui.model = TableModel(data_cross,header_cross)
		print("Load Crossings Table")
		ui.tableView_2.setModel(ui.model)
		
		ui.model = TableModel(data_switch,header_switch)
		print("Load Switch Table")
		ui.tableView_3.setModel(ui.model)
		
		print("Load Line Edit")
		ui.lineEdit.editingFinished.connect(lambda: self.input_changed(ui))
		
		print("Load Maintenance Order Table")
		header_m = ['Change Switch/Block']
		data_m = [['N/A']]
		ui.model = TableModel(data_m, header_m)
		ui.tableView_5.setModel(ui.model)
		
		print("Load CTC inputs")
		header_ctc = ['Train ID', 'Commanded Speed', 'Authority']
		data_ctc = [['N/A','N/A','N/A']]
		ui.model = TableModel(data_ctc, header_ctc)
		ui.tableView_4.setModel(ui.model)
		
	def input_changed(self, ui):
		qtext = ui.lineEdit.text()
		text_input = str(qtext)
		print(text_input)
		self.manage_input(ui, text_input)
		
	def manage_input(self, ui, text_input):
		global track_occupancy
		choice = text_input[0]
		if choice == "S" or choice == "s":
			ui.label.setText("New Switch State")
			ui.label.adjustSize()
			track_input = text_input[1:]
			self.update_switch(ui, track_input)
		if choice == "B" or choice == "b":
			ui.label.setText("New Track Occupancy")
			ui.label.adjustSize()
			track_input = text_input[1:]
			self.update_block(ui, track_input)
		elif choice == "m":
			ui.label.setText("Maintenance request")
			ui.label.adjustSize()
			bit_in = text_input[1:]
			self.block_or_switch(ui, bit_in)
			print("Maintenance request")
		#else:
		#	ui.label.setText("Not a valid command")
		#	ui.label.adjustSize()
		#	print("Not a valid request")
		
	#def input_new_occupancy(self, ui, new_track):
	#	track_occupancy = new_track
	#	self.blue_update_occupancy(ui)
			
	#PLC Blue_Line Controller
	def blue_update_occupancy(self, ui):
		global track_occupancy
		#Switch_1=track_occupancy[15]
		if track_occupancy[4] == "1":
			Switch_1 = "0"
		elif track_occupancy[5] == "1":
			Switch_1 = "0"
		elif track_occupancy[10] == "1":
			Switch_1 = "1"
		else:
			Switch_1 = track_occupancy[15]
		track_occupancy = track_occupancy[0:15] + Switch_1
		self.update_tables(ui)
	
	def update_switch(self, ui, track_input):
		global track_occupancy
		track_occupancy = track_occupancy[0:-1] + track_input[-1]
		self.blue_update_occupancy(ui)
		
	def update_block(self, ui, track_input):
		global track_occupancy
		#track_occupancy[ord(track_input[0])-1] = track_input[-1]
		index = int(track_input[0:-2]) - 1
		set_state = track_input[-1]
		temp = ""
		for x in range(15):
			if x == index:
				temp += set_state
			else:
				temp += track_occupancy[x]
		temp += track_occupancy[15]
		print(temp)
		track_occupancy = temp
		self.blue_update_occupancy(ui)
		
	#Update tables w/ new occupancy
	def update_tables(self,ui):
		self.block_parse(ui)
		self.cross_parse(ui)
		self.switch_parse(ui)
		
	def block_parse(self, ui):
		global track_occupancy
		line = 'Blue'
		new_data = [[0,0,0],
					[0,0,0],
					[0,0,0],
					[0,0,0],
					[0,0,0],
					[0,0,0],
					[0,0,0],
					[0,0,0],
					[0,0,0],
					[0,0,0],
					[0,0,0],
					[0,0,0],
					[0,0,0],
					[0,0,0],
					[0,0,0]]
		for x in range(15):
			new_data[x][0] = 'Block_' + str(x+1)
			if track_occupancy[x] == "0":
				new_data[x][1] = 'Empty'
			else:
				new_data[x][1] = 'Occupied'
			new_data[x][2] = line
			
		header = ['Block', 'Status', 'Line']
		
		ui.model = TableModel(new_data, header)
		ui.tableView.setModel(ui.model)
    
	def cross_parse(self, ui):
		new_data = [['N/A', 'N/A'],['N/A', 'N/A']]
		
		header = ['Crossing', 'Line']
		
		ui.model = TableModel(new_data, header)
		ui.tableView_2.setModel(ui.model)
        
	def switch_parse(self, ui):
		global track_occupancy
		new_data = [[0,0],
					[0,0]]
		new_data[0][0] = 'Switch_1'
		new_data[0][1] = track_occupancy[15]
		new_data[1][0] = 'N/A'
		new_data[1][1] = 'N/A'
		header = ['Switch', 'Status']
		
		ui.model = TableModel(new_data, header)
		ui.tableView_3.setModel(ui.model) 
		
	#Maintenance Orders
	def block_or_switch(self, ui, bit_in):
		global track_occupancy
		temp = ""
		print(bit_in)
		for x in range(16):
			if bit_in[x] == "0" and track_occupancy[x] == "0":
				temp += "0"
			elif bit_in[x] == "0" and track_occupancy[x] == "1":
				temp += "1"
			elif bit_in[x] == "1" and track_occupancy[x] == "0":
				temp += "1"
			else:
				temp += "0"
		print(temp)
		track_occupancy = temp
		self.update_tables(ui)

		

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    
    prog = wayside_qtui_test(MainWindow)
    
    
    
    MainWindow.show()
    sys.exit(app.exec_())
