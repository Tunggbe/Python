ten = input('Mời nhập tên: ')
tuoi = int(input('Mời nhập tuổi: '))

if tuoi <1:
	print('Mời nhập tuổi >1')
else:
	print('Xin chào! Tôi là {}, tôi năm nay {} tuổi.'.format(ten,tuoi))