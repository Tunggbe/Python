print('Xin chào đến với công cụ tính giai thừa')
print('Vui lòng nhập số giai thừa cần tính')
a = int(input())

if a < 0:
	print('Số tính giai thừa phải lớn hơn 0')
else:
	giai_thua = 1
	for i in range(1, a+1):
		giai_thua = giai_thua*i
		print(giai_thua)
	print(giai_thua)
