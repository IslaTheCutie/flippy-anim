import svg
import json

_SVG_OP = {
	'deou': 'out',
	'deov': 'over',
	'soat': 'atop',
}
_SVG_BLEND = {
	'dark': 'darken',
	'ovrl': 'overlay',
}

def encodeSVG(layers: list[dict]) -> svg.SVG:
	elem = [
		svg.Filter(
			id=code,
			elements=[svg.FeComposite(operator=op, in2='SourceGraphic')]
		) for code, op in _SVG_OP.items()
	] + [
		svg.Filter(
			id=code,
			elements=[svg.FeBlend(mode=mode, in2='strokeFill')]
		) for code, mode in _SVG_BLEND.items()
	]
	
	for layer in layers:
		elem += encodeSVGLayer(layer)
	return svg.SVG(
		width = 470,
		height = 470,
		elements = elem
	)


def encodeSVGLayer(layer: dict) -> list[svg.Element]:
	elem = []
	if not 'image' in layer:
		return elem
	img = layer['image']
	
	data = img['data']
	if 'curr' in img:
		data[:img['curr']]
	
	for item in data:
		size = item['size'] if ('size' in item) else None
		
		if item['type'].startswith('d'):
			x = item['x']
			y = item['y']
			colour, alpha = _readCol(item['color'])
			compOp = item['comp'] if 'comp' in item else None
			
			nextElem = None #next element to add to the list of elements
			if item['type'] == 'dl':
				stroke, fill = ('transparent', colour) if ('fill' in item and item['fill']) else (colour, 'none')
				
				path = [svg.M(x, y)]
				pointIter = iter(item['points'])
				for pos in pointIter:
					path.append(svg.l(pos, next(pointIter)))
				nextElem = svg.Path(d=path, stroke=stroke, opacity=alpha, fill=fill, stroke_width=size, stroke_linejoin='round', stroke_linecap='round')
				
			elif item['type'] == 'dc':
				stroke, fill = (colour, 'none')
				
				lerpT = item['t'] if 't' in item else 0.5
				path = [svg.M(x, y)]
				pointIter = iter(item['points'])
				for pos in pointIter:
					nextX = x + pos;
					nextY = y + next(pointIter)
					lerpedX = lerp(x, nextX, lerpT)
					lerpedY = lerp(y, nextY, lerpT)
					path.append(svg.Q(x, y, lerpedX, lerpedY))
					x = nextX
					y = nextY
				path.append(svg.L(nextX, nextY))
				nextElem = svg.Path(d=path, stroke=stroke, opacity=alpha, fill=fill, stroke_width=size, stroke_linejoin='round', stroke_linecap='round')
				
			else:
				print(item['type'])
			
			if not nextElem is None:
				if not compOp is None and compOp:
					nextElem.filter = f'url(#{compOp})'
					print(nextElem.filter)
				elem.append(nextElem)
	
	return elem

def _readCol(colour: str) -> (str, float):
	if len(colour) == 7:
		return colour, 1.0
	else:
		return colour[0:7], (int(colour[7:9], 16))/0xFF

def lerp(a, b, c):
	return a+((b-a)*c)
