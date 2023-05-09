try:
	n = int(input('Mời nhập số tự nhiên: '))

	if n < 0:
		print('Mời nhập số tự nhiên lớn hơn 0')
	elif n == 0:
		print('nothing!!')
	else:
		for i in range(1, n+1):
			if n % i == 0:
				print(i, end= " ")
			else:
				continue
except:
	print('Đầu vào không hợp lệ')