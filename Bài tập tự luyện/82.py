def xu_ly(a):
	a = a.split()
	for i in a:
		so_lan_xuat_hien = a.count(i)
		if so_lan_xuat_hien == 1:
			# list_da_xu_ly += i
			print(i, end = " ")

def main():
	a = input('Mời nhập chuỗi cần kiểm tra: ')
	xu_ly(a)

main()