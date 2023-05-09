def nhap_sai():
	print('Mời bạn nhập 1 hoặc 2')

def bac1(a, b):
	if a == 0 and b == 0:
		return 'Phương trình có vô số nghiệm'
	elif a == 0:
			return 'Phương trình vô nghiệm'
	else:
		ket_qua = -b/a
		return 'Phương trình có 1 nghiệm duy nhất x = {}'.format(ket_qua)
	
def bac2(a, b, c):
	if a == 0:
		ket_qua = -c/b
		return 'Phương trình có 1 nghiệm duy nhất x = -c/b = {}'.format(ket_qua)
		if b == 0:
			return 'Phương trình vô nghiệm'
			if c == 0:
				return 'Phương trình vô số nghiệm'
	else:
		delta = b**2 - 4*a*c
		if delta < 0:
			return 'Phương trình vô nghiệm'
		elif delta == 0:
			ket_qua = -b/(2*a)
			return 'Phương trình có 1 nghiệm kép x1 = x2 = {}'.format(ket_qua)
		else:
			x1 = (-b + delta**1/2)/ 2*a
			x2 = (-b - delta**1/2)/ 2*a
			return 'Phương trình có 2 nghiệm phân biệt x1 = {}, x2 = {}'.format(x1, x2)

bac_phuong_trinh = input('1 là phương trình bậc nhất, 2 là phương trình bậc 2: ')


if bac_phuong_trinh == "1":
	a, b = map(float, input('Mời nhập hệ số cách nhau bời dấu SPACE theo aX+b=0:').split())
	print(bac1(a, b))
elif bac_phuong_trinh == "2":
	a, b, c = map(float, input('Mời nhập hệ số cách nhau bời dấu SPACE theo aX^2+bX+c=0: ').split())
	print(bac2(a, b, c))
else:
	nhap_sai()



