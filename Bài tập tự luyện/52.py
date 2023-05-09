def kiem_tra_so_hoan_thien(n):
	uoc = 1
	tong_uoc = 0
	while uoc < n:
		if n % uoc == 0:
			tong_uoc += uoc
			uoc += 1
		else: 
			uoc += 1
	if tong_uoc == n:
		return True
	return False

def liet_ke_so_hoan_thien(n):

	for i in range(1, n):
		if kiem_tra_so_hoan_thien(i) == True:
			print(i, end = " ")


n = int(input('Mời nhập số: '))

if n < 0:
	print('Vui lòng nhập số lớn hơn 0')
elif n == 0:
	print('nothing!')
else:
	liet_ke_so_hoan_thien(n)


