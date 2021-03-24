class TrackController:
	#Initialize track controller and all the wayside controllers
	def __init__(self, line, speed, authority):
		self.speed = speed
		self.authority = authority
		self.line = line
		self.waysides = []
		if self.line == "red":
			r1 = Wayside(self, r1, line, auth1, "r1.txt")
			r2 = Wayside(self, r2, line, auth2, "r2.txt")
			r3 = Wayside(self, r3, line, auth3, "r3.txt")
			self.waysides.append(r1)
			self.waysides.append(r2)
			self.waysides.append(r3)
		else:
			g1 = Wayside(self, g1, line, auth1, "g1.txt")
			g2 = Wayside(self, g2, line, auth2, "g2.txt")
			g3 = Wayside(self, g3, line, auth3, "g3.txt")
			g4 = Wayside(self, g4, line, auth4, "g4.txt")
			g5 = Wayside(self, g5, line, auth5, "g5.txt")
			self.waysides.append(g1)
			self.waysides.append(g2)
			self.waysides.append(g3)
			self.waysides.append(g4)
			self.waysides.append(g5)
			
	def maintenance_order(self, order):
		if self.line == "red":
			or1 = order[0:22]
			or2 = order[23:44] + order[66:75]
			or3 = order[45:65]
			self.waysides[0].m_order(self.wayside[0], or1)
			self.waysides[1].m_order(self.wayside[1], or2)
			self.waysides[2].m_order(self.wayside[2], or3)
		else:
			or1 = order[0:19]
			or2 = order[20:34] + order[146:149]
			or3 = order[35:72]
			or4 = order[73:100]
			or5 = order[101:145]
			self.waysides[0].m_order(self.wayside[0], or1)
			self.waysides[1].m_order(self.wayside[1], or2)
			self.waysides[2].m_order(self.wayside[2], or3)
			self.waysides[3].m_order(self.wayside[3], or4)
			self.waysides[4].m_order(self.wayside[4], or5)
	
	def new_authority(self, authority):
		
	#CTC calls this with occupancy from track model uses this	
	def update_occupancy(self, occupancy):
		if self.line == "red":
			self.waysides[0].update(self.wayside[0], or1)
			self.waysides[1].update(self.wayside[1], or2)
			self.waysides[2].update(self.wayside[2], or3)
		else:
			self.waysides[0].update(self.wayside[0], or1)
			self.waysides[1].update(self.wayside[1], or2)
			self.waysides[2].update(self.wayside[2], or3)
			self.waysides[3].update(self.wayside[3], or4)
			self.waysides[4].update(self.wayside[4], or5)
	
	#CTC needs to use this to send to get switches, crossings, authority, 
	def get_states(self):
		for i in self.waysides:
			return self.waysides[i].get_occupancy(self.waysides[i])
		for i in self.waysides:
			return self.waysides[i].get_switch(self.waysides[i])
		for i in self.waysides:
			return self.waysides[i].get_cross(self.waysides[i])
		for i in self.waysides:
			return self.waysides[i].get_auth(self.waysides[i])
