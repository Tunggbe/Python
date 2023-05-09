print('Nhap 3 canh cua 1 tam giac cach nhau boi dau SPACE')
a, b, c = map(float, input().split())

if a+b>c and a+c>b and b+c>a:
	print('{}, {}, {} la cua 1 tam giac'.format(a,b,c))
else:
	print('{}, {}, {} khong phai la cua 1 tam giac'.format(a,b,c))	