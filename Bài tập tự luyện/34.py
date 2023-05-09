x = float(input('Nhập cơ số x: '))
n = int(input('Nhập số mũ n: '))

if n < 0:
	print("Số mũ n không được nhỏ hơn 0")
else:
	giai_thua = 1
	s = 1
	for i in range(1, 2*n+1):
		giai_thua = giai_thua * i
		if i % 2 == 0:
			s += pow(x, i)/giai_thua
		else:
			s -= pow(x, i)/giai_thua

	print('{:.2f}'.format(s))
