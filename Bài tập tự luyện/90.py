def xu_ly(a, b):
	ket_qua = []
	for i in a:
		if i not in b:
			ket_qua.append(i)
	for i in b:
		if i not in a:
			ket_qua.append(i)
	for i in ket_qua:
		print(i, end = " ")



def main():
	a = input('Mời nhập chuỗi 1: ').split()
	b = input('Mời nhập chuỗi 2: ').split()
	xu_ly(a,b)

main()