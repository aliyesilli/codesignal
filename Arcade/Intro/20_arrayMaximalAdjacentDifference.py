def arrayMaximalAdjacentDifference(inputArray):
	x = set()
	for i in range(1,len(inputArray)):
		a = abs(inputArray[i]-inputArray[i-1])
		if a not in x: x.add(a)
	return max(x)