def commonCharacterCount(s1, s2):
	s3 = (s2 + '.')[:-1]
	a = 0
	for i in range(len(s1)):
		if s1[i] in s3: 
			s3 = s3[:s3.find(s1[i])]+s3[s3.find(s1[i])+1:]
			a = a+1
	return a;