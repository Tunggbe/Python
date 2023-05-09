def xu_ly(a):
	a = a.split()
	danh_sach_gia = 0
	if len(a) == 0:
		print('Danh sách rỗng')
	elif len(a) == 1:
		print('Danh sách chỉ có 1 thành phần')
	else:
		for i in range(len(a)):
			if i == 0:
				continue
			try:
				if i>0 and (int(a[i-1]) < int(a[i])):
					print("danh sách trên không phải danh sách giảm")
					break
				else: 
					danh_sach_gia += 1
			except:
				print("Vui lòng nhập số")
				break
		if danh_sach_gia != 0:
			print("danh sách trên là 1 danh sách giảm")

def main():
	a = input('Mời nhập chuỗi cần kiểm tra: ')
	xu_ly(a)

main()