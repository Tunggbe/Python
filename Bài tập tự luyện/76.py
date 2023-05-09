def trung_binh_cong(b):
	tong = 0
	for i in b:
		tong += float(i)
	trung_binh_cong = round(tong/len(b),2)
	print(trung_binh_cong)

def is_float(so_hang):
	try:
		float(so_hang)
		return True
	except:
		return False

# def nhap(promt):
# 	dau_vao = input(promt)
# 	return dau_vao

def xu_ly_ly_tu(promt):
	dau_vao = input(promt)
	dau_vao1 = dau_vao.split(" ")
	b = []
	khong_hop_le = []
	if len(dau_vao1) >= 3:
		for so_hang in dau_vao1:
			if is_float(so_hang) or so_hang.isdigit():
				b += so_hang
				# print(so_hang)
			else:
				khong_hop_le += so_hang
		while len(khong_hop_le) != 0:
			xu_ly_ly_tu(promt)
		return b
	else:
		if len(dau_vao) == 1 and (dau_vao == "e" or dau_vao == "E"):
			return dau_vao

# def kiem_tra(chuoi):
# 	while len(chuoi) != 0:
# 		a = xu_ly_ly_tu('Mời bạn nhập lại các số cần tính trung bình cộng cách nhau bởi dấu cách, Nhập E để thoát:')


		
 



def main():
	while True:
		a = xu_ly_ly_tu('Mời bạn nhập các số cần tính trung bình cộng cách nhau bởi dấu cách, Nhập E để thoát:')
		print(a)
		if a == "e" or a == "E":
			break
		# kiem_tra(a[1])
		print(a)
		trung_binh_cong(a)
		
main()