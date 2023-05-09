try:
	print('Loại phương trình cần giải')
	loai_phuong_trinh = int(input())
	if loai_phuong_trinh == 1:
		print('Điền hệ số theo mẫu aX+b=0')
		a, b = map(float, input().split())
		print('X=', -b/a)
	elif loai_phuong_trinh == 2:
		print('điền hệ số theo mẫu aX^2+bX+c=0')
		a, b, c = map(float, input().split())
		delta = b**2 - 4*a*c
		if a == 0:
			if b == 0:
				if c == 0:
					print('phương trình có vô số nghiệm')
				else:
					print('phương trình vô nghiệm')
			else:
				print('phương trình có 1 nghiệm duy nhất x =', -c/b)
		else:
			if delta < 0:
				print('Phương trình vô nghiệm')
			elif delta == 0: 
				print('phương trình có nghiệm kép là', -b/2*a)
			elif delta > 0:
				x1 = (-b + (delta)**1/2)/2*a
				x2 = (-b - (delta)**1/2)/2*a
				print("phương trình có 2 nghiệm x1 là {} và x2 là {}".format(x1,x2))
except: 
	print('Dữ liệu đầu vào không hợp lệ')