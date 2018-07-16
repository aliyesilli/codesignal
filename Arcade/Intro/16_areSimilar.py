def areSimilar(a, b):
	d = 0
	def checkelements(a, b):
		c = b[:]
		for i in range(len(a)):
			if a[i] not in c:
				return False
				break
			else:
				c.remove(a[i])
		return True
	if checkelements(a, b) == True:
		for i in range(len(b)):
			if a[i] != b[i]:
				d += 1
			else:
				pass
	if d > 2: return False
	else: return checkelements(a, b);