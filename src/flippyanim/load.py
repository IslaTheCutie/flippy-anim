from typing import Optional

HEAD = 'flipanim.com project'
HEAD_VER = '02'

def loadRaw(path: str, start: int=0, end: Optional[int]=None) -> list[Optional[str]]:
	"""Decompress and load a FlipAnim project without parsing its JSON strings.
	
	path - a .flipanim project file
	start - which compressed data block to start from (default 0)
	end - which compressed data block to stop at (default None)
	"""
	if not end is None:
		if start > end:
			raise ValueError('`start` is after `end`')
	
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
	
	from js2py.base import PyJsUint8Array
	out = []
	blockNum = 0
	while pos < len(data):
		l = int.from_bytes(data[pos:pos+4], byteorder='little')
		pos += 4
		
		if blockNum >= start:
			out.append(
				js.decompressFromUint8Array(
					PyJsUint8Array(data[pos:pos+l])
				)
			)
		blockNum += 1
		if (not end is None) and blockNum >= end:
			break
		
		pos += l
	return out

def load(path: str, start: int=0, end: Optional[int]=None) -> list[Optional[dict]]:
	"""Decompress and load a FlipAnim project.
	
	path - a .flipanim project file
	start - which compressed data block to start from (default 0)
	end - which compressed data block to stop at (default None)
	"""
	data = loadRaw(path, start, end)
	import json
	return [json.loads(item) for item in data]
