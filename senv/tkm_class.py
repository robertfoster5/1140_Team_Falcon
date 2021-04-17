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
		self.past = 0
	
#_______________________________________________________________________
	
	#change block location
	def set_block(self,blocks,num):
		self.block = self.past
		print(str(self.num)+" num")
		if self.way == 1:
			if blocks[num].switch.top == 0:
				self.block = blocks[num].num+1
				print("hi")
			else:
				if blocks[self.block-1].switch.state == 0:
					self.block = blocks[num].num+1
					print("bye")
				else:
					self.block = blocks[num].switch.bottom
					print("fine")
					
		#else:
			#if past.switch.top == 0:
				#self.block = past.num
			#else:
				#if past.switch.bottom == block.num and past.switch.state == 0:
					#self.block = 
			
		signals.tkm_get_block.emit(self.block)
		print(str(self.block) + " block tkm")
		print("/////////////////////////////////////////////////////////////////////////////////////")
		signals.tkm_get_blength.emit(blocks[num].length)
		signals.tkm_get_train_auth.emit(blocks[int(self.block-1)].auth)
		print(str(blocks[int(self.block-1)].auth) + " tkm auth")
		
		if blocks[int(self.block-1)].beacon1 == 0 and blocks[int(self.block-1)].beacon2 == 0:
			pass
		elif blocks[int(self.block-1)].beacon1 == 0 and blocks[int(self.block-1)].beacon2 != 0:
			signals.tkm_get_beacon(blocks[int(self.block-1)].beacon2)
		elif blocks[int(self.block-1)].beacon1 != 0 and blocks[int(self.block-1)].beacon2 == 0:
			signals.tkm_get_beacon(blocks[int(self.block-1)].beacon1)
		elif blocks[int(self.past-1)].beacon2 != 0 and way == 1:
			signals.tkm_get_beacon(blocks[int(self.past-1)].beacon2)
		elif blocks[int(self.past-1)].beacon1 != 0 and way == -1:
			signals.tkm_get_beacon(blocks[int(self.block-1)].beacon1)
		else:
			if self.way == 1:
				signals.tkm_get_beacon.emit(blocks[int(self.block-1)].beacon1)
			else:
				signals.tkm_get_beacon.emit(blocks[int(self.block-1)].beacon2)
			
		return blocks[int(self.block - 1)].auth
#_______________________________________________________________________
	
	def set_speed(self,block):
		#print(block.speed)
		print(block.s_limit)
		
		if block.s_limit > block.speed:
			self.speed = block.speed
		else:
			self.speed = block.s_limit
			#print(block.speed)
		#print(self.speed)
		#signals.tkm_get_speed.emit(self.speed)
		print(str(block.num) + " block num")
		if block.s_limit > block.speed:
			self.speed = block.speed
			
		else:
			self.speed = block.s_limit
			print(block.speed)
		print(self.speed)
		#signals.tkm_get_speed.emit(self.speed)
		return self.speed
	
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
	def set_way(self,block,yard):
		if block[yard-2].occ == 0 and block[yard-2].auth == 1:
			self.way = -1
		elif block[yard].occ == 0 and block[yard].auth == 1:
			self.way = 1
			
		#signals.tkm_get_auth.emit(block[yard-1].auth)


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
		self.speed = -1
		
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
		
		#self.speed = 0
	
#_______________________________________________________________________
	
	#set occ of track
	def set_occ(self, occ):
		self.occ = occ
	
#_________________________________________length, grade, and speed limit of block
		self.length = length
		self.grade = grade
		self.s_limit = s_limit
		
		#if station, name of statio______________________________
	
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
#_______________________________________________________________________
	
	#set speed
	def set_speed(self, s):
		self.speed = s
			
		

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
		
		if self.line == "red":
			q = 1
		else:
			q = 0
		
		
		yards = []
		r = 0
		while r<self.end and q != 2:
			if self.blocks[r].switch.top == -1 or self.blocks[r].switch.bottom == -1:
				yards.append(int(self.blocks[r+1].num))
			r = r+1
		#print(str(yards[1]) + " yard 2")
		self.yards = yards
		
		
		self.check_swit()
		self.check_stat()
		self.check_und()
	
