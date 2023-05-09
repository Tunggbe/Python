try:
	print('Nhập số thứ nhất')
	a = int(input())
	print('Nhập số cuối cùng')
	b = int(input())

	if a > b or a == b:
		print('Số đầu tiên phải nhỏ hơn số cuối cùng')
	else:
		dem = 0
		for i in range(a,b+1):
			if i % 5 == 0:
				print(i)
				dem += 1
				if dem > 10:
					break
except:
	print('Giá trị đầu vào không hợp lệ')
