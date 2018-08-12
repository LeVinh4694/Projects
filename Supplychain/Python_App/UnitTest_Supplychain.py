# UnitTest_Supplychain.py

import unittest
from unittest.mock import patch
from web3 import Web3
from Supplychain import *

class MyTest(unittest.TestCase):
	def __init__(self, *args):
		self.web3 = Web3(Web3.HTTPProvider('http://localhost:8080', request_kwargs={'timeout': 60}))
		self.sc = SupplyChain(self.web3)

	@patch('getpass.getpass', return_value = '123')
	def testUnlockAccount1(self, *args):
		self.assertFalse(self.sc.UnlockAccount())

	@patch('getpass.getpass', return_value = '123456')
	def test_UnlockAccount_2(self, *args):
		self.assertTrue(self.sc.UnlockAccount())

if __name__ == '__main__':
	unittest.main()