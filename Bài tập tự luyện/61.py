def bien_doi_chuoi(s):
	if len(s) == 0:
		s = ""
	elif s[0] == '*' and s[-1] == '*':
		s = s.title()
	elif s[0] == '-' and s[-1] == '-':
		s = s.swapcase()
	else:
		s = s.swapcase()
	
	return s

s = input('Mời nhập chuỗi: ')

print(bien_doi_chuoi(s))