def de_quy(n):
	if n > 0:
		return n + de_quy(n-1)

	return 0

n = int(input('Mời nhập số cần dệ quy: '))

if n < 0:
	print('Số phải lớn hơn 0')
else:
	print(de_quy(n))