def shapeArea(n):
	b = (n*2)-1
	for i in range(b+1):
		if i <= 2: b=b+0
		elif i%2 == 0: b=b+0
		else: b=b+(2*((n*2)-i))
	return b;