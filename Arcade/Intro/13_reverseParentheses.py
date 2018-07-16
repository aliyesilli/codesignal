def reverseParentheses(s):
	a1 = []
	a2 = []
	a3 = []
	c = (s + '.')[:-1]
	#Find first index of Parentheses -- a1
	for i in range(len(s)):
		if s[i] == '(': 
			a1.append(i)
	#Find second index of Parentheses -- a2
	for x in a1:
		b1 = 0
		b2 = 0
		c1 = []
		k = s[x+1:]
		for i in range(len(k)):
			if k[i] == '(': b1 = b1+1
			if k[i]	== ')': b2 = b2+1
			if b2 > b1: 
				c1.append(i)
				break
		a2.append(c1[0]+x+1)
	#Create double dimensional array with first and second indexes of each Parentheses and sort it based on second column -- a3
	for i in range(len(a1)):
		a3.append([a1[i],a2[i]+1])
	a3 = sorted(a3,key=lambda x: (x[1]))
	#reverse string of each Parentheses
	for i in range(len(a3)):
		d = c[a3[i][0]:a3[i][1]]
		c = c.replace(d,d[::-1])
	return c.replace('(','').replace(')','');