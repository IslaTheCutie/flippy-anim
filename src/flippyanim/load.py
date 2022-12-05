#from .compress import PyJsHoisted_decompressFromUint8Array_

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
	
	from os.path import dirname
	with open(dirname(__file__)+'/decompress.js', 'r') as f:
		compressJs = f.read()
	
	from js2py import EvalJs
	js = EvalJs({})
	js.execute(compressJs)
	
	import json
	from js2py.base import PyJsUint8Array
	out = []
	while pos < len(data):
		l = int.from_bytes(data[pos:pos+4], byteorder='little')
		pos += 4
		
		out.append(json.loads(
			js.decompressFromUint8Array(
				PyJsUint8Array(data[pos:pos+l])
			)
		))
		pos += l
	return out
