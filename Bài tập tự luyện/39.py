try:
	n = int(input('Mời nhập số tự nhiên: '))

	if n < 0:
		print('Mời nhập số tự nhiên lớn hơn 0')
	elif n == 0:
		print('nothing!!')
	else:
		uoc = 1
		tong_uoc = 0
		while uoc < n:
			if n % uoc == 0:
				tong_uoc += uoc 
				uoc += 1
			else:
				uoc += 1
		if tong_uoc == n:
			print(n, "là số hoàn hảo")
		else:
			print(n, "không phải là số hoàn hảo")
except:
	print('Đầu vào không hợp lệ')