def giai_thua(so_can_tinh):
	if so_can_tinh == 0:
		return 1
	return so_can_tinh * giai_thua(so_can_tinh-1)

a = int(input('Mời nhập số cần tính'))

if a < 0:
	print("vui lòng nhập số lớn hơn 0")
else:
	print(giai_thua(a))
