# ABI.py

RegistrarContract_ADDR = '0x0607440eF946aA0A1a5e7bd2c8570dfAAeC659a0'

RegistrarContract_ABI = [ { "constant": False, "inputs": [ { "name": "id_number", "type": "uint64" }, { "name": "accAddr", "type": "address" } ], "name": "NewRecord", "outputs": [], "payable": False, "stateMutability": "nonpayable", "type": "function", "signature": "0x1580a08a" }, { "constant": True, "inputs": [ { "name": "id_number", "type": "uint64" } ], "name": "GetInfo", "outputs": [ { "name": "", "type": "address", "value": "0x0000000000000000000000000000000000000000" }, { "name": "", "type": "address", "value": "0x0000000000000000000000000000000000000000" } ], "payable": False, "stateMutability": "view", "type": "function", "signature": "0xc7979314" }, { "inputs": [], "payable": False, "stateMutability": "nonpayable", "type": "constructor", "signature": "constructor" } ]
SummaryContract_ABI = []
SupplyContract_ABI = []