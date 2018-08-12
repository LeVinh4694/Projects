# Supplychain.py

import sys, os
# Import get password library
import getpass
# Import library for Web3 Ethereum
from web3 import Web3

class SupplyChain:
	def __init__(self, obj):
		self.obj = obj

	def CheckBalance(self):
		return self.obj.fromWei(self.obj.eth.getBalance(self.obj.eth.coinbase), 'ether')

	def UnlockAccount(self):
		self.pwd = getpass.getpass(prompt="Insert password: ")
		ret = self.obj.personal.unlockAccount(self.obj.eth.coinbase, self.pwd)
		return ret

	def SendEther(self, receiver, amount):
		# Check received account is existed
		if not self.obj.isAddress(receiver):
			return 'Invalid account address.'
		# Unlock account
		if not self.UnlockAccount():
			return 'Password is incorrect.'
		try:
			# Send transaction
			self.tx_hash = self.obj.eth.sendTransaction({'from':self.obj.eth.coinbase, 
										'to':self.obj.toChecksumAddress(receiver), 
										'value': self.obj.toWei(amount, 'ether')})
			return True
		except ValueError as e:
			return e

web3 = Web3(Web3.HTTPProvider('http://localhost:8080', request_kwargs={'timeout': 60}))
sc = SupplyChain(web3)
print(sc.CheckBalance(), 'Ether')
print(sc.SendEther('0x487f3fb0eebf1a9894914c8b5286f9b761f7fa35', 10))