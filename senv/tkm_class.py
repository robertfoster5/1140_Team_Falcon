import random
from signals import signals

def kmhr_to_ms(num):
	num = round(num*0.277778,2)
	return num

#total num
train_num = 0

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
		now = random.randrange(0,10)
		if self.sales+now > 300:
			hol = self.sales+now -300
			now = now - hol
		else:
			"hi"
		self.sales = self.sales + now
		self.occ = self.occ + now
		return self.sales

#_______________________________________________________________________
	
	#number of passengers boarding given train
	def get_boarding(self,occ):
		max_train = 150
		board = random.randrange(0,max_train)
		if board > self.occ:
			board = self.occ
			self.occ = 0
		else:
			self.occ = self.occ - board
		signals.tkm_get_pass_count.emit
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
		#normal switch
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
		
		#disembark and boarding
		self.dis = 0
		self.boar = 0
	
#_______________________________________________________________________
	
	#change block location
	def set_block(self,blocks,num,line,flag):
		self.past = self.block
		#print(str(self.num)+" train num")
		num = int(num)
		#determine what next block is
		#green
		if line == "Green":
			if self.way == 1:
				if '''blocks[num-1].switch.top == 0''' and int(blocks[num-1].num) != 100 and flag != 1 or (int(blocks[num-1].num) == 63):
					self.block = blocks[num].num
				elif int(blocks[num-1].num) == 100:
					self.block = 85
					self.way = -1
				elif flag == 1:
					self.block = 29
					self.way = -1
					#print(self.way)
				else:
					if blocks[num-1].switch.state == 0:
						self.block = blocks[num-1].switch.top
					else:
						self.block = blocks[num-1].switch.bottom
						self.way = -1
			#way = -1
			else:
				if blocks[num-1].num != 1 and blocks[num-1].num != 77:
					self.block = blocks[num-1].num-1
				elif blocks[num-1].num == 77:
					self.block = 101
					self.way = 1
				elif blocks[num-1].num == 1:
					self.block = 13
					self.way = 1
			'''
			if self.way == 1:
				if blocks[num].switch.top == 0:
					self.block = blocks[num].num+1
					
				else:
					if blocks[self.block-1].switch.state == 0:
						self.block = blocks[num].num+1
						
					else:
						self.block = blocks[num].switch.bottom
			'''
		#red
		else:
			# way = 1
			if self.way == 1:
				if '''blocks[num-1].switch.top == 0''' and int(blocks[num-1].num) != 66 and int(blocks[num-1].num) != 71 and flag != 1:
					self.block = blocks[num].num
				elif int(blocks[num-1].num) == 66 :
					#if blocks[53].switch.state == 1:
					self.block = 52
					self.way = -1
				elif int(blocks[num-1].num) == 71:
					#if blocks[39].switch.state == 1:
					self.block = 38
					self.way = -1
				elif flag == 1:
					#if blocks[28].switch.state == 1:
					self.block = 27
					self.way = -1
				else:
					if blocks[num-1].switch.state == 0:
						self.block = blocks[num-1].switch.top
					else:
						self.block = blocks[num-1].switch.bottom
						self.way = -1
			else:# way == -1
				if '''blocks[num-2].switch.top == 0''' and int(blocks[num-1].num) != 33 and int(blocks[num-1].num) != 44 and int(blocks[num-1].num) != 72 and int(blocks[num-1].num) != 67 and int(blocks[num-1].num) != 1 or int(blocks[num-1].num) == 9:
					self.block = blocks[num-1].num-1
				elif int(blocks[num-1].num) == 72:
					self.block = 33
					self.way = 1
				elif int(blocks[num-1].num) == 67:
					self.block = 44
					self.way = 1
				elif int(blocks[num-1].num) == 44:
					self.block = 67
					self.way = 1
				elif int(blocks[num-1].num) == 33:
					self.block = 72
					self.way = 1
				elif int(blocks[num-1].num) == 1:
					self.block = 16
					self.way = 1
				
		
		
		#change block occupancy and send next block info to TNM
		blocks[int(self.past)-1].occ = 0
		blocks[int(self.block)-1].occ = 1
		signals.tkm_get_block.emit(self.block,self.num)
		#print(str(self.block) + " block tkm")
		#print("/////////////////////////////////////////////////////////////////////////////////////")
		#print(str(blocks[int(self.block)-1].length)+" this is block length")
		signals.tkm_get_blength.emit(blocks[int(self.block)-1].length,self.num)
		signals.tkm_get_train_auth.emit(blocks[int(self.block-1)].auth,self.num)
		signals.tkm_get_elev.emit(blocks[int(self.block-1)].elev,self.num)
		#print(str(blocks[int(self.block-1)].auth) + " tkm auth")
		
		#check for beacons to send
		if blocks[int(self.block-1)].beacon1 == 0 and blocks[int(self.block-1)].beacon2 == 0:
			pass
		elif blocks[int(self.block-1)].beacon1 == 0 and blocks[int(self.block-1)].beacon2 != 0:
			signals.tkm_get_beacon.emit(blocks[int(self.block-1)].beacon2,self.num)
		elif blocks[int(self.block-1)].beacon1 != 0 and blocks[int(self.block-1)].beacon2 == 0:
			signals.tkm_get_beacon.emit(blocks[int(self.block-1)].beacon1,self.num)
		elif blocks[int(self.past-1)].beacon2 != 0 and self.way == 1:
			signals.tkm_get_beacon.emit(blocks[int(self.past-1)].beacon2,self.num)
		elif blocks[int(self.past-1)].beacon1 != 0 and self.way == -1:
			signals.tkm_get_beacon.emit(blocks[int(self.block-1)].beacon1,self.num)
		else:
			if self.way == 1:
				signals.tkm_get_beacon.emit(blocks[int(self.block-1)].beacon1,self.num)
			else:
				signals.tkm_get_beacon.emit(blocks[int(self.block-1)].beacon2,self.num)
			
		return blocks[int(self.block - 1)].auth
