def fin(n):
	if n == 1 or n == 2:
		return 1
	return fin(n - 1) + fin(n - 2)

n = int(input('Mời nhập số thứ tự trong dãy finbonancci: '))

if n < 0 or n == 0:
	print('Mời nhập số lớn hơn 0')
else:
	print(fin(n))
