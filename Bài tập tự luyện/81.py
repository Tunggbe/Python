def kiem_tra_so_nguyen_to(n):
	so_can_kiem_tra = int(n)
	if so_can_kiem_tra < 2:
		return False
	else:
		for i in range(2,so_can_kiem_tra):
			if so_can_kiem_tra % i == 0:
				return False
		return True

def xu_ly(danh_sach):
	try:
		danh_sach = danh_sach.split()
		danh_sach_so_nguyen_to = []
		for so in danh_sach:
			if kiem_tra_so_nguyen_to(so):
				danh_sach_so_nguyen_to.append(so)
				print(so, end = " ")
	except:
		print('Danh sách không hợp lệ')


def main():
	a = input('Mời bạn nhập dãy số cần kiểm tra: ')
	xu_ly(a)

main()