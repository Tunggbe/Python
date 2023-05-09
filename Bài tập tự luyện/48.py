def tong_chu_so(so_tu_nhien, tuy_chon):
	tong = 0
	while so_tu_nhien > 0:
		if so_tu_nhien % 2 == tuy_chon:
			tong += so_tu_nhien % 10
		so_tu_nhien = so_tu_nhien // 10
	return tong
		

def tinh_tich(so_tu_nhien):
	return tong_chu_so(so_tu_nhien, 0) * tong_chu_so(so_tu_nhien, 1)
	


a = int(input())
if a < 0:
	print('Vui lòng nhập số tự nhiên: ')
else:
	print(tinh_tich(a))