#_______________________________________________________________________
	#sending a new commanded speed to TNM
	#if limit is smaller send limit, if commanded is smaller send commanded
	def set_speed_new(self,block):
		#print(block.s_limit)
		#print(block.speed)
		#print(block.num)
		if block.s_limit > block.speed:
			self.speed = block.speed
		else:
			self.speed = block.s_limit
			#print(block.speed)
		#print(self.speed)
		#signals.tkm_get_speed.emit(self.speed)
		#print(str(block.num) + " block num")
		if block.s_limit > block.speed:
			self.speed = block.speed
			
		else:
			self.speed = block.s_limit
			#print(block.speed)
		#print(str(round(self.speed,1)) + " mps tkm ")
		#signals.tkm_get_speed.emit(self.speed)
		return self.speed
	
#_______________________________________________________________________
	#for if the train is starting form rest
	def set_speed(self,block):
		#print(block[int(self.block-1)].s_limit)
		#print(block[int(self.block-1)].speed)
		#print(block[int(self.block-1)].num)
		if block[int(self.block-1)].s_limit > block[int(self.block-1)].speed:
			self.speed = block[int(self.block-1)].speed
		else:
			self.speed = block[int(self.block-1)].s_limit
			
		if block[int(self.block-1)].s_limit > block[int(self.block-1)].speed:
			self.speed = block[int(self.block-1)].speed
			
		else:
			self.speed = block[int(self.block-1)].s_limit
			#print(block[int(self.block-1)].speed)
		#print(str(round(self.speed,1)) + " mps tkm ")
		#signals.tkm_get_speed.emit(self.speed)
		return self.speed

#_______________________________________________________________________
	
	#increase number of passengers
	def inc_occ(self,mor):
		self.occ = self.occ + mor
	
#_______________________________________________________________________
	
	#update disembarking
	def update_disembark(self):
		if self.occ >1:
			self.dis = random.randrange(0,self.occ)
		self.occ = self.occ - self.dis
		
	#update boarding
	def update_board(self, blocks):
		if blocks[int(self.block)-1].station.occ > 0:
			self.boar = blocks[int(self.block)-1].station.get_boarding(self.occ)
		self.occ = self.occ + self.boar
		

