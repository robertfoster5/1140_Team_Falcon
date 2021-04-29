class Wayside:
	#Creates initial wayside with empty variables to be filled by PLC settings
	def __init__(self, plcfile, line):
		self.plcfile = plcfile
		self.line = line
		self.authority = []
		self.switch_name = []
		self.switch_state = []
		self.m_switch_state = []
		self.mode = 0
		self.sw_order = []
		self.bl_order = []
		self.cross_name = []
		self.cross_state = []
		self.block_name = []
		self.block_health = []
		self.block_occ = []
		self.sw_connect = []
		self.sw_safety_connect = []
		self.cr_connect = []
		self.b_speed = []
		self.num_switch = 0
		self.num_cross = 0
		self.num_block = 0
		#Function to load all variables from plc file
		self.load_plc()
	
		#updates all components of wayside
	def update_ws(self):
		#self.switch_safety()
		#self.safety_change()
		self.cross_change()
		self.switch_state_change()
	
		#Failed safety function to analyze connections around switches if they were safe
	"""def switch_safety():
		for i in range(num_switch):
			swname = self.switch_name[i]
			if self.line == "Red":
				if swname == "1":
					
				elif swname == "2":
					
				elif swname == "3":
					
				elif swname == "4":
					
				elif swname == "5":
					
				elif swname == "6":
						
			elif self.line == "Green":
				if swname == "1":
					
				elif swname == "2":
					
				elif swname == "3":
					
				elif swname == "4":
					
				elif swname == "5":
					
				elif swname == "6":
					
				elif swname == "7":
		
		#function to adjust authority and speed to stop trains from hitting each other	
	def safety_change(self):
		for i in range(self.num_block):
			if self.block_occ[i] == "1":
				if i < 3 """
		
		#change maintenance of a block				
	def m_order_block(self, order):
		temp_block = []
		temp_occ = []
		self.bl_order = []
		self.bl_order = order
		for i in range(len(order)):
			if order[i] == "1" and self.block_health[i] == "1":
				temp_block.append("0")
			if order[i] == "1" and self.block_health[i] == "0":
				self.mode = 1
				temp_block.append("1")
			if order[i] == "0" and self.block_health[i] == "1":
				self.mode = 1
				temp_block.append("0")
			if order[i] == "0" and self.block_health[i] == "0":
				temp_block.append("0")
		self.block_health = []
		self.block_health = temp_block
		"""for i in range(len(order)):
			if order[i] == "0" and self.block_occ[i] == "0":
				temp_occ.append("0")
			if order[i] == "0" and self.block_occ[i] == "1":
				temp_occ.append("1")
			if order[i] == "1" and self.block_occ[i] == "0":
				self.mode = 1
				temp_occ.append("1")
			if order[i] == "1" and self.block_occ[i] == "1":
				self.mode = 1
				temp_occ.append("1")
		self.block_occ = []
		self.block_occ = temp_occ"""
		
		#manually change switches			
	def m_order_switch(self, order):
		self.sw_order = []
		self.sw_order = order
		temp = self.switch_state
		self.m_switch_state = []
		for i in range(self.num_switch):
			if temp[i] == "0" and self.sw_order[i] == "0":
				self.m_switch_state.append("0")
			elif temp[i] == "0" and self.sw_order[i] == "1":
				self.m_switch_state.append("1")
				self.mode = 1
			elif temp[i] == "1" and self.sw_order[i] == "0":
				self.m_switch_state.append("1")
			elif temp[i] == "1" and self.sw_order[i] == "1":
				self.mode = 1
				self.m_switch_state.append("0")
			else:
				self.m_switch_state.append(temp[i])
		
		#sets new occupancy for wayside
	def occ_change(self, occupancy):
		temp = []
		for i in range(self.num_block):
			temp.append(occupancy[i])
		self.block_occ = []
		self.block_occ = temp
		
		#changes crossing settings if occupancy is nearby crossing				
	def cross_change(self):
		if self.num_cross != 0:
			cr1 = self.cr_connect[0]
			index1 = self.block_name.index(cr1)
			if self.block_occ[int(index1) - 1] == "1" or self.block_occ[int(index1)] == "1" or self.block_occ[int(index1)+1] == "1":
				self.cross_state[0] = "1"
			else:
				self.cross_state[0] = "0"
	
		#changes switch setting based on authority, occupancy, and defaults
	def switch_state_change(self):
		temp_count = 0
		self.switch_state = []
		#goes through all switches
		if self.num_switch > 0:
			for i in range(self.num_switch):
				#creates variables for indexing
				fork = 0
				swname = self.switch_name[i]
				sw1 = self.sw_connect[temp_count][0]
				sw2 = self.sw_connect[temp_count][1]
				sw3 = self.sw_connect[temp_count+1][0]
				sw4 = self.sw_connect[temp_count+1][1]
				index1 = self.block_name.index(sw1)
				index2 = self.block_name.index(sw2)
				index3 = self.block_name.index(sw3)
				
				if sw4 != "yard":
					index4 = self.block_name.index(sw4)
				#Changes switch state if there is an occupancy not before a fork
				if sw4 != "yard" and (self.block_occ[int(index2)] == "1" or self.block_occ[int(index4)] =="1"):
					if self.block_occ[int(index2)] == "1":
						self.switch_state.append("0")
						fork = 0
					elif self.block_occ[int(index4)] == "1":
							self.switch_state.append("1")
							fork = 0
				elif sw4 == "yard" and self.block_occ[int(index2)] == "1":
					self.switch_state.append("0")
				elif sw4 == "yard" and self.block_occ[int(index2)] == "0" and self.authority[int(index1)] == "1" and self.authority[int(index2)] == "1":
					self.switch_state.append("0")
				elif sw4 == "yard" and self.block_occ[int(index2)] == "0" and self.authority[int(index1)] == "1" and self.authority[int(index2)] == "0":
					self.switch_state.append("1")
				else:
					fork = 1
				#Changes switch states based on line and switch defaults	
				if self.line == "Green" and fork == 1:
					if swname == "1" or swname == "2" or swname == "6":
						self.switch_state.append("0")
					elif swname == "3":
						if self.authority[int(index1)] == "1":
							self.switch_state.append("0")
						else:
							self.switch_state.append("1")
					elif swname == "4":
						if self.authority[int(index2)] == "1" and self.authority[int(index1)] == "1":
							self.switch_state.append("0")
						else:
							self.switch_state.append("1")
					elif swname == "5":
						self.switch_state.append("1")
					else:
						self.switch_state.append("0")
				elif self.line == "Red" and fork == 1:
					if swname == "1":
						if self.authority[int(index3)] == "1":
							self.switch_state.append("0")
						else:
							self.switch_state.append("1")
					elif swname == "2":
						if self.authority[10] == "1":
							self.switch_state.append("0")
						else:
							self.switch_state.append("1")
					elif swname == "3" or swname == "5" or swname == "7":
						self.switch_state.append("0")
					elif swname == "4" or swname == "6":
						self.switch_state.append("1")
					else:
						self.switch_state.append("0")
				else:
					self.switch_state.append("0")
				temp_count = temp_count +2
		
		#parses through PLC file		
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
				self.m_switch_state.append("0")
				self.sw_order.append("0")
				self.num_switch = self.num_switch +1
			#cross
			elif line[0:2] == "cr" and proc == 0:
				self.cross_name.append(line[2:-1])
				self.cross_state.append("0")
				self.num_cross = self.num_cross +1
			#blocks
			elif line[0:2] == "bl" and proc == 0:
				self.block_name.append(line[2:-1])
				self.block_health.append("0")
				self.block_occ.append("0")
				self.authority.append("0")
				self.b_speed.append(0)
				self.bl_order.append("0")
				self.num_block = self.num_block +1
			#stopping distance
			elif line[0:2] == "st" and proc == 0:
				self.stop_distance = int(line[2:])
			#end
			elif line == "end var\n":
				proc = 1
				break
			linecount = linecount +1;
		for line in plc[linecount+1:]:
			#creates switch connections
			if line[0:2] == "sw":
				d1 = plc[linecount+2]
				d2 = plc[linecount+3]
				d3 = plc[linecount+4]
				d4 = plc[linecount+5]
				self.sw_connect.append([d1[0:-1], d2[0:-1]])
				self.sw_connect.append([d3[0:-1], d4[0:-1]])
			#creates crossing connections
			if line[0:2] == "cr":
				d1 = plc[linecount+2]
				self.cr_connect.append(d1[0:-1])
			if line[0:2] == "end proc":
				break
			linecount = linecount+1
		f.close()
		
if __name__ == '__main__':
	Wayside.main()
		
