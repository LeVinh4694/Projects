# Supplychain.py

import sys, os
# Import get password library
import getpass
# Import library for Web3 Ethereum
from web3 import Web3
# Import contract ABI
from ABI import *

__author__ = 'Le Quang Vinh'
__license__ = 'GPL'
__version__ = '1.0.0'

class SupplyChain:
	def __init__(self, obj):
		self.obj = obj
		self.RegistrarContract = self.obj.eth.contract(address=RegistrarContract_ADDR,
														abi=RegistrarContract_ABI)
		
	def CreateContractInstance(self, address, abi):
		return self.obj.eth.contract(address=address, abi=abi)

	def CheckBalance(self):
		return self.obj.fromWei(self.obj.eth.getBalance(self.obj.eth.coinbase), 'ether')

	def UnlockAccount(self):
		self.pwd = getpass.getpass(prompt="Insert password: ")
		ret = self.obj.personal.unlockAccount(self.obj.eth.coinbase, self.pwd)
		return ret

	def SendEther(self, receiver, amount):
		# Return error if receiver address or ether amount is incorrect
		if not self.obj.isAddress(receiver):
			return 'Invalid account address'
		if not type(amount) == int:
			return 'Invalid Ether amount'
		# Unlock account
		if not self.UnlockAccount():
			return 'Password is incorrect'
		try:
			# Send transaction
			self.tx_hash = self.obj.eth.sendTransaction({'from':self.obj.eth.coinbase, 
										'to':self.obj.toChecksumAddress(receiver), 
										'value': self.obj.toWei(amount, 'ether')})
			return True
		except:
			print(sys.exc_info()[1])
			return False
			
	def Registrar_NewRecord(self, id_number, accAddr):
		# Return error if ID number or account address is invalid
		if not type(id_number) == int:
			return 'Invalid ID number'
		if not self.obj.isAddress(accAddr):
			return 'Invalid account address'
		# Unlock account (return incorrect password if failed)
		if not self.UnlockAccount():
			return 'Password is incorrect'

		try:
			# Set base account for transaction
			self.obj.eth.defaultAccount = self.obj.toChecksumAddress(self.obj.eth.coinbase)
			# Send transaction
			self.tx_hash = self.RegistrarContract.functions.NewRecord(id_number,
										self.obj.toChecksumAddress(accAddr)).transact()
			return True
		except:
			print(sys.exc_info()[1])
			return False

	def Registrar_GetInfo(self, id_number):
		# Return error if ID number is invalid
		if not type(id_number) == int:
			return 'Invalid ID number'
		try:
			return self.RegistrarContract.functions.GetInfo(id_number).call()
		except:
			print(sys.exc_info()[1])
			return False
			
web3 = Web3(Web3.HTTPProvider('http://localhost:8080', request_kwargs={'timeout': 60}))
sc = SupplyChain(web3)