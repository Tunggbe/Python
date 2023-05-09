def tong_trung_binh_cac_so(s):
	s = s.split()
	tong = 0
	so_ky_tu = ""
	for i in s:
		if i.isdigit() == True:
			tong += int(i)
			so_ky_tu += str(int(i))
	if len(so_ky_tu) == 0:
		trung_binh = 0
	else:		
		trung_binh = tong/len(so_ky_tu)
	return print("{}\n{}".format(tong, trung_binh))

s = input("Mời nhập chuỗi: ")

tong_trung_binh_cac_so(s)