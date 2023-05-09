try:
	print('Nhập số đầu tiên')
	a = int(input())
	print('Nhập số cuối cùng')
	b = int(input())

	if a > b:
		print('Số cuối cùng phải lớn hơn số đầu tiên')
	else:
		tong = 0
		while a <= b:
			tong += a
			a += 1
		print('Tổng dãy số là {}'.format(tong))
except:
	print('Đầu vào không hợp lệ')