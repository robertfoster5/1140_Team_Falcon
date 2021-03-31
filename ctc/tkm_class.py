class Block:
	
	def __init__(self,num,length,grade,s_limit,station,switch,cross,elev,c_elev,occ):
		#10 inputs
		#number of block
		self.num = num
		
		#length, grade, and speed limit of block
		self.length = length
		self.grade = grade
		self.s_limit = s_limit
		
		#if station, name of station passed, if not 0
		self.station = station
		
		#if switch number of non-seqeuntual block number passed, if not 0
		self.switch = switch
		
		#crossing = 1, if not = 0
		self.cross = cross
		
		#current and cumalitve elevation
		self.elev = elev
		self.c_elev = elev
		
		#occupancy
		self.occ = occ
		
	def set_Occ(self, occ):
		self.occ = occ
		


class Station:
	
	def __init__(self,name,block):
		#name and location of station
		self.name = name
		self.block = block		
		

class Train:
	def __init__(self,num,way,occ):
		#train number
		self.num = num
		#direction of travel 1 for counting up, 0 for counting down
		self.way = way
		#number of passengers
		self.occ = occ
