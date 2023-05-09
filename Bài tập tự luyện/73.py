def list_va_list_binh_phuong(n):
	bac1 = [i for i in range(n)]
	bac2 = [i**2 for i in range(n)]
	return bac1, bac2

n = int(input("Mời nhập số: "))

if n < 0:
	print('Vui lòng nhập số tự nhiên:')
else:
	bac1, bac2 = list_va_list_binh_phuong(n)
	print(*bac1)
	print(*bac2)