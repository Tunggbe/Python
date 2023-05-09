print("Chào mừng đến với máy kiểm tra số nguyên tố")
a = int(input("Mời nhập số cần kiểm tra: "))

if a < 0:
	print("Mời nhập số nguyên lớn hơn 0")
elif a < 2:
	print(a, "không là số nguyên tố")
else:
	for i in range(2, a):
		if a % i == 0:
			print(a, "không phải là một số nguyên tố")
			break
	else:
		print("{} là số nguyên tố".format(a))


