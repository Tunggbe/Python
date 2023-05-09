print("Nhập giá trị đầu vào")
a = int(input())

if 9 < a < 1:
	print('vui lòng nhập giá trị trong khoảng (1,9)')
else:
	for i in range(a):
		for j in range(a - i,0, -1):
			print(j, end="")
		print()
