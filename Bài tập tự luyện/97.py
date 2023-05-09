a = input('Mời nhập số tự nhiên: ')
try:
	if int(a) < 0:
		print('Vui lòng nhập số tự nhiên > 0')
	else:
		ket_qua = []
		for i in range(int(a)):
			ket_qua.append(a)
		print(tuple([a,tuple(ket_qua)]))
except:
	print("Định dạng đầu vào không hợp lệ")