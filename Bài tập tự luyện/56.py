def chuoi_con_dao_nguoc(a,b,s):
	s_con = s[a:b+1]
	s_dao_nguoc = s_con[::-1]
	print(s_dao_nguoc)
try:
	s = input('Nhập chuỗi: ')
	a, b = map(int, input("Nhập số 2 a và b cách nhau bởi dấu cách: ").split()) 


	if a < 0 or b < 0:
		print('Vui lòng nhập a, b là số tự nhiên')
	elif a > b:
		print('Vui lòng nhập a nhỏ hơn hoặc bằng b')
	elif a > len(s) or b > len(s):
		if a > len(s):
			print("Số a lớn hơn chiều dài của chuỗi")
		else:
			print('Số b lớn hơn chiều dài của chuỗi')
	else:
		chuoi_con_dao_nguoc(a,b,s)
except:
	print('Định dạng đầu vào không hợp lệ')