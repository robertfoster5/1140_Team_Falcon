import unittest

from tkm_class import Station
from tkm_class import Crossing
from tkm_class import Switch
from tkm_class import Train
from tkm_class import Block
from tkm_class import Track
from tkm_class import Track_Heater
from tkm_class import Envi_Temp

from tkm_functions import f_to_c

class Test_TKM_Methods(unittest.TestCase):
	
	def test_track_heater(self):
		#test __init__
		th = Track_Heater()
		self.assertFalse(th.state)
		
		th.toggle(1)
		self.assertTrue(th.state)
		
	def test_envi_temp(self):
		#test __init__
		et = Envi_Temp(69)
		self.assertEqual(et.temp,f_to_c(69))
		self.assertFalse(et.th.state)
		
		#test set_temp
		et.set_temp(30)
		self.assertEqual(et.temp,f_to_c(30))
		self.assertTrue(et.th.state)
		
	def test_train(self):
		#test __init__
		t1 = Train(3,1,20)
		self.assertEqual(t1.num,3)
		self.assertEqual(t1.way,1)
		self.assertEqual(t1.block,20)
		self.assertFalse(t1.occ)
		
		#test set_block
		t1.set_block(25)
		self.assertEqual(t1.block,25)
		
		#test inc_occ
		t1.inc_occ(69)
		self.assertEqual(t1.occ,69)
		
		#test disembark
		num = t1.disembark()
		self.assertEqual(t1.occ,(69-num))
		self.assertTrue(num >= 0)
		
		

if __name__ == '__main__':
	unittest.main()
