class TrackController:
	#Initialize track controller and all the wayside controllers
	def __init__(self, line, speed, authority):
		self.speed = speed
		self.authority = authority
		self.line = line
		self.waysides = []
		if self.line == "r":
			auth1 = authority[0:22]
			auth2 = authority[23:44] + authority[66:75]
			auth3 = authority[45:65]
			r1 = Wayside(self, r1, line, auth1, "r1.txt")
			r2 = Wayside(self, r2, line, auth2, "r2.txt")
			r3 = Wayside(self, r3, line, auth3, "r3.txt")
			self.waysides.append(r1)
			self.waysides.append(r2)
			self.waysides.append(r3)
		else:
			auth1 = authority[0:19]
			auth2 = authority[20:34] + authority[146:149]
			auth3 = authority[35:72]
			auth4 = authority[73:100]
			auth5 = authority[101:145]
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
		if self.line == "r":
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
		if self.line == "r":
			auth1 = authority[0:22]
			auth2 = authority[23:44] + authority[66:75]
			auth3 = authority[45:65]
			self.waysides[0].new_auth(self.wayside[0], auth1)
			self.waysides[1].new_auth(self.wayside[1], auth2)
			self.waysides[2].new_auth(self.wayside[2], auth3)
		else:
			auth1 = authority[0:19]
			auth2 = authority[20:34] + authority[146:149]
			auth3 = authority[35:72]
			auth4 = authority[73:100]
			auth5 = authority[101:145]
			self.waysides[0].new_auth(self.wayside[0], auth1)
			self.waysides[1].new_auth(self.wayside[1], auth2)
			self.waysides[2].new_auth(self.wayside[2], auth3)
			self.waysides[3].new_auth(self.wayside[3], auth4)
			self.waysides[4].new_auth(self.wayside[4], auth5)
			
	#CTC calls this with occupancy from track model uses this	
	def update_occupancy(self, occupancy):
		if self.line == "r":
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
	def get_occupancy(self):
		for i in self.waysides:
			return self.waysides[i].get_occupancy(self.waysides[i])
			
	def get_switch_states(self):
		for i in self.waysides:
			return self.waysides[i].get_switch(self.waysides[i])
			
	def get_cross_states(self):	
		for i in self.waysides:
			return self.waysides[i].get_cross(self.waysides[i])
			
	def get_authority(self):
		for i in self.waysides:
			return self.waysides[i].get_auth(self.waysides[i])