#_______________________________________________________________________

	#set way
	def set_way(self,block,yard):
		if block[yard-2].occ == 0 and block[yard-2].auth == 1:
			self.way = -1
		elif block[yard].occ == 0 and block[yard].auth == 1:
			self.way = 1			
		#signals.tkm_get_auth.emit(block[yard-1].auth)
		
	#destroy train
	def destroy(self):
		val = self.block
		self.way = 0
		self.occ = 0
		self.block = -1
		self.speed = 0
		self.past = 0
		signals.tkm_get_destroy.emit(self.num)
		return val


class Block:
	def __init__(self,line,sect,num,length,grade,s_limit,station,swit_t,swit_b,cross,stat_side,elev,c_elev,und):
		#14 inputs
		#line of block, section of block, number of block
		self.health = 0
		self.line = line
		self.sect = sect
		self.num = num
		
		#length, grade, and speed limit of block
		self.length = length
		self.grade = grade
		self.s_limit = kmhr_to_ms(s_limit)
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
		
		#beacon
		self.beacon1 = 0
		self.beacon2 = 0
		
		#authority
		self.auth = 0
		
	
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
		
		#chieck if red or green line
		if self.line == "red":
			q = 1
		else:
			q = 0
		
		#generate yard block numbers
		yards = []
		r = 0
		
		if self.line == "Red":
			yards.append(9)
		else:
			yards.append(57)
			yards.append(63)
		
		self.yards = yards
		
		#setting beacons and switches after loading all blocks
		self.check_swit()
		self.check_stat()
		self.check_und()
	
#_______________________________________________________________________
	
	#update train boarding and disembarking
	def update_dis(self,i):
		self.train[i].update_disembark()
		self.train[i].update_board(self.blocks)
		self.set_occ(self.get_occ())
		signals.tkm_get_pass_count.emit(self.train[i].occ,self.train[i].num)
		
#_______________________________________________________________________
	
	#add a train to track
	def add_train(self,letter):#n,way,block):
		global train_num
		'''
		if len(train_num) == 0:
			n = 1
			train_num.append(train_num)
		else:
			i = 0
			while i < len(train_num):
				if i+1 != train[i]:
					n = i+1
					train_num.append(train_num)
		'''
		if self.line == "Red":
			way = -1
			blo = 9
			n = train_num+1
		elif self.line == "Green":
			way = 1
			blo = 63
			n = train_num+1
		
		train_num = train_num+1
		self.train.append(Train(n,way,blo))
		signals.tkm_get_train_num.emit(n,self.line)
		signals.tkm_get_block.emit(self.blocks[blo-1].num,self.train[-1].num)
		signals.tkm_get_blength.emit(self.blocks[blo-1].length,self.train[-1].num)
		self.blocks[blo-1].occ = 1
		bull = self.get_occ()
		signals.tkm_get_occ.emit(bull)
		s = self.train[len(self.train)-1].set_speed_new(self.blocks[blo-1])
		#print("speeeeeeeeeeeeeeeeed "+str(s))
		#print(str(s) + " tkm")
		#signals.tkm_get_speed.emit(s)
		signals.tkm_get_train_auth.emit(bool(self.blocks[blo-1].auth),self.train[-1].num)
		#print("tkm auth " + str(self.blocks[blo-1].auth))
		#print(block.s_limit)
		
		#print(str(s) + " tkm - add train")
		signals.tkm_get_speed.emit(s,self.train[-1].num)
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
			#print(p)
			#print(str(self.blocks[p].switch.start))
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
		elif self.line == "Blue":
			b = 0b00000001
		
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
				
				if a == len(self.blocks)-1:
					10
				else:
					self.blocks[a-1].set_beac_u(b,1)
				b = b+1
				
			a = a+1

