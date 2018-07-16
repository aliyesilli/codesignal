def allLongestStrings(inputArray):
	a = []
	b = 0
	for i in range(len(inputArray)): 
		if len(str(inputArray[i])) > b: 
			b = len(str(inputArray[i]))
	for j in range(len(inputArray)): 
		if len(str(inputArray[j])) == b: 
			a.append(inputArray[j])
	return a;
