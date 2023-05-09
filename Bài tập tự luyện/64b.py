def noi_chuoi(s):
	dau_noi = "-"
	s = s.split()
	s = dau_noi.join(s)

	return s

s = input('Mời nhập chuỗi: ')

print(noi_chuoi(s))
