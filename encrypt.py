import base64
import os
import sys
from Crypto.Cipher import AES

def pad(string):
	pad = '['
	return string + (32 - len(string) % 32) * pad

def r_k():
	f = open('/etc/nginx/apple', 'r')
	k = f.read(32)
	iv = f.read(16)
	return AES.new(k, AES.MODE_CBC, iv)

def encode(in_file_name, out_file_name):
	bs = AES.block_size
	in_file = open(in_file_name, 'rb')
	out_file = open(out_file_name, 'wb')
	finished = False
	cipher = r_k()
	while not finished:
		chunk = in_file.read(1024*bs)
		if len(chunk) == 0 or len(chunk) % bs != 0:
			p_l = (bs - len(chunk) % bs) or bs
			chunk+=p_l*chr(p_l)
			finished = True
		out_file.write(cipher.encrypt(chunk))


def decode(in_file_name, out_file_name):
	bs = AES.block_size
	in_file = open(in_file_name, 'rb')
	out_file = open(out_file_name, 'wb')
	finished = False
	cipher = r_k()
	next_chunk = ''
	while not finished:
		chunk, next_chunk = next_chunk, cipher.decrypt(in_file.read(1024*bs))
		if len(next_chunk) == 0:
			p_l = ord(chunk[-1])
			chunk = chunk[:-p_l]
			finished = True
		out_file.write(chunk)


if __name__ == '__main__':
	decode(sys.argv[1], sys.argv[2])
