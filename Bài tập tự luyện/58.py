def chuoi_ket_qua(s):
	if s == '':
		s = "ing"
	elif s[-3:-1] + s[-1] == 'ing':
		s = s[0:len(s)-3] + 'ly'
	elif s[-3:0] + s[-1] != 'ing':
		s = s + 'ing'
	return s

s = input('Mời nhập chuỗi: ')

print(chuoi_ket_qua(s))