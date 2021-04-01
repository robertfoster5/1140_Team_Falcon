import random
from signals import signals

class Station:
	def __init__(self,name,block,side):
		#name and location of station
		self.name = name
		self.block = block
		
		#sales and current number of people at station
		self.sales = 0
		self.occ = 0
		self.train = 0
		self.side = side

#_______________________________________________________________________
		
	#number of ticket sales
	def get_sales(self):
		self.sales = random.randrange(10,1000)
		self.occ = self.occ + self.sales
		return self.sales

#_______________________________________________________________________
	
	#number of passengers boarding given train
	def get_boarding(self,train):
		board = random.randrange(0,100)
		train.inc_occ(board)
		return board
		

class Crossing:
	def __init__(self,block):
		#block location and state
		self.block = block
		self.state = 0
	
#_______________________________________________________________________
	
	#toggles crossing state	
	def toggle(self):
		if state == 0:
			self.state = 1
		else:
			self.state = 0

class Switch:
	def __init__(self, num, sta1, sto1, sta2, sto2):
		#no switch
		if sta1 == 0 and sto1 == 0 and sta2 == 0 and sto2 == 0:
			self.start = num
			self.top = 0
			self.bottom = 0
			self.state = 0
		#to yard
		elif sta2 == -1:
			self.start = sto2
			self.top = sto2+1
			self.bottom = -1
			self.state = 0
		#from yard
		elif sto1 == -1:
			self.start = sta1
			self.top = sta1-1
			self.bottom = -1
			self.state = 0
		else:
			if sta1 == sta2:
				self.start = sta1
				self.top = sto1
				self.bottom = sto2
				self.state = 0
			elif sto1 == sto2:
				self.start = sto1
				self.top = sta1
				self.bottom = sta2
				self.state = 0	
				self.state = 0	

class Train:
	def __init__(self,num,way,block):
		#train number
		self.num = num
		#direction of travel 1 for counting up, 0 for counting down
		self.way = way
		#number of passengers
		self.occ = 0
		#block location
		self.block = block
		#commanded speed
		self.speed = 0
	
#_______________________________________________________________________
	
	#change block location
	def set_block(self,block):
		self.block = block
	
#_______________________________________________________________________
	
	def set_speed(self,block):
		if self.block.s_limit > self.block.speed:
			self.speed = self.block.speed
		else:
			self.speed = self.block.s_limit
	
#_______________________________________________________________________
	
	#increase number of passengers
	def inc_occ(self,mor):
		self.occ = self.occ + mor
	
#_______________________________________________________________________
	
	#disembarking
	def disembark(self):
		les = random.randrange(0,self.occ)
		self.occ = self.occ - les
		return les

#_______________________________________________________________________

	#set way
	def set_way(self,block):
		r = 0


class Block:
	def __init__(self,line,sect,num,length,grade,s_limit,station,swit_t,swit_b,cross,stat_side,elev,c_elev,und):
		#14 inputs
		#line of block, section of block, number of block
		self.line = line
		self.sect = sect
		self.num = num
		
		#length, grade, and speed limit of block
		self.length = length
		self.grade = grade
		self.s_limit = s_limit
		
		#if station, name of station passed, if not 0
		if station != 0:
			self.station = Station(station,self.num,stat_side)
		else:
			self.station = Station(0,self.num,0)
		
		#if switch number of non-seqeuntual block number passed, if not 0
		self.swit_t = swit_t
		self.swit_b = swit_b
		
		#no switch
		if swit_t == [0,0] and swit_b == [0,0]:
			self.switch = Switch(self.num,0,0,0,0)
		#to yard
		elif swit_t[0] == 0 and swit_t[1] == 0:
			self.switch = Switch(0,0,0,-1,swit_b[1])
		#from yard
		elif swit_b[0] == 0 and swit_b[1] == 0:
			self.switch = Switch(0,swit_t[0],-1,0,0)
		#normal switch
		else:
			self.switch = Switch(0,swit_t[0],swit_t[1],swit_b[0],swit_b[1])
		
		
		#crossing = 1, if not = 0
		if cross == 1:
			self.cross = Crossing(self.num)
		else:
			self.cross = cross
		
		
		#current and cumalitve elevation
		self.elev = elev
		self.c_elev = c_elev
		
		#underground
		self.und = und
		
		#occupancy
		self.occ = 0
		
		self.beacon1 = 0
		self.beacon2 = 0
		
		self.auth = 0
		
		self.speed = 0
	
#_______________________________________________________________________
	
	#set occ of track
	def set_occ(self, occ):
		self.occ = occ
	
#_______________________________________________________________________
	
	#set station beacons	
	def set_beac(self, beac):
		b = beac|0b00100000
		self.beacon1 = beac
		self.beacon2 = b
	
