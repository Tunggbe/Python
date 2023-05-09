def kiem_tra_so(n):
	if n == 1:
		return False
	for i in range(2, n):
		if n % i == 0:
			return False
	return True


def liet_ke_so(a, b):
	for i in range(a, b+1):
		if kiem_tra_so(i):
			print(i, end=" ")
			


a, b = map(int, input('Mời nhập a, b cách nhau bởi dấu cách: ').split())

if a < 0 or b < 0:
	print('Số phải lớn hơn 0')
elif a > b:
	print('Số đầu tiên phải nhỏ hơn số thứ 2')
else:
	liet_ke_so(a, b)