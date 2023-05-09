def in_list(s):
	s = s.split()
	for i,j in enumerate(s):
		print("{} {}".format(i, j))



s = input("Mời nhập chuỗi: ")

in_list(s)