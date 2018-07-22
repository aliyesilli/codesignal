def alphabeticShift(inputString):
    a = 'abcdefghijklmnopqrstuvwxyz'
    b = list(inputString)
    c = []
    d= [['z','a']]
    for i in range(len(b)):
    	if b[i] == 'z':
    		pass
    	elif b[i] not in c:
    		c.append(b[i])
    		d += [[a[a.find(b[i])],a[a.find(b[i])+1]]]
    for i in range(len(b)):
    	for j in range(len(d)):
    		if b[i] == d[j][0]:
    			b[i] = d[j][1]
    			break
    return ''.join(b)