#_______________________________________________________________________
	
	#set tunnel beacons
	def set_beac_u(self, beac, num):
		if num == 0:
			self.beacon1 = beac
			self.beacon2 = 0
			
		elif num == 1:
			b = beac|0b00100000
			self.beacon1 = 0
			self.beacon2 = b
			

class Track:
	def __init__(self, blocks):
		#array of blocks
		self.blocks = blocks
		
		#start and end of track
		self.start = blocks[0].num
		self.end = blocks[-1].num
		
		#line of track
		self.line = blocks[0].line
		self.train = []
		
		self.check_swit()
		self.check_stat()
		self.check_und()
	
#_______________________________________________________________________
	
	def add_train(self,num,way,block):
		self.train.append(Train(num,way,block))
	
#_______________________________________________________________________
	
	#get train matching number back
	def get_train(self,num):
		q = 0
		
		while q < len(self.train):
			if num == self.train.num:
				break
			q = q+1
		
		return self.train[q]
	
#_______________________________________________________________________
	
	#fix switches
	def check_swit(self):
		p = 0
		while p<self.end:
			if self.blocks[p].switch.start != self.blocks[p].num and self.blocks[p].switch.bottom != -1:
				self.blocks[self.blocks[p].switch.start-1].switch = Switch(0,self.blocks[p].swit_t[0],self.blocks[p].swit_t[1],self.blocks[p].swit_b[0],self.blocks[p].swit_b[1])
				self.blocks[p].switch = Switch(self.blocks[p].num,0,0,0,0)
			
			#yards	
			elif self.blocks[p].switch.start != self.blocks[p].num and self.blocks[p].switch.bottom == -1:
				#if self.blocks[p].switch.start < self.blocks[p].switch.top:
				self.blocks[self.blocks[p].switch.start-1].switch = self.blocks[p].switch
				self.blocks[p].switch = Switch(self.blocks[p].num,0,0,0,0)
					
			p = p+1
	
#_______________________________________________________________________

	#set switches
	def set_swit(self,swits):
		q = 1
		r = 0
		while r < self.end:
			while self.blocks[r].switch.top == 0:
				r = r+1
			
			self.blocks[r].switch.state = int(swits[q])
			r = r+1
			q = q+1		
	
	
#_______________________________________________________________________
	
	#set up beacons		
	def check_stat(self):
		if self.line == "Red":
			b = 0b00000001
		elif self.line == "Green":
			b = 0b10000001
		
		a = 0
		
		while a < self.end:
			if self.blocks[a].station.name != 0:
				self.blocks[a].set_beac(b)
				b = b+1
			
			a = a+1
	
#_______________________________________________________________________
	#set up tunnel beacons		
	def check_und(self):
		if self.line == "Red":
			b = 0b01000001
		elif self.line == "Green":
			b = 0b11000001
		
		a = 0
		
		while a < self.end:
			if self.blocks[a].und == 1:
				self.blocks[a].set_beac_u(b,0)
				
				while self.blocks[a].und == 1:
					a = a+1
				
				self.blocks[a-1].set_beac_u(b,1)
				b = b+1
				
			a = a+1

#_______________________________________________________________________
	#get track occupancy	
	def get_occ(self):
		c = 0 
		occ = ""
		while c < int(self.end):
			occ = occ + str(self.blocks[c].occ)
			c = c+1
		return occ
		
#_______________________________________________________________________
	#set track occupancy
	def set_occ(self,occ):
		d = 1
		while d <= int(self.end):
			self.blocks[d].occ = int(occ[d])
			d = d+1
			
		self.set_train_block()
	
#_______________________________________________________________________
	#get blocks
	def get_blocks(self):
		return self.blocks
		
#_______________________________________________________________________
	#set speed of blocks
	def set_speed(self,speeds):
		l = 1
		while l <= int(self.end):
			self.blocks[l].speed = speeds[l]
			l = l+1
	
#_______________________________________________________________________
	#set train blocks
	def set_train_block(self):
		r = 1
		q = 0
		while r <= len(self.train):
			while self.blocks[q].occ == 0:
				q = q+1
				
			self.train[r].set_block(q)
			self.train[r].set_speed(self.blocks[q])
			r = r+1
			q = q+1
			
			
#_______________________________________________________________________
	#set authority
	def set_auth(self,auth):
		r = 1
		q = 0
		while r <= int(self.end):
			self.blocks[q].auth = auth[r]
			r = r+1
			q = q+1
		
		r = 0
		while r < len(self.train):
			train[r].set_way(self.blocks)
		

from tkm_functions import f_to_c

class Track_Heater:
	def __init__(self):
		#state of heater 1 = on
		self.state = 0
		
	def toggle(self,num):
		self.state = num
		
class Envi_Temp:
	def __init__(self,temp):
		self.temp = f_to_c(temp)
		self.th = Track_Heater()
		if self.temp <= 4.44:
			self.th.toggle(1)
			
	def set_temp(self,temp):
		self.temp = f_to_c(temp)
		if self.temp <= 4.44:
			self.th.toggle(1)
