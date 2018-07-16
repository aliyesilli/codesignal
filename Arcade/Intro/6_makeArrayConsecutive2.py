def makeArrayConsecutive2(statues):
	a = range(min(statues),max(statues)+1)
	x = set()
	for i in a:
		if i not in statues: x.add(i)
	return len(x);