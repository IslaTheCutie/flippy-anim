
#def _fromCharCode(x) -> str:
	#return x.to_bytes(2, 'little').decode('UTF-16', errors='ignore')

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
		#a.append(_fromCharCode(t))
	
	_decompress(len(n), 32768, n)

def _decompress(t, n, r):
	i = u = c = None
	o = [0,1,2]
	m = f = []
	p = d = 4
	h = 3
	y = ''
	val = r[0]
	position = n
	index = 1
	a = 0
	l = 2**2
	s = 1
	while s != l:
		u = v.val & v.position,
		v.position >>= 1,
		0 == v.position && (v.position = n, v.val = r[v.index++]),
		a |= (u > 0 ? 1 : 0) * s,
		s <<= 1;
	#switch (a) {
		#case 0:
			#for (a = 0, l = Math.pow(2, 8), s = 1; s != l; ) u = v.val & v.position,
			#v.position >>= 1,
			#0 == v.position && (v.position = n, v.val = r[v.index++]),
			#a |= (u > 0 ? 1 : 0) * s,
			#s <<= 1;
			#c = e(a);
			#break;
		#case 1:
			#for (a = 0, l = Math.pow(2, 16), s = 1; s != l; ) u = v.val & v.position,
			#v.position >>= 1,
			#0 == v.position && (v.position = n, v.val = r[v.index++]),
			#a |= (u > 0 ? 1 : 0) * s,
			#s <<= 1;
			#c = e(a);
			#break;
		#case 2:
			#return ''
	#}
	#for (f[3] = c, i = c, m.push(c); ; ) {
		#if (v.index > t) return '';
		#for (a = 0, l = Math.pow(2, h), s = 1; s != l; ) u = v.val & v.position,
		#v.position >>= 1,
		#0 == v.position && (v.position = n, v.val = r[v.index++]),
		#a |= (u > 0 ? 1 : 0) * s,
		#s <<= 1;
		#switch (c = a) {
			#case 0:
				#for (a = 0, l = Math.pow(2, 8), s = 1; s != l; ) u = v.val & v.position,
				#v.position >>= 1,
				#0 == v.position && (v.position = n, v.val = r[v.index++]),
				#a |= (u > 0 ? 1 : 0) * s,
				#s <<= 1;
				#f[d++] = e(a),
				#c = d - 1,
				#p--;
				#break;
			#case 1:
				#for (a = 0, l = Math.pow(2, 16), s = 1; s != l; ) u = v.val & v.position,
				#v.position >>= 1,
				#0 == v.position && (v.position = n, v.val = r[v.index++]),
				#a |= (u > 0 ? 1 : 0) * s,
				#s <<= 1;
				#f[d++] = e(a),
				#c = d - 1,
				#p--;
				#break;
			#case 2:
				#return m.join('')
		#}
		#if (0 == p && (p = Math.pow(2, h), h++), f[c]) y = f[c];
			#else {
			#if (c !== d) return null;
			#y = i + i.charAt(0)
		#}
		#m.push(y),
		#f[d++] = i + y.charAt(0),
		#i = y,
		#0 == --p && (p = Math.pow(2, h), h++)
	#}
