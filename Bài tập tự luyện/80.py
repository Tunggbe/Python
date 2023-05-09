def xu_ly(danh_sach):
	danh_sach = danh_sach.split()
	if len(danh_sach) == 0:
		print('Chuỗi rỗng!')
	else:
		try: 
			for i in range(len(danh_sach)-2,-1,-1):
				for j in range(len(danh_sach)-1,i,-1):
					if float(danh_sach[i]) > float(danh_sach[j]):
						tmp = danh_sach[i]
						danh_sach[i] = danh_sach[j]
						danh_sach[j] = tmp
			for i in danh_sach:
				print(i, end = " ")
		except:
			print('Đầu vào không hợp lệ')

def main():
	danh_sach = input('Mời nhập chuỗi cần sắp xếp: ')
	xu_ly(danh_sach)

main()