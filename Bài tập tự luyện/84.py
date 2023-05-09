def xu_ly(a,b):
	a = a.split()
	b = int(b)
	ket_qua = []
	c = 0
	if b == 0:
		print('Định dạng đầu vào không hợp lệ')
	else:
		if b > len(a):
			ket_qua = a
		else:
			for i in range(1,len(a)):
				if i % b == 0:
					ket_qua.extend(a[c:i])
					ket_qua.append('Kteam')
					c = i
			ket_qua.extend(a[-2:])
		for i in ket_qua:
			print(i, end = " ")

def main(): 
	a = input('Mời nhập chuỗi: ')
	b = input('Mời nhập số: ')
	xu_ly(a,b)

main()