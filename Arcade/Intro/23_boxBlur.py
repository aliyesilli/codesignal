def boxBlur(image):
	a = []
	a1 = []
	a2 = []
	if len(image[0]) < 3: a = []
	for j in range(0,len(image)-2):
		for i in range(0,len(image[0])-2):
			k = 0
			a1 = [
			[image[0+j][0+i],image[0+j][1+i],image[0+j][2+i]],
			[image[1+j][0+i],image[1+j][1+i],image[1+j][2+i]],
			[image[2+j][0+i],image[2+j][1+i],image[2+j][2+i]]]
			k = sum([sum(l) for l in a1])/9
			a2.append(k)
		a.append(a2)
		a2 = []
	return a

