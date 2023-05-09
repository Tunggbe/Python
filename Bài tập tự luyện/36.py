so_nhap_vao = int(input("Nhập số cần tính: "))

if so_nhap_vao < 0:
	print('vui lòng nhập số tự nhiên')
else:
	tong_so_chan = 0
	tong_so_le = 0
	while so_nhap_vao > 0:
		chu_so_cuoi = so_nhap_vao % 10
		if chu_so_cuoi % 2 == 0:
			tong_so_chan += chu_so_cuoi
		else:
			tong_so_le += chu_so_cuoi
		so_nhap_vao = so_nhap_vao//10
	tich_cac_chu_so = tong_so_le * tong_so_chan
	print(tich_cac_chu_so)
		