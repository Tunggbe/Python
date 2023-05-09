try:
	n = int(input('Mời nhập số tự nhiên: '))

	if n < 0:
		print('Mời nhập số tự nhiên lớn hơn 0')
	elif n == 0:
		print('nothing!!')
	else:
		uoc = n
		while uoc > 0:
			if n % uoc == 0:
				print(uoc, end= " ")
				uoc -= 1
			else:
				uoc -= 1
except:
	print('Đầu vào không hợp lệ')

	
