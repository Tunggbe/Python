def chuoi_ket_qua(s1, s2):
		if len(s1) < 5:
			if len(s2) < 5:
				return s1*3 + s2*3
			else:
				return s1*3 + s2
		else:
			if len(s2) < 5:
				return s2*3 + s1
			else:
				return s1 + s2

s1 = str(input("Mời nhập s1: "))
s2 = str(input("Mời nhập s2: "))

print(chuoi_ket_qua(s1,s2))
