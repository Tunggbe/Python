def xoa_khoang_trang_thua(s):
	s = s.strip()
	while "  " in s:
		s = s.replace("  ", " ")
	
	return s

def can_giua_cac_cau(s):
	s = s.split(".")
	longest = ""
	for i in s:
		i = xoa_khoang_trang_thua(i)
		if len(i) > len(longest):
			longest = i
	for j in s:
		print(xoa_khoang_trang_thua(j).center(len(longest)))



s = input('Mời bạn nhập chuỗi: ')


can_giua_cac_cau(s)