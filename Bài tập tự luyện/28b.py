try:
	print('Nhập số cần viết bảng cửu chương')
	a = int(input())

	if 1 > a < 9:
		print("Số tính bảng cửu chương phải nằm trong khoảng (1,9)")
	else:
		i = 1
		while i <= 9:
			bang_cuu_chuong = a*i
			i += 1
			print("{} * {} = {}".format(a,i,bang_cuu_chuong))
except:
	print('Định dạng đầu vào không hợp lệ')
