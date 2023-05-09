def xoa_khoang_trang_thua(s):
	s = s.strip()
	while "  " in s:
		s = s.replace("  ", " ")
	return s

s = input('Mời nhập chuỗi: ')


print(xoa_khoang_trang_thua(s))