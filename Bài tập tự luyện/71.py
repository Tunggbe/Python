def digit_char_symbol(s):
	digit = ""
	char = ""
	symbol = ""
	for i in s:
		if i.isdigit() == True:
			digit += i
		elif i.islower() == True or i.isupper() == True:
			char += i
		else: 
			symbol += i

	return print("{}\n{}\n{}\n{}{}{}".format(len(digit),len(char),len(symbol),digit,char,symbol))


s = input('Mời nhập chuỗi: ')

digit_char_symbol(s)