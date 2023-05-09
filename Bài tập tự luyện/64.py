def noi_chuoi(s):
	s = s.strip()
	while " " in s:
		s = s.replace(" ", "-")
	return s
s = input("Mời nhập chuỗi: ")

print(noi_chuoi(s))