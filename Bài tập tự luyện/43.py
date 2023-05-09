def ten_ban_cao_hon(tenA, chieu_caoA, tenB, chieu_caoB):
	if int(chieu_caoA) < 0 or int(chieu_caoB) < 0:
		print('Vui lòng nhập chiều cao lớn hơn 0')
	else:
		if chieu_caoA > chieu_caoB:
			print('{} cao hơn {}'.format(tenA, tenB))
		elif chieu_caoA == chieu_caoB:
			print('{} cao bằng {}'.format(tenA, tenB))
		else:
			print('{} thấp hơn {}'.format(tenA, tenB))

tenA ,chieu_caoA = input('Nhập tên và chiều cao cách nhau bởi SPACE: ').split()
tenB ,chieu_caoB = input('Nhập tên và chiều cao cách nhau bởi SPACE: ').split()

ten_ban_cao_hon(tenA, chieu_caoA, tenB, chieu_caoB)