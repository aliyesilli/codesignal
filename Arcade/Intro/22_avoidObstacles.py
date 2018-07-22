def avoidObstacles(inputArray):
	for i in range(1, max(inputArray)):
        a = any([x for x in inputArray if not x%i])
        if a == False: return i
	return max(inputArray) + 1