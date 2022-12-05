import svg
import json

def readCol(colour):
	if len(colour) == 7:
		return colour, 1.0
	else:
		return colour[0:7], norm(colour[7:9])

def lerp(a, b, c):
	return a+((b-a)*c)

def norm(a):
	return (int(a, 16))/0xFF

def encodeSVG(layers):
	e = []
	for layer in layers:
		e += encodeSVGLayer(layer)
	return svg.SVG(
		width = 470,
		height = 470,
		elements = e
	)

def encodeSVGLayer(layer):
	e = []
	if not 'image' in layer:
		return e
	
	for item in layer['image']['data']:
		size = item['size'] if ('size' in item) else None
		
		if item['type'] == 'dl':
			x = item['x']
			y = item['y']
			colour, alpha = readCol(item['color'])
			
			stroke, fill = ('transparent', colour) if ('fill' in item and item['fill']) else (colour, 'none')
			path = [svg.M(x, y)]
			pointIter = iter(item['points'])
			for pos in pointIter:
				path.append(svg.l(pos, next(pointIter)))
			e.append(svg.Path(d=path, stroke=stroke, opacity=alpha, fill=fill, stroke_width=size, stroke_linejoin='round', stroke_linecap='round'))
		elif item['type'] == 'dc':
			x = item['x']
			y = item['y']
			colour, alpha = readCol(item['color'])
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
			e.append(svg.Path(d=path, stroke=stroke, opacity=alpha, fill=fill, stroke_width=size, stroke_linejoin='round', stroke_linecap='round'))
		else:
			print(item['type'])
		
	
	return e
