a = input('Mời nhập số tự nhiên: ')
if int(a) < 0:
	print('Vui lòng nhập số tự nhiên > 0')
else:
	ket_qua = []
	for i in range(int(a)):
		ket_qua.append(i)
	print(tuple(ket_qua))