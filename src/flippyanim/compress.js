var e = String.fromCharCode;

function compressToUint8Array(e){
	for(var t = compress(e), n = new Uint8Array(t.length * 2), r = 0, o = t.length; r < o; r++){
		var a = t.charCodeAt(r);
		n[2 * r] = a >>> 8,
		n[2 * r + 1] = a % 256
	}
	return n
}

function compress(t){
	return _compress(
		t,
		16,
		function(t){
			return e(t)
		}
	)
}

function _compress(e, t, n){
	if(null == e) return '';
	var r, o, i, a = {}, u = {}, l = '', s = '', c = '', f = 2, p = 3, d = 2, h = [], y = 0, m = 0;
	for(i = 0; i < e.length; i += 1) if(l = e.charAt(i), Object.prototype.hasOwnProperty.call(a, l) || (a[l] = p++, u[l] = !0), s = c + l, Object.prototype.hasOwnProperty.call(a, s)) c = s;
		else{
		if(Object.prototype.hasOwnProperty.call(u, c)){
			if(c.charCodeAt(0) < 256){
				for(r = 0; r < d; r++) y <<= 1,
				m == t - 1 ? (m = 0, h.push(n(y)), y = 0) : m++;
				for(o = c.charCodeAt(0), r = 0; r < 8; r++) y = y << 1 | 1 & o,
				m == t - 1 ? (m = 0, h.push(n(y)), y = 0) : m++,
				o >>= 1
			}else{
				for(o = 1, r = 0; r < d; r++) y = y << 1 | o,
				m == t - 1 ? (m = 0, h.push(n(y)), y = 0) : m++,
				o = 0;
				for(o = c.charCodeAt(0), r = 0; r < 16; r++) y = y << 1 | 1 & o,
				m == t - 1 ? (m = 0, h.push(n(y)), y = 0) : m++,
				o >>= 1
			}
			--f == 0 &&(f = Math.pow(2, d), d++),
			delete u[c]
		} else for(o = a[c], r = 0; r < d; r++) y = y << 1 | 1 & o,
		m == t - 1 ?(m = 0, h.push(n(y)), y = 0) : m++,
		o >>= 1;
		--f == 0 && (f = Math.pow(2, d), d++),
		a[s] = p++,
		c = String(l)
	}
	if('' !== c){
		if(Object.prototype.hasOwnProperty.call(u, c)){
			if(c.charCodeAt(0) < 256){
				for(r = 0; r < d; r++) y <<= 1,
				m == t - 1 ?(m = 0, h.push(n(y)), y = 0) : m++;
				for(o = c.charCodeAt(0), r = 0; r < 8; r++) y = y << 1 | 1 & o,
				m == t - 1 ?(m = 0, h.push(n(y)), y = 0) : m++,
				o >>= 1
			}else{
				for(o = 1, r = 0; r < d; r++) y = y << 1 | o,
				m == t - 1 ?(m = 0, h.push(n(y)), y = 0) : m++,
				o = 0;
				for(o = c.charCodeAt(0), r = 0; r < 16; r++) y = y << 1 | 1 & o,
				m == t - 1 ?(m = 0, h.push(n(y)), y = 0) : m++,
				o >>= 1
			}
			--f == 0 &&(f = Math.pow(2, d), d++),
			delete u[c]
		} else for(o = a[c], r = 0; r < d; r++) y = y << 1 | 1 & o,
		m == t - 1 ?(m = 0, h.push(n(y)), y = 0) : m++,
		o >>= 1;
		--f == 0 &&(f = Math.pow(2, d), d++)
	}
	for(o = 2, r = 0; r < d; r++) y = y << 1 | 1 & o,
	m == t - 1 ?(m = 0, h.push(n(y)), y = 0) : m++,
	o >>= 1;
	for(;;){
		if(y <<= 1, m == t - 1){
			h.push(n(y));
			break
		}
		m++
	}
	return h.join('')
}
