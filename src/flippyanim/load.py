from .decompress import *

HEAD = 'flipanim.com project'
HEAD_VER = '02'

def load(path: str): #will eventually return a list of FlipAnim layer JSON objects
	with open(path, 'rb') as f:
		data = f.read()
	
	pos = 0
	l = len(HEAD)
	if data[pos:pos+l].decode() != HEAD:
		raise ValueError('Bad header')
	
	pos += l
	l = len(HEAD_VER)
	if data[pos:pos+l].decode() != HEAD_VER:
		raise ValueError('Unsupported header version')
	
	pos += l
	
	out = []
	while pos < len(data):
		l = int.from_bytes(data[pos:pos+4], byteorder='little')
		pos += 4
		
		out.append(decompress(data[pos:pos+l]))
		
		pos += l
	return out

