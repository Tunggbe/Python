print("Chào mừng đến với máy in số nguyên tố từ a đến b")
a = int(input("Mời nhập số a: "))
b = int(input("Mời nhập số b: "))


if a < 0 or b < 0:
	print("Mời nhập số nguyên lớn hơn 0")
elif a > b:
	print("a nhỏ hơn b")
else:
	for i in range(a, b+1):
		for j in range(2, i):
			if i % j == 0:
				break
		else:
			print(i, end= " ")
