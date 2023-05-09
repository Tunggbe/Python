def xoa_khoang_trang_thua(s):
	s = s.strip()
	while "  " in s:
		s =	s.replace("  ", " ")
	
	return s

def hien_thi_cau(s):
	ket_qua = ""
	s = s.split(".")
	for i in s:
		i = xoa_khoang_trang_thua(i)
		ket_qua = ket_qua + '\n' + i.title()
	return ket_qua

s = input('Mời nhập chuỗi: ')


print(hien_thi_cau(s))