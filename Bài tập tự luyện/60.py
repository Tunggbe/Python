def bien_doi_chuoi(s):
	if len(s) == 0:
		s = ""
	elif s[0].islower() == False and s[0].isupper() == False:
		s = s
	elif s[0].islower() == False:
		s = s.lower()
	elif s[0].islower() == True:
		s = s.upper()

	return s


s = input('Vui lòng nhập chuỗi: ')

print(bien_doi_chuoi(s))