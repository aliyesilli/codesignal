def centuryFromYear(year):
	a = str(year)
	if a.replace(a[-2:len(a)],'') == '': return 1
	return int(a.replace(a[-2:len(a)],'')) if a[-1:len(a)] == '0' else int(a.replace(a[-2:len(a)],''))+1;