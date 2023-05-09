try:
	n = int(input('Mời nhập số tự nhiên: '))

	if n < 0:
		print('Mời nhập số tự nhiên lớn hơn 0')
	elif n == 0:
		print('nothing!!')
	else:
		tong_uoc = 0
		for i in range(1, n):
			if n % i == 0:
				tong_uoc += i	
			else:
				continue
		if tong_uoc == n:
			print(n, 'là số hoàn hảo')
		else:
			print(n, 'không phải là số hoàn hảo')
except:
	print('Đầu vào không hợp lệ')