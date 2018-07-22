def isIPv4Address(inputString):
	if inputString.count('.') != 3: return False
	a = inputString.split('.')
	for i in range(len(a)):
		if a[i].isdigit() == False: return False
		if len(a[i]) == 0: return False
		if int(a[i]) < 0 or int(a[i]) > 255: return False
	return True
