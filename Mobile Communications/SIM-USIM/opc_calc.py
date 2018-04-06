#!/usr/bin/env python

"""
Simple script to calculate OPC from Ki and OP.

3GPP TS 35.206 was used to code this script.
"""
__author__ = "mgp25"
__github__ = "https://github.com/mgp25"

from Crypto.Cipher import AES
from Crypto.Util.strxor import strxor
import sys, getopt, binascii


def main(argv):
   try:
	   opts, args = getopt.getopt(argv,"k:o:h",["ki=","op=", 'help'])
   except getopt.GetoptError:
	   print_usage()
	   sys.exit(2)

   ki = None
   op = None
   for opt, arg in opts:
	   if opt in ('-h', '--help'):
		   print_usage()
		   sys.exit()
	   elif opt in ("-k", "--ki"):
		   ki = arg
	   elif opt in ("-o", "--op"):
		   op = arg
	   else:
		   print_usage()
		   sys.exit()

   if ki is not None and op is not None:
       print('\nOPc value: '+derive_milenage_opc(ki, op).decode('utf-8'))
   else:
       print_usage()

def derive_milenage_opc(ki_hex, op_hex):
	"""
	Run the milenage algorithm to calculate OPC from Ki and OP.

    Following 3GPP TS 35.206
	"""
	# We pass in hex string and now need to work on bytes
	aes = AES.new(h2b(ki_hex), AES.MODE_CBC, h2b('00000000000000000000000000000000'))
	opc_bytes = aes.encrypt(h2b(op_hex))
	return b2h(strxor(opc_bytes, h2b(op_hex)))

def h2b(s):
	return bytes(bytearray.fromhex(s))

def b2h(s):
	return binascii.hexlify(s)

def print_usage():
	print('Usage:')
	print('	opc_calc.py -k <Ki> -o <OP>')
	print('	opc_calc.py --ki <Ki> --op <OP>')

if __name__ == "__main__":
   main(sys.argv[1:])
