try:
	print('Nhập số a')
	a = int(input())
	print('Nhập số b')
	b = int(input())

	if a > b:
		print('Số đầu tiên lớn hơn số cuối cùng')
	else:
		tong = 0
		for i in range(a, b+1):
			tong += i
		print('Tổng dãy số là {}'.format(tong))
except:
	print('Đầu vào không hợp lệ')