class Wayside:
	def __init__(self, plcfile, line):
		self.plcfile = plcfile
		self.line = line
		self.authority = []
		self.switch_name = []
		self.switch_state = []
		self.cross_name = []
		self.cross_state = []
		self.block_name = []
		self.block_health = []
		self.block_occ = []
		self.sw_connect = []
		self.cr_connect = []
		self.num_switch = 0
		self.num_cross = 0
		self.load_plc()
	
	def update_wayside(self):
		print("ws: update_wayside")
		self.cross_change()
		self.switch_state_change()
			
	def m_order_block(self, order):
		print("ws: m order block")
		temp_block = []
		if order != "0":
			for i in range(len(order)):
				if order[i] == "1" and self.block_health[i-1] == "1":
					temp_block.append("0")
				if order[i] == "1" and self.block_health[i-1] == "0":
					temp_block.append("1")
				if order[i] == "1" and self.switch_state[i-1] == "1":
					temp_switch.append("0")
				if order[i] == "1" and self.switch_state[i-1] == "0":
					temp_switch.append("1")
			self.block_health = []
			temp = self.block_occ
			self.block_occ = []
		for i in range(len(order)):
			self.block_health.append(temp_block[i])
			if temp[i] == "0" and temp_block[i] == "0":
				self.bloc_occ.append("0")
			if temp[i] == "0" and temp_block[i] == "1":
				self.bloc_occ.append("1")
			if temp[i] == "1" and temp_block[i] == "0":
				self.bloc_occ.append("1")
			if temp[i] == "1" and temp_block[i] == "1":
				self.bloc_occ.append("0")
					
	def m_order_switch(self, order):
		print("ws: m order switch")
		temp_switch = []
		temp = self.switch_state
		self.switch_state = []
		for i in range(len(order)):
			if temp[i] == "0" and temp_switch[i] == "0":
				self.switch_state.append("0")
			if temp[i] == "0" and temp_switch[i] == "1":
				self.switch_state.append("1")
			if temp[i] == "1" and temp_switch[i] == "0":
				self.switch_state.append("1")
			if temp[i] == "1" and temp_switch[i] == "1":
				self.switch_state.append("0")
					
	def cross_change(self):
		print("cross_change")
		if self.num_cross != 0:
			for i in range(self.num_cross):
				if self.block_occ[self.cr_connect[i]-2] == "1" or self.block_occ[self.cr_connect[i]-1] == "1" or self.block_occ[self.cr_connect[i]] == "1":
					self.cr_connect[i] = "1"
				else:
					self.cr_connect[i] = "0"
	
	def switch_state_change(self):
		print("switch_change")
		temp_count = 0
		self.switch_state = []
		if self.num_switch > 0:
			for i in range(self.num_switch):
				sw1 = self.sw_connect[temp_count][0]
				sw2 = self.sw_connect[temp_count][1]
				sw3 = self.sw_connect[temp_count+1][0]
				sw4 = self.sw_connect[temp_count+1][1]
				index1 = self.block_name.index(sw1)
				index2 = self.block_name.index(sw2)
				index4 = "0"
				index3 = "0"
				if sw4 == "yard":
					index3 = self.block_name.index(sw3)
				elif sw3 == "yard":
					index4 = self.block_name.index(sw4)
				else:
					index3 = self.block_name.index(sw3)
					index4 = self.block_name.index(sw4)
				if self.authority[int(index1)] == "1" and self.authority[int(index2)] == "1":
					self.switch_state.append("0")
				elif self.authority[int(index3)] == "1" and sw4 == "yard" and self.authority[int(index2)] == "0":
					self.switch_state.append("1")
				elif self.authority[int(index4)] == "1" and sw3 == "yard" and self.authority[int(index1)] == "0":
					self.switch_state.append("1")
				elif self.authority[int(index3)] == "1" and self.authority[int(index4)] == "1" and sw3 != "yard" and sw4 != "yard":
					self.switch_state.append("1")
				else:
					self.switch_state.append("0")
				temp_count = temp_count + 2
			
	def load_plc(self):
		f = open(self.plcfile)
		swcount = 0
		crcount = 0
		blcount = 0
		linecount = 0
		swc = 0
		swr = 0
		crc = 0
		proc = 0
		plc = f.readlines()
		for line in plc[0:]:
			if line == "var":
				proc = 0
			#switch
			elif line[0:2] == "sw" and proc == 0:
				self.switch_name.append(line[2:-1])
				self.switch_state.append("0")
				self.num_switch = self.num_switch +1
			#cross
			elif line[0:2] == "cr" and proc == 0:
				self.cross_name.append(line[2:-1])
				self.cross_state.append("0")
				self.num_cross = self.num_cross +1
			elif line[0:2] == "bl" and proc == 0:
				self.block_name.append(line[2:-1])
				self.block_health.append("0")
				self.block_occ.append("0")
			#stopping distance
			elif line[0:2] == "st" and proc == 0:
				self.stop_distance = int(line[2:])
			#end
			elif line == "end var\n":
				proc = 1
				break
			linecount = linecount +1;
		for line in plc[linecount+1:]:
			if line[0:2] == "sw":
				d1 = plc[linecount+2]
				d2 = plc[linecount+3]
				d3 = plc[linecount+4]
				d4 = plc[linecount+5]
				self.sw_connect.append([d1[0:-1], d2[0:-1]])
				self.sw_connect.append([d3[0:-1], d4[0:-1]])
			if line[0:2] == "cr":
				d1 = plc[linecount+2]
				self.cr_connect.append(int(d1[0:-1]))
			if line[0:2] == "end proc":
				break
			linecount = linecount+1
		f.close()
		
if __name__ == '__main__':
	Wayside.main()
		
