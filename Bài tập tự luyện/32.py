print('Nhập giá trị đầu vào')
a = int(input())

if a < 0:
	print("Giá trị phải lớn hơn 0")
else:
	maAscii = 65
	for i in range(a):
		khoang_trang = " "*(((a-i)*2)-2)
		print(khoang_trang , end ="")

		for j in range(2*i+1):
			chu_cai = chr(maAscii)
			print(chu_cai, "", end = "")	
			maAscii += 1

			if(chr(maAscii)>'Z'):
				maAscii = 65
		print()