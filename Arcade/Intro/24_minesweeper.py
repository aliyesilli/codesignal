def minesweeper(matrix):
	a1 = []
	a2 = []
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			a = 0
			if i == 0:
				if j == 0:
					a = matrix[i][j+1]+matrix[i+1][j]+matrix[i+1][j+1]
				elif j == len(matrix[i])-1:
					a = matrix[i][j-1]+matrix[i+1][j-1]+matrix[i+1][j]
				else:
					a = matrix[i][j-1]+matrix[i][j+1]+matrix[i+1][j-1]+matrix[i+1][j]+matrix[i+1][j+1]
			elif i == len(matrix)-1:
				if j == 0:
					a = matrix[i-1][j]+matrix[i-1][j+1]+matrix[i][j+1]
				elif j == len(matrix[i])-1:
					a = matrix[i-1][j-1]+matrix[i-1][j]+matrix[i][j-1]
				else:
					a = matrix[i-1][j-1]+matrix[i-1][j]+matrix[i-1][j+1]+matrix[i][j-1]+matrix[i][j+1]
			else:
				if j == 0:
					a = matrix[i-1][j]+matrix[i-1][j+1]+matrix[i][j+1]+matrix[i+1][j]+matrix[i+1][j+1]
				elif j == len(matrix[i])-1:
					a = matrix[i-1][j-1]+matrix[i-1][j]+matrix[i][j-1]+matrix[i+1][j-1]+matrix[i+1][j]
				else:	
					a = matrix[i-1][j-1]+matrix[i-1][j]+matrix[i-1][j+1]+matrix[i][j-1]+matrix[i][j+1]+matrix[i+1][j-1]+matrix[i+1][j]+matrix[i+1][j+1]
			a1.append(a)
		a2.append(a1)
		a1 = []
	return a2