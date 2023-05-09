def thay_the_nguyen_am(s):
	dem_so = 0
	for i in range(len(s)):
		if s[i] in 'ueoai' or s[i] in 'UEOAI':
			s = s.replace(s[i], "$")
			dem_so += 1

	return "{}\n{}".format(dem_so,s)



s = input("Mời nhập chuỗi: ")

print(thay_the_nguyen_am(s))