import pandas as pd

def palindromeRearranging(inputString):
	b = list(map(lambda x: (x,1), inputString))
	c = pd.DataFrame(data=b, columns=['c1', 'c2']).groupby('c1',as_index = False).agg({'c2':'sum'})
	d = c[(c.c2%2 == 1)]
	if len(d) < 2: return True
	else: return False;
