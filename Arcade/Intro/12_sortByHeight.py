def sortByHeight(a):
	b = []
	c = [x for x in a if x != -1]
	c.sort()
	for i in range(len(a)):
		if a[i] == -1: b.append(-1)
		else:
			b.append(c[0])
			del c[0]
	return b;