#_______________________________________________________________________
	
	def add_train(self,n,way,block):
		self.train.append(Train(n,way,block.num))
		signals.tkm_get_block.emit(block.num)
		signals.tkm_get_blength.emit(block.length)
		block.occ = 1
		bull = self.get_occ()
		signals.tkm_get_occ.emit(bull)
		#print(str(block.set_speed()) +" bk speed")
		#print(str(self.blocks[62].speed) +" bk 63")
		s = self.train[n-1].set_speed(block)
		print(str(s) + " tkm")
		signals.tkm_get_speed.emit(s)
		signals.tkm_get_train_auth.emit(bool(block.auth))
		print("tkm auth " + str(block.auth))
		print(block.s_limit)
		s = self.train[n-1].set_speed(block)
		print(str(s) + " tkm - add train")
		signals.tkm_get_speed.emit(s)
		#signals.tkm_get_auth.emit(block.auth)
		
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
		while r < self.end-1 and q < len(swits)-1:
			while self.blocks[r].switch.top == 0 and r < self.end -1:
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
				
				while self.blocks[a].und == 1 and a < len(self.blocks)-1:
					a = a+1
				
				self.blocks[a-1].set_beac_u(b,1)
				b = b+1
				
			a = a+1

#_______________________________________________________________________
	#get track occupancy	
	def get_occ(self):
		c = 0 
		occ = []
		occ.append("1")
		while c < int(self.end):
			occ.append(str(self.blocks[c].occ))
			c = c+1
		return occ
		
#_______________________________________________________________________
	#set track occupancy
	def set_occ(self,occ):
		d = 1
		while d <= int(self.end)-1:
			self.blocks[d-1].occ = int(occ[d])
			d = d+1
			
		#self.set_train_block(True)
		
		bull = self.get_occ()
		signals.tkm_get_occ.emit(bull)
	
#_______________________________________________________________________
	#get blocks
	def get_blocks(self):
		return self.blocks
		
#_______________________________________________________________________
	#set speed of blocks
	def set_speed(self,speeds):
		n = 1
		while n <= int(self.end):
			self.blocks[n-1].set_speed(float(speeds[n]))
			#print(str(speeds[n]) + " speed " + str(self.blocks[n-1].speed))
			n = n+1
	
#_______________________________________________________________________
	#set train blocks
	def set_train_block(self,cool):
		if(cool):
			r = 1
			q = 0
			a = []
			s = 0
			while r <= len(self.train):
				while self.blocks[q].occ == 0 and q < self.end-1:
					q = q+1
				
				print(str(q)+" this is q") 
				a.append(self.train[r-1].set_block(self.blocks,q))
				self.blocks[q+1].occ = 1
				self.blocks[q].occ = 0
				
				s = self.train[r-1].set_speed(self.blocks[q])
				r = r+1
				q = q+1
				
			bull = self.get_occ()
			self.set_occ(bull)
			print(str(s) + "tkm")
			signals.tkm_get_speed.emit(s)
			signals.tkm_get_auth.emit(a)
			
			
#_______________________________________________________________________
	#set authority
	def set_auth(self,auth):
		#print("auth")
		r = 1
		q = 0
		check = 0
		while r <= int(self.end):
			self.blocks[q].auth = int(auth[r])
			r = r+1
			q = q+1
		
		if len(self.train) == 0:
			if self.blocks[self.yards[0]].auth == 1:
				#print("if")
				if ((self.blocks[self.yards[0]-1].auth == 0 and self.blocks[self.yards[0]+1].auth == 1) or (self.blocks[self.yards[0]-1].auth == 1 and self.blocks[self.yards[0]+1].auth == 0)) and self.blocks[self.yards[0]].occ == 0:
					self.add_train(len(train)+1,1,self.blocks[self.yards[0]-1])
					self.train[len(train)-1].set_way(self.blocks,self.yards[0])
				

			elif self.blocks[self.yards[1]-1].auth == 1:
				if ((self.blocks[self.yards[1]-2].auth == 0 and self.blocks[self.yards[1]].auth == 1) or (self.blocks[self.yards[1]-2].auth == 1 and self.blocks[self.yards[1]].auth == 0)) and self.blocks[self.yards[1]-1].occ == 0:
					self.add_train(len(self.train)+1,1,self.blocks[self.yards[1]-1])
					#print(str(self.yards[1]-1) + " yards 1")
					self.train[len(self.train)-1].set_way(self.blocks,self.yards[1]-1)
			elif self.blocks[self.yards[1]].auth == 1:
				#print("elif")
				if ((self.blocks[self.yards[1]-1].auth == 0 and self.blocks[self.yards[1]+1].auth == 1) or (self.blocks[self.yards[1]-1].auth == 1 and self.blocks[self.yards[1]+1].auth == 0)) and self.blocks[self.yards[1]].occ == 0:
					self.add_train(len(self.train)+1,1,self.blocks[self.yards[1]])
					self.train[len(self.train)-1].set_way(self.blocks,self.yards[1])

		

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
