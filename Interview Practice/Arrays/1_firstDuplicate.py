def firstDuplicate(a):
	x = set()
	for i in a: 
		if i in x: return i 
		x.add(i)
	if len(x) == len(a): return -1	
	return;