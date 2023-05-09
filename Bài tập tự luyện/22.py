try:
	print('Nhập 3 cạnh của 1 tam giác')
	a, b, c = map(float, input().split())

	if a+b>c and a+c>b and b+c>a:
		if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
			if a == b or a == c or b == c:
				print('Tam giác có cạnh {}, {}, {} là tam giác vuông cân'.format(a,b,c))
			else:
				print('Tam giác có cạnh {}, {}, {} là tam giác vuông'.format(a,b,c))
		elif a == b or a == c or b == c:
			if a == b == c:
				print('Tam giác có cạnh {}, {}, {} là tam giác đều'.format(a,b,c))
			else:	
				print('Tam giác có cạnh {}, {}, {} là tam giác cân'.format(a,b,c))
			
		elif a*a + b*b < c*c or a*a + c*c < b*b or b*b + c*c < a*a:
			print('Tam giác có cạnh {}, {}, {} là tam giác tù'.format(a,b,c))
		else:
			print('Tam giác có cạnh {}, {}, {} là tam giác nhọn'.format(a,b,c))
	else:
		print('3 cạnh trên không phải là cạnh của 1 tam giác')
except:
	print('Vui lòng nhập đúng cú pháp')