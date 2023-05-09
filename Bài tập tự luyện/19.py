print('Nhap 2 so va dau phep tinh')
a, b, c = input().split()
try:	
	a = float(a)
	c = float(c)
	print(a)
	print(c)
	if b != "+" and b != '-' and b != "*" and b != '/' and b != ":" and b == "x" and b == "X" and b == ".":
		print('dau phep tinh khong hop le')
	else:
		if b == "+":
			phep_cong = a + c
			print('{} + {} = {}'.format(a,c,phep_cong))
		elif b == "-":
			phep_tru = a - c
			print('{} - {} = {}'.format(a,c,phep_tru))
		elif b == "*"  :
			phep_nhan = a * c
			print('{} * {} = {}'.format(a,c,phep_nhan))
		elif b == "/" or b == ":":
			if c == 0:
				print("Khong the chia cho 0")
			else:
				phep_chia = a / c
				print('{} / {} = {}'.format(a,c,phep_chia))
except: 
	print("dau vao khong hop le")