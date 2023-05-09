def xoa_trung_lap(s):
	ket_qua = ""
	for i in range(len(s)):
		if s[i] not in ket_qua:
			ket_qua += s[i]

	return ket_qua


s = input('Mời nhập chuỗi: ')

print(xoa_trung_lap(s))

