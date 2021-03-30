class Wayside:
	def __init__(self, plcfile):
		self.plcfile = plcfile
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
		self.load_plc()
	
	def update_wayside(self, authority, occupancy, order):
		self.occupancy = occupancy
		self.authority = authority
		self.m_order(order)	
		self.cross_change()
			
	def m_order(self, order):
		temp_block = []
		temp_switch = []
		block = 0
		switch = 0
		if order != "0":
			for i in range(len(order)):
				if order[i] == "b":
					block = 1
				if order[i] == "s":
					switch = 1
				if order[i] == "1" and self.block_health[i-1] == "1" and block == 1:
					temp_block.append("0")
				if order[i] == "1" and self.block_health[i-1] == "0" and block == 1:
					temp_block.append("1")
				if order[i] == "1" and self.switch_state[i-1] == "1" and switch == 1:
					temp_switch.append("0")
				if order[i] == "1" and self.switch_state[i-1] == "0" and switch == 1:
					temp_switch.append("1")
		if block == 1:
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
		if switch == 1:
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
		for i in len(self.cr_connect):
			if block_occ[cr_connect[i]-2] == "1" or block_occ[cr_connect[i]-1] == "1" or block_occ[cr_connect[i]] == "1":
				self.cr_connect[i] = "1"
			else:
				self.cr_connect[i] = "0"
	
	def switch_state(self):
		for i in self.num_switch:
			if 
			
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
				self.switch_name.append("Switch " + line[2:-1])
				self.switch_state.append("0")
				self.num_switch = self.num_switch +1
			#cross
			elif line[0:2] == "cr" and proc == 0:
				self.cross_name.append("Crossing " + line[2:-1])
				self.cross_state.append("0")
			elif line[0:2] == "bl" and proc == 0:
				self.block_name.append("Block " + line[2:-1])
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
				self.sw_connect.append([int(d1[0:-2]), int(d2[0:-2])])
				self.sw_connect.append([int(d3[0:-2]), int(d4[0:-2])])
			if line[0:2] == "cr":
				d1 = plc[linecount+1]
				self.cr_connect.append(int(d1[0:-2]))
			if line[0:2] == "end proc":
				break
			linecount = linecount+1
		f.close()
		
if __name__ == '__main__':
	Wayside.main()
		
