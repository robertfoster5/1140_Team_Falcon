class Wayside:
	def __init__(self, plcfile):
		self.plcfile = plcfile
		
	def m_order(self, order):
		
	def new_auth(self, authority):
		self.authority = authority
		
	def change_auth(self, authority):
		
	def load_plc(self):
		f = open(self.plcfile)
		swcount = 0
		crcount = 0
		blcount = 0
		linecount = 0
		swc = 0
		swr = 0
		crc
		proc = 0
		plc = f.readlines()
		for line in plc[0:]:
			print(line)
			if line == "var":
				proc = 0
			#switch
			elif line[0:2] == "sw" and proc == 0:
				switch_name[swcount][0] = "Switch " + line[2:]
				switch_name[swcount][1] = "0" 
				swcount = swcount + 1
			#cross
			elif line[0:2] == "cr" and proc == 0:
				cross_name[crcount][0] = "Crossing " + line[2:]
				cross_name[crcount][1] = "0"
				crcount = crcount + 1
			#block
			elif line[0:2] == "bl" and proc == 0:
				block_name[blcount][0] = "Block " + line[2:]
				block_name[blcount][1] = "0"
				blcount = blcount + 1
			#end
			elif line == "end var":
				proc = 1
				break
			else:
				linecount = linecount +1;
		for line in plc[linecount:]:
			print("proc")
			print(line)
			if line[0:2] == "sw":
				sw_connect[swr][0] = [plc[linecount+1], plc[linecount+2]]
				sw_connect[swr][1] = [plc[linecount+3], plc[linecount+4]]
				swr = swr + 1
			if line[0:2] == "cr":
				cr_connect[crc][0] = plc[linecount+1]
		f.close()
