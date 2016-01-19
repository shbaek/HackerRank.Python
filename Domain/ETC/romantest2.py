# romantest2.py
import unittest, roman1
class ToRomanBadInput(unittest.TestCase):
	def test_too_large(self):
		'''to_roman은 큰 숫자를 입력하면 실패 해야 합니다..'''
		self.assertRaises(roman1.OutOfRangeError, roman1.to_roman, 4000);