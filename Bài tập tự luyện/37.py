so_nhap_vao = int(input("Mời nhập vào số tự nhiên: "))

if so_nhap_vao < 0:
	print("Số nhập vào phải là số tự nhiên")
elif so_nhap_vao == 1 or so_nhap_vao == 2:
	print('1')
else:
	fin1 = 1
	fin2 = 1
	for i in range(so_nhap_vao-2):
		fin3 = fin1 + fin2
		fin1 = fin2
		fin2 = fin3
	print(fin3)
