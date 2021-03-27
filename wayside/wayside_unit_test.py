import unittest
from wayside_trk_control import TrackController
from wayside_ws_control import Wayside

class TrackControllerTestCase(unittest.TestCase):
	#def test_instantiate_trk_control(self):
	#	for i in range(76):
	#		speed[i] = 0
	#		authority[i] = 0
	#	red = TrackController("r", speed, authority)
	#	for i in range(150):
	#		gspeed[i] = 0
	#		gauthority[i] = 0
	#	green = TrackController("g", gspeed, gauthority)
	#	green1 = Wayside("g1.txt")
		
	#def test_wayside_plc_load(self):
	#	self.assertTrue(green1.num_blocks() == 20)
	#	self.assertTrue(green1.get_cross() == 1)
	#	self.assertTrue(green1.get_switch() ==  0)
	
	#def test_maintenance_order(self):
	#	green1.m_order("100000000000000000")
	#	self.assertTrue(green1.get_occupancy("100000000000000000")
		
	#def test_new_authority(self):
	#	for i in range(20):
	#		auth[i] = 0
	#	green1.new_auth(auth)
	def test_plc(self):
		green1 = Wayside("g1.txt")
		
if __name__ == '__main__':
	unittest.main()
		
