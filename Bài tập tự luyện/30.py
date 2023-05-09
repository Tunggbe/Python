print("Nhập giá trị đầu vào")
a = int(input())

if 9 < a < 1:
	print('vui lòng nhập giá trị trong khoảng (1,9)')
else:
	for i in range(1,a+1):
		line = ""
		for j in range(1,i+1):
			line = "{} {}".format(line, j)
		print(line)

