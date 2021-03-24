class Wayside:
	def __init__(self, plcfile):
		self.plcfile = plcfile
		
	def load_plc(self, plcfile):
		plc = PLC(self, plcfile)
	
	
