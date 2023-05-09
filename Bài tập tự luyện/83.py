def xu_ly(danh_sach, so):
	try:
		so = int(so)
		danh_sach = danh_sach.split()
		danh_sach = danh_sach * so
		for i in range(so):
			print(danh_sach[i], end = " ")
	except:
		print("Đầu vào không hợp lệ")

def main():
	a = input("Nhập chuỗi cần kiểm tra: ")
	b = input("Nhập số tự nhiên n: ")
	xu_ly(a, b)

main()