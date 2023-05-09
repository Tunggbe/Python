def ky_tu_k_trung_lap(s):
	ket_qua = ""
	for i in s:
		if i not in ket_qua:
			ket_qua += i
	return ket_qua

def dem_ky_tu(s):
	for i in ky_tu_k_trung_lap(s):
		ket_qua2 = s.count(i)
		print("'{}': {}".format(i, ket_qua2), end = "; ")

s = input('Mời nhập chuỗi: ')

dem_ky_tu(s)