def chuoi_dan_xen(s1,s2):
	s2_dao = s2[::-1]
	chuoi_ket_qua = ""
	if len(s1) >= len(s2):
		for i in range(len(s1)+1):
			if i < len(s1):
				chuoi_ket_qua += s1[i]
				if i < len(s2_dao):
					chuoi_ket_qua += s2_dao[i]
	if len(s1) < len(s2):
		for i in range(len(s2_dao)+1):
			if i < len(s2_dao):
				chuoi_ket_qua += s2_dao[i]
				if i < len(s1):
					chuoi_ket_qua += s1[i]
	return chuoi_ket_qua


	



s1 = input('Mời nhập chuỗi S1: ')
s2 = input('Mời nhập chuỗi S2: ')

print(chuoi_dan_xen(s1,s2))