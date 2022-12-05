
def _charFromCode(x) -> str:
	return x.to_bytes(2, 'little').decode('UTF-16')

def decompress(t):
	if t is None:
		return ''
	
	if len(t) & 1:
		raise ValueError('Uneven number of bytes in compressed data')
	
	n = [None] * (len(t) // 2)
	for r in range(len(n)):
		n[r] = 256 * t[2 * r] + t[2 * r + 1]
	
	#a = []
	#for t in n:
		#a.append(_strFromCharCode(t))
	
	return _decompress(len(n), 32768, n)

def _decompress(t, n, r):
	u = c = None
	o = [0,1,2]
	m = []
	p = d = 4
	h = 3
	y = [0]
	val = r[0]
	position = n
	index = 1
	a = 0
	l = 2**2
	s = 1
	while s != l:
		u = val & position
		position >>= 1
		if position == 0:
			position = n
			val = r[index]
			index += 1
		if u > 0:
			a |= s
		s <<= 1
	
	if a == 0:
			a = 0
			l = 2**8
			s = 1
			while s != l:
				u = val & position
				position >>= 1
				if position == 0:
					position = n
					val = r[index]
					index += 1
				if u > 0:
					a |= s
				s <<= 1
			c = a
	elif a == 1:
			a = 0
			l = 2**16
			s = 1
			while s != l:
				u = val & position
				position >>= 1
				if position == 0:
					position = n
					val = r[index]
					index += 1
				if u > 0:
					a |= s
				s <<= 1
			c = a
	elif a == 2:
			return ''
	
	f = [0,0,0,c]
	i = [c]
	print(f'I: {i}')
	m.append(_charFromCode(c))
	while True:
		if index > t:
			return ''
		
		a = 0
		l = 2**h
		s = 1
		while s != l:
			u = val & position
			position >>= 1
			if position == 0:
				position = n
				val = r[index]
			if u > 0:
				a |= s
			s <<= 1
		
		c = a
		if c == 0:
			#a = 0
			l = 2**8
			s = 1
			while s != l:
				u = val & position
				position >>= 1
				if position == 0:
					position = n
					val = r[index]
				if u > 0:
					a |= s
				s <<= 1
			while len(f) <= d:
				f.append(0)
			f[d] = a
			d += 1
			c = d - 1
			p -= 1
		elif c == 1:
			a = 0
			l = 2**16
			s = 1
			while s != l:
				u = val & position
				position >>= 1
				if position == 0:
					position = n
					val = r[index]
				if u > 0:
					a |= s
				s <<= 1
			while len(f) <= d:
				f.append(0)
			f[d] = a
			d += 1
			c = d - 1
			p -= 1
		elif c == 2:
			return ''.join(m)
		
		madeIt = False
		if p == 0:
			p = 2**h
			h += 1
			if f[c]:
				madeIt = True
				y = [f[c]]
		if not madeIt:
			if c != d:
				print(f'rip... madeIt={madeIt}')
				return m;
			y = i + [i[0]]
		
		m.append(y)
		while len(f) <= d:
			f.append(0)
		f[d] = i + [y[0]]
		d += 1
		i = y
		p -= 1
		if p == 0:
			p = 2**h
			h += 1
	