#_______________________________________________________________________
	#get track occupancy	
	def get_occ(self):
		c = 0 
		occ = []
		if self.line == "Red":
			occ.append("0")
		else:
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
		global train_num
		
		n = 1
		#print(len(self.blocks))
		#print(len(speeds))
		
		while n <= int(self.end):
			self.blocks[n-1].set_speed(float(speeds[n]))
			#if float(speeds[n]) != 0:
				#print(str(self.blocks[n-1].speed)+" speed   " + str(self.blocks[n-1].num)+ " num")
			#print(str(speeds[n]) + " speed " + str(self.blocks[n-1].speed))
			n = n+1
		
		if len(self.train) > 0:
			i = 0
			while i < len(self.train):
				if self.blocks[int(self.train[i].block-1)].speed > 0 and '''self.train[i].speed == 0''' and self.blocks[int(self.train[i].block-1)].auth == 1:
					if self.blocks[int(self.train[i].block-1)].speed < self.blocks[int(self.train[i].block-1)].s_limit:
						signals.tkm_get_train_auth.emit(self.blocks[int(self.train[i].block-1)].auth,self.train[i].num)
						signals.tkm_get_speed.emit(self.blocks[int(self.train[i].block-1)].speed,self.train[i].num)
						#print(str(self.blocks[int(self.train[i].block-1)].speed)+" spppppppppppppppppppppppppppeeeeeeeeeeeeeeeeeeddddd")
						#print(str(self.blocks[int(self.train[i].block-1)].auth) + " aaaaaaaaaaaauuuuuuuuuuuuuuttttttttttttttthhhhhhhhh")
						#print(str(self.train[i].num)+ " train num")
					else:
						signals.tkm_get_train_auth.emit(self.blocks[int(self.train[i].block-1)].auth,self.train[i].num)
						signals.tkm_get_speed.emit(self.blocks[int(self.train[i].block-1)].s_limit,self.train[i].num)
						#print(str(self.blocks[int(self.train[i].block-1)].s_limit)+" spppppppppppppppppppppppppppeeeeeeeeeeeeeeeeeeddddd")
						#print(str(self.blocks[int(self.train[i].block-1)].auth) + " aaaaaaaaaaaauuuuuuuuuuuuuuttttttttttttttthhhhhhhhh")
						#print(str(self.train[i].num)+ " train num")
				i = i+1
	
#_______________________________________________________________________
	#set train blocks
	def set_train_block(self,num):
		s = 0
		f = 0
		
		i = 0
		while i < len(self.train):
			#print(self.train[i].num)
			#print(num)
			if num == self.train[i].num:
				break
			i = i+1
		
		
		way = self.train[i].way
		
		if self.line == "Green":
			if self.train[i].block == 150:
				q = 28
				f = 1
			else:
				q = int(self.train[i].block)
		elif self.line == "Red":
			if self.train[i].block == 76:
				q = 26
				f = 1
			else:
				q = int(self.train[i].block)
		
		
		#print(str(q)+" this is q") 
			
		a = self.train[i].set_block(self.blocks,q,self.line,f)
		#pas = a[0]
		#self.blocks[a[0]-1].occ == 0
		#self.blocks[int(self.train[num-1].block)-1].occ = 1
		
		s = self.train[i].set_speed(self.blocks)
		
				
		bull = self.get_occ()
		self.set_occ(bull)
		#print(str(s) + "tkm")
		#print(str(s)+" track model speed")
		signals.tkm_get_speed.emit(s,self.train[i].num)
		#signals.tkm_get_auth.emit(a)
			
			
#_______________________________________________________________________
	#set authority
	def set_auth(self,auth):		
		r = 1
		q = 0
		check = 0
		#print(str(auth))
		while r <= int(self.end):
			self.blocks[q].auth = int(auth[r])
			#if int(auth[r]) == 1:
				#print(self.blocks[q].num)
			r = r+1
			q = q+1
		
		'''
		if self.line == "Green":
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
						
		elif self.line == "Red":
			if len(self.train) == 0:
				if self.blocks[self.yards[0]-1].auth == 1:
					self.add_train(len(self.train)+1,-1,self.blocks[self.yards[0]-1])
		'''
	#set health of blocks
	def set_health(self,health):
		i = 1
		d = 0
		while d < len(self.blocks):
			self.blocks[d].health = health[i]
			i = i+1
			d = d+1
			

from tkm_functions import f_to_c

class Track_Heater:
	def __init__(self):
		#state of heater 1 = on
		self.state = 0
	#toggle heater	
	def toggle(self,num):
		self.state = num
		
class Envi_Temp:
	def __init__(self,temp):
		self.temp = f_to_c(temp)
		self.th = Track_Heater()
		if self.temp <= 4.44:
			self.th.toggle(1)
	#set temp if below 40 turn on track heater		
	def set_temp(self,temp):
		self.temp = f_to_c(temp)
		if self.temp <= 4.44:
			self.th.toggle(1)
