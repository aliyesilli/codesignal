def isLucky(n):
	a = str(n)[:len(str(n))/2]
	b = str(n)[len(str(n))/2:]
	asum = 0
	bsum = 0
	for i in range(len(a)): asum = asum+int(a[i])
	for j in range(len(b)): bsum = bsum+int(b[j])
	if asum == bsum: return True
	else: return False;

