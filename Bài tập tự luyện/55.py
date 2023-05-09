def kiem_tra_chuoi_con(s1, s2):
	if s2 in s1:
		print('chuỗi "{}" nằm trong chuỗi "{}" {} lần'.format(s2, s1, s1.count(s2)))
	else:
		print('chuỗi "{}" không nằm trong chuỗi "{}"'.format(s2, s1))

a = input()
b = input()

kiem_tra_chuoi_con(a,b)