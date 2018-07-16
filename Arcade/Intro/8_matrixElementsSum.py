def matrixElementsSum(matrix):
	b = [row[:] for row in matrix]
	a = 0
	for i in range(len(b)):
		for j in range(len(b[i])):
			if i == 0: a = a+b[i][j]
			elif b[i-1][j] == 0: b[i][j] = 0
			else: a = a+b[i][j]
	return a;