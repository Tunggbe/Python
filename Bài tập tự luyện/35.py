so_nhap_vao = int(input("Nhập số cần đảo ngược: "))

if so_nhap_vao < 0:
	print("Số không thể nhỏ hơn 0")
else:
	so_dao_nguoc = 0
	while  so_nhap_vao > 0:
		chu_so_cuoi = so_nhap_vao % 10
		so_dao_nguoc = so_dao_nguoc*10 + chu_so_cuoi
		so_nhap_vao = so_nhap_vao/10
		so_nhap_vao = round(so_nhap_vao)
	print(so_dao_nguoc)
		

