import base64
import os
from Crypto.Cipher import AES

def pad(string):
	pad = '['
	return string + (32 - len(string) % 32) * pad

def r_k():
	f = open('apple', 'r')
	f.readline()
	k = f.read(32)
	iv = f.read(16)
	return AES.new(k, AES.MODE_CBC, iv)

def encode(string):
	return base64.b64encode(r_k().encrypt(pad(string)))

def decode(string):
	return r_k().decrypt(base64.b64decode(string)).rstrip('[')


if __name__ == '__main__':
	
	string = "hello"
	e = encode(string)
	d = decode(e)
	print e

	print d
