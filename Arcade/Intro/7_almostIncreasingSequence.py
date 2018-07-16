def almostIncreasingSequence(sequence):

	def isIncreasingSequence(sequence):
		for i in range(1,len(sequence)):
			if sequence[i-1] >= sequence[i]: return False
		else: pass
		return True


	for x in range(0,len(sequence)):
		b = sequence[:x]+sequence[x+1:]
		if isIncreasingSequence(b)== True: return True
	else: pass
	return False;
