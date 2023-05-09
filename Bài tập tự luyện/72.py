def dem_tu(s):
	s = s.split()
	tu_thoa_man = 0
	for i in s:
		chu = False
		so = False
		for j in i:
			if j.isalpha():
				chu = True
			elif j.isdigit():
				so = True
		if chu == True and so == True:
			tu_thoa_man += 1

	return tu_thoa_man

s = input("Mời nhập chuỗi: ")

print(dem_tu(s))