var e = String.fromCharCode; 

function decompressFromUint8Array(t){
	if(null == t) return decompress(t);
	for(var n = new Array(t.length / 2), r = 0, o = n.length; r < o; r++)
		n[r] = 256 * t[2 * r] + t[2 * r + 1];
	var a = [];
	return n.forEach(function(t){
		a.push(e(t))
	}),
	decompress(a.join(''))
}

function decompress(e){
	return null == e ? '' : '' == e ? null : _decompress(e.length, 32768, function(t){
		return e.charCodeAt(t)
	})
}

function _decompress(t, n, r){
	var o, i, a, u, l, s, c, p = 4, d = 4, h = 3, y = '', f = [], m = [],
	v = {
		val: r(0),
		position: n,
		index: 1
	};
	for(o = 0; o < 3; o += 1) f[o] = o;
	for(a = 0, l = Math.pow(2, 2), s = 1; s != l; )
		u = v.val & v.position,
		v.position >>= 1,
		0 == v.position &&(v.position = n, v.val = r(v.index++)),
		a |=(u > 0 ? 1 : 0) * s,
		s <<= 1;
	switch(a){
		case 0:
			for(a = 0, l = Math.pow(2, 8), s = 1; s != l; )
				u = v.val & v.position,
				v.position >>= 1,
				0 == v.position &&(v.position = n, v.val = r(v.index++)),
				a |=(u > 0 ? 1 : 0) * s,
				s <<= 1;
			c = e(a);
			break;
		case 1:
			for(a = 0, l = Math.pow(2, 16), s = 1; s != l; )
				u = v.val & v.position,
				v.position >>= 1,
				0 == v.position &&(v.position = n, v.val = r(v.index++)),
				a |=(u > 0 ? 1 : 0) * s,
				s <<= 1;
			c = e(a);
			break;
		case 2:
			return ''
	}
	for(f[3] = c, i = c, m.push(c); ; ){
		if(v.index > t) return '';
		for(a = 0, l = Math.pow(2, h), s = 1; s != l; )
			u = v.val & v.position,
			v.position >>= 1,
			0 == v.position &&(v.position = n, v.val = r(v.index++)),
			a |=(u > 0 ? 1 : 0) * s,
			s <<= 1;
		switch(c = a){
			case 0:
				for(a = 0, l = Math.pow(2, 8), s = 1; s != l; )
					u = v.val & v.position,
					v.position >>= 1,
					0 == v.position &&(v.position = n, v.val = r(v.index++)),
					a |=(u > 0 ? 1 : 0) * s,
					s <<= 1;
				f[d++] = e(a),
				c = d - 1,
				p--;
				break;
			case 1:
				for(a = 0, l = Math.pow(2, 16), s = 1; s != l; )
					u = v.val & v.position,
					v.position >>= 1,
					0 == v.position &&(v.position = n, v.val = r(v.index++)),
					a |=(u > 0 ? 1 : 0) * s,
					s <<= 1;
				f[d++] = e(a),
				c = d - 1,
				p--;
				break;
			case 2:
				return m.join('')
		}
		if(0 == p &&(p = Math.pow(2, h), h++), f[c]){
			y = f[c];
		}else{
			if(c !== d) return null;
			y = i + i.charAt(0)
		}
		m.push(y),
		f[d++] = i + y.charAt(0),
		i = y,
		0 == --p &&(p = Math.pow(2, h), h++)
	}
}
