def adjacentElementsProduct(inputArray):
	if len(inputArray) == 0: return 0
	if len(inputArray) == 1: inputArray[0]	
	b = inputArray[0]*inputArray[1]
	for i in range(0,len(inputArray)-1):
		if inputArray[i]*inputArray[i+1] > b: b=inputArray[i]*inputArray[i+1]
	return b;