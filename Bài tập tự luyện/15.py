try:	
	print('nhap ten cua ban thu nhat')
	ten_a = input()
	print('nhap ten cua ban thu hai')
	ten_b = input()
	print("nhap chieu cao cua ban", ten_a)
	chieu_cao_a = input()
	print('nhap chieu cao cua ban', ten_b)
	chieu_cao_b = input()
	hop_le = False
	chieu_cao_A = int(chieu_cao_a)
	chieu_cao_B = int(chieu_cao_b)


	print("chieu cao phai la so tu nhien")

	if chieu_cao_A < 0:
		print('chieu cao', ten_a, 'khong hop le')
	elif chieu_cao_B < 0:
		print('chieu cao', ten_b, 'khong hop le')
	else:
		if chieu_cao_A > chieu_cao_B: 
			print(ten_a ,"cao hon", ten_b)
		elif chieu_cao_A == chieu_cao_B:
			print(ten_a, 'va', ten_b, 'cao bang nhau')
		elif chieu_cao_A < chieu_cao_B:
			print(ten_a ,'thap hon', ten_b)
except:
	print("khong hop le")