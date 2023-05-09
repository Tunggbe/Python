def xoa_ky_tu(s):
	ket_qua = ''
	for i in range(len(s)):
		if len(s) % 2 == 0:	
			if i % 2 == 1:
				ket_qua += s[i]
		else:
			if i % 2 == 0:
				ket_qua += s[i]
	return ket_qua


s = input('Mời nhập chuỗi: ')

print(xoa_ky_tu(s))