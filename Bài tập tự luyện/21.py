try:
	print('Nhập 3 số cách nhau bởi khoảng trắng tương ứng aX^2+bX+c')
	a, b, c = map(float, input().split())

	delta = b**2 - 4*a*c
	print('delta bằng', delta)
	if a == 0:
		if b == 0:
			if c == 0:
				print('Phương trình vô số nghiệm')
			else:
				print('phương trình vô nghiêm')
		else:
			print('phương trình có 1 nghiệm duy nhất: {}'.format(-c/b))
	else:
		if delta < 0:
			print('phương trình vô nghiệm')
		elif delta == 0:
			x = -b/2*a
			print('Phương trình có nghiệm kép: x1 = x2 = {}'.format(x))
		elif delta > 0:	
			x1 = (-b + delta**(1/2)) / 2*a
			x2 = (-b - delta**(1/2)) / 2*a
			print(x1)
			print(x2)
			print('Phương trình có 2 nghiệm phân biệt: {} và {}'.format(x1,x2))
except:
	print('Định dạng đầu vào không hợp lệ')