import pandas as pd

def firstNotRepeatingCharacter(s):
	b = list(map(lambda x: (x,1), s))
	c = pd.DataFrame(data=b, columns=['c1', 'c2']).groupby('c1',as_index = False).agg({'c2':'sum'})
	d = c[(c.c2 == 1)]
	if len(d['c1'].values.tolist()) == 0: return '_'	
	for i in list(s): 
		if i in d['c1'].values.tolist(): return i 
	return;

