def cong(a, b):
	return a + b
def tru(a, b):
	return a - b
def nhan(a, b):
	return a * b
def chia(a, b):
	if b == 0:
		return "chia0"
	return a / b
def may_tinh(phep_tinh, cong, tru, nhan, chia):
	if phep_tinh == '+':
		return cong(a, b)
	elif phep_tinh == '-':
		return tru(a, b)
	elif phep_tinh == "x" or phep_tinh == '.':
		return nhan(a, b)
	elif phep_tinh == '/' or phep_tinh == ':':
		return chia(a, b)


a, phep_tinh, b = input("Mời nhập phép tính: ").split()

a = float(a)
b = float(b)
ket_qua = may_tinh(phep_tinh, cong, tru, nhan, chia)
if phep_tinh != '+' and phep_tinh != '-' and phep_tinh != 'x' and phep_tinh != '.' and phep_tinh != ':' and phep_tinh != '/':
	print('Vui lòng nhập đúng dấu tính')
elif ket_qua == "chia0":
	print('Không thể chia 1 số cho 0')
else:
	print('{} {} {} = {}'.format(a, phep_tinh, b, ket_qua ))