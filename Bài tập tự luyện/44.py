def tinh_tong(*args):
	tong = 0
	for i in args:
		tong += i
	return tong

print(tinh_tong(1, 2, 4, 